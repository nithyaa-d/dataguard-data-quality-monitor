
from pathlib import Path

import yaml


def load_rules(config_path="config/quality_rules.yaml"):
    """Load data quality rules from a YAML configuration file."""

    path = Path(config_path)

    if not path.exists():
        raise FileNotFoundError(
            f"Quality rules file not found: {path}"
        )

    with path.open("r", encoding="utf-8") as file:
        rules = yaml.safe_load(file)

    return rules or {}
