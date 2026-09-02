# QA Audit – Maplini v0.20.9

## Scope
Walkthrough Transition Polish: make Ja/Nej route transitions visually unambiguous on the existing canvas without adding administration or a permanent HUD.

## Implemented behavior
- Possible routed next nodes can show their existing connector label directly above the node during Follow Process.
- Once a route question resolves uniquely, non-selected alternatives disappear from the walkthrough emphasis.
- The selected target node receives a stronger but professional chosen state.
- The selected connector receives a stronger chosen-route state.
- Temporary route labels and chosen states are removed by the central walkthrough cleanup path.
- Existing v0.20.7 auto-advance and v0.20.8 canvas-follow behavior are preserved.
- Manual route handling and deviation requirements are unchanged.

## Automated QA
- `python -m py_compile app.py`: PASS
- Python pytest: **248/248 passed**
- JavaScript test files: **27/27 passed**
- `node --check` on all core JS files: **22/22 passed**
- Full Chromium `tests/browser_interaction_smoke.py`: PASS
- Critical DOM hierarchy: PASS
- Duplicate HTML IDs: **0**
- APP_VERSION: **0.20.9**

## Regression note
The inherited test suite contains exact release-string assertions. They were advanced from `0.20.8` to `0.20.9`; functional assertions were retained. Two focused regression tests were added for route badges/chosen-route states and cleanup.

## Data / migration
- No process-data schema change.
- No Supabase migration required.
