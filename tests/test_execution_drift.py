from runtime_admissibility.engines import evaluate_runtime_admissibility
from runtime_admissibility.simulation import load_scenario


def test_execution_drift_escalates() -> None:
    scenario = load_scenario("scenarios/execution_drift.json")
    runtime = evaluate_runtime_admissibility(scenario)
    assert runtime.decision.value == "ESCALATE"
    assert runtime.failed_predicates == ("execution_integrity",)
