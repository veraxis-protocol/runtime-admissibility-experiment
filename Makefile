.PHONY: install test run clean

install:
	python -m pip install -e ".[dev]"

test:
	pytest

run:
	python -m runtime_admissibility.cli scenarios --out results/all_scenarios_output.json

clean:
	rm -rf .pytest_cache .mypy_cache .ruff_cache build dist *.egg-info
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
