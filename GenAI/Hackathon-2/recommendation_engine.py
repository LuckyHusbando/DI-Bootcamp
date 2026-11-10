
"""Shared retrieval, preference parsing, evidence assessment, and ranking logic.

This module is used by both app.py and evaluate.py so evaluation measures the
same recommendation logic that the Streamlit application uses.
"""
from __future__ import annotations

import re
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

LABELS = [
    "cafe", "food", "vegan", "vegetarian", "bakery", "mexican", "israeli",
    "art", "culture", "history", "architecture", "outdoors", "beach", "surfing",
    "nightlife", "cocktails", "music", "market", "shopping", "quiet", "budget",
    "romantic",
]

UNKNOWN_VALUES = {"", "unknown", "nan", "none", "null", "not recorded"}
NOT_APPLICABLE_VALUES = {"not_applicable", "not applicable", "n/a"}

KEYWORDS = {
    "cafe": [
        r"\bcaf[eé]s?\b", r"\bcoffee\b", r"\bespresso\b",
        r"\bread\b.*\b(book|work)\b"
    ],
    "food": [
        r"\bfood\b", r"\beat\b", r"\brestaurant\b",
        r"\b(lunch|dinner|brunch)\b"
    ],
    "vegan": [r"\bvegan\b", r"\bplant[- ]based\b"],
    "vegetarian": [r"\bvegetarian\b", r"\bmeat[- ]free\b"],
    "bakery": [
        r"\bbakery\b", r"\bpastr(y|ies)\b",
        r"\bcroissant\b", r"\bbread\b"
    ],
    "mexican": [
        r"\bmexican\b", r"\btacos?\b", r"\bburritos?\b",
        r"\bquesadillas?\b"
    ],
    "israeli": [
        r"\bisraeli food\b", r"\bmiddle eastern\b",
        r"\bhummus\b", r"\bfalafel\b", r"\bshakshuka\b"
    ],
    "art": [
        r"\bart\b", r"\bgaller(y|ies)\b", r"\bartistic\b",
        r"\bcreative\b", r"\bexhibition\b"
    ],
    "culture": [
        r"\bcultur(e|al)\b", r"\bmuseum\b", r"\btheat(re|er)\b",
        r"\bdance\b", r"\bperformance\b"
    ],
    "history": [
        r"\bhistor(y|ic|ical)\b", r"\bheritage\b", r"\bold town\b"
    ],
    "architecture": [
        r"\barchitecture\b", r"\barchitectural\b", r"\bbauhaus\b"
    ],
    "outdoors": [
        r"\boutdoors?\b", r"\boutside\b", r"\bgarden\b",
        r"\bpark\b", r"\bnature\b", r"\bopen[- ]air\b"
    ],
    "beach": [
        r"\bbeach\b", r"\bseaside\b", r"\bby the sea\b",
        r"\bcoast\b", r"\bocean\b"
    ],
    "surfing": [r"\bsurf(ing|board)?\b", r"\bwaves\b"],
    "nightlife": [
        r"\bnightlife\b", r"\bnight out\b", r"\bparty\b", r"\bclub\b"
    ],
    "cocktails": [
        r"\bcocktails?\b", r"\bmixology\b", r"\bwine bar\b"
    ],
    "music": [
        r"\bmusic\b", r"\blive music\b", r"\bconcert\b",
        r"\bjazz\b", r"\bdj\b"
    ],
    "market": [
        r"\bmarkets?\b", r"\bflea market\b",
        r"\bfarmers'? market\b", r"\bshuk\b"
    ],
    "shopping": [
        r"\bshopping\b", r"\bboutiques?\b",
        r"\bhandmade\b", r"\bdesign shops\b"
    ],
    "quiet": [
        r"\bquiet\b", r"\bpeaceful\b", r"\bcalm\b",
        r"\btranquil\b", r"\blow[- ]noise\b"
    ],
    "budget": [
        r"\bcheap\b", r"\baffordable\b", r"\binexpensive\b",
        r"\bbudget[- ]friendly\b", r"\blow[- ]cost\b"
    ],
    "romantic": [
        r"\bromantic\b", r"\bdate\b", r"\bintimate\b", r"\bcouples?\b"
    ],
}

