# QA AUDIT – Maplini v0.11.7

## Scope
Contextual node toolbar built on v0.11.6.

## Functional contract
- Toolbar is visible only for editable node selections and hidden for connector/read-only contexts.
- Single selection exposes Next, Format, Duplicate and Delete.
- Multi-selection exposes Format, Background color, Duplicate, Arrange and Delete.
- Next reuses the existing Quick Next Step flow.
- Format reuses the existing formatting panel and opens mobile tools when needed.
- Background color uses the existing multi-select `updateStyle` path and therefore one Undo checkpoint per change.
- Arrange reuses existing Align/Distribute functions.
- Duplicate/Delete reuse existing editing and selection logic.
- Toolbar follows the selection during drag/resize and compensates for canvas zoom.
- Toolbar clicks are excluded from connector hit-testing.

## Automated QA
- Python syntax: PASS (`app.py`, `google_docs.py`, `maplini_google_ui.py`).
- Pytest: 162/162 PASS.
- JavaScript suites: 21/21 PASS.
- `node --check` for all `maplini_*_core.js`: PASS.
- Embedded editor JavaScript syntax: PASS.
- Critical desktop DOM hierarchy: PASS.
- Contextual toolbar DOM placement inside `#p48-canvas`: PASS.

## Known limitations
- The compact toolbar intentionally exposes only the highest-frequency commands; full formatting remains in the existing sidebar.
