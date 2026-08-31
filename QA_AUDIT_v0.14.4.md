# QA Audit v0.14.4

Scope: connector selection/drag regression.

Expected behavior:
- Pointer-down on an editable connector arms drag immediately.
- A short click selects only.
- Movement beyond threshold creates one Undo checkpoint and moves connector routing.
- SVG and HTML hit targets share the same behavior.
- Pointer capture keeps the gesture stable inside the editor iframe.
