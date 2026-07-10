# Reviewer Guide

Inspect these files first:

1. `src/runtime_admissibility/predicates.py`
2. `src/runtime_admissibility/engines.py`
3. `scenarios/financial_transaction_state_change.json`
4. `tests/test_dcf_static_failure.py`
5. `results/sample_runtime_admissibility_output.json`

## Reviewer commands

```bash
pip install -e ".[dev]"
pytest
python -m runtime_admissibility.cli scenarios
```
