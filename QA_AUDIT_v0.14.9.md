# QA Audit v0.14.9

## Scope
Stability and browser-polish pass on the v0.14.8 simplified information architecture.

## Verified fixes
- Nested `details` menus preserve their open parent: Sheets inside Export and Processyta/Logotyp/Skala inside More.
- Unrelated transient menus still close when another top-level menu opens.
- The mobile normal bottom bar remains exactly four actions.
- Redo and Fullscreen remain available as secondary mobile actions rather than being functionally removed.
- Free connector drag remains delta-based, follows moved nodes and supports Undo.

## Browser smoke coverage
Chromium executes the embedded editor HTML/JS and verifies:
1. free connector drag in one gesture,
2. connector route follows a moved source node while retaining free offset,
3. Undo restores the node move,
4. Export -> Excel/Google Sheets nested menu remains open,
5. More -> Processyta nested menu remains open,
6. unrelated top-level menus close,
7. mobile normal bar has four actions,
8. mobile secondary Fullscreen is reachable and activates fullscreen state.

## Verified release gates
- `py_compile`: passed.
- `pytest`: 184/184 passed.
- JavaScript suites: 25/25 passed.
- Chromium browser interaction smoke: passed.
- Core JavaScript syntax: passed.
- Embedded editor JavaScript syntax: passed.
- Critical DOM hierarchy: passed.
- No duplicate HTML IDs detected.
- ZIP integrity: passed.
