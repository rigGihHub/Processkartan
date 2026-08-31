# QA Audit v0.14.6

## Scope
True free connector movement plus visual/UX polish.

## Connector contract
- Dragging a connector body switches/updates it to `routing: free`.
- Free route uses relative middle-body offsets, not detached absolute endpoints.
- Both endpoints stay attached to their respective nodes.
- Moving either node recomputes the route from new anchors plus saved offset.
- Smart Layout resets internal connectors to automatic orthogonal geometry.
- Process scaling scales the free-route offset.
- One drag creates one Undo checkpoint.

## Release gates
Python syntax, full pytest, all JS suites, core JS syntax, embedded editor JS, critical structural checks and ZIP integrity.
