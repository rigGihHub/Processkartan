# QA Audit – Maplini v0.20.0

## Scope
Game-feel microinteractions for process building and Follow Process.

## Automated QA
- `python -m py_compile app.py`: PASS
- Python pytest: **234/234 passed**
- JavaScript test files: **27/27 passed**
- `node --check` on all core JS files: PASS
- Full Chromium `tests/browser_interaction_smoke.py`: **PASS**
- Critical DOM hierarchy: PASS
- Duplicate HTML IDs: **0**
- APP_VERSION: **0.20.0**

## Game-feel behavior
- `FLOW ×N` is based only on actual consecutive build actions within a 12-second window.
- New nodes created through Smart Next / decision branches receive transient spawn feedback.
- Walkthrough Ja/Nej answers receive transient visual feedback.
- Successful no-deviation walkthrough summary receives a short success pulse.
- `prefers-reduced-motion` disables the new animations.

## Data / migration
- No process-data schema change.
- No Supabase migration required.

## Environment note
The Python environment emitted an unrelated artifact-tool spreadsheet warmup warning while Maplini test commands completed successfully.
