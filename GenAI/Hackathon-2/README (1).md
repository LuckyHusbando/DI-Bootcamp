# AI-Powered Personalized Place Discovery and Recommendation System for Tel Aviv

**GENZ-AI**

An AI-powered platform that helps people discover places and experiences in Tel Aviv through personalized recommendations based on their interests, preferences, budget and desired atmosphere.

---

## 1. Project Overview

AI City Discovery is a personalized place recommendation system designed to make discovering Tel Aviv easier and more relevant to individual users.

Instead of browsing generic lists of popular places, users can describe the experience they are looking for in natural language.

For example:

> "I want an affordable, quiet café where I can read a book and sit outside."

The system processes the request, identifies relevant preferences and criteria, searches its place database, ranks matching locations and generates explanations for its recommendations.

The goal is to recommend places based not only on their popularity, but also on how well they match the experience each user wants.

## 2. Development Process

The project was developed in stages.

### Stage 1 — Initial Recommendation System

The initial prototype established the core application architecture:

- Streamlit user interface.
- Tel Aviv place database.
- Keyword-based preference recognition.
- Natural-language request criteria extraction.
- Semantic search using Sentence Transformers.
- FAISS similarity retrieval.
- Hybrid recommendation ranking.
- Assessment of supporting, contradictory and missing information.
- AI-generated recommendation explanations using Ollama and Llama 3.2.
- Initial evaluation framework and automated tests.

### Stage 2 — Dataset Expansion and Preference Classification

The next development stage focused on expanding the training data and introducing a trained preference classification model.

The work included:

- Generating synthetic examples using Faker.
- Updating the dataset schema to support 22 preference labels.
- Expanding the preference training dataset to 242 examples.
- Fine-tuning DistilBERT using Parameter-Efficient Fine-Tuning (PEFT) and Low-Rank Adaptation (LoRA).
- Saving the trained adapter.
- Integrating the adapter into the Streamlit application.

### Stage 3 — Current Development

The current project includes the original recommendation architecture and the additional LoRA-based preference classifier.

Further work can focus on independent model evaluation, improving dataset quality, expanding and verifying place information, and refining recommendation accuracy.

## 3. System Architecture

```text
USER
  |
  v
STREAMLIT APPLICATION
  |
  |-- Natural-language request
  |-- Selected preferences
  |-- Budget and location
  |
  v
REQUEST UNDERSTANDING
  |
  |-- Preference classification
  |     |-- DistilBERT + LoRA
  |     |-- Keyword-based fallback
  |
  |-- Request criteria extraction
  |
  v
PLACE DATABASE
  |
  v
SEMANTIC RETRIEVAL
  |
  |-- Sentence Transformers
  |-- all-MiniLM-L6-v2
  |-- FAISS
  |
  v
RECOMMENDATION ENGINE
  |
  |-- Preference matching
  |-- Semantic relevance
  |-- Evidence assessment
  |-- Data quality assessment
  |-- Budget and neighborhood adjustments
  |
  v
HYBRID RANKING
  |
  v
GENERATIVE EXPLANATIONS
  |
  |-- Ollama
  |-- Llama 3.2
  |
  v
PERSONALIZED RESULTS
  |
  |-- Recommended places
  |-- Explanations
  |-- Relevant details
  |-- Missing information
  |-- Navigation links
```

## 4. Technologies

| Technology | Role in the project |
|---|---|
| Python | Main programming language |
| Streamlit | Interactive application interface |
| Pandas | Dataset management and processing |
| DistilBERT | Preference classification base model |
| PEFT / LoRA | Parameter-efficient model fine-tuning |
| Sentence Transformers | Semantic text embeddings |
| all-MiniLM-L6-v2 | Embedding model used for semantic retrieval |
| FAISS | Similarity search over embeddings |
| Ollama | Local generative AI integration |
| Llama 3.2 | Recommendation explanation generation |
| Scikit-learn | Machine learning utilities and evaluation |
| PyTorch | Model execution and training |
| Hugging Face Transformers | Transformer model and tokenizer support |

## 5. Machine Learning Components

The system contains three distinct AI components.

### 5.1 Preference Classification — DistilBERT + LoRA

The preference classifier identifies what users are looking for from natural-language requests.

The original implementation included a keyword-based classification baseline.

The updated implementation introduces DistilBERT fine-tuned using PEFT/LoRA for multi-label classification.

The model is configured to recognize 22 preference categories:

- Food
- Culture
- Café
- Art
- Outdoors
- Quiet
- Budget
- Beach
- History
- Bakery
- Cocktails
- Market
- Vegetarian
- Nightlife
- Music
- Shopping
- Romantic
- Vegan
- Mexican
- Israeli
- Architecture
- Surfing

**Training dataset**

The expanded dataset contains 242 synthetically generated examples. Faker was used as part of the data-generation process.

**Reported training results**

| Metric | Result |
|---|---:|
| Base model | distilbert-base-uncased |
| Fine-tuning method | PEFT / LoRA |
| Classification labels | 22 |
| Training examples | 242 |
| Training epochs | 3 |
| Epoch 1 training loss | 0.4707 |
| Epoch 2 training loss | 0.3285 |
| Epoch 3 training loss | 0.2771 |
| Trainable parameters | 1.1147% |

Training loss decreased from 0.4707 to 0.2771 across three epochs, representing an approximately 41.1% reduction.

The trained adapter is stored in:

`models/preference-lora/`

The application loads the adapter using:

`PeftModel.from_pretrained()`

**Evaluation status:** Training completion and adapter integration are present. Independent validation metrics on unseen examples have not yet been established.

### 5.2 Semantic Search — Sentence Transformers and FAISS

Semantic search identifies places based on the meaning of a request rather than relying exclusively on exact keyword matches.

