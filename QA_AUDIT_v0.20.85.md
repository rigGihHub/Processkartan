# QA audit – Maplini v0.20.85

## Scope

Readability correction based on a real desktop screenshot of a two-step process.

## Expected result

- Activity labels wrap at word boundaries.
- Legacy narrow activity boxes remain readable.
- Small maps do not show the duplicate horizontal navigator.
- Large-map navigation and process geometry remain unchanged.

## Verification

- Full Python and JavaScript regression suites.
- Core JavaScript syntax checks.
- Desktop browser check with a narrow saved activity and a small process.
