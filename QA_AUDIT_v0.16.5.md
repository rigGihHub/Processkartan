# QA Audit v0.16.5

## Scope
Magnetic node alignment and clearer quick-toolbar naming.

## Verified behavior
- Node movement follows an invisible 10 px base grid.
- Near another node, left/center/right and top/center/bottom alignment snaps within tolerance.
- Center-to-center alignment has stronger capture because it produces visually straight connectors even for differently sized node types.
- A subtle temporary guide appears only during node-to-node snap; the grid itself stays invisible.
- Group movement preserves relative geometry.
- If connected node centers become exactly horizontal or vertical, their connector becomes straight with automatic anchors and stale manual offsets are cleared.
- Quick toolbar now says `Egenskaper` instead of `Formatera`.

## Verified release gates
- `py_compile`: passed.
- `pytest`: 203/203 passed.
- JavaScript suites: 25/25 passed.
- Focused Chromium magnetic-alignment smoke: passed.
- Core JavaScript syntax: passed.
- Embedded editor JavaScript syntax: passed.
- Critical DOM hierarchy: passed.
- Duplicate HTML IDs: none detected.
- ZIP integrity: passed.

## Deployment
Not pushed or deployed.
