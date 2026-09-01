# QA Audit v0.18.2

## Scope
Direct node dragging and cleaner object rendering.

## Verified
- A non-selected object can be grabbed directly on its visible label and moved in one pointer gesture.
- The node becomes selected as part of that gesture.
- Inline text editing still prevents the drag handler from stealing text interaction.
- Object role badges are no longer rendered above object nodes.
- `objectRole` remains in node data and DOM dataset for methodology/analysis logic.
- Focused Chromium smoke verified direct label drag and absence of object-role badge.

## Gates
- py_compile: passed.
- pytest: 215/215 passed.
- JavaScript suites: 26/26 passed.
- Focused Chromium direct-drag smoke: passed.
- Core JavaScript syntax: passed.
- Embedded JavaScript syntax: passed.
- Critical DOM hierarchy: passed.
- Duplicate HTML IDs: none detected.
- ZIP integrity: passed.

## Deployment
Not pushed or deployed.
