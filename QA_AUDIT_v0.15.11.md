# QA Audit v0.15.11

## Scope
- Fix the odd first impression on an empty process.
- Make A4 portrait the default PDF/page format.
- Reduce false-positive runtime safety banners.

## Verified behavior
- Empty-state card CSS now lives inside the embedded editor iframe.
- Empty processes display a styled centered start card instead of raw text at the top-left.
- A4 portrait is selected by default.
- JS default and page-spec fallback are both A4 portrait.
- Generic window/unhandled-rejection diagnostics are logged without showing the red data-safety banner.
- Explicit Maplini operation errors still show the banner.
- Healthy process restore clears stale runtime warning state.

## Verified release gates
- `py_compile`: passed.
- `pytest`: 197/197 passed.
- JavaScript suites: 25/25 passed.
- Chromium browser interaction smoke: passed.
- Browser verified A4P default and visible styled empty-state card.
- Core JavaScript syntax: passed.
- Embedded editor JavaScript syntax: passed.
- Critical DOM hierarchy: passed.
- Duplicate HTML IDs: none detected.
- ZIP integrity: passed.

## Deployment
Not pushed or deployed.
