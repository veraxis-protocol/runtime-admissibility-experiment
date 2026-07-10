from pathlib import Path

from runtime_admissibility.simulation import load_scenario, run_path


def test_all_scenarios_validate() -> None:
    for scenario_file in Path("scenarios").glob("*.json"):
        scenario = load_scenario(scenario_file)
        assert scenario["scenario_id"]


def test_run_directory_returns_one_result_per_scenario() -> None:
    outputs = run_path("scenarios")
    assert len(outputs) == len(list(Path("scenarios").glob("*.json")))
    assert all("static_authorization_system" in output for output in outputs)
    assert all("runtime_admissibility_system" in output for output in outputs)