CATEGORY_ALIASES = {
    "coffee": {"cafe"},
    "cafe": {"cafe"},
    "bakery": {"bakery", "cafe", "food"},
    "restaurant": {"food"},
    "vegan restaurant": {"food", "vegan"},
    "vegetarian restaurant": {"food", "vegetarian"},
    "mexican restaurant": {"food", "mexican"},
    "israeli restaurant": {"food", "israeli"},
    "museum": {"art", "culture", "history"},
    "gallery": {"art", "culture"},
    "historic site": {"culture", "history", "architecture"},
    "historic neighborhood": {"culture", "history", "architecture"},
    "public space": {"outdoors"},
    "port and public space": {"outdoors"},
    "beach": {"outdoors", "beach"},
    "bar": {"nightlife"},
    "cocktail bar": {"nightlife", "cocktails"},
    "market": {"market", "shopping"},
}

# Criteria are deliberately evidence-based. Missing information is not proof.
CRITERIA = {
    "quiet": {
        "label": "Quiet atmosphere",
        "weight": .08,
        "query_patterns": [
            r"\bquiet\b", r"\bpeaceful\b", r"\bcalm\b",
            r"\btranquil\b", r"\blow[- ]noise\b"
        ],
        "positive": [
            "quiet", "peaceful", "calm", "tranquil",
            "low noise", "low-noise"
        ],
        "negative": [
            "noisy", "loud", "high noise", "high-noise"
        ],
        "fields": [
            "atmosphere", "features", "description", "amenities"
        ],
    },
    "relaxed_atmosphere": {
        "label": "Relaxed atmosphere",
        "weight": .04,
        "query_patterns": [
            r"\brelaxed\b", r"\blaid[- ]back\b", r"\beasygoing\b"
        ],
        "positive": [
            "relaxed", "laid-back", "laid back", "easygoing"
        ],
        "negative": ["tense", "hectic"],
        "fields": ["atmosphere", "description", "features"],
    },
    "outdoor_seating": {
        "label": "Outdoor seating",
        "weight": .10,
        "query_patterns": [
            r"\boutdoor seating\b", r"\bseat outside\b",
            r"\bsit outside\b", r"\bsit outdoors\b",
            r"\bpatio\b", r"\bterrace\b", r"\bcourtyard\b",
            r"\boutdoor space\b"
        ],
        "positive": [
            "outdoor seating", "outside seating",
            "courtyard seating", "patio seating",
            "terrace seating", "garden seating",
            "seating outdoors"
        ],
        "negative": [
            "indoor only", "no outdoor seating",
            "without outdoor seating"
        ],
        "fields": ["outdoor_features", "amenities"],
    },
    "not_crowded": {
        "label": "Avoid crowded places",
        "weight": .07,
        "query_patterns": [
            r"\bnot (?:too )?crowded\b",
            r"\buncrowded\b",
            r"\bavoid (?:the )?crowds?\b",
            r"\bnot too busy\b",
            r"\bless crowded\b"
        ],
        "positive": [
            "not crowded", "uncrowded", "spacious",
            "quiet corner", "less crowded"
        ],
        "negative": [
            "crowded", "packed", "very busy",
            "usually busy", "tourist crowds"
        ],
        "fields": [
            "atmosphere", "features", "description", "amenities"
        ],
    },
    "creative_atmosphere": {
        "label": "Creative atmosphere",
        "weight": .04,
        "query_patterns": [
            r"\bcreative\b", r"\bartistic\b",
            r"\bdesign[- ]?oriented\b",
            r"\bcreative atmosphere\b"
        ],
        "positive": [
            "creative", "artistic", "artist-run",
            "design atmosphere", "creative space"
        ],
        "negative": [],
        "fields": [
            "atmosphere", "secondary_categories",
            "features", "description"
        ],
    },
    "non_touristy": {
        "label": "Avoid touristy places",
        "weight": .07,
        "query_patterns": [
            r"\bnot touristy\b",
            r"\bnon[- ]touristy\b",
            r"\bavoid tourist(?:y| traps?)\b",
            r"\bnot a tourist trap\b",
            r"\bmore local than touristy\b",
            r"\b(?:do not|don.t) want\b.{0,45}\btouristy\b",
            r"\b(?:do not|don.t) want\b.{0,45}\btourist trap\b"
        ],
        "positive": [
            "not touristy", "non-touristy", "local atmosphere",
            "mostly locals", "neighborhood spot", "local neighborhood"
        ],
        "negative": [
            "touristy", "tourist attraction",
            "tourist trap", "popular tourist destination"
        ],
        "fields": [
            "atmosphere", "features", "description",
            "secondary_categories", "place_type"
        ],
    },
}

