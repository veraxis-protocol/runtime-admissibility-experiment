# Validation Matrix

| Scenario | Static result | Runtime result | Demonstrated failure mode |
|---|---:|---:|---|
| `financial_transaction_state_change` | APPROVE | ESCALATE | Dynamic Classification Failure |
| `authority_revocation` | APPROVE | BLOCK | Authority Drift |
| `evidence_contradiction` | APPROVE | ESCALATE | Evidence Collapse |
| `execution_drift` | APPROVE | ESCALATE | Execution Drift |
| `context_loss` | APPROVE | ESCALATE | Context/State Incompatibility |
| `correction_unavailable` | APPROVE | ESCALATE | Correctability failure |
| `low_consequence_allowed` | APPROVE | APPROVE | No failure |
