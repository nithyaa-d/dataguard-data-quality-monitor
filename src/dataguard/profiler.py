"""Data profiling utilities for DataGuard."""

import pandas as pd
from pandas.api.types import is_numeric_dtype


def profile_dataframe(df: pd.DataFrame) -> dict:
    """
    Generate a data-quality profile for a pandas DataFrame.

    Args:
        df: Input pandas DataFrame.

    Returns:
        Dictionary containing dataset-level and column-level metrics.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")

    total_rows = len(df)
    total_columns = len(df.columns)

    column_profiles = []

    for column in df.columns:
        series = df[column]
        missing_count = int(series.isna().sum())

        column_profile = {
            "name": str(column),
            "data_type": str(series.dtype),
            "non_null_count": int(series.count()),
            "missing_count": missing_count,
            "missing_percentage": (
                round((missing_count / total_rows) * 100, 2)
                if total_rows > 0
                else 0.0
            ),
            "unique_count": int(series.nunique()),
        }

        if is_numeric_dtype(series):
            column_profile["statistics"] = {
                "minimum": (
                    float(series.min()) if series.notna().any() else None
                ),
                "maximum": (
                    float(series.max()) if series.notna().any() else None
                ),
                "mean": (
                    round(float(series.mean()), 2)
                    if series.notna().any()
                    else None
                ),
            }

        column_profiles.append(column_profile)

    return {
        "row_count": total_rows,
        "column_count": total_columns,
        "duplicate_row_count": int(df.duplicated().sum()),
        "total_missing_values": int(df.isna().sum().sum()),
        "columns": column_profiles,
    }