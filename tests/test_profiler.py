
import pandas as pd

from src.dataguard.profiler import profile_dataframe


def test_profile_returns_correct_dimensions():
    df = pd.DataFrame({
        "customer_id": ["C001", "C002", "C003"],
        "revenue": [100, 200, 300],
    })

    result = profile_dataframe(df)

    assert result["row_count"] == 3
    assert result["column_count"] == 2


def test_profile_counts_missing_values():
    df = pd.DataFrame({
        "name": ["Alice", None, "Charlie"],
        "revenue": [100, None, 300],
    })

    result = profile_dataframe(df)

    assert result["total_missing_values"] == 2

    profiles = {
        column["name"]: column
        for column in result["columns"]
    }

    assert profiles["name"]["missing_count"] == 1
    assert profiles["revenue"]["missing_count"] == 1


def test_profile_detects_duplicate_rows():
    df = pd.DataFrame({
        "customer_id": ["C001", "C002", "C002"],
        "name": ["Alice", "Bob", "Bob"],
    })

    result = profile_dataframe(df)

    assert result["duplicate_row_count"] == 1


def test_profile_calculates_numeric_statistics():
    df = pd.DataFrame({
        "revenue": [100, 200, 300],
    })

    result = profile_dataframe(df)

    revenue_profile = result["columns"][0]

    assert revenue_profile["statistics"]["minimum"] == 100
    assert revenue_profile["statistics"]["maximum"] == 300
    assert revenue_profile["statistics"]["mean"] == 200


def test_profile_handles_empty_dataframe():
    df = pd.DataFrame()

    result = profile_dataframe(df)

    assert result["row_count"] == 0
    assert result["column_count"] == 0
    assert result["duplicate_row_count"] == 0
    assert result["total_missing_values"] == 0
