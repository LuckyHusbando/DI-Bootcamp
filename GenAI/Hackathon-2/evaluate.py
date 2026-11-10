
"""Evaluate AI City Discovery using the same engine as app.py.

The relevance judgments below are initial human-authored judgments.
Review them before reporting results in academic work.

Run:
    python evaluate.py

Optional:
    python evaluate.py --top-k 5
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer

from recommendation_engine import (
    EMBED_MODEL,
    extract_preferences,
    rank,
    read_places,
    retrieve,
)

DATA_FILE = Path("data/places_demo.csv")
OUTPUT_FILE = Path("evaluation_results.csv")

# Each query contains:
# query: natural-language user request
# relevant: manually judged relevant place names
# category: broad evaluation category
#
# These are starting judgments, not independently verified ground truth.

TEST_CASES = [
    {
        "query": "I want a quiet cafe where I can read.",
        "relevant": ["Cafe Alma", "Cafelix Jaffa", "Mae Cafe"],
        "category": "cafe",
    },
    {
        "query": "I want a cafe with outdoor seating and good coffee.",
        "relevant": ["Cafe Alma", "Cafelix Jaffa", "HOC House of Coffee"],
        "category": "cafe",
    },
    {
        "query": "Find me an affordable place for coffee and reading.",
        "relevant": ["HOC House of Coffee", "Cafe Alma", "Mae Cafe"],
        "category": "cafe",
    },
    {
        "query": "I want a relaxed cafe with a creative atmosphere.",
        "relevant": ["Cafe Alma", "Lorenz and Mintz", "Cafelix Jaffa"],
        "category": "cafe",
    },
    {
        "query": "I am looking for a vegan restaurant.",
        "relevant": ["Anastasia", "Meshek Barzilay", "The Green Roll"],
        "category": "food",
    },
    {
        "query": "I want vegetarian food in Tel Aviv.",
        "relevant": ["Anastasia", "Meshek Barzilay", "The Green Roll"],
        "category": "food",
    },
    {
        "query": "I want Mexican food and tacos.",
        "relevant": ["Taqueria"],
        "category": "food",
    },
    {
        "query": "I want to try Israeli food.",
        "relevant": ["Haachim", "Meshek Barzilay"],
        "category": "food",
    },
    {
        "query": "I want to eat fresh bread and pastries.",
        "relevant": [
            "Alexander Bread and Bakery",
            "Lehamim",
            "Lachmanina",
        ],
        "category": "food",
    },
    {
        "query": "I want to go out for cocktails at night.",
        "relevant": ["223 Bar", "Butler"],
        "category": "nightlife",
    },
    {
        "query": "Find somewhere with nightlife and music.",
        "relevant": ["223 Bar", "Butler"],
        "category": "nightlife",
    },
    {
        "query": "I want to explore art and museums.",
        "relevant": [
            "Tel Aviv Museum of Art",
            "Nahum Gutman Museum",
            "Suzanne Dellal Centre",
        ],
        "category": "culture",
    },
    {
        "query": "I want to discover history and architecture.",
        "relevant": [
            "Old Jaffa",
            "Neve Tzedek",
            "Hatachana",
        ],
        "category": "culture",
    },
    {
        "query": "I want to visit an art and design market.",
        "relevant": [
            "Nahalat Binyamin Artists Market",
            "Carmel Market",
        ],
        "category": "shopping",
    },
    {
        "query": "I want to go shopping and discover local markets.",
        "relevant": [
            "Nahalat Binyamin Artists Market",
            "Carmel Market",
        ],
        "category": "shopping",
    },
    {
        "query": "I want to spend time outdoors near the sea.",
        "relevant": [
            "Gordon Beach",
            "Hilton Beach",
            "Frishman Beach",
            "Jerusalem Beach",
        ],
        "category": "outdoors",
    },
    {
        "query": "I want to go surfing.",
        "relevant": [
            "Hilton Beach",
            "Gordon Beach",
        ],
        "category": "outdoors",
    },
    {
        "query": "I want a beach where I can relax.",
        "relevant": [
            "Gordon Beach",
            "Frishman Beach",
            "Hilton Beach",
        ],
        "category": "outdoors",
    },
    {
        "query": "I want to explore Jaffa and its historic port.",
        "relevant": [
            "Old Jaffa",
            "Jaffa Port",
        ],
        "category": "culture",
    },
    {
        "query": "I want a cultural place with exhibitions and events.",
        "relevant": [
            "Tel Aviv Museum of Art",
            "Suzanne Dellal Centre",
            "Nahum Gutman Museum",
        ],
        "category": "culture",
    },
    {
        "query": "I want somewhere relaxed, not too crowded, with good coffee and outdoor seating.",
        "relevant": [
            "Cafe Alma",
            "Cafelix Jaffa",
            "Mae Cafe",
        ],
        "category": "complex",
    },
    {
        "query": "I don't want a touristy place. I prefer somewhere local.",
        "relevant": [
            "Cafelix Jaffa",
            "Mae Cafe",
            "Lorenz and Mintz",
        ],
        "category": "complex",
    },
    {
        "query": "I want a creative place where I can sit outside and talk.",
        "relevant": [
            "Cafe Alma",
            "Lorenz and Mintz",
            "Jaffa Port",
        ],
        "category": "complex",
    },
    {
        "query": "I want somewhere quiet and peaceful to spend the afternoon.",
        "relevant": [
            "Cafe Alma",
            "Cafelix Jaffa",
            "Mae Cafe",
        ],
        "category": "complex",
    },
    {
        "query": "I want a place for a romantic date.",
        "relevant": [
            "Butler",
            "Neve Tzedek",
            "Jaffa Port",
        ],
        "category": "complex",
    },
    {
        "query": "I want to explore a neighborhood with art, culture and cafes.",
        "relevant": [
            "Neve Tzedek",
            "Old Jaffa",
            "Suzanne Dellal Centre",
        ],
        "category": "complex",
    },
    {
        "query": "I want to spend time at a market and discover local products.",
        "relevant": [
            "Carmel Market",
            "Nahalat Binyamin Artists Market",
        ],
        "category": "shopping",
    },
    {
        "query": "I want to visit a museum and learn about local history.",
        "relevant": [
            "Nahum Gutman Museum",
            "Tel Aviv Museum of Art",
            "Old Jaffa",
        ],
        "category": "culture",
    },
    {
        "query": "I want a bakery for fresh bread and coffee.",
        "relevant": [
            "Alexander Bread and Bakery",
            "Lehamim",
            "Lachmanina",
        ],
        "category": "food",
    },
    {
        "query": "I want to spend the day at the port and enjoy the outdoors.",
        "relevant": [
            "Jaffa Port",
            "Tel Aviv Port",
        ],
        "category": "outdoors",
    },
]


def precision_at_k(
    ranked_names: list[str],
    relevant: set[str],
    k: int,
) -> float:
    if k <= 0:
        return 0.0

    top = ranked_names[:k]

    if not top:
        return 0.0

    hits = sum(name in relevant for name in top)

    return hits / k


def recall_at_k(
    ranked_names: list[str],
    relevant: set[str],
    k: int,
) -> float:
    if not relevant:
        return 0.0

    hits = sum(
        name in relevant
        for name in ranked_names[:k]
    )

    return hits / len(relevant)


def dcg_at_k(
    ranked_names: list[str],
    relevant: set[str],
    k: int,
) -> float:
    score = 0.0

    for position, name in enumerate(
        ranked_names[:k],
        start=1,
    ):
        relevance = 1 if name in relevant else 0

        score += relevance / np.log2(position + 1)

    return float(score)


def ndcg_at_k(
    ranked_names: list[str],
    relevant: set[str],
    k: int,
) -> float:
    actual = dcg_at_k(
        ranked_names,
        relevant,
        k,
    )

    ideal_count = min(
        len(relevant),
        k,
    )

    ideal = sum(
        1 / np.log2(position + 1)
        for position in range(1, ideal_count + 1)
    )

    if ideal == 0:
        return 0.0

    return actual / ideal


def reciprocal_rank(
    ranked_names: list[str],
    relevant: set[str],
) -> float:
    for position, name in enumerate(
        ranked_names,
        start=1,
    ):
        if name in relevant:
            return 1.0 / position

    return 0.0


def validate_test_cases(
    df: pd.DataFrame,
) -> list[dict]:
    available = set(df["name"].astype(str))

    validated = []

    for index, case in enumerate(
        TEST_CASES,
        start=1,
    ):
        relevant = set(case["relevant"])

        missing = sorted(
            relevant - available
        )

        if missing:
            print(
                f"WARNING: Test case {index} references "
                f"places not present in the dataset: {missing}"
            )

        valid_relevant = relevant & available

        if not valid_relevant:
            print(
                f"WARNING: Test case {index} has no "
                "relevant places in the dataset. Skipping."
            )
            continue

        validated.append(
            {
                **case,
                "relevant": valid_relevant,
            }
        )

    return validated


def evaluate(
    df: pd.DataFrame,
    encoder: SentenceTransformer,
    top_k: int,
) -> pd.DataFrame:
    test_cases = validate_test_cases(df)

    rows = []

    for index, case in enumerate(
        test_cases,
        start=1,
    ):
        query = case["query"]
        relevant = case["relevant"]

        preferences, _, _ = extract_preferences(
            query
        )

        candidates = retrieve(
            df,
            query,
            encoder,
        )

        ranked = rank(
            candidates,
            preferences,
            budget=None,
            area="Any",
            number=len(df),
            query=query,
        )

        ranked_names = [
            str(place["name"])
            for place in ranked
        ]

        top_names = ranked_names[:top_k]

        hits = [
            name
            for name in top_names
            if name in relevant
        ]

        rows.append(
            {
                "case_id": index,
                "query": query,
                "category": case["category"],
                "relevant_places": " | ".join(
                    sorted(relevant)
                ),
                "recommended_places": " | ".join(
                    top_names
                ),
                "relevant_found": len(hits),
                "relevant_total": len(relevant),
                "precision_at_k": precision_at_k(
                    ranked_names,
                    relevant,
                    top_k,
                ),
                "recall_at_k": recall_at_k(
                    ranked_names,
                    relevant,
                    top_k,
                ),
                "ndcg_at_k": ndcg_at_k(
                    ranked_names,
                    relevant,
                    top_k,
                ),
                "reciprocal_rank": reciprocal_rank(
                    ranked_names,
                    relevant,
                ),
                "first_result_relevant": (
                    bool(ranked_names)
                    and ranked_names[0] in relevant
                ),
            }
        )

    return pd.DataFrame(rows)


def print_summary(
    results: pd.DataFrame,
    top_k: int,
) -> None:
    if results.empty:
        print("No valid test cases were evaluated.")
        return

    print("\n" + "=" * 65)
    print("AI CITY DISCOVERY — EVALUATION RESULTS")
    print("=" * 65)

    print(
        f"\nNumber of evaluated queries: {len(results)}"
    )

    print(
        f"Evaluation cutoff: K = {top_k}"
    )

    metrics = [
        "precision_at_k",
        "recall_at_k",
        "ndcg_at_k",
        "reciprocal_rank",
        "first_result_relevant",
    ]

    print("\nOVERALL METRICS")

    for metric in metrics:
        value = results[metric].mean()

        print(
            f"{metric}: {value:.4f}"
        )

    print("\nRESULTS BY CATEGORY")

    grouped = (
        results
        .groupby("category")[metrics]
        .mean()
        .round(4)
    )

    print(grouped.to_string())

    failed = results[
        ~results["first_result_relevant"]
    ]

    print(
        "\nQueries where the first recommendation "
        f"was not relevant: {len(failed)}"
    )

    if not failed.empty:
        for _, row in failed.iterrows():
            print(
                f"\nQuery: {row['query']}"
            )
            print(
                f"Recommendations: "
                f"{row['recommended_places']}"
            )
            print(
                f"Relevant places: "
                f"{row['relevant_places']}"
            )

    print("\n" + "=" * 65)


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Evaluate the AI City Discovery recommendation engine."
        )
    )

    parser.add_argument(
        "--top-k",
        type=int,
        default=3,
        help="Number of recommendations to evaluate (default: 3).",
    )

    args = parser.parse_args()

    if args.top_k < 1:
        parser.error("--top-k must be at least 1.")

    if not DATA_FILE.exists():
        raise FileNotFoundError(
            f"Dataset not found: {DATA_FILE}"
        )

    print("Loading places database…")

    df = read_places(DATA_FILE)

    print(
        f"Loaded {len(df)} places."
    )

    print(
        f"Loading embedding model: {EMBED_MODEL}"
    )

    encoder = SentenceTransformer(EMBED_MODEL)

    print(
        f"Evaluating {len(TEST_CASES)} initial test cases…"
    )

    results = evaluate(
        df,
        encoder,
        args.top_k,
    )

    if results.empty:
        raise RuntimeError(
            "Evaluation produced no valid results."
        )

    results.to_csv(
        OUTPUT_FILE,
        index=False,
        encoding="utf-8-sig",
    )

    print_summary(
        results,
        args.top_k,
    )

    print(
        f"\nDetailed results saved to: {OUTPUT_FILE.resolve()}"
    )

    print(
        "\nIMPORTANT: These results use initial manual relevance "
        "judgments. They are not an independent benchmark and "
        "should be reviewed before academic reporting."
    )


if __name__ == "__main__":
    main()
