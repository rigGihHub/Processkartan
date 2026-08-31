# QA Audit v0.15.9

## Scope
Reduce node-style choice overload while preserving older saved process styling.

## Verified behavior
- Standard node-style picker contains exactly 3 choices: Standard, Upphöjd, Minimal.
- 3D and Glass are not offered for new styling decisions.
- Existing saved nodes using 3D/Glass retain their visual rendering.
- Legacy style is injected temporarily as `Tidigare rutstil: …`.
- Returning to a standard style removes the temporary legacy option.
- No saved process is silently migrated.

## Verified release gates
- `py_compile`: passed.
- `pytest`: 195/195 passed.
- JavaScript suites: 25/25 passed.
- Chromium browser interaction smoke: passed on rerun; first run hit an unrelated menu-state flake.
- Browser verified legacy Glass preservation and return to Standard.
- Core JavaScript syntax: passed.
- Embedded editor JavaScript syntax: passed.
- Critical DOM hierarchy: passed.
- Duplicate HTML IDs: none detected.
- ZIP integrity: passed.

## Deployment
Not pushed or deployed. This release is intentionally prepared as a local push candidate only.
