# QA Audit v0.14.7

## Scope
P0 integrity and core interaction fixes identified by the total app review.

## Verified changes
- Workspace save payload uses the workspace owner's id, not the active editor's id.
- Supabase migration hardens insert/update policy so workspace process `owner_id` must equal `workspaces.owner_id`.
- Connector drag uses pointer delta from pointerdown, preserving the starting route and preventing endpoint-grab jumps.
- The document capture listener no longer consumes the first connector drag gesture as selection-only.
- Free connector offsets remain unchanged when an attached node is moved; route endpoints follow node geometry.
- Google Sheets Processsteg header now includes `Dokumentlänk` and uses 13 columns.
- Startup resize handler no longer calls the removed `refreshLinkQuickToolbar`.

## Browser interaction smoke
The release includes `tests/browser_interaction_smoke.py`, which executes the actual embedded editor DOM/JS in headless Chromium. The harness substitutes only browser storage objects because the QA environment blocks native storage on the synthetic about:blank origin. It verifies:
1. an unselected connector can be dragged in one gesture,
2. drag delta matches pointer delta without a jump,
3. moving a connected node changes the connector path while preserving free-route offsets,
4. Undo restores the node move.

## Release gates
- Python syntax
- full pytest
- all Node JS suites
- all core JS syntax checks
- embedded editor JS syntax
- Chromium interaction smoke
- critical DOM structure
- ZIP integrity

## Deployment note
Workspace deployments require `supabase_schema_v0147.sql`. Until that migration is applied, the client-side owner fix is present but the database policy hardening is not.
