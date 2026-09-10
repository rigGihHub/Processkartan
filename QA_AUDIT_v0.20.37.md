# QA AUDIT – Maplini v0.20.37

## Scope
Lightweight Responsibility View based on existing `processInfo.responsibleRole`. No automatic node movement and no schema/RLS change.

## Results
- Python/pytest: 350/350 PASS
- JavaScript test files: 27/27 PASS
- Core JavaScript syntax (`node --check`): PASS
- Chromium browser interaction smoke: PASS
- Critical DOM: PASS
- Static duplicate IDs: PASS (see release validation)
- ZIP integrity: PASS after packaging

## Product guardrails
- Responsibility is an optional visual overlay, not a BPMN editor.
- Existing node positions and process logic are unchanged.
- Existing responsibleRole metadata is reused.
- No deviation/admin expansion.
- No Supabase migration, RLS or dependency change.
