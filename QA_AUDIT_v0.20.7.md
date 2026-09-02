# QA Audit – Maplini v0.20.7

## Scope
Focused Follow Process interaction: single-question clarity, safe auto-advance and keyboard answering.

## Automated QA
- `python -m py_compile app.py`: PASS
- Python pytest: **242/242 passed**
- JavaScript test files: **27/27 passed**
- `node --check` on all core JS files: PASS
- Full Chromium `tests/browser_interaction_smoke.py`: PASS
- Critical DOM hierarchy: PASS
- Duplicate HTML IDs: **0**
- APP_VERSION: **0.20.7**

## Walkthrough behavior
- Single question renders without numeric prefix.
- J/N keyboard shortcuts answer Ja/Nej when one question is active.
- Quick synthetic question auto-advances when there is one next edge.
- Explicit control question auto-advances on Yes only when there is one next edge.
- Route question auto-advances only when automatic routing resolves a unique edge.
- Explicit control No that requires deviation details does not auto-advance.
- Zero deviation count is visually suppressed during an otherwise clean run.

## Data / migration
- No process-data schema change.
- No Supabase migration required.
