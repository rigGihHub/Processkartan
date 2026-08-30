# QA audit — Maplini v0.10.45

Scope: insert-step-on-connector flow built from v0.10.44.

Acceptance targets:
- selected connector exposes **＋ Infoga steg**
- one action replaces A→B with A→new→B
- one Undo checkpoint is created
- connector visual style is retained without stale manual via coordinates
- existing connector label stays on the source-side segment
- new node is selected and enters inline text editing
- read-only mode cannot insert a step
- existing connector selection/drag/routing remains intact

## Verification
- `python -m py_compile`: passed
- `pytest -q`: **152 passed**
- all Node.js test suites: passed
- embedded JavaScript `node --check`: passed
- BeautifulSoup desktop DOM contract: passed
- no database/config/dependency changes
- physical browser/mobile verification: not performed in this build environment
