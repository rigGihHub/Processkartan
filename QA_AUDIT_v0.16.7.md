# QA Audit v0.16.7

## Scope
Smart connector cleanup after node movement, creation and Smart Layout.

## Verified behavior
- Automatic links use straight routing when connected node centers share an axis.
- Non-aligned automatic links use orthogonal routing.
- Manual free-routing and fixed-anchor connectors are preserved during ordinary dragging.
- Smart Layout may normalize connector geometry because it explicitly owns the layout.
- Newly created links and + Nästa links are polished immediately.
- Automatic via/free offsets are cleared during normalization.

## Gates
- py_compile: passed.
- pytest: 205/205 passed.
- JavaScript suites: 25/25 passed.
- Focused Chromium straight/orthogonal routing smoke: passed.
- Embedded JavaScript syntax: passed.
- Critical DOM hierarchy: passed.
- Duplicate HTML IDs: none detected.
- ZIP integrity: passed.

## Deployment
Not pushed or deployed.
