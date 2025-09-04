"""Basic tests for configuration loading."""
from __future__ import annotations

import json


def test_config_contains_required_fields() -> None:
    with open("config/config.json", "r", encoding="utf-8") as f:
        cfg = json.load(f)
    assert {"start", "end", "cash", "strategy", "stocks"} <= cfg.keys()
    assert isinstance(cfg["stocks"], list) and cfg["stocks"]
