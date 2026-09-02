# QA Audit – Maplini v0.20.3

## Scope
Canvas-first process building rhythm and keyboard/direct-connection shortcuts.

## Automated QA
- `python -m py_compile app.py`: PASS
- Python pytest: **237/237 passed**
- JavaScript test files: **27/27 passed**
- `node --check` on all core JS files: PASS
- Full Chromium `tests/browser_interaction_smoke.py`: PASS
- Critical DOM hierarchy: PASS
- Duplicate HTML IDs: **0**
- APP_VERSION: **0.20.3**

## Interaction behavior
- Tab on one selected eligible node creates the recommended next step.
- Tab on Decision creates Ja/Nej branches.
- Shift+Tab opens the existing next-step choice menu.
- Enter on one selected node starts inline editing.
- Ctrl/Cmd+D remains the duplication shortcut; duplicates now receive immediate visual feedback and are brought into view.
- Dragging a connector more than 70 logical px to blank canvas creates and connects the recommended next node.
- Existing connector-to-existing-node behavior remains intact.
- No reward mechanics were introduced.

## Data / migration
- No process-data schema change.
- No Supabase migration required.

## Environment note
The Python environment may emit an unrelated artifact-tool spreadsheet warmup warning while Maplini commands complete successfully.
