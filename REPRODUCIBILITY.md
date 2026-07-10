# Reproducibility Statement

This repository is designed for deterministic reproduction of the paper's minimal experiment.

## Environment

- Python 3.10 or later
- No runtime dependencies beyond the Python standard library
- `pytest` for test execution

## Commands

```bash
pip install -e ".[dev]"
pytest
python -m runtime_admissibility.cli scenarios --out results/all_scenarios_output.json
```

## Determinism

The scenario files are static JSON documents. The engines do not use randomness, network access, external APIs, clocks, or live data.

## Data

All data are synthetic. No personal, confidential, financial, or customer data are included.

## Expected outputs

Sample outputs are included in `results/`. New outputs can be reproduced by running the CLI against `scenarios/`.
