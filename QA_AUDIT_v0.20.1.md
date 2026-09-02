# QA Audit – Maplini v0.20.1

## Scope
Tactile canvas interaction without reward mechanics.

## Automated QA
- `python -m py_compile app.py`: PASS
- Python pytest: **235/235 passed**
- JavaScript test files: **27/27 passed**
- `node --check` on all core JS files: PASS
- Full Chromium `tests/browser_interaction_smoke.py`: PASS
- Critical DOM hierarchy: PASS
- Duplicate HTML IDs: **0**
- APP_VERSION: **0.20.1**

## Interaction behavior
- FLOW streak / reward UI removed.
- Dragging a node adds temporary lift feedback.
- Magnetic alignment adds temporary snap feedback and stronger guides.
- Connector drag previews valid targets.
- Valid connector targets use a temporary highlight and the preview line changes state.
- Completed connection gives a short confirmation pulse only.
- Walkthrough Ja/Nej use the same neutral press animation.
- `prefers-reduced-motion` disables motion feedback.

## Data / migration
- No process data schema change.
- No Supabase migration required.

## Environment note
The Python environment emitted an unrelated artifact-tool spreadsheet warmup warning while Maplini commands completed successfully.
