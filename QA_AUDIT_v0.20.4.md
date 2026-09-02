# QA Audit – Maplini v0.20.4

## Scope
Multi-selection formation feel, group movement, quick arrangement and keyboard nudging.

## Automated QA
- `python -m py_compile app.py`: PASS
- Python pytest: **238/238 passed**
- JavaScript test files: **27/27 passed**
- `node --check` on all core JS files: PASS
- Full Chromium `tests/browser_interaction_smoke.py`: PASS
- Critical DOM hierarchy: PASS
- Duplicate HTML IDs: **0**
- APP_VERSION: **0.20.4**

## Interaction behavior
- Two or more selected nodes display a temporary common selection hull.
- Hull updates live while selected nodes are dragged as a group.
- Multi-selection quick toolbar exposes align, distribute and selected-layout actions.
- Arrow keys nudge all selected nodes by 2 px; Shift+Arrow uses 20 px.
- Existing internal connector-via movement is preserved during group drag.
- Selection hull is visual only and is not persisted as process data.
- No reward mechanics were introduced.

## Regression note
Historical tests that asserted the old multi-selection arrange controls were removed were intentionally updated because v0.20.4 reintroduces them as a compact contextual multi-selection tool, not as the old global arrange UI.

## Data / migration
- No process-data schema change.
- No Supabase migration required.

## Environment note
The Python environment emitted an unrelated artifact-tool spreadsheet warmup warning while Maplini commands completed successfully.
