# QA Audit v0.16.4

## Scope
Blank-canvas click must clear the selected node/link while preserving drag-to-pan.

## Verified behavior
- Select a node, click blank canvas: selection clears.
- Select a node, drag blank canvas: canvas pans normally.
- Drag gestures are distinguished from stationary press/release by movement tracking.
- Pointer capture no longer prevents deselection because blank-click clearing occurs on pointerup when no pan movement occurred.
- Existing canvas click fallback remains in place for blank SVG/background surfaces.

## Verified release gates
- `py_compile`: passed.
- `pytest`: 202/202 passed.
- JavaScript suites: 25/25 passed.
- Focused Chromium deselect + pan smoke: passed.
- Core JavaScript syntax: passed.
- Embedded editor JavaScript syntax: passed.
- Critical DOM hierarchy: passed.
- Duplicate HTML IDs: none detected.
- ZIP integrity: passed.

## Deployment
Not pushed or deployed.
