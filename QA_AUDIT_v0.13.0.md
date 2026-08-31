# QA Audit – Maplini v0.13.0

## Scope
Mobile UX: contextual bottom toolbar, custom canvas pan/pinch gestures, larger connector touch targets and a bounded mobile editor viewport.

## Verification
- `python -m py_compile app.py google_docs.py maplini_google_ui.py` – PASS
- `pytest -q` – **164/164 PASS**
- All `tests/test_*.js` – **22/22 PASS**
- `node --check maplini_mobile_core.js` – PASS
- All `maplini_*_core.js` syntax checks – PASS
- Longest embedded editor `<script>` after core injection – PASS
- Critical desktop DOM contract – PASS
- ZIP integrity – PASS (completed during release packaging)

## Mobile behavior checked
- Normal mobile bottom bar exposes Add, Undo, Redo, Fit and Tools.
- Node selection switches the bar to Next, Properties, Duplicate and Delete; Next hides when the selected node cannot create a next step.
- Blank-canvas one-finger touch pans both axes without moving nodes.
- Two-finger pinch computes distance/midpoint and zooms around the gesture center, clamped to 25–150 %.
- Selection mode, nodes, resize handles, connector hit areas and quick toolbars are excluded from canvas pan gestures.
- Connector touch target is 44 px and the bend handle receives an expanded touch area.
- Mobile editor viewport is bounded (`clamp(520px, 68dvh, 760px)`) so vertical pan remains inside the canvas.
- Safe-area bottom inset is respected.
- Desktop `.p48-body > .p48-side + #p48-scroll` contract remains intact.

## Known limitation
The first v0.13 release optimizes touch interaction and command access. Long-press multi-select and gesture-driven connector creation remain candidates for a later mobile refinement.

## Data / security
No database, Supabase schema, OAuth, secret or dependency changes.
