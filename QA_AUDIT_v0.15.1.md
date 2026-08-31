# QA Audit v0.15.1

## Scope
Improve the first-use experience without adding tutorials, onboarding popups or permanent controls.

## Product contract
- Empty editable process shows one focused canvas start card.
- User can add Start or Activity directly from the card.
- First node is selected and enters inline text editing.
- Guide disappears once a node exists.
- Shared read-only views do not show authoring onboarding.
- Existing sidebar palette and mobile add flows remain available.

## Browser verification
Chromium executes the real embedded editor and verifies the established connector/menu/mobile/process-check flows plus:
1. clearing to a genuinely empty process displays the empty-canvas guide,
2. both first-step actions are visible,
3. clicking `Lägg till Start` creates exactly one Start node,
4. the guide disappears immediately after first-node creation.

## Verified release gates
- `py_compile`: passed.
- `pytest`: 187/187 passed.
- JavaScript suites: 25/25 passed.
- Chromium browser interaction smoke: passed.
- All core JavaScript syntax checks: passed.
- Embedded editor JavaScript syntax: passed.
- Critical body/sidebar/scroll/canvas DOM hierarchy: passed.
- Empty-state DOM placement: passed.
- Duplicate HTML IDs: none detected.
- ZIP integrity: passed.

## Environment note
Python processes can emit an unrelated artifact-tool spreadsheet warmup timeout on stderr in this environment. It does not affect Maplini test exit codes or browser interaction results.
