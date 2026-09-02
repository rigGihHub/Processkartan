# QA Audit – Maplini v0.20.2

## Scope
Desktop navigation, zoom anchoring and marquee-selection feel.

## Automated QA
- `python -m py_compile app.py`: PASS
- Python pytest: **236/236 passed**
- JavaScript test files: **27/27 passed**
- `node --check` on all core JS files: PASS
- Full Chromium `tests/browser_interaction_smoke.py`: PASS
- Critical DOM hierarchy: PASS
- Duplicate HTML IDs: **0**
- APP_VERSION: **0.20.2**

## Interaction behavior
- Ctrl/Cmd + wheel zooms around the pointer position.
- Shift + wheel horizontal scroll behavior remains available.
- Spacebar temporarily enables pan without leaving selection mode.
- Middle mouse drag pans blank canvas.
- Marquee selection previews intersecting nodes before pointer release.
- Existing mobile pinch/pan path is unchanged.
- No reward mechanics were introduced.

## Data / migration
- No process-data schema change.
- No Supabase migration required.

## Environment note
The Python environment may emit an unrelated artifact-tool spreadsheet warmup warning while Maplini commands complete successfully.
