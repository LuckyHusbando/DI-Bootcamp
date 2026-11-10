
"""AI City Discovery — Streamlit application."""
from __future__ import annotations

import json
import os
from pathlib import Path

import ollama
import pandas as pd
import streamlit as st
import torch
from dotenv import load_dotenv
from peft import PeftModel
from sentence_transformers import SentenceTransformer
from transformers import (
    AutoModelForSequenceClassification,
    AutoTokenizer,
)

from recommendation_engine import (
    EMBED_MODEL,
    LABELS,
    criteria_to_plain_text,
    dataset_quality_report,
    extract_preferences,
    extract_request_criteria,
    is_not_applicable,
    is_unknown,
    missing_information,
    rank,
    read_places,
    retrieve,
    usable_text,
)

load_dotenv()

BASE_MODEL = "distilbert-base-uncased"
MODEL_DIR = Path("models/preference-lora")
DATA_FILE = Path("data/places_demo.csv")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2:1b")

st.set_page_config(
    page_title="AI City Discovery",
    page_icon="📍",
    layout="wide",
)


@st.cache_resource(show_spinner="Loading semantic search model…")
def get_encoder():
    return SentenceTransformer(EMBED_MODEL)


@st.cache_resource(show_spinner=False)
def get_lora_classifier():
    """Load an adapter only when its saved label schema matches the app."""
    config_file = MODEL_DIR / "adapter_config.json"
    labels_file = MODEL_DIR / "labels.json"

    if not config_file.exists() or not labels_file.exists():
        return (
            None,
            None,
            "Keyword baseline — no compatible trained adapter found",
        )

    try:
        saved = json.loads(
            labels_file.read_text(encoding="utf-8")
        )

        saved_labels = (
            saved.get("labels", saved)
            if isinstance(saved, dict)
            else saved
        )

        if list(saved_labels) != LABELS:
            return (
                None,
                None,
                "Keyword baseline — adapter label schema "
                "does not match current 22 labels",
            )

        tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL)

        base_model = (
            AutoModelForSequenceClassification.from_pretrained(
                BASE_MODEL,
                num_labels=len(LABELS),
                problem_type="multi_label_classification",
            )
        )

        model = PeftModel.from_pretrained(
            base_model,
            str(MODEL_DIR),
        )

        model.eval()

        return tokenizer, model, "DistilBERT + LoRA"

    except Exception as exc:
        return (
            None,
            None,
            "Keyword baseline — adapter could not be loaded "
            f"({type(exc).__name__})",
        )


def classify_preferences(text: str):
    tokenizer, model, status = get_lora_classifier()

    if model is None:
        labels, scores, method = extract_preferences(text)

        return (
            labels,
            scores,
            status if status.startswith("Keyword baseline") else method,
        )

    batch = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        max_length=128,
    )

    with torch.no_grad():
        probabilities = torch.sigmoid(
            model(**batch).logits[0]
        ).cpu().tolist()

    scores = dict(zip(LABELS, probabilities))

    selected = [
        label
        for label, score in scores.items()
        if score >= 0.5
    ]

    return selected, scores, status


def generate_explanations(
    query: str,
    places: list[dict],
) -> dict[str, str]:
    """Generate explanations using only information recorded in the dataset."""

    facts = []

    fields = [
        "name",
        "category",
        "description",
        "neighborhood",
        "features",
        "atmosphere",
        "activities",
        "environment",
        "outdoor_features",
        "dietary_options",
        "opening_hours",
        "price_level",
    ]

    for place in places:
        facts.append(
            {
                field: (
                    usable_text(
                        place.get(field, "unknown")
                    )
                    or "Not recorded"
                )
                for field in fields
            }
        )

    prompt = (
        "For each supplied place, write one concise sentence explaining "
        "only the recorded reasons it may fit the request. "
        "Do not infer or invent facts. If evidence is absent, do not claim it. "
        "Return a JSON object mapping each exact place name to its sentence.\n"
        f"User request: {query}\n"
        f"Place records: {json.dumps(facts, ensure_ascii=False)}"
    )

    try:
        response = ollama.chat(
            model=OLLAMA_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            format="json",
            options={"temperature": 0.1},
        )

        parsed = json.loads(
            response["message"]["content"]
        )

        if isinstance(parsed, dict):
            return {
                str(key): str(value)
                for key, value in parsed.items()
            }

    except Exception:
        pass

    return {
        place["name"]: place.get(
            "description",
            "No description recorded.",
        )
        for place in places
    }


def display_value(place: dict, field: str) -> str:
    value = place.get(field, "unknown")

    if is_not_applicable(value):
        return "Not applicable"

    if is_unknown(value):
        return "Not recorded"

    return str(value)


