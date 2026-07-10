from runtime_admissibility.engines import evaluate_runtime_admissibility
from runtime_admissibility.simulation import load_scenario


def test_context_loss_escalates() -> None:
    scenario = load_scenario("scenarios/context_loss.json")
    runtime = evaluate_runtime_admissibility(scenario)
    assert runtime.decision.value == "ESCALATE"
    assert runtime.failed_predicates == ("compatible_state",)
