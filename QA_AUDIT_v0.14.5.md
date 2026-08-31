# QA Audit v0.14.5

## Scope
Editing stability and UX cleanup before further feature work.

## Verified contracts
- Multi-page canvas size is used by Smart Layout.
- Contextual toolbar clamps against current logical canvas width.
- Browser resize recalculates canvas/page extents, horizontal navigation and toolbars.
- Transient menus close on Escape and blank-canvas interaction.
- Retired Align/Distribute UI no longer has active click wiring.
- Connector drag, zoom, page navigation, Smart Layout, autosave, Undo/Redo and mobile regression suites remain covered.

## Release gates
Python syntax, full pytest, all JS suites, JS syntax, embedded editor JS, structural DOM checks and ZIP integrity.
