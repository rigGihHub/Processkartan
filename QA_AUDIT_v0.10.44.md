# QA Audit – Maplini v0.10.44

Scope: connector labels and automatic decision-branch labels.

Checks:
- Python compile
- embedded JavaScript syntax (`node --check`)
- connector/core Node test suites
- full pytest regression suite: 151 passed
- desktop DOM contract with `.p48-side` and `#p48-scroll` inside `.p48-body`
- connector label state serialization and normalization
- PDF/DOCX snapshot path includes connector labels
- Excel/Google Sheets connector sheet includes `Piltext`
- ZIP integrity

Compatibility:
- Existing links normalize with an empty `label` and render unchanged.
- New ordinary links remain unlabeled.
- First and second new outgoing links from a decision suggest `Ja` and `Nej`; users can edit/remove them.
- No database, OAuth, secrets or dependency changes.

Known limitations:
- Labels use the geometric midpoint of the connector. Collision-aware label placement is deferred to the later smart-layout/connector-routing work.
- Physical browser/device QA still requires deployment verification.
