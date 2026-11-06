
import pytest
import pandas as pd

from src.dataguard.validators import validate_dataframe


@pytest.fixture
def quality_rules():
    return {
        "required_columns": ["customer_id", "email", "revenue"],
        "unique_columns": ["customer_id"],
        "email_columns": ["email"],
        "date_columns": ["signup_date"],
        "numeric_columns": ["revenue"],
        "non_negative_columns": ["revenue"],
        "allowed_values": {
            "country": ["Sweden", "Norway"],
        },
    }


@pytest.fixture
def sample_dataframe():
    return pd.DataFrame({
        "customer_id": ["C001", "C002", "C002", None],
        "email": [
            "alice@example.com",
            "invalid-email",
            "charlie@example.com",
            None,
        ],
        "signup_date": [
            "2026-01-10",
            "not-a-date",
            "2026-03-15",
            "2026-04-01",
        ],
        "revenue": [100, -50, "invalid", 200],
        "country": ["Sweden", "Atlantis", "Norway", "Sweden"],
    })


def test_missing_required_values(sample_dataframe, quality_rules):
    results = validate_dataframe(sample_dataframe, quality_rules)

    customer_check = next(
        r for r in results
        if r["rule"] == "required_column"
        and r["column"] == "customer_id"
    )

    assert customer_check["failed_count"] == 1
    assert customer_check["passed"] is False


def test_duplicate_values(sample_dataframe, quality_rules):
    results = validate_dataframe(sample_dataframe, quality_rules)

    check = next(
        r for r in results
        if r["rule"] == "unique_values"
    )

    assert check["failed_count"] == 1


def test_invalid_emails(sample_dataframe, quality_rules):
    results = validate_dataframe(sample_dataframe, quality_rules)

    check = next(
        r for r in results
        if r["rule"] == "valid_email"
    )

    assert check["failed_count"] == 1


def test_invalid_dates(sample_dataframe, quality_rules):
    results = validate_dataframe(sample_dataframe, quality_rules)

    check = next(
        r for r in results
        if r["rule"] == "valid_date"
    )

    assert check["failed_count"] == 1


def test_non_numeric_values(sample_dataframe, quality_rules):
    results = validate_dataframe(sample_dataframe, quality_rules)

    check = next(
        r for r in results
        if r["rule"] == "numeric_values"
    )

    assert check["failed_count"] == 1


def test_negative_values(sample_dataframe, quality_rules):
    results = validate_dataframe(sample_dataframe, quality_rules)

    check = next(
        r for r in results
        if r["rule"] == "non_negative_values"
    )

    assert check["failed_count"] == 1


def test_unexpected_values(sample_dataframe, quality_rules):
    results = validate_dataframe(sample_dataframe, quality_rules)

    check = next(
        r for r in results
        if r["rule"] == "allowed_values"
        and r["column"] == "country"
    )

    assert check["failed_count"] == 1
    assert check["severity"] == "WARNING"


def test_missing_column_is_reported(sample_dataframe, quality_rules):
    quality_rules["required_columns"].append("phone_number")

    results = validate_dataframe(sample_dataframe, quality_rules)

    check = next(
        r for r in results
        if r["column"] == "phone_number"
    )

    assert check["passed"] is False
    assert check["failed_count"] == 1


def test_results_use_python_booleans(sample_dataframe, quality_rules):
    results = validate_dataframe(sample_dataframe, quality_rules)

    assert all(type(r["passed"]) is bool for r in results)
