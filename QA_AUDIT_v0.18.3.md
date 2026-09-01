# QA Audit v0.18.3

## Scope
Direct page setup at the canvas.

## Verified
- A compact sticky control is visible directly over the canvas.
- Initial summary shows `A4 stående · Auto`.
- Quick control changes A4/A3 and portrait/landscape immediately.
- Quick control changes page count between automatic and 1–8 pages.
- Existing Export page settings stay synchronized with the quick control in both directions.
- Print-page labels and page count update immediately after changes.
- Focused Chromium smoke changed A4 portrait → A3 landscape, set 3 pages, verified three A3 landscape page boundaries, then changed the Export selector back to A4 portrait and verified reverse synchronization.

## Gates
- py_compile: passed.
- pytest: 216/216 passed.
- JavaScript suites: 26/26 passed.
- Focused Chromium page-settings smoke: passed.
- Core JavaScript syntax: passed.
- Embedded JavaScript syntax: passed.
- Critical DOM hierarchy: passed.
- Duplicate HTML IDs: none detected.
- ZIP integrity: passed.

## Deployment
Not pushed or deployed.
