# QA Audit v0.14.1

Scope: connector dragging, horizontal navigation for multiple print pages, zoom direction.

Acceptance:
- selected connector hit target starts drag; one actual drag creates one undo checkpoint.
- strict straight connector remains straight until user drags it; drag changes it to an orthogonal manual route because a direct segment has no movable midpoint.
- logical canvas expands to fit all selected PDF pages and overflow nodes, so horizontal scrollbar/nav can reach them.
- Zoom out decreases scale; zoom in increases scale; 25–150% clamps retained.
- desktop DOM structure unchanged.
