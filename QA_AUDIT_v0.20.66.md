# QA Audit – Maplini v0.20.66

## Scope
Contextual sidebar and step editor simplification only. No backend/schema/RLS/OAuth change.

## Verified
- `python -m py_compile app.py`: PASS
- `pytest -q`: 446 passed
- 33 JS core test files: PASS
- `node --check` for 30 `maplini_*_core.js` files: PASS
- `tests/browser_interaction_smoke.py`: PASS
- `tests/browser_v02065_ui_simplification.py`: PASS
- `tests/browser_v02066_contextual_sidebar.py`: PASS
- Context panel visually precedes build palette after selection in Chromium.
- Input/output controls exist once and inside step editor.
- Advanced fields stay collapsed until user opens **Mer om steget**.
- Existing IDs and persisted process fields preserved.
