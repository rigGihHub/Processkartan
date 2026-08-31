# QA Audit v0.15.7

## Scope
Reduce typography choice overload while preserving older saved process styling.

## Verified behavior
- Standard font picker contains exactly 7 choices.
- Removed decorative and overlapping font choices are not offered for new formatting.
- Legacy saved fonts can be injected temporarily as `Tidigare typsnitt: …`.
- Returning to a current font removes the temporary legacy option.
- No saved process style is silently rewritten.

## Verified release gates
- `py_compile`: passed.
- `pytest`: 193/193 passed.
- JavaScript suites: 25/25 passed.
- Chromium browser interaction smoke: passed.
- Browser verified exactly seven standard font options.
- Browser verified legacy `Caveat` can be preserved temporarily and removed again when returning to Inter.
- Core JavaScript syntax: passed.
- Embedded editor JavaScript syntax: passed.
- Critical DOM hierarchy: passed.
- Duplicate HTML IDs: none detected.
- ZIP integrity: passed.

## Deployment
Not pushed or deployed. This release is intentionally prepared as a local push candidate only.
