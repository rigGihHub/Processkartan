# QA Audit – Maplini v0.19.9

## Scope
Quick shape picker in the contextual node toolbar.

## Automated QA
- `python -m py_compile app.py`: PASS
- Python pytest: **233/233 passed**
- JavaScript test files: **27/27 passed**
- `node --check` on all core JS files: PASS
- Full Chromium `tests/browser_interaction_smoke.py`: PASS
- Critical DOM hierarchy: PASS
- Duplicate HTML IDs: **0**
- APP_VERSION: **0.19.9**

## Interaction behavior
- Shape picker exposes exactly four shape presets.
- Current/shared shape is reflected in the quick-toolbar icon.
- Multi-selection uses the existing `updateStyle()` path.
- A quick shape change is one existing undoable style operation.
- The picker closes after a shape is chosen.
- Full shape selection remains available under Utseende.

## Data / migration
- No data model change from v0.19.8.
- No Supabase migration required.

## Environment note
The Python environment emitted an unrelated artifact-tool spreadsheet warmup warning, while Maplini test commands completed successfully.
