
import re

import pandas as pd


EMAIL_PATTERN = re.compile(
    r"^[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+@"
    r"[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+$"
)


def validate_dataframe(df, rules):
    """Run configurable data quality checks on a DataFrame."""

    results = []

    def add_result(rule, column, severity, failed_count, message):
        results.append({
            "rule": rule,
            "column": column,
            "severity": severity,
            "failed_count": int(failed_count),
            "passed": bool(failed_count == 0),
            "message": message,
        })

    # 1. Required columns
    for column in rules.get("required_columns", []):
        if column not in df.columns:
            add_result(
                "required_column",
                column,
                "ERROR",
                1,
                f"Required column '{column}' is missing.",
            )
        else:
            failed = df[column].isna().sum()
            add_result(
                "required_column",
                column,
                "ERROR",
                failed,
                f"Column '{column}' must not contain missing values.",
            )

    # 2. Unique values
    for column in rules.get("unique_columns", []):
        if column not in df.columns:
            continue

        failed = df[column].duplicated(keep="first").sum()
        add_result(
            "unique_values",
            column,
            "ERROR",
            failed,
            f"Column '{column}' must contain unique values.",
        )

    # 3. Email format
    for column in rules.get("email_columns", []):
        if column not in df.columns:
            continue

        values = df[column].dropna().astype(str).str.strip()
        failed = (~values.str.match(EMAIL_PATTERN)).sum()

        add_result(
            "valid_email",
            column,
            "ERROR",
            failed,
            f"Column '{column}' contains invalid email addresses.",
        )

    # 4. Date validity
    for column in rules.get("date_columns", []):
        if column not in df.columns:
            continue

        values = df[column].dropna()
        parsed = pd.to_datetime(values, errors="coerce")
        failed = parsed.isna().sum()

        add_result(
            "valid_date",
            column,
            "ERROR",
            failed,
            f"Column '{column}' contains invalid dates.",
        )

    # 5. Numeric validity
    for column in rules.get("numeric_columns", []):
        if column not in df.columns:
            continue

        values = df[column].dropna()
        numeric_values = pd.to_numeric(values, errors="coerce")
        failed = numeric_values.isna().sum()

        add_result(
            "numeric_values",
            column,
            "ERROR",
            failed,
            f"Column '{column}' must contain numeric values.",
        )

    # 6. Non-negative values
    for column in rules.get("non_negative_columns", []):
        if column not in df.columns:
            continue

        values = pd.to_numeric(df[column], errors="coerce")
        failed = (values < 0).sum()

        add_result(
            "non_negative_values",
            column,
            "ERROR",
            failed,
            f"Column '{column}' must not contain negative values.",
        )

    # 7. Allowed values
    for column, allowed in rules.get("allowed_values", {}).items():
        if column not in df.columns:
            continue

        values = df[column].dropna().astype(str).str.strip()
        failed = (~values.isin(allowed)).sum()

        add_result(
            "allowed_values",
            column,
            "WARNING",
            failed,
            f"Column '{column}' contains unexpected values.",
        )

    return results