The system uses:

- Sentence Transformers.
- `all-MiniLM-L6-v2` for text embeddings.
- FAISS for similarity-based retrieval.

This component is separate from the DistilBERT + LoRA preference classifier.

### 5.3 Generative AI — Ollama and Llama 3.2

Ollama provides local access to the Llama 3.2 model.

The generative component creates natural-language explanations for recommendations using the available place information.

A fallback mechanism is included when generative explanations are unavailable.

The generative model does not replace the retrieval or ranking system.

## 6. Recommendation Engine

The recommendation engine combines semantic relevance and preference matching.

The current hybrid ranking uses:

| Component | Weight |
|---|---:|
| Semantic similarity | 55% |
| Preference-tag coverage | 45% |

Additional adjustments account for available evidence, data quality, known prices and neighborhood information.

The system also assesses whether requested characteristics are:

- Supported by the available information.
- Contradicted by the available information.
- Mixed or conflicting.
- Unknown due to insufficient information.

Missing information is not automatically interpreted as evidence that a place satisfies a user's request.

The ranking scores are used to order recommendations. They should not be interpreted as calibrated probabilities or guaranteed measures of recommendation accuracy.

## 7. Data

The project uses two main datasets.

### `Data/places_demo.csv`

Contains the place information used by the recommendation system, including location details, categories, descriptions, features, atmosphere and other available attributes.

The dataset is a development dataset and should not be treated as a fully verified, real-time directory of Tel Aviv businesses.

### `Data/preferences_train.csv`

Contains the expanded synthetic training examples used for the 22-label preference classification task.

The dataset was expanded using Faker-generated data.

Synthetic examples are useful for development and experimentation but do not necessarily represent the full diversity of real user language.

### `Data/Old Data/`

Contains previous project data retained during development.

## 8. Evaluation and Testing

The project includes an evaluation framework and automated tests.

### Recommendation evaluation

`evaluate.py` includes manually defined test cases and relevance judgments.

The evaluation framework calculates:

- Precision@K
- Recall@K
- NDCG@K
- Mean Reciprocal Rank (MRR)

These metrics assess the ordering and relevance of recommendations against the available manual judgments.

### Automated tests

`test_engine.py` contains automated tests for recommendation-engine functionality.

### Future evaluation work

Further validation should include:

- Independent test examples not used during training.
- Precision, recall and F1-score for the LoRA classifier.
- Comparison between the keyword baseline and trained classifier.
- Analysis of performance across all 22 labels.
- Additional recommendation relevance testing.

## 9. Project Structure

```text
AI-powered-personalized-place-discovery-and-recommendation-system-for-Tel-Aviv/
│
├── app.py
│   Main Streamlit application.
│
├── recommendation_engine.py
│   Preference processing, retrieval, ranking
│   and evidence assessment.
│
├── evaluate.py
│   Recommendation evaluation framework.
│
├── train_lora.py
│   DistilBERT LoRA training script.
│
├── test_engine.py
│   Automated recommendation-engine tests.
│
├── requirements.txt
│   Python dependencies.
│
├── Data/
│   ├── places_demo.csv
│   ├── preferences_train.csv
│   └── Old Data/
│
├── models/
│   └── preference-lora/
│       ├── adapter_config.json
│       ├── adapter_model.safetensors
│       ├── labels.json
│       ├── tokenizer_config.json
│       ├── tokenizer.json
│       └── README.md
│
├── .gitignore
│
├── .env
│   Local configuration; not committed.
│
└── .venv/
    Local Python virtual environment; not committed.
```

## 10. Installation and Execution

### Requirements

- Python 3.10 or compatible version.
- Git.
- Visual Studio Code or another Python development environment.
- Ollama installed locally for Llama-based explanations.

### Clone the repository

```bash
git clone https://github.com/13loy22/AI-powered-personalized-place-discovery-and-recommendation-system-for-Tel-Aviv.git

cd AI-powered-personalized-place-discovery-and-recommendation-system-for-Tel-Aviv
```

### Create a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv

.\.venv\Scripts\Activate.ps1
```

### Install dependencies

```powershell
python -m pip install --upgrade pip

pip install -r requirements.txt
```

### Configure Ollama

Install Ollama and download the configured model:

```powershell
ollama pull llama3.2:1b
```

Create a local `.env` file containing:

```env
OLLAMA_MODEL=llama3.2:1b
```

Ensure Ollama is running before using the generative explanation component.

### Run the application

```powershell
streamlit run app.py
```

The application should open in a browser at:

`http://localhost:8501`

## 11. Current Limitations

The current implementation is a working development prototype, not a fully deployed commercial recommendation platform.

Known limitations include:

- Place information is based on a demonstration dataset and requires further verification.
- Training data is synthetic and relatively small.
- Independent validation of the trained LoRA classifier is still required.
- Training loss alone does not establish classification accuracy.
- Recommendation quality depends on the completeness and accuracy of the place database.
- Live Google Places integration is not currently part of the implemented system.
- Persistent user profiles and feedback-based personalization remain future development possibilities.

## 12. Future Development

Potential next steps include:

1. Independently evaluating the trained preference classifier.
2. Improving the diversity and quality of training examples.
3. Expanding and verifying the Tel Aviv place database.
4. Improving recommendation relevance and ranking.
5. Integrating live place information and opening hours.
6. Adding maps and navigation functionality.
7. Introducing user feedback and persistent preference profiles.
8. Improving the application interface and presentation.

## 13. Project Goal

AI City Discovery aims to create a more meaningful way to explore a city.

By combining natural-language understanding, semantic retrieval, personalized ranking and generative AI, the platform aims to understand not just where people want to go, but what kind of experience they are looking for.

**GENZ-AI — Personalized discovery of Tel Aviv, one experience at a time.**
