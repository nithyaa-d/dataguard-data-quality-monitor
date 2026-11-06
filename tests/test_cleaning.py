
import pandas as pd

from src.dataguard.cleaning import clean_dataframe


def test_trim_whitespace():
    df = pd.DataFrame({
        "name": [" Alice ", "Bob "]
    })

    cleaned, summary = clean_dataframe(df)

    assert cleaned["name"].tolist() == ["Alice", "Bob"]
    assert summary["changes"]["trimmed_values"] == 2


def test_standardize_empty_strings():
    df = pd.DataFrame({
        "email": ["alice@example.com", ""]
    })

    cleaned, summary = clean_dataframe(df)

    assert pd.isna(cleaned.loc[1, "email"])
    assert summary["changes"]["standardized_empty_strings"] == 1


def test_drop_duplicate_rows():
    df = pd.DataFrame({
        "id": [1, 2, 2],
        "name": ["Alice", "Bob", "Bob"]
    })

    cleaned, summary = clean_dataframe(
        df,
        drop_duplicate_rows=True
    )

    assert len(cleaned) == 2
    assert summary["changes"]["removed_duplicate_rows"] == 1


def test_duplicates_preserved_by_default():
    df = pd.DataFrame({
        "id": [1, 1, 2]
    })

    cleaned, summary = clean_dataframe(df)

    assert len(cleaned) == 3
    assert summary["changes"]["removed_duplicate_rows"] == 0


def test_original_dataframe_is_not_modified():
    df = pd.DataFrame({
        "name": [" Alice "]
    })

    original = df.copy()

    clean_dataframe(df)

    pd.testing.assert_frame_equal(df, original)


def test_cleaning_summary():
    df = pd.DataFrame({
        "name": [" Alice ", "Bob"],
        "email": ["", "bob@example.com"]
    })

    cleaned, summary = clean_dataframe(df)

    assert summary["original_rows"] == 2
    assert summary["cleaned_rows"] == 2
    assert summary["original_missing_values"] == 0
    assert summary["cleaned_missing_values"] == 1
