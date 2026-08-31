# QA Audit v0.15.3

## Scope
Fix connector-label readability/ownership and node-delete visibility.

## Product contract
- Each connector owns its own explicit label.
- New connectors start without automatic Ja/Nej text.
- Existing saved labels remain intact.
- Label text updates live while typing.
- Labels render as readable white badges offset from the connector path/drag handle.
- Delete-node action is visible only when exactly one node is selected.
- Delete-node action is hidden for connector-only selection and no selection.

## Browser verification
Chromium executes the actual embedded editor and verifies the established interaction flows plus:
1. dragging/selecting a connector leaves the node-delete action hidden,
2. entering `Godkänd` updates that connector's stored label live,
3. the SVG label badge renders and contains the entered text,
4. moving/selecting a node makes the node-delete action visible,
5. free connector movement and Undo continue to work.

## Verified release gates
- `py_compile`: passed.
- `pytest`: 189/189 passed.
- JavaScript suites: 25/25 passed.
- Chromium browser interaction smoke: passed.
- All core JavaScript syntax checks: passed.
- Embedded editor JavaScript syntax: passed.
- Critical body/sidebar/scroll/canvas DOM hierarchy: passed.
- Duplicate HTML IDs: none detected.
- ZIP integrity: passed.

## Environment note
Python processes can emit an unrelated artifact-tool spreadsheet warmup timeout on stderr in this environment. It does not affect Maplini test exit codes or browser interaction results.
