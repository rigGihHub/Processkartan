# QA AUDIT – Maplini v0.11.6

## Scope
Multi-select formatting built on v0.11.5.

## Functional contract
- Formatering-panel enters `multi` context for 2+ selected nodes.
- Shared formatting applies to every selected node.
- Selection is preserved after formatting.
- One Undo checkpoint is created per formatting action.
- Connected links are invalidated/redrawn when node styling can affect geometry.
- Document link and Inputs/Outputs remain single-node only.
- Read-only mode disables formatting controls.
- Text alignment controls are separated from layout Align controls to prevent event collisions.

## Automated QA
- Python syntax: PASS (`app.py`, `google_docs.py`, `maplini_google_ui.py`).
- Pytest: 161/161 PASS.
- JavaScript suites: 21/21 PASS.
- `node --check` for all `maplini_*_core.js`: PASS.
- Embedded editor JavaScript syntax: PASS.
- Critical desktop DOM hierarchy: PASS.

## Known limitation
When selected nodes have mixed values, native color/select controls cannot display a true “mixed” state. The panel explicitly explains that the first selected node is shown until the user chooses a new value; no node is changed merely by opening the panel.
