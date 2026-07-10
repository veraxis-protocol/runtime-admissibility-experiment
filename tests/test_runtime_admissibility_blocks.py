from runtime_admissibility.engines import evaluate_runtime_admissibility
from runtime_admissibility.simulation import load_scenario


def test_runtime_admissibility_escalates_state_change() -> None:
    scenario = load_scenario("scenarios/financial_transaction_state_change.json")
    result = evaluate_runtime_admissibility(scenario)
    assert result.decision.value == "ESCALATE"
    assert result.runtime_admissible is False
    assert result.defective_reliance_prevented is True
    assert result.failed_predicates == ("compatible_state",)