SEARCH_FIELDS = [
    "name", "category", "description", "neighborhood", "address",
    "features", "place_type", "secondary_categories", "atmosphere",
    "activities", "music_type", "dietary_options", "environment",
    "kosher_status", "amenities", "outdoor_features",
]

DEFAULTS = {
    "address": "unknown",
    "features": "unknown",
    "atmosphere": "unknown",
    "activities": "unknown",
    "music_type": "unknown",
    "dietary_options": "unknown",
    "environment": "unknown",
    "kosher_status": "unknown",
    "price_level": "unknown",
    "rating": "unknown",
    "opening_hours": "unknown",
    "google_maps_url": "unknown",
    "source_url": "unknown",
    "verification_status": "unknown",
    "place_type": "unknown",
    "secondary_categories": "unknown",
    "amenities": "unknown",
    "outdoor_features": "unknown",
    "price_type": "unknown",
    "price_amount": "unknown",
    "price_currency": "unknown",
    "rating_source": "unknown",
    "last_verified": "unknown",
    "data_quality_status": "unknown",
}


def is_unknown(value: Any) -> bool:
    if value is None or pd.isna(value):
        return True
    return str(value).strip().lower() in UNKNOWN_VALUES


def is_not_applicable(value: Any) -> bool:
    if value is None or pd.isna(value):
        return False
    return str(value).strip().lower() in NOT_APPLICABLE_VALUES


def usable_text(value: Any) -> str:
    if is_unknown(value) or is_not_applicable(value):
        return ""
    return str(value).strip()


def read_places(source: str | Path | Any) -> pd.DataFrame:
    df = pd.read_csv(source)

    required = ["name", "category", "description", "neighborhood"]
    missing = [col for col in required if col not in df.columns]

    if missing:
        raise ValueError(
            f"Missing required CSV columns: {', '.join(missing)}"
        )

    for col, default in DEFAULTS.items():
        if col not in df.columns:
            df[col] = default

    for col in df.columns:
        if df[col].dtype == "object":
            df[col] = (
                df[col]
                .fillna("unknown")
                .astype(str)
                .str.strip()
            )

    for col in ("price_level", "price_amount", "rating"):
        cleaned = df[col].map(
            lambda value: (
                np.nan
                if str(value).strip().lower()
                in (UNKNOWN_VALUES | NOT_APPLICABLE_VALUES)
                else value
            )
        )
        df[f"{col}_numeric"] = pd.to_numeric(
            cleaned, errors="coerce"
        )

    df["search_text"] = df[SEARCH_FIELDS].apply(
        lambda row: ". ".join(
            filter(None, (usable_text(value) for value in row))
        ),
        axis=1,
    )

    empty_search = df["search_text"].eq("")
    df.loc[empty_search, "search_text"] = df.loc[
        empty_search, "name"
    ]

    return df


def extract_preferences(
    text: str,
) -> tuple[list[str], dict[str, float], str]:
    lowered = text.lower()

    scores = {
        label: float(
            any(
                re.search(pattern, lowered)
                for pattern in patterns
            )
        )
        for label, patterns in KEYWORDS.items()
    }

    selected = [
        label for label, score in scores.items() if score > 0
    ]

    return (
        selected,
        scores,
        "Keyword baseline (22-label schema)",
    )


def extract_request_criteria(query: str) -> dict[str, dict]:
    lowered = query.lower()

    return {
        key: value
        for key, value in CRITERIA.items()
        if any(
            re.search(pattern, lowered)
            for pattern in value["query_patterns"]
        )
    }


