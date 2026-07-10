from runtime_admissibility.engines import evaluate_runtime_admissibility, evaluate_static_authorization
from runtime_admissibility.simulation import load_scenario


def test_authority_revocation_blocks_runtime_reliance() -> None:
    scenario = load_scenario("scenarios/authority_revocation.json")
    static = evaluate_static_authorization(scenario)
    runtime = evaluate_runtime_admissibility(scenario)
    assert static.decision.value == "APPROVE"
    assert static.defective_reliance is True
    assert runtime.decision.value == "BLOCK"
    assert runtime.failed_predicates == ("valid_authority",)
