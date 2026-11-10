
"""Train a multi-label DistilBERT classifier with LoRA.

The training data must contain:
    - A text column
    - One binary column for each of the 22 application labels

The current 10-example dataset with 10 labels is intentionally rejected.
It is not sufficient for reliable training and does not match app.py.

Run:
    python train_lora.py
"""

from __future__ import annotations

import json
import random
from pathlib import Path

import numpy as np
import pandas as pd
import torch
from sklearn.metrics import classification_report, f1_score
from sklearn.model_selection import train_test_split
from torch.utils.data import DataLoader, Dataset
from transformers import (
    AutoModelForSequenceClassification,
    AutoTokenizer,
)
from peft import (
    LoraConfig,
    TaskType,
    get_peft_model,
)

from recommendation_engine import LABELS


# ---------------------------------------------------------------------
# CONFIGURATION
# ---------------------------------------------------------------------

BASE_MODEL = "distilbert-base-uncased"

DATA_FILE = Path("data/preferences_train.csv")
OUTPUT_DIR = Path("models/preference-lora")

TEXT_COLUMN = "text"

MIN_EXAMPLES = 100
MIN_POSITIVES_PER_LABEL = 10
MIN_NEGATIVES_PER_LABEL = 10

TEST_SIZE = 0.20
RANDOM_SEED = 42

MAX_LENGTH = 128
BATCH_SIZE = 8
EPOCHS = 3
LEARNING_RATE = 2e-4
THRESHOLD = 0.5


# ---------------------------------------------------------------------
# REPRODUCIBILITY
# ---------------------------------------------------------------------

def set_seed(seed: int = RANDOM_SEED) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)

    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


# ---------------------------------------------------------------------
# DATASET
# ---------------------------------------------------------------------

class PreferenceDataset(Dataset):
    def __init__(
        self,
        texts: list[str],
        labels: np.ndarray,
        tokenizer,
    ):
        self.texts = texts
        self.labels = labels
        self.tokenizer = tokenizer

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, index):
        encoded = self.tokenizer(
            self.texts[index],
            truncation=True,
            padding="max_length",
            max_length=MAX_LENGTH,
            return_tensors="pt",
        )

        item = {
            key: value.squeeze(0)
            for key, value in encoded.items()
        }

        item["labels"] = torch.tensor(
            self.labels[index],
            dtype=torch.float32,
        )

        return item


# ---------------------------------------------------------------------
# VALIDATION
# ---------------------------------------------------------------------

def validate_training_data(
    df: pd.DataFrame,
) -> np.ndarray:
    if TEXT_COLUMN not in df.columns:
        raise ValueError(
            f"Training file must contain a '{TEXT_COLUMN}' column."
        )

    missing_labels = [
        label
        for label in LABELS
        if label not in df.columns
    ]

    extra_columns = [
        column
        for column in df.columns
        if column not in [TEXT_COLUMN, *LABELS]
    ]

    if missing_labels:
        raise ValueError(
            "Training data does not match the application's "
            "22-label schema.\n"
            f"Missing labels: {missing_labels}\n\n"
            "The current dataset contains only 10 labels. "
            "It cannot train the application's 22-label classifier."
        )

    if extra_columns:
        print(
            "WARNING: Additional columns will be ignored:",
            extra_columns,
        )

    df[TEXT_COLUMN] = (
        df[TEXT_COLUMN]
        .fillna("")
        .astype(str)
        .str.strip()
    )

    if (df[TEXT_COLUMN] == "").any():
        raise ValueError(
            "Training data contains empty text examples."
        )

    if df[TEXT_COLUMN].duplicated().any():
        duplicates = int(
            df[TEXT_COLUMN].duplicated().sum()
        )

        raise ValueError(
            f"Training data contains {duplicates} duplicate queries. "
            "Review duplicates before training."
        )

    label_frame = df[LABELS].copy()

    for label in LABELS:
        label_frame[label] = pd.to_numeric(
            label_frame[label],
            errors="coerce",
        )

    if label_frame.isna().any().any():
        raise ValueError(
            "Label columns must contain only numeric 0 or 1 values."
        )

    values = label_frame.to_numpy(dtype=np.float32)

    if not np.isin(values, [0.0, 1.0]).all():
        raise ValueError(
            "All label values must be binary: 0 or 1."
        )

    if len(df) < MIN_EXAMPLES:
        raise ValueError(
            f"Only {len(df)} training examples were found. "
            f"At least {MIN_EXAMPLES} are required by this "
            "training configuration."
        )

    positives = values.sum(axis=0)
    negatives = len(values) - positives

    insufficient = []

    for index, label in enumerate(LABELS):
        if positives[index] < MIN_POSITIVES_PER_LABEL:
            insufficient.append(
                f"{label}: {int(positives[index])} positive examples"
            )

        if negatives[index] < MIN_NEGATIVES_PER_LABEL:
            insufficient.append(
                f"{label}: {int(negatives[index])} negative examples"
            )

    if insufficient:
        raise ValueError(
            "Insufficient examples for one or more labels:\n"
            + "\n".join(insufficient)
        )

    return values


# ---------------------------------------------------------------------
# MODEL TRAINING
# ---------------------------------------------------------------------

