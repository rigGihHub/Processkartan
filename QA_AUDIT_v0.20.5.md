# QA Audit – Maplini v0.20.5

## Automated QA
- `python -m py_compile app.py`: PASS
- Python pytest: **239/239 passed**
- JavaScript test files: **27/27 passed**
- `node --check` on all core JS files: PASS
- Full Chromium `tests/browser_interaction_smoke.py`: PASS
- Critical DOM hierarchy: PASS
- Duplicate HTML IDs: **0**
- APP_VERSION: **0.20.5**

## Connector behavior
- New automatic connectors are marked `autoManaged:true`.
- Auto-managed connectors adapt live between straight and orthogonal geometry.
- Near-axis tolerance is 10 logical px.
- User-selected routing or anchor changes disable auto-management for that connector.
- Free/manual connector work remains protected.

## Data / migration
- Backward-compatible connector-style metadata only.
- No Supabase schema migration required.
