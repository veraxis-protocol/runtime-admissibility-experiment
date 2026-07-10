from runtime_admissibility.engines import evaluate_static_authorization
from runtime_admissibility.simulation import load_scenario


def test_static_authorization_produces_dcf_under_state_change() -> None:
    scenario = load_scenario("scenarios/financial_transaction_state_change.json")
    result = evaluate_static_authorization(scenario)
    assert result.decision.value == "APPROVE"
    assert result.defective_reliance is True
    assert "Dynamic Classification Failure" in result.failure_modes
    assert "Reliance Without Admissibility" in result.failure_modes
