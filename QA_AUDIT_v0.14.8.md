# QA Audit v0.14.8

## Scope
Information-architecture simplification without removing core capabilities.

## Desktop contract
- Permanent command surface: process name, New, Save, Share, Undo/Redo, Zoom/Fit, Smart Layout, Export, More.
- PDF/DOCX/Excel/Google Sheets and page controls are grouped under Export.
- Analysis, selection actions, canvas appearance, logo and process scaling are grouped under More.
- Existing element IDs remain intact for established event wiring.
- Critical body/sidebar/scroll/canvas DOM nesting is preserved.
- No duplicate HTML IDs detected.

## Mobile contract
- Normal bottom bar contains exactly four actions: Add, Undo, Fit, Tools.
- Selection mode remains contextual.
- Redo and fullscreen are no longer permanent bottom-bar actions; the broader tool surface remains available through the mobile tools panel.

## Verified release gates
- `py_compile`: passed.
- `pytest`: 183/183 passed.
- JavaScript suites: 25/25 passed.
- Chromium browser interaction smoke: passed.
- Core JavaScript syntax: passed.
- Embedded editor JavaScript syntax: passed.
- Critical DOM hierarchy: passed.
- ZIP integrity: passed.

## Notes
The browser-smoke command emitted an unrelated artifact-tool warmup timeout on stderr in the environment, but the interaction smoke itself completed successfully with exit code 0 and `browser interaction smoke ok`.
