from __future__ import annotations

from typing import Any, Mapping

from runtime_admissibility.models import Decision, EngineResult, PredicateResult
from runtime_admissibility.predicates import PREDICATES


def _classification_permissible(scenario: Mapping[str, Any]) -> bool:
    return scenario.get("t0", {}).get("classification") == "Permissible"


def _state_changed(scenario: Mapping[str, Any]) -> bool:
    return scenario.get("t0", {}).get("institutional_state") != scenario.get("t2", {}).get("institutional_state")


def _predicate_results(action: Mapping[str, Any], state: Mapping[str, Any]) -> tuple[PredicateResult, ...]:
    return tuple(predicate(action, state) for predicate in PREDICATES)


def _failure_modes(scenario: Mapping[str, Any], runtime_admissible: bool, failed: tuple[str, ...], re_evaluated: bool) -> tuple[str, ...]:
    modes: list[str] = []
    if _classification_permissible(scenario) and _state_changed(scenario) and not re_evaluated:
        modes.append("Dynamic Classification Failure")
    if not runtime_admissible:
        modes.append("Reliance Without Admissibility")
    if "valid_authority" in failed or "within_scope" in failed:
        modes.append("Authority Drift")
    if "sufficient_evidence" in failed:
        modes.append("Evidence Collapse")
    if "compatible_state" in failed:
        modes.append("Context or State Incompatibility")
    if "execution_integrity" in failed:
        modes.append("Execution Drift")
    if "correctable" in failed:
        modes.append("Correctability Failure")
    return tuple(dict.fromkeys(modes))


def evaluate_runtime_admissibility(scenario: Mapping[str, Any]) -> EngineResult:
    action = scenario["action"]
    current_state = scenario["t2"]
    results = _predicate_results(action, current_state)
    failed = tuple(result.name for result in results if not result.passed)
    admissible = not failed
    if admissible:
        decision = Decision.APPROVE
        explanation = "all runtime admissibility predicates passed"
    elif "valid_authority" in failed or "within_scope" in failed:
        decision = Decision.BLOCK
        explanation = "authority or scope predicate failed"
    else:
        decision = Decision.ESCALATE
        explanation = "one or more runtime predicates failed; review required"
    return EngineResult(
        decision=decision,
        runtime_admissible=admissible,
        defective_reliance=False,
        defective_reliance_prevented=not admissible,
        failed_predicates=failed,
        failure_modes=_failure_modes(scenario, admissible, failed, re_evaluated=True),
        predicate_results=results,
        explanation=explanation,
    )


def evaluate_static_authorization(scenario: Mapping[str, Any]) -> EngineResult:
    action = scenario["action"]
    current_state = scenario["t2"]
    runtime_results = _predicate_results(action, current_state)
    failed = tuple(result.name for result in runtime_results if not result.passed)
    runtime_admissible_at_t2 = not failed
    if _classification_permissible(scenario):
        decision = Decision.APPROVE
        defective = not runtime_admissible_at_t2
        explanation = "static system approved because action was permissible at classification time"
    else:
        decision = Decision.BLOCK
        defective = False
        explanation = "static system blocked because action was not permissible at classification time"
    return EngineResult(
        decision=decision,
        runtime_admissible=None,
        defective_reliance=defective,
        defective_reliance_prevented=False,
        failed_predicates=failed,
        failure_modes=_failure_modes(scenario, runtime_admissible_at_t2, failed, re_evaluated=False) if defective else tuple(),
        predicate_results=tuple(),
        explanation=explanation,
    )


def run_scenario(scenario: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "scenario_id": scenario["scenario_id"],
        "title": scenario.get("title", ""),
        "classification_time": scenario.get("classification_time", "t0"),
        "reliance_time": scenario.get("reliance_time", "t2"),
        "static_authorization_system": evaluate_static_authorization(scenario).to_dict(),
        "runtime_admissibility_system": evaluate_runtime_admissibility(scenario).to_dict(),
    }
