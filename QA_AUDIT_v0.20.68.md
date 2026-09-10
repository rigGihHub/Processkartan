# QA Audit – Maplini v0.20.68 Canvas Visual Hierarchy

## Scope
- Improves scanability of the process canvas without changing process semantics.
- Clearer visual hierarchy for activity, start/end, decision, object, subprocess and document nodes.
- Quieter outer canvas surface, lighter depth effects and clearer typography.
- Main-flow vs branch connectors get stronger visual weighting without changing stored link data.
- Link labels and responsibility chips are toned down so step titles remain primary.
- Selected nodes get a clearer focus ring.
- User-controlled canvas/background and node color data remain authoritative; no process data migration.
- No Supabase, RLS, OAuth or process-schema changes.

## Verification
- `python -m py_compile app.py`: PASS
- `pytest -q`: 452 passed
- 38 JavaScript unit-test files: PASS
- `node --check` for 30 `maplini_*_core.js` files: PASS
- `tests/browser_interaction_smoke.py`: PASS
- `tests/browser_v02068_canvas_visual_hierarchy.py`: PASS
- `tests/browser_mobile_canvas_fit_readability.py`: PASS
- `tests/browser_v02061_empty_step_suggestions.py`: PASS
- Critical DOM/interaction regressions covered by full pytest + browser smoke suite: PASS
- ZIP excludes cache/pyc/venv/secrets/environment files.
