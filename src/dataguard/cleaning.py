
import pandas as pd


def clean_dataframe(
    df,
    trim_whitespace=True,
    standardize_empty_strings=True,
    drop_duplicate_rows=False,
):
    """
    Apply safe, configurable cleaning operations.

    The original DataFrame is never modified.
    Missing values are not automatically deleted or filled.
    """

    cleaned_df = df.copy()

    original_rows = len(cleaned_df)
    original_missing = int(cleaned_df.isna().sum().sum())

    changes = {
        "trimmed_values": 0,
        "standardized_empty_strings": 0,
        "removed_duplicate_rows": 0,
    }

    # 1. Remove leading and trailing whitespace from text columns.
    if trim_whitespace:
        for column in cleaned_df.select_dtypes(
            include=["object", "string"]
        ).columns:
            original = cleaned_df[column].copy()

            cleaned_df[column] = cleaned_df[column].map(
                lambda value: value.strip()
                if isinstance(value, str)
                else value
            )

            changes["trimmed_values"] += int(
                (original != cleaned_df[column]).fillna(False).sum()
            )

    # 2. Convert empty strings to proper missing values.
    if standardize_empty_strings:
        for column in cleaned_df.select_dtypes(
            include=["object", "string"]
        ).columns:
            empty_mask = cleaned_df[column].eq("")
            changes["standardized_empty_strings"] += int(
                empty_mask.sum()
            )
            cleaned_df.loc[empty_mask, column] = pd.NA

    # 3. Remove completely duplicated rows only when requested.
    if drop_duplicate_rows:
        before = len(cleaned_df)
        cleaned_df = cleaned_df.drop_duplicates().copy()
        changes["removed_duplicate_rows"] = before - len(cleaned_df)

    summary = {
        "original_rows": original_rows,
        "cleaned_rows": len(cleaned_df),
        "original_missing_values": original_missing,
        "cleaned_missing_values": int(
            cleaned_df.isna().sum().sum()
        ),
        "changes": changes,
    }

    return cleaned_df, summary