# ---------------------------------------------------------------------
# APPLICATION HEADER
# ---------------------------------------------------------------------

st.title("📍 AI City Discovery")

st.caption(
    "Personalized place discovery for Tel Aviv"
)

st.info(
    "Development prototype using a small sample dataset. "
    "Place details, prices, ratings and opening hours may be incomplete "
    "or unverified. Recommendations are not live availability checks."
)


# ---------------------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------------------

with st.sidebar:
    st.header("Search settings")

    uploaded = st.file_uploader(
        "Upload a places CSV",
        type=["csv"],
    )

    number = st.slider(
        "Number of recommendations",
        min_value=2,
        max_value=6,
        value=3,
    )


# ---------------------------------------------------------------------
# LOAD DATASET
# ---------------------------------------------------------------------

try:
    places_df = read_places(
        uploaded if uploaded is not None else DATA_FILE
    )

except Exception as exc:
    st.error(
        f"Could not load the places database: {exc}"
    )
    st.stop()

if places_df.empty:
    st.error(
        "The places database contains no records."
    )
    st.stop()

quality = dataset_quality_report(places_df)

price_known = quality.get(
    "price_level",
    {},
).get("known", 0)

areas = ["Any"] + sorted(
    {
        value
        for value in places_df["neighborhood"].tolist()
        if not is_unknown(value)
        and not is_not_applicable(value)
    }
)


# ---------------------------------------------------------------------
# SEARCH INTERFACE
# ---------------------------------------------------------------------

col_a, col_b = st.columns([2, 1])

with col_a:
    request = st.text_area(
        "Describe what you are looking for",
        placeholder=(
            "A relaxed cafe with outdoor seating, good coffee, "
            "and somewhere to talk."
        ),
        height=110,
    )

with col_b:
    area = st.selectbox(
        "Neighborhood",
        areas,
    )

    if price_known:
        budget_choice = st.selectbox(
            "Maximum business price level",
            ["No preference", 1, 2, 3, 4],
        )
    else:
        budget_choice = "No preference"

        st.caption(
            "Budget ranking is disabled: "
            "no numeric price levels are recorded."
        )

interests = st.multiselect(
    "Interests and categories",
    LABELS,
    help=(
        "Add explicit categories to your natural-language request."
    ),
)


# ---------------------------------------------------------------------
# RUN RECOMMENDATION PIPELINE
# ---------------------------------------------------------------------

if st.button(
    "Find places",
    type="primary",
    use_container_width=True,
):
    if not request.strip() and not interests:
        st.error(
            "Describe what you want or select at least one interest."
        )
        st.stop()

    query = " ".join(
        [
            request.strip(),
            *interests,
        ]
    ).strip()

    predicted, model_scores, method = classify_preferences(
        query
    )

    preferences = sorted(
        set(predicted) | set(interests)
    )

    with st.spinner(
        "Retrieving and ranking places…"
    ):
        encoder = get_encoder()

        candidates = retrieve(
            places_df,
            query,
            encoder,
        )

        results = rank(
            candidates,
            preferences,
            (
                None
                if budget_choice == "No preference"
                else int(budget_choice)
            ),
            area,
            number,
            query,
        )

        explanations = (
            generate_explanations(query, results)
            if results
            else {}
        )

    st.session_state["last_search"] = {
        "query": query,
        "preferences": preferences,
        "scores": model_scores,
        "method": method,
        "results": results,
        "explanations": explanations,
    }


# ---------------------------------------------------------------------
# DISPLAY RESULTS
# ---------------------------------------------------------------------

search = st.session_state.get("last_search")

