# Scenario Schema

Each scenario is a JSON file with these top-level fields:

```json
{
  "scenario_id": "string",
  "title": "string",
  "classification_time": "t0",
  "reliance_time": "t2",
  "action": {},
  "t0": {},
  "t2": {},
  "expected": {}
}
```

Each `t0` and `t2` state must include:

- `authority`
- `evidence`
- `institutional_state`
- `execution`
- `correction`
- `recognized_consequence_classes`
