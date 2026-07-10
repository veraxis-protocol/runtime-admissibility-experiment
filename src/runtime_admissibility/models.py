from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any, Mapping


class Decision(str, Enum):
    APPROVE = "APPROVE"
    ESCALATE = "ESCALATE"
    BLOCK = "BLOCK"


@dataclass(frozen=True)
class PredicateResult:
    name: str
    passed: bool
    reason: str


@dataclass(frozen=True)
class EngineResult:
    decision: Decision
    runtime_admissible: bool | None
    defective_reliance: bool
    defective_reliance_prevented: bool
    failed_predicates: tuple[str, ...]
    failure_modes: tuple[str, ...]
    predicate_results: tuple[PredicateResult, ...]
    explanation: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "decision": self.decision.value,
            "runtime_admissible": self.runtime_admissible,
            "defective_reliance": self.defective_reliance,
            "defective_reliance_prevented": self.defective_reliance_prevented,
            "failed_predicates": list(self.failed_predicates),
            "failure_modes": list(self.failure_modes),
            "predicate_results": [
                {"name": r.name, "passed": r.passed, "reason": r.reason}
                for r in self.predicate_results
            ],
            "explanation": self.explanation,
        }


Scenario = Mapping[str, Any]
State = Mapping[str, Any]
