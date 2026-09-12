# QA Audit – Maplini v0.20.78 Unified Controls

## Scope
Visual-system pass only. No process-schema, Supabase, RLS or OAuth changes.

## Verification
- `python -m py_compile app.py`: PASS
- `pytest -q`: 479/479 PASS
- `node --check` across 30 `maplini_*_core.js` files: PASS
- 38 JavaScript core/unit test files: PASS
- `python tests/browser_v02078_unified_controls.py`: PASS
- `python tests/browser_interaction_smoke.py`: PASS

## Browser issue caught during QA
The process-name input still inherited the legacy blue focus outline because it has no explicit `type="text"` attribute. The unified selector was expanded to cover implicit text inputs and `.p48-name`; Chromium was rerun after the fix.

## Result
PASS – release candidate is packaged but not live/deployed.
