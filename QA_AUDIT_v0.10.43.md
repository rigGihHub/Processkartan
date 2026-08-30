# QA Audit – Maplini v0.10.43

Scope: smart connector anchors and orthogonal routing.

Checks:
- Python compile
- embedded JavaScript syntax
- Node connector/core test suites
- full pytest regression suite
- desktop DOM contract
- ZIP integrity

Compatibility:
- Existing saved links without routing/anchorMode normalize to straight/manual.
- Newly created links default to orthogonal/auto.
- No database, OAuth, secrets or dependency changes.