def assess_request_criterion(
    place: dict,
    criterion: dict,
) -> tuple[str, list[str]]:
    evidence = []

    for field in criterion["fields"]:
        value = usable_text(place.get(field, "unknown"))
        if value:
            evidence.append(value)

    joined = " | ".join(evidence).lower()

    if not joined:
        return "unknown", []

    # Find phrase occurrences with their character positions. A longer phrase
    # can contain a shorter phrase with the opposite polarity, for example:
    # "no outdoor seating" contains "outdoor seating", and "not crowded"
    # contains "crowded". In those cases, the longer phrase determines the
    # meaning instead of incorrectly producing a mixed result.
    def find_occurrences(terms: list[str]) -> list[tuple[str, int, int]]:
        occurrences = []
        for term in terms:
            for match in re.finditer(re.escape(term), joined):
                occurrences.append((term, match.start(), match.end()))
        return occurrences

    positive_occurrences = find_occurrences(criterion["positive"])
    negative_occurrences = find_occurrences(criterion["negative"])

    def keep_unambiguous_occurrences(
        own_occurrences: list[tuple[str, int, int]],
        opposite_occurrences: list[tuple[str, int, int]],
    ) -> list[str]:
        kept = []
        for term, start, end in own_occurrences:
            is_overridden = any(
                start < opposite_end
                and opposite_start < end
                and len(opposite_term) > len(term)
                for opposite_term, opposite_start, opposite_end
                in opposite_occurrences
            )
            if not is_overridden and term not in kept:
                kept.append(term)
        return kept

    positive_hits = keep_unambiguous_occurrences(
        positive_occurrences, negative_occurrences
    )
    negative_hits = keep_unambiguous_occurrences(
        negative_occurrences, positive_occurrences
    )

    if positive_hits and not negative_hits:
        return "supported", positive_hits

    if negative_hits and not positive_hits:
        return "contradicted", negative_hits

    if positive_hits and negative_hits:
        return "mixed", positive_hits + negative_hits

    return "unknown", []


def get_place_tags(place: dict) -> set[str]:
    tags: set[str] = set()

    fields = [
        "category", "features", "place_type",
        "secondary_categories", "activities",
        "dietary_options", "music_type", "kosher_status",
    ]

    chunks = []

    for field in fields:
        value = usable_text(
            place.get(field, "unknown")
        ).lower()

        if value:
            chunks.append(value)

            tags.update(
                item.strip().replace("-", "_")
                for item in re.split(r"[,;|]", value)
                if item.strip()
            )

    category = usable_text(
        place.get("category", "unknown")
    ).lower()

    tags.update(CATEGORY_ALIASES.get(category, set()))

    place_type = (
        usable_text(place.get("place_type", "unknown"))
        .lower()
        .replace(" ", "_")
    )

    type_aliases = {
        "cafe": {"cafe"},
        "restaurant": {"food"},
        "bakery": {"bakery", "cafe", "food"},
        "bar": {"nightlife", "cocktails"},
        "beach": {"beach", "outdoors"},
        "market": {"market", "shopping"},
        "museum": {"art", "culture", "history"},
        "museum_or_art_venue": {"art", "culture", "history"},
        "public_space": {"outdoors"},
        "historic_site_or_complex": {
            "culture", "history", "architecture"
        },
        "cultural_venue": {"culture", "art"},
    }

    tags.update(type_aliases.get(place_type, set()))

    metadata = " ".join(chunks)

    for label, patterns in KEYWORDS.items():
        if any(
            re.search(pattern, metadata)
            for pattern in patterns
        ):
            tags.add(label)

    # Generic "outdoors" does not prove outdoor seating.
    return tags


