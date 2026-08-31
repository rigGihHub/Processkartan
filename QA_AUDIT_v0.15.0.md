# QA Audit v0.15.0

## Scope
Make the existing structural Processkontroll understandable and actionable without adding AI or feature creep.

## Product contract
- Each finding has a deterministic Swedish action recommendation.
- Severity maps to user-facing priority: Åtgärda först / Kontrollera / Förbättring.
- Highest-priority finding is surfaced as Börja här.
- Findings with affected nodes can focus them directly on the canvas.
- Global findings remain readable even when there is no node to focus.
- Clean processes receive a clear positive empty state.
- Analysis remains local and deterministic.

## Browser verification
Chromium executes the real embedded editor and verifies:
1. existing free-connector drag in one gesture,
2. connector follows moved node while retaining free offset,
3. Undo restores node movement,
4. nested Export/More menu stability,
5. four-action mobile primary bar and secondary fullscreen,
6. Processkontroll opens from the real UI,
7. actionable finding data includes `action` and `priority`,
8. Börja här and Gör så här render when findings exist.

## Verified release gates
- `py_compile`: passed.
- `pytest`: 186/186 passed.
- JavaScript suites: 25/25 passed.
- Chromium browser interaction smoke: passed.
- All `maplini_*_core.js` syntax checks: passed.
- Embedded editor JavaScript syntax: passed.
- Critical body/sidebar/scroll/canvas DOM hierarchy: passed.
- Analysis panel DOM contract: passed.
- Duplicate HTML IDs: none detected.
- ZIP integrity: passed.

## Environment note
Python processes emitted an unrelated artifact-tool spreadsheet warmup timeout on stderr in this environment. It did not affect exit codes, Maplini tests or browser interaction results.
