# Contributing

Contributions are welcome if they improve reproducibility, clarity, formal precision, or scenario coverage.

## Good contributions

- Add a new scenario demonstrating one of the failure modes.
- Improve predicate explanations or reason traces.
- Add tests that make expected behavior more explicit.
- Improve documentation without turning the repository into a vendor implementation.
- Add formal-model notes that remain implementation-independent.

## Contribution rules

1. Keep scenarios synthetic.
2. Do not include confidential, personal, customer, or regulated data.
3. Do not add commercial platform dependencies.
4. Keep predicates deterministic unless a future paper explicitly introduces probabilistic admissibility.
5. Every new scenario must include:
   - `scenario_id`
   - `classification_time`
   - `reliance_time`
   - `action`
   - `t0`
   - `t2`
   - `expected`
6. Every new failure mode must have at least one test.

## Development workflow

```bash
pip install -e ".[dev]"
pytest
python -m runtime_admissibility.cli scenarios
```
