# QA Audit — Maplini v0.11.1

## Scope
Faster Editing: multi-select group move built directly from v0.11.0.

## Implemented
- Drag any node inside a multi-selection to move the full selected group.
- One shared snapped/clamped delta preserves relative node positions.
- Connected arrows redraw continuously while the group moves.
- External connectors follow the moved endpoint.
- Manual via points on internal connectors move with the selected group.
- Multi-selection remains active after the drag.
- One group drag = one Undo operation.
- Read-only behavior remains unchanged.

## Verification
- Python compile: PASS (`app.py`, `google_docs.py`, `maplini_google_ui.py`).
- Pytest: PASS — 156/156.
- Node test suites: PASS — 21/21.
- Rendered embedded JavaScript `node --check`: PASS — 18 script blocks.
- Desktop DOM contract: PASS:
  - `.p48-body` exists.
  - `.p48-side` and `#p48-scroll` remain inside `.p48-body`.
  - `#p48-controls` remains inside the sidebar.
  - `#p48-canvas` remains inside the canvas scroll area.
- ZIP integrity: PASS.

## Regression focus
- Single-node drag still uses the same group-move path with one node.
- Node resize still invalidates geometry and redraws connectors.
- Copy/paste/duplicate from v0.11.0 remains covered by regression tests.
- Smart connector routing, labels and insert-on-connector remain covered.

## Known limitations
- Physical Android/iPhone/browser smoke testing has not been performed in this environment.
- Group movement does not yet expose align/distribute commands; those remain planned Faster Editing work.

## Data / deployment
- No database migration.
- No OAuth/config/secrets changes.
- No dependency changes.