if search:
    st.subheader("Your recommendations")

    st.caption(
        f"Preference interpretation: {search['method']}"
    )

    criteria = extract_request_criteria(
        search["query"]
    )

    if criteria:
        st.write(
            "Request criteria detected: "
            + ", ".join(
                criteria_to_plain_text(criteria)
            )
        )

    if not search["results"]:
        st.warning(
            "No matching places were found. "
            "Try a broader request."
        )

    for index, place in enumerate(
        search["results"],
        start=1,
    ):
        with st.container(border=True):
            st.markdown(
                f"### {index}. {place['name']}"
            )

            st.write(
                search["explanations"].get(
                    place["name"],
                    place.get("description", ""),
                )
            )

            neighborhood = (
                usable_text(
                    place.get("neighborhood", "unknown")
                )
                or "Neighborhood not recorded"
            )

            st.caption(
                f"{place.get('category', 'Place')} "
                f"· {neighborhood} "
                f"· Ranking score: "
                f"{place['recommendation_score']:.3f}"
            )

            matched = place.get(
                "matched_preferences",
                [],
            )

            if matched:
                st.caption(
                    "Matched interests: "
                    + ", ".join(matched)
                )

            # ---------------------------------------------------------
            # CRITERION EVIDENCE
            # ---------------------------------------------------------

            if place.get("criterion_assessments"):
                with st.expander(
                    "Evidence for your request"
                ):
                    for criterion, status in (
                        place["criterion_assessments"].items()
                    ):
                        evidence = (
                            place["criterion_evidence"].get(
                                criterion,
                                [],
                            )
                        )

                        st.write(
                            f"**{criterion}:** "
                            f"{status.replace('_', ' ')}"
                        )

                        if evidence:
                            st.caption(
                                "Recorded evidence: "
                                + ", ".join(evidence)
                            )

                        elif status == "unknown":
                            st.caption(
                                "The database does not contain "
                                "enough information to confirm this."
                            )

            # ---------------------------------------------------------
            # PLACE INFORMATION AND DATA QUALITY
            # ---------------------------------------------------------

            with st.expander(
                "Place information and data quality"
            ):
                fields = [
                    "address",
                    "place_type",
                    "secondary_categories",
                    "atmosphere",
                    "activities",
                    "music_type",
                    "dietary_options",
                    "environment",
                    "kosher_status",
                    "amenities",
                    "outdoor_features",
                    "opening_hours",
                    "price_level",
                    "price_type",
                    "price_amount",
                    "price_currency",
                    "rating",
                    "rating_source",
                    "last_verified",
                    "data_quality_status",
                ]

                labels = {
                    "place_type": "Place type",
                    "secondary_categories": "Other categories",
                    "dietary_options": "Dietary options",
                    "kosher_status": "Kosher status",
                    "price_level": "Business price level",
                    "price_amount": "Price amount",
                    "last_verified": "Last verified",
                    "data_quality_status": "Data quality",
                }

                for field in fields:
                    st.write(
                        f"**{labels.get(field, field.replace('_', ' ').title())}:** "
                        f"{display_value(place, field)}"
                    )

                missing = missing_information(place)

                if missing:
                    st.warning(
                        "Not recorded: "
                        + ", ".join(missing)
                    )

                source = usable_text(
                    place.get("source_url", "unknown")
                )

                if source.startswith("http"):
                    st.markdown(
                        f"[Open information source]({source})"
                    )

                maps = usable_text(
                    place.get("google_maps_url", "unknown")
                )

                if maps.startswith("http"):
                    st.markdown(
                        f"[Open in Google Maps]({maps})"
                    )

                st.caption(
                    "Source status: "
                    + display_value(
                        place,
                        "verification_status",
                    )
                )


# ---------------------------------------------------------------------
# MODEL AND RANKING DIAGNOSTICS
# ---------------------------------------------------------------------

if search:
    with st.expander(
        "Model and ranking diagnostics"
    ):
        st.write(
            "These values are diagnostic scores, "
            "not probabilities or calibrated confidence."
        )

        st.json(
            {
                "query": search["query"],
                "preferences": search["preferences"],
                "classification_method": search["method"],
                "preference_scores": search["scores"],
                "labels": LABELS,
                "embedding_model": EMBED_MODEL,
                "ranking_components": (
                    "55% normalized semantic similarity + "
                    "45% preference-tag coverage; "
                    "small explicit-evidence adjustments; "
                    "optional known price/neighborhood adjustments."
                ),
            }
        )

        diagnostics = pd.DataFrame(
            search["results"]
        )

        visible_columns = [
            "name",
            "semantic_score",
            "semantic_score_01",
            "preference_match",
            "criterion_adjustment",
            "recommendation_score",
        ]

        visible_columns = [
            column
            for column in visible_columns
            if column in diagnostics.columns
        ]

        st.dataframe(
            diagnostics[visible_columns],
            use_container_width=True,
        )


# ---------------------------------------------------------------------
# DATASET COVERAGE
# ---------------------------------------------------------------------

with st.expander(
    "Dataset coverage and current places database"
):
    st.write(
        f"Records: {len(places_df)}"
    )

    quality_df = (
        pd.DataFrame.from_dict(
            quality,
            orient="index",
        )
        .rename_axis("Field")
        .reset_index()
    )

    st.dataframe(
        quality_df,
        use_container_width=True,
    )

    st.caption(
        "Unknown fields are excluded from evidence-based confirmation "
        "and should not be interpreted as negative facts."
    )

    st.dataframe(
        places_df.drop(
            columns=[
                "search_text",
                "price_level_numeric",
                "price_amount_numeric",
                "rating_numeric",
            ],
            errors="ignore",
        ),
        use_container_width=True,
    )
