# QA Audit v0.17.3

## Scope
Canvas performance for larger process maps.

## Verified behavior
- Node geometry cache invalidates only the node that moved/resized instead of every node.
- Node-to-link adjacency is cached so connected links can be found without scanning every connector each drag frame.
- Full connector renders rebuild adjacency after graph changes.
- Drag/resize uses fast geometry mode: live connector paths update while expensive marker/label/hit-segment DOM work is deferred.
- A complete connector render runs at gesture end.
- A focused Chromium smoke created 40 nodes and 39 links, dragged a middle node, verified fast mode during the gesture, and verified all 39 connectors remained after final render.

## Gates
- py_compile: passed.
- pytest: 211/211 passed.
- JavaScript suites: 25/25 passed.
- Focused Chromium large-map smoke: passed.
- Core JavaScript syntax: passed.
- Embedded JavaScript syntax: passed.
- Critical DOM hierarchy: passed.
- Duplicate HTML IDs: none detected.
- ZIP integrity: passed.

## Deployment
Not pushed or deployed.
