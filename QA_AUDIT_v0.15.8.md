# QA Audit v0.15.8

## Scope
Reduce Processyta background choice overload while preserving older saved canvas styling.

## Verified behavior
- Standard background picker contains exactly 5 choices: Enfärgad, Prickar, Rutnät, Bild, Vattenstämpel.
- Decorative/advanced legacy types are removed from the normal picker.
- Rendering support for legacy types remains in the editor.
- A legacy saved type can be injected temporarily as `Tidigare bakgrund: …`.
- Returning to a standard background removes the temporary legacy option.
- No saved process is silently migrated.

## Verified release gates
- `py_compile`: passed.
- `pytest`: 194/194 passed.
- JavaScript suites: 25/25 passed.
- Chromium browser interaction smoke: passed.
- Browser verified exactly five standard background choices.
- Browser verified legacy `texture-paper` preservation and return to `solid`.
- Core JavaScript syntax: passed.
- Embedded editor JavaScript syntax: passed.
- Critical DOM hierarchy: passed.
- Duplicate HTML IDs: none detected.
- ZIP integrity: passed.

## Deployment
Not pushed or deployed. This release is intentionally prepared as a local push candidate only.
