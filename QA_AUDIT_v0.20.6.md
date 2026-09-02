# QA Audit – Maplini v0.20.6

## Scope
Visual flow rhythm for newly created steps and local flow emphasis.

## Automated QA
- `python -m py_compile app.py`: PASS
- Python pytest: **240/240 passed**
- JavaScript test files: **27/27 passed**
- `node --check` on all core JS files: PASS
- Full Chromium `tests/browser_interaction_smoke.py`: PASS
- Critical DOM hierarchy: PASS
- Duplicate HTML IDs: **0**
- APP_VERSION: **0.20.6**

## Behavior
- Adaptive main-flow gap by source/target type.
- Wider decision spacing and branch cross-gap.
- `smartNextStepPosition` accepts configurable `crossGap`.
- Single-node selection subtly emphasizes connected auto-managed links.
- Existing manual node positions and manually controlled connectors are not auto-rearranged.

## Data / migration
- No process-data schema change.
- No Supabase migration required.
