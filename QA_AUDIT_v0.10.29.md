# Maplini v0.10.29 — Destructive & Shared Flow RC2

## Verkliga problem åtgärdade
- Process deletion rensade inte `cloudLoadedProcessIds` / `cloudLoadedProcessScopes`, vilket kunde lämna stale scope-state.
- Delete fortsatte även om lokal pre-save inte kunde verifieras. Nu avbryts destruktiv radering om säkerhetskopian inte kan skapas.
- Om lokal write efter delete misslyckas återställs pre-delete snapshot i minnet och primary local storage.
- Sista-process-fallback får nu `localModifiedAt`.
- Shared-link load validerade inte payload via reliability-reglerna och rapporterade fetch/parse-fel endast till console.
- Inloggad Save gjorde redundant persist + local flush före `saveCurrentToCloud()`, som gjorde samma arbete igen.
- Clipboard fallback kunde misslyckas utan användarfeedback.

## Ny modul
`maplini_flow_core.js` kapslar shared-row canonicalization och deterministisk process-delete transition.

## Begränsning
Molnradering som misslyckas efter lyckad lokal radering är fortfarande medvetet en partial-success:
processen är borta lokalt och användaren får tydlig varning om att molnkopian inte kunde raderas.