def evaluate_model(
    model,
    loader,
    device,
):
    model.eval()

    predictions = []
    actuals = []

    with torch.no_grad():
        for batch in loader:
            labels = batch.pop("labels").to(device)

            batch = {
                key: value.to(device)
                for key, value in batch.items()
            }

            logits = model(**batch).logits

            probabilities = torch.sigmoid(logits)

            predicted = (
                probabilities >= THRESHOLD
            ).cpu().numpy()

            predictions.extend(predicted)
            actuals.extend(
                labels.cpu().numpy()
            )

    y_pred = np.asarray(predictions, dtype=int)
    y_true = np.asarray(actuals, dtype=int)

    macro_f1 = f1_score(
        y_true,
        y_pred,
        average="macro",
        zero_division=0,
    )

    micro_f1 = f1_score(
        y_true,
        y_pred,
        average="micro",
        zero_division=0,
    )

    return macro_f1, micro_f1, y_true, y_pred


def train():
    set_seed()

    if not DATA_FILE.exists():
        raise FileNotFoundError(
            f"Training data not found: {DATA_FILE}"
        )

    print("Loading training data...")

    df = pd.read_csv(DATA_FILE)

    print(
        f"Training examples found: {len(df)}"
    )

    labels = validate_training_data(df)

    texts = df[TEXT_COLUMN].tolist()

    print("\nLabel distribution:")

    for index, label in enumerate(LABELS):
        positive_count = int(
            labels[:, index].sum()
        )

        print(
            f"{label}: {positive_count} positive / "
            f"{len(labels) - positive_count} negative"
        )

    # A fixed random split is used after checking label support.
    # For a larger research dataset, iterative multilabel
    # stratification would be preferable.

    (
        train_texts,
        test_texts,
        train_labels,
        test_labels,
    ) = train_test_split(
        texts,
        labels,
        test_size=TEST_SIZE,
        random_state=RANDOM_SEED,
    )

    tokenizer = AutoTokenizer.from_pretrained(
        BASE_MODEL
    )

    train_dataset = PreferenceDataset(
        train_texts,
        train_labels,
        tokenizer,
    )

    test_dataset = PreferenceDataset(
        test_texts,
        test_labels,
        tokenizer,
    )

    train_loader = DataLoader(
        train_dataset,
        batch_size=BATCH_SIZE,
        shuffle=True,
    )

    test_loader = DataLoader(
        test_dataset,
        batch_size=BATCH_SIZE,
        shuffle=False,
    )

    device = torch.device(
        "cuda" if torch.cuda.is_available() else "cpu"
    )

    print(
        f"\nTraining device: {device}"
    )

    base_model = (
        AutoModelForSequenceClassification.from_pretrained(
            BASE_MODEL,
            num_labels=len(LABELS),
            problem_type="multi_label_classification",
        )
    )

    config = LoraConfig(
        task_type=TaskType.SEQ_CLS,
        r=8,
        lora_alpha=16,
        lora_dropout=0.1,
        target_modules=["q_lin", "v_lin"],
        modules_to_save=[
            "pre_classifier",
            "classifier",
        ],
    )

    model = get_peft_model(
        base_model,
        config,
    )

    model.to(device)

    model.print_trainable_parameters()

    optimizer = torch.optim.AdamW(
        filter(
            lambda parameter: parameter.requires_grad,
            model.parameters(),
        ),
        lr=LEARNING_RATE,
    )

    # -------------------------------------------------------------
    # TRAINING LOOP
    # -------------------------------------------------------------

    print("\nStarting LoRA training...")

    for epoch in range(EPOCHS):
        model.train()

        total_loss = 0.0

        for batch in train_loader:
            labels_batch = batch.pop(
                "labels"
            ).to(device)

            batch = {
                key: value.to(device)
                for key, value in batch.items()
            }

            optimizer.zero_grad()

            outputs = model(
                **batch,
                labels=labels_batch,
            )

            loss = outputs.loss

            loss.backward()

            optimizer.step()

            total_loss += loss.item()

        average_loss = (
            total_loss / max(1, len(train_loader))
        )

        print(
            f"Epoch {epoch + 1}/{EPOCHS} "
            f"— training loss: {average_loss:.4f}"
        )

    # -------------------------------------------------------------
    # TEST EVALUATION
    # -------------------------------------------------------------

    macro_f1, micro_f1, y_true, y_pred = (
        evaluate_model(
            model,
            test_loader,
            device,
        )
    )

    print("\nTEST RESULTS")

    print(
        f"Macro F1: {macro_f1:.4f}"
    )

    print(
        f"Micro F1: {micro_f1:.4f}"
    )

    print(
        "\nClassification report:"
    )

    print(
        classification_report(
            y_true,
            y_pred,
            target_names=LABELS,
            zero_division=0,
        )
    )

    # -------------------------------------------------------------
    # SAVE ADAPTER AND METADATA
    # -------------------------------------------------------------

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    model.save_pretrained(
        OUTPUT_DIR
    )

    tokenizer.save_pretrained(
        OUTPUT_DIR
    )

    metadata = {
        "labels": LABELS,
        "base_model": BASE_MODEL,
        "training_examples": len(train_texts),
        "test_examples": len(test_texts),
        "epochs": EPOCHS,
        "learning_rate": LEARNING_RATE,
        "batch_size": BATCH_SIZE,
        "threshold": THRESHOLD,
        "random_seed": RANDOM_SEED,
        "macro_f1": float(macro_f1),
        "micro_f1": float(micro_f1),
    }

    (OUTPUT_DIR / "labels.json").write_text(
        json.dumps(
            metadata,
            indent=2,
        ),
        encoding="utf-8",
    )

    print(
        f"\nLoRA adapter saved to: {OUTPUT_DIR}"
    )


if __name__ == "__main__":
    try:
        train()

    except (
        FileNotFoundError,
        ValueError,
    ) as exc:
        print("\nTRAINING NOT STARTED")
        print(str(exc))
        print(
            "\nThis is an intentional data-quality safeguard. "
            "The application can continue using its keyword baseline."
        )
