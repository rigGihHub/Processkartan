# QA Audit – Maplini v0.20.17

Release: **Connector Crossing Reduction**

## Scope
- Auto-managed orthogonal connectors now score real interior crossings against unrelated existing connector segments.
- Node collisions remain the strongest routing constraint.
- Shared source/target fan-out is exempt from crossing penalties.
- Candidate corridors from existing connector geometry are bounded to keep mixed-anchor routing scalable.
- Manual routing, free routing and manual anchor modes remain untouched.
- No data model or Supabase migration.

## Verification
- `python -m py_compile app.py`: PASS
- Python pytest: **265/265 PASS**
- JavaScript test files: **27/27 PASS**
- Core JavaScript `node --check`: **22/22 PASS**
- Chromium browser interaction smoke: PASS
- Critical DOM contract: PASS
- Literal HTML IDs: **273**, duplicates: **0**
- APP_VERSION: **0.20.17**

## Targeted routing checks
- Base orthogonal route with an unrelated connector crossing is detected.
- Smart orthogonal routing can choose a zero-crossing alternate corridor.
- Shared source/target connectors are not penalized as avoidable crossings.
- Crossing avoidance works even when there are no node obstacles.
- Corridor candidates are capped to the most relevant values near the natural route.

## Browser smoke note
During QA, the existing `<details>` menu smoke assertion was intermittently faster than Chromium's queued native `toggle` event. The test harness now waits 20 ms before asserting that unrelated menus closed. Repeated browser-smoke runs passed after this timing stabilization; no product menu behavior was changed for this item.
