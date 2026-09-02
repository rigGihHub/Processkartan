# QA Audit – Maplini v0.20.8

## Scope
Visual Walkthrough Position: connect the existing Follow Process interaction to the process map itself without adding a new admin surface.

## Implemented behavior
- Current walkthrough node receives a distinct professional focus state on the canvas.
- Previously committed walkthrough nodes are toned down to create a visible trail.
- Possible next nodes are subtly highlighted.
- Relevant outgoing connectors are highlighted.
- Once a route question resolves to one unique Ja/Nej edge, only that resolved edge is emphasized as the route forward.
- Canvas follows the current node with smooth scrolling when it leaves a central comfort zone.
- Walkthrough following does not change zoom automatically.
- Existing control-question deviation behavior and v0.20.7 auto-advance behavior are preserved.
- Walkthrough backdrop was reduced so the process map remains readable behind the walkthrough panel.

## Automated QA
- `python -m py_compile app.py`: PASS
- Python pytest: **246/246 passed**
- JavaScript test files: **27/27 passed**
- `node --check` on all core JS files: **22/22 passed**
- Full Chromium `tests/browser_interaction_smoke.py`: PASS
- Critical DOM hierarchy: PASS
- Duplicate HTML IDs: **0**
- APP_VERSION: **0.20.8**

## Regression note
The inherited Python regression suite pinned the exact previous release string (`0.20.7`) in three test files. Those version assertions were advanced to `0.20.8`; no functional assertions were removed.

## Data / migration
- No process-data schema change.
- No Supabase migration required.
