# QA Audit v0.20.70 – Read Scan Guide

- `python -m py_compile app.py`: PASS
- `pytest -q`: 457 passed
- All `maplini_*_core.js` via `node --check`: PASS
- All JS unit tests: PASS
- `tests/browser_interaction_smoke.py`: PASS
- Read guide remains read-mode only; no process data/schema/RLS/OAuth changes.
- Start/end navigation uses existing node selection + viewport visibility.
- Decision branches are never ranked or inferred as a main path.