def retrieve(
    df: pd.DataFrame,
    query: str,
    encoder: SentenceTransformer,
    top_k: int | None = None,
) -> list[dict]:
    if df.empty:
        return []

    import faiss

    texts = df["search_text"].fillna("").tolist()

    vectors = encoder.encode(
        texts,
        convert_to_numpy=True,
        normalize_embeddings=True,
    ).astype("float32")

    index = faiss.IndexFlatIP(vectors.shape[1])
    index.add(vectors)

    query_vector = encoder.encode(
        [query],
        convert_to_numpy=True,
        normalize_embeddings=True,
    ).astype("float32")

    count = (
        len(df)
        if top_k is None
        else min(max(1, int(top_k)), len(df))
    )

    scores, ids = index.search(query_vector, count)

    output = []

    for score, idx in zip(scores[0], ids[0]):
        if idx >= 0:
            row = df.iloc[int(idx)].to_dict()
            row["semantic_score"] = float(score)
            output.append(row)

    return output


def rank(
    candidates: list[dict],
    preferences: list[str],
    budget: int | None = None,
    area: str = "Any",
    number: int = 3,
    query: str = "",
) -> list[dict]:

    requested = set(preferences)
    criteria = extract_request_criteria(query)

    assessed = []

    for original in candidates:
        place = dict(original)
        tags = get_place_tags(place)

        matched = requested & tags

        semantic = float(
            place.get("semantic_score", 0.0)
        )

        semantic01 = min(
            1.0,
            max(0.0, (semantic + 1.0) / 2.0),
        )

        tag_coverage = (
            len(matched) / max(1, len(requested))
        )

        score = (
            .55 * semantic01
            + .45 * tag_coverage
        )

        criterion_status = {}
        criterion_evidence = {}
        adjustment = 0.0

        for key, criterion in criteria.items():
            status, hits = assess_request_criterion(
                place, criterion
            )

            criterion_status[criterion["label"]] = status
            criterion_evidence[criterion["label"]] = hits

            if status == "supported":
                adjustment += criterion["weight"]
            elif status == "contradicted":
                adjustment -= criterion["weight"]

        score += adjustment

        price = place.get(
            "price_level_numeric", np.nan
        )

        if budget is not None and pd.notna(price):
            score += (
                .08
                if float(price) <= budget
                else -.12
            )

        neighborhood = usable_text(
            place.get("neighborhood", "unknown")
        )

        if (
            area != "Any"
            and neighborhood.casefold() == area.casefold()
        ):
            score += .05

        place["recommendation_score"] = round(
            max(0.0, min(1.0, score)), 4
        )

        place["semantic_score_01"] = round(
            semantic01, 4
        )

        place["preference_match"] = round(
            tag_coverage, 4
        )

        place["matched_preferences"] = sorted(matched)

        place["criterion_assessments"] = criterion_status
        place["criterion_evidence"] = criterion_evidence

        place["criterion_adjustment"] = round(
            adjustment, 4
        )

        # This is diagnostic metadata, not a calibrated probability.
        assessed.append(place)

    assessed.sort(
        key=lambda item: (
            item["recommendation_score"],
            item.get("semantic_score", 0),
        ),
        reverse=True,
    )

    return assessed[:max(1, number)]


def missing_information(place: dict) -> list[str]:
    fields = [
        "address", "opening_hours", "price_level", "rating",
        "dietary_options", "atmosphere", "activities",
        "environment", "amenities", "outdoor_features",
        "kosher_status",
    ]

    labels = {
        "price_level": "Price level",
        "dietary_options": "Dietary options",
        "kosher_status": "Kosher status",
        "opening_hours": "Opening hours",
        "outdoor_features": "Outdoor features",
    }

    return [
        labels.get(field, field.replace("_", " ").title())
        for field in fields
        if is_unknown(place.get(field, "unknown"))
    ]


def dataset_quality_report(df: pd.DataFrame) -> dict:
    fields = [
        "address", "opening_hours", "price_level", "rating",
        "atmosphere", "activities", "dietary_options",
        "environment", "kosher_status", "amenities",
        "outdoor_features", "last_verified",
        "data_quality_status",
    ]

    report = {}

    for field in fields:
        if field not in df:
            continue

        count = int(
            df[field].map(is_unknown).sum()
        )

        report[field] = {
            "known": len(df) - count,
            "unknown": count,
            "coverage_pct": round(
                100 * (len(df) - count) / max(1, len(df)),
                1,
            ),
        }

    return report


def criteria_to_plain_text(criteria: dict) -> list[str]:
    return [
        value["label"]
        for value in criteria.values()
    ]
