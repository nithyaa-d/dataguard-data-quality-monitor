
import pytest

from src.dataguard.rules import load_rules


def test_load_valid_yaml_rules(tmp_path):
    config_file = tmp_path / "quality_rules.yaml"

    config_file.write_text(
        """
required_columns:
  - customer_id
  - email

unique_columns:
  - customer_id
""",
        encoding="utf-8",
    )

    rules = load_rules(config_file)

    assert "required_columns" in rules
    assert rules["required_columns"] == ["customer_id", "email"]
    assert rules["unique_columns"] == ["customer_id"]


def test_load_empty_yaml_file(tmp_path):
    config_file = tmp_path / "quality_rules.yaml"
    config_file.write_text("", encoding="utf-8")

    rules = load_rules(config_file)

    assert rules == {}


def test_missing_rules_file():
    with pytest.raises(FileNotFoundError):
        load_rules("nonexistent_rules.yaml")
