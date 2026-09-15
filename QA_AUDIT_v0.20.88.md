# QA audit – Maplini v0.20.88

## Scope

Make the desktop palette clickable and context-aware while preserving explicit free placement by drag and drop.

## Required checks

- Desktop click with no selection creates a standalone node.
- Desktop click with one eligible selected node creates and connects the next node.
- Object in, Start and Note remain standalone.
- A selected Decision opens explicit branch choices rather than guessing.
- Drag and drop remains standalone and position-controlled.
- Undo, persistence and connector rendering continue through existing creation paths.
