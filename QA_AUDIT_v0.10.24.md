# Maplini v0.10.24 — Selection, Undo/Redo & Interaction State Hardening

Real issues fixed:
- `clearCanvas()` cleared node selection but not connector selection, allowing stale connector context after restore/process switch.
- Deleting one connector erased all selected-link indices instead of reindexing surviving selections.
- Keyboard Delete/Backspace now resolves node/link/multi/mixed selection deterministically.
- Escape exits area-selection mode and clears current selection state.
- Undo/redo refreshes formatting and link-control context after restoring state.

New pure `maplini_selection_core.js` centralizes selection normalization, delete-action resolution and link-index reindexing.

Physical-device interaction and deployed smoke testing are not claimed offline.
