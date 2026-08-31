# QA Audit v0.15.2

## Scope
Replace the browser-native New Process prompt with a consistent Maplini flow.

## Product contract
- Clicking New Process opens an in-app dialog.
- Current process is persisted before the naming flow opens.
- Name field receives focus and selects the default name.
- Enter creates; Escape, Cancel and backdrop close without creating.
- Blank names show inline validation.
- Created process immediately enters the existing empty-canvas first-step experience.
- No browser `prompt()` remains in the New Process workflow.

## Browser verification
Chromium executes the real embedded editor and verifies the established connector/menu/mobile/process-check/first-time flows plus:
1. New Process opens the Maplini dialog and backdrop.
2. Name input receives focus.
3. Enter creates a process with the typed name.
4. Successful creation returns to the empty-canvas first-step guide.
5. Escape closes the dialog without creating another process.

## Verified release gates
- `py_compile`: passed.
- `pytest`: 188/188 passed.
- JavaScript suites: 25/25 passed.
- Chromium browser interaction smoke: passed.
- All core JavaScript syntax checks: passed.
- Embedded editor JavaScript syntax: passed.
- Critical body/sidebar/scroll/canvas DOM hierarchy: passed.
- New Process dialog/backdrop DOM: passed.
- Duplicate HTML IDs: none detected.
- ZIP integrity: passed.

## Environment note
Python processes can emit an unrelated artifact-tool spreadsheet warmup timeout on stderr in this environment. It does not affect Maplini exit codes, tests or browser interaction results.
