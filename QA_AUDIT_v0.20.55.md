# QA AUDIT v0.20.55

Release focus: Source Change Detection.

## Implemented
- Deterministic comparison of stored source evidence against a newly uploaded source version.
- Classifies source traces as unchanged, changed, missing, or unknown.
- Shows old evidence and nearest new evidence for review.
- Never rewrites the process automatically.
- Existing source traceability remains intact.

## QA executed
- `python -m py_compile app.py` — PASS
- `pytest -q` — PASS, 420 tests
- all `tests/*.js` via Node — PASS
- `node --check maplini_*_core.js` — PASS
- `browser_v02054_understand_relations.py` — PASS
- `browser_v02055_source_change.py` — PASS
- `browser_interaction_smoke.py` — PASS
- Critical embedded-core placeholder coverage — PASS after adding Source Change core to browser harness

## Release judgment
Push-ready candidate. Not verified live. Do not claim deployed/live.
