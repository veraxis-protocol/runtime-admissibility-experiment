# Runtime Admissibility Experiment

**Runtime Admissibility Experiment** is a minimal, deterministic, reviewable research repository accompanying the paper:

> **Runtime Admissibility as a Computational Primitive for Institutional Reliance**  
> Arkadiy Miteiko and Ignacio Adrian Lerer, 2026

The repository demonstrates a precise computational distinction:

1. a **static authorization system** may continue relying on a prior permissibility classification after institutional state has changed;
2. a **runtime admissibility system** re-evaluates current authority, evidence, state, scope, consequence, execution integrity, and correctability before institutional reliance.

The primary demonstrated failure mode is **Dynamic Classification Failure (DCF)**.

---

## Core formal claim

Institutional reliance on a machine-generated action requires runtime admissibility at the moment of reliance:

```math
Rel(x,t) \Rightarrow RA(x,t)
```

Defective reliance occurs when an institution relies without runtime admissibility:

```math
Rel(x,t) \land \neg RA(x,t)
```

Runtime admissibility is modeled as a conjunctive predicate:

```math
RA(x,t) \Leftrightarrow
VA(x,A_t) \land SE(x,E_t) \land CS(x,S_t) \land WS(x,A_t,C)
\land CB(x,C) \land EI(x,t) \land COR(x,C)
```

| Predicate | Meaning |
|---|---|
| `VA(x,A_t)` | Valid authority exists for action `x` under current authority envelope `A_t`. |
| `SE(x,E_t)` | Sufficient evidence exists under current evidentiary basis `E_t`. |
| `CS(x,S_t)` | Action `x` is compatible with current institutional state `S_t`. |
| `WS(x,A_t,C)` | Action `x` is within delegated scope for consequence class `C`. |
| `CB(x,C)` | Consequence class `C` is bounded and recognized. |
| `EI(x,t)` | Execution integrity is preserved at time `t`. |
| `COR(x,C)` | Correction, challenge, or remediation remains available. |

---

## What this repository demonstrates

### System A: Static authorization

Checks whether an action was permissible at `t0`.

It does **not** re-evaluate current institutional state at `t2`.

Under material state change, it may produce:

```text
APPROVE -> defective reliance
```

### System B: Runtime admissibility

Checks all runtime admissibility predicates at `t2`.

Under material state change, it produces:

```text
ESCALATE or BLOCK -> defective reliance prevented
```

---

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
pytest
```

Run one simulation:

```bash
python -m runtime_admissibility.cli scenarios/financial_transaction_state_change.json
```

Run all scenarios:

```bash
python -m runtime_admissibility.cli scenarios --out results/all_scenarios_output.json
```

---

## Repository layout

```text
runtime-admissibility-experiment/
  README.md
  LICENSE
  CITATION.cff
  CODE_OF_CONDUCT.md
  CONTRIBUTING.md
  SECURITY.md
  REPRODUCIBILITY.md
  Makefile
  pyproject.toml
  requirements-dev.txt
  .gitignore
  .github/workflows/tests.yml
  .github/ISSUE_TEMPLATE/bug_report.md
  .github/ISSUE_TEMPLATE/scenario_request.md
  docs/
    formal_model.md
    experiment_protocol.md
    scenario_schema.md
    reviewer_guide.md
    validation_matrix.md
  ontology/
    predicates.json
  paper/
    formal_model.md
  scenarios/
    financial_transaction_state_change.json
    authority_revocation.json
    evidence_contradiction.json
    execution_drift.json
    context_loss.json
    correction_unavailable.json
    low_consequence_allowed.json
  src/runtime_admissibility/
    __init__.py
    models.py
    predicates.py
    engines.py
    simulation.py
    cli.py
  tests/
    test_dcf_static_failure.py
    test_runtime_admissibility_blocks.py
    test_authority_revocation.py
    test_evidence_contradiction.py
    test_execution_drift.py
    test_context_loss.py
    test_correction_unavailable.py
    test_low_consequence_allowed.py
    test_scenario_schema.py
  results/
    sample_static_failure_output.json
    sample_runtime_admissibility_output.json
```

---

## Expected primary result

For the primary DCF scenario, the static authorization system approves the transaction because it was permissible at `t0`.

The runtime admissibility system escalates because the current state at `t2` invalidates the state-compatibility predicate.

```json
{
  "scenario_id": "financial_transaction_state_change",
  "static_authorization_system": {
    "decision": "APPROVE",
    "defective_reliance": true,
    "failure_modes": ["Dynamic Classification Failure", "Reliance Without Admissibility"]
  },
  "runtime_admissibility_system": {
    "decision": "ESCALATE",
    "runtime_admissible": false,
    "defective_reliance_prevented": true,
    "failed_predicates": ["compatible_state"]
  }
}
```

---

## Research artifact boundaries

This repository is intentionally:

- **implementation-independent**: no commercial platform assumptions;
- **deterministic**: same scenario files produce the same outputs;
- **auditable**: each predicate returns reasons, not just booleans;
- **extensible**: new scenarios can be added without changing engine logic;
- **safe for peer review**: no personal, customer, financial, or confidential data.

This repository does **not** provide legal advice, regulatory certification, financial compliance certification, or a production governance system.

---

## Citation

Use `CITATION.cff` for software citation metadata.

---

## License

MIT License.
