from __future__ import annotations

from typing import Any, Mapping

from runtime_admissibility.models import PredicateResult


def _get(state: Mapping[str, Any], *path: str, default: Any = None) -> Any:
    current: Any = state
    for key in path:
        if not isinstance(current, Mapping) or key not in current:
            return default
        current = current[key]
    return current


def valid_authority(action: Mapping[str, Any], state: Mapping[str, Any]) -> PredicateResult:
    authority = _get(state, "authority", default={})
    if not authority.get("valid", False):
        return PredicateResult("valid_authority", False, "authority envelope is invalid")
    action_type = action.get("type")
    permitted = authority.get("permitted_action_types", [])
    if action_type not in permitted:
        return PredicateResult("valid_authority", False, f"action type {action_type!r} is not permitted")
    return PredicateResult("valid_authority", True, "current authority envelope permits action type")


def sufficient_evidence(action: Mapping[str, Any], state: Mapping[str, Any]) -> PredicateResult:
    evidence = _get(state, "evidence", default={})
    if not evidence.get("sufficient", False):
        return PredicateResult("sufficient_evidence", False, "evidence is insufficient")
    if evidence.get("contradicted", False):
        return PredicateResult("sufficient_evidence", False, "evidence is contradicted")
    if not evidence.get("current", False):
        return PredicateResult("sufficient_evidence", False, "evidence is not current")
    return PredicateResult("sufficient_evidence", True, "evidence is sufficient, current, and not contradicted")


def compatible_state(action: Mapping[str, Any], state: Mapping[str, Any]) -> PredicateResult:
    institutional_state = _get(state, "institutional_state", default={})
    account_status = institutional_state.get("account_status")
    counterparty_status = institutional_state.get("counterparty_status")
    review_required = institutional_state.get("threshold_review_required", False)
    if account_status not in {"active", "normal"}:
        return PredicateResult("compatible_state", False, f"account status is {account_status!r}")
    if counterparty_status != "clear":
        return PredicateResult("compatible_state", False, f"counterparty status is {counterparty_status!r}")
    if review_required:
        return PredicateResult("compatible_state", False, "threshold review is required before reliance")
    return PredicateResult("compatible_state", True, "current institutional state is compatible")


def within_scope(action: Mapping[str, Any], state: Mapping[str, Any]) -> PredicateResult:
    authority = _get(state, "authority", default={})
    amount = action.get("amount", 0)
    max_amount = authority.get("max_amount")
    consequence_class = action.get("consequence_class")
    allowed_classes = authority.get("allowed_consequence_classes", [])
    if max_amount is not None and amount > max_amount:
        return PredicateResult("within_scope", False, f"amount {amount} exceeds authority maximum {max_amount}")
    if consequence_class not in allowed_classes:
        return PredicateResult("within_scope", False, f"consequence class {consequence_class!r} is outside delegated scope")
    return PredicateResult("within_scope", True, "action is within delegated scope")


def consequence_bounded(action: Mapping[str, Any], state: Mapping[str, Any]) -> PredicateResult:
    consequence = action.get("consequence_class")
    recognized = _get(state, "recognized_consequence_classes", default=[])
    if consequence not in recognized:
        return PredicateResult("consequence_bounded", False, f"consequence class {consequence!r} is not recognized")
    return PredicateResult("consequence_bounded", True, "consequence class is recognized and bounded")


def execution_integrity(action: Mapping[str, Any], state: Mapping[str, Any]) -> PredicateResult:
    execution = _get(state, "execution", default={})
    if not execution.get("matches_evaluated_action", False):
        return PredicateResult("execution_integrity", False, "execution action differs from evaluated action")
    return PredicateResult("execution_integrity", True, "execution matches evaluated action")


def correctable(action: Mapping[str, Any], state: Mapping[str, Any]) -> PredicateResult:
    correction = _get(state, "correction", default={})
    if not correction.get("available", False):
        return PredicateResult("correctable", False, "correction or challenge path is unavailable")
    return PredicateResult("correctable", True, "correction or challenge path remains available")


PREDICATES = (
    valid_authority,
    sufficient_evidence,
    compatible_state,
    within_scope,
    consequence_bounded,
    execution_integrity,
    correctable,
)
