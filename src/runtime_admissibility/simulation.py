from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from runtime_admissibility.engines import run_scenario


def load_scenario(path: str | Path) -> dict[str, Any]:
    with Path(path).open("r", encoding="utf-8") as fh:
        data = json.load(fh)
    validate_scenario(data)
    return data


def validate_scenario(scenario: dict[str, Any]) -> None:
    required = {"scenario_id", "title", "classification_time", "reliance_time", "action", "t0", "t2", "expected"}
    missing = required.difference(scenario)
    if missing:
        raise ValueError(f"scenario missing required fields: {sorted(missing)}")
    for state_name in ("t0", "t2"):
        state = scenario[state_name]
        for key in ("authority", "evidence", "institutional_state", "execution", "correction", "recognized_consequence_classes"):
            if key not in state:
                raise ValueError(f"{state_name} missing {key}")


def run_path(path: str | Path) -> list[dict[str, Any]]:
    p = Path(path)
    if p.is_dir():
        return [run_scenario(load_scenario(scenario_file)) for scenario_file in sorted(p.glob("*.json"))]
    return [run_scenario(load_scenario(p))]


def write_json(path: str | Path, payload: Any) -> None:
    with Path(path).open("w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=2, sort_keys=True)
        fh.write("\n")
