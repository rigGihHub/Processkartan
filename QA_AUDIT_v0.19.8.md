# QA Audit – Maplini v0.19.8

## Scope
Standard shape presets for nodes plus improved automatic layout spacing / visual rhythm.

## Automated QA
- `python -m py_compile app.py`: PASS
- Python pytest: **232/232 passed**
- JavaScript test files: **27/27 passed**
- All `maplini_*_core.js` `node --check`: PASS
- Full Chromium `tests/browser_interaction_smoke.py`: PASS
- Shape persistence/normalization test in state core: PASS
- Critical DOM hierarchy: PASS
- Duplicate HTML IDs: **0**
- APP_VERSION: **0.19.8**

## Shape behavior
- `shapePreset` persists in normalized node data.
- Allowed values: `standard`, `rectangle`, `rounded`, `pill`.
- Invalid values fall back to `standard`.
- Shape changes reuse the existing multi-selection style update path.
- Decision nodes retain the diamond for Typstandard but can be explicitly overridden with a standard box shape.

## Layout rhythm
- Smart layout spacing changed from `118 / 52` to **132 / 64** for main-flow / cross-flow gaps.
- Existing layout, routing and undo behavior are otherwise unchanged.

## Data / migration
- No Supabase migration required.
- Existing process records remain backward-compatible because missing `shapePreset` normalizes to `standard`.

## Environment note
The Python environment emitted an unrelated artifact-tool spreadsheet warmup warning during startup; the Maplini commands themselves exited successfully.
