# QA Audit v0.10.40

Scope: menu dismissal behavior and persisted visual node styles.

- Processyta and Google Sheets dropdowns close on outside pointer press.
- Opening one dropdown closes the other.
- Share flyout closes on outside pointer press.
- Node style choices: Standard, 3D, Upphöjd skugga, Glas, Minimal/platt.
- Chosen style can be applied to one selected node or all nodes.
- Node style persists through process normalization/save/reload.
- Apply-to-all creates one Undo checkpoint.
- Existing node geometry remains unchanged; styles are visual only.
- Export snapshot includes equivalent shadow treatment for visual styles.
- No Supabase schema, secrets, dependencies or external configuration changes.

## Verification
- pytest: 144/144 passed.
- All Node.js test suites passed.
- Python compile passed.
- Embedded main JavaScript `node --check` passed.
- Desktop DOM contract passed.
- Clean ZIP integrity passed; no cache, secrets, virtualenv or Git metadata included.
