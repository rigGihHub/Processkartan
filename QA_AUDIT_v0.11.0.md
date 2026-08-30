# QA Audit — Maplini v0.11.0

## Scope
First Faster Editing release: duplicate, copy and paste of selected process nodes.

## Functional contract
- `Duplicera` duplicates the currently selected node(s) with a small positional offset.
- Ctrl/Cmd+C copies selected node(s) to Maplini's editing clipboard.
- Ctrl/Cmd+V pastes from that clipboard.
- Ctrl/Cmd+D duplicates selection.
- Multi-node copies preserve links whose source and target are both inside the copied selection.
- Links to nodes outside the copied selection are intentionally not duplicated.
- Node properties, document URLs, Inputs/Outputs, sizes and visual styles are deep-copied.
- Manual connector via coordinates are offset together with duplicated nodes.
- Paste/duplicate selects the newly created node(s).
- Each paste/duplicate is one Undo checkpoint.
- Shortcuts are ignored while editing INPUT/TEXTAREA/SELECT/contenteditable fields.
- Read-only mode prevents paste/duplicate.

## Regression checks
- Existing connector routing/labels/insert-step behavior remains unchanged.
- Existing selection/delete behavior remains unchanged.
- Desktop DOM contract remains two-column sidebar + canvas.
- No database/schema/dependency changes.

## Executed QA
- Python compile: PASS (`app.py`, `google_docs.py`, `maplini_google_ui.py`).
- Pytest: **155/155 PASS**.
- Node.js suites: **21/21 PASS**.
- Rendered embedded scripts: `node --check` PASS.
- BeautifulSoup desktop DOM contract: PASS.
- ZIP integrity and clean-package check: PASS before release.

## Known limitation
- Ctrl/Cmd+C/V is guaranteed inside the current Maplini browser session. Maplini also attempts to mirror copied Maplini payloads to the browser clipboard where browser permissions allow it; cross-reload clipboard restoration is not treated as guaranteed in this release.
