
"""Automated tests for the AI City Discovery recommendation engine.

Run:
    python -m pytest test_engine.py -v
"""

import pandas as pd
import pytest

from recommendation_engine import (
    assess_request_criterion,
    extract_preferences,
    extract_request_criteria,
    get_place_tags,
    is_unknown,
    missing_information,
    rank,
    read_places,
)


# ---------------------------------------------------------------------
# FIXTURES
# ---------------------------------------------------------------------

@pytest.fixture
def sample_place():
    return {
        "name": "Example Cafe",
        "category": "Cafe",
        "description": "A neighborhood cafe serving coffee.",
        "neighborhood": "Jaffa",
        "features": "quiet atmosphere, creative space",
        "atmosphere": "quiet and artistic",
        "activities": "reading, conversation",
        "environment": "indoor and outdoor",
        "outdoor_features": "courtyard seating",
        "amenities": "outdoor seating",
        "dietary_options": "vegetarian",
        "kosher_status": "unknown",
        "price_level": "unknown",
        "price_level_numeric": float("nan"),
        "rating": "unknown",
        "opening_hours": "unknown",
        "semantic_score": 0.8,
    }


@pytest.fixture
def sample_dataframe(sample_place):
    return pd.DataFrame([sample_place])


# ---------------------------------------------------------------------
# UNKNOWN DATA
# ---------------------------------------------------------------------

def test_unknown_values():
    assert is_unknown("unknown")
    assert is_unknown("")
    assert is_unknown(None)
    assert not is_unknown("quiet")


# ---------------------------------------------------------------------
# PREFERENCE EXTRACTION
# ---------------------------------------------------------------------

def test_extract_cafe_preference():
    preferences, scores, method = extract_preferences(
        "I want a nice cafe."
    )

    assert "cafe" in preferences
    assert scores["cafe"] == 1.0


def test_extract_vegan_preference():
    preferences, _, _ = extract_preferences(
        "I am looking for vegan food."
    )

    assert "vegan" in preferences


def test_extract_multiple_preferences():
    preferences, _, _ = extract_preferences(
        "I want a quiet cafe near the beach."
    )

    assert "cafe" in preferences
    assert "quiet" in preferences
    assert "beach" in preferences


# ---------------------------------------------------------------------
# NATURAL-LANGUAGE CRITERIA
# ---------------------------------------------------------------------

def test_detect_not_touristy():
    criteria = extract_request_criteria(
        "I don't want a touristy place."
    )

    assert "non_touristy" in criteria


def test_detect_not_crowded():
    criteria = extract_request_criteria(
        "I want somewhere not too crowded."
    )

    assert "not_crowded" in criteria


def test_detect_outdoor_seating():
    criteria = extract_request_criteria(
        "I want to sit outside."
    )

    assert "outdoor_seating" in criteria


def test_detect_quiet():
    criteria = extract_request_criteria(
        "I am looking for a peaceful place."
    )

    assert "quiet" in criteria


# ---------------------------------------------------------------------
# PLACE TAGS
# ---------------------------------------------------------------------

def test_place_tags_include_cafe(sample_place):
    tags = get_place_tags(sample_place)

    assert "cafe" in tags


def test_place_tags_include_vegetarian(sample_place):
    tags = get_place_tags(sample_place)

    assert "vegetarian" in tags


# ---------------------------------------------------------------------
# EVIDENCE ASSESSMENT
# ---------------------------------------------------------------------

def test_outdoor_seating_supported(sample_place):
    criterion = extract_request_criteria(
        "I want outdoor seating."
    )["outdoor_seating"]

    status, evidence = assess_request_criterion(
        sample_place,
        criterion,
    )

    assert status == "supported"
    assert evidence


def test_missing_evidence_is_unknown(sample_place):
    sample_place["outdoor_features"] = "unknown"
    sample_place["amenities"] = "unknown"

    criterion = extract_request_criteria(
        "I want outdoor seating."
    )["outdoor_seating"]

    status, evidence = assess_request_criterion(
        sample_place,
        criterion,
    )

    assert status == "unknown"
    assert evidence == []


def test_contradictory_evidence(sample_place):
    sample_place["outdoor_features"] = "indoor only"
    sample_place["amenities"] = "no outdoor seating"

    criterion = extract_request_criteria(
        "I want outdoor seating."
    )["outdoor_seating"]

    status, _ = assess_request_criterion(
        sample_place,
        criterion,
    )

    assert status == "contradicted"


# ---------------------------------------------------------------------
# RANKING
# ---------------------------------------------------------------------

def test_rank_returns_results(sample_place):
    results = rank(
        candidates=[sample_place],
        preferences=["cafe"],
        number=3,
        query="I want a quiet cafe.",
    )

    assert len(results) == 1
    assert results[0]["name"] == "Example Cafe"


def test_rank_score_is_bounded(sample_place):
    results = rank(
        candidates=[sample_place],
        preferences=["cafe", "quiet"],
        number=3,
        query="I want a quiet cafe.",
    )

    score = results[0]["recommendation_score"]

    assert 0.0 <= score <= 1.0


def test_rank_includes_criterion_assessment(sample_place):
    results = rank(
        candidates=[sample_place],
        preferences=["cafe"],
        number=3,
        query="I want outdoor seating.",
    )

    assert "Outdoor seating" in (
        results[0]["criterion_assessments"]
    )


# ---------------------------------------------------------------------
# MISSING INFORMATION
# ---------------------------------------------------------------------

def test_missing_information_detected(sample_place):
    missing = missing_information(sample_place)

    assert "Price level" in missing
    assert "Rating" in missing
    assert "Opening hours" in missing


def test_missing_information_not_empty(sample_place):
    missing = missing_information(sample_place)

    assert isinstance(missing, list)


# ---------------------------------------------------------------------
# CSV LOADING
# ---------------------------------------------------------------------

def test_read_places(tmp_path):
    csv_file = tmp_path / "places.csv"

    pd.DataFrame(
        [
            {
                "name": "Test Cafe",
                "category": "Cafe",
                "description": "A test cafe.",
                "neighborhood": "Jaffa",
            }
        ]
    ).to_csv(
        csv_file,
        index=False,
    )

    df = read_places(csv_file)

    assert len(df) == 1
    assert df.iloc[0]["name"] == "Test Cafe"
    assert "search_text" in df.columns
    assert "price_level_numeric" in df.columns


def test_read_places_rejects_missing_required_columns(tmp_path):
    csv_file = tmp_path / "invalid.csv"

    pd.DataFrame(
        [
            {
                "name": "Test Cafe",
                "category": "Cafe",
            }
        ]
    ).to_csv(
        csv_file,
        index=False,
    )

    with pytest.raises(ValueError):
        read_places(csv_file)
