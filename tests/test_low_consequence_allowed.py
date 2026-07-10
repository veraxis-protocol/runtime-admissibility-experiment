from runtime_admissibility.engines import evaluate_runtime_admissibility, evaluate_static_authorization
from runtime_admissibility.simulation import load_scenario


def test_low_consequence_allowed_is_approved_by_both_systems() -> None:
    scenario = load_scenario("scenarios/low_consequence_allowed.json")
    static = evaluate_static_authorization(scenario)
    runtime = evaluate_runtime_admissibility(scenario)
    assert static.decision.value == "APPROVE"
    assert static.defective_reliance is False
    assert runtime.decision.value == "APPROVE"
    assert runtime.runtime_admissible is True
    assert runtime.failed_predicates == ()
