# QA Audit – Maplini v0.20.39

Focus: **Safe Cleanup Preview**.

## Product contract
- `✨ Snygga till` is preview-first.
- Preview paints proposed positions on the canvas without mutating saved node coordinates.
- `Behåll som det är` restores the exact original positions and creates no Undo entry.
- `Använd` commits the proposed positions as one Undo operation.
- Process nodes, links and flow semantics are unchanged.
- Isolated/unconnected nodes remain untouched.
- Automatic connected links are polished only when the preview is accepted.
- No schema, Supabase, RLS, OAuth or dependency change.

## Automated QA
- `python -m py_compile app.py`: PASS
- Python pytest: **357/357 PASS**
- JavaScript test files: **27/27 PASS**
- Core JS `node --check`: **22/22 PASS**
- Chromium desktop interaction smoke: PASS
- Chromium v0.20.38 fast-building regression smoke: PASS
- Chromium v0.20.39 cleanup preview/apply/cancel smoke: PASS
- Chromium mobile Read/Follow smoke: PASS
- Chromium mobile canvas-fit/readability smoke: PASS
- Critical DOM hierarchy: PASS
- Static HTML IDs (BeautifulSoup): **311 IDs / 0 duplicates**
- ZIP integrity: PASS after packaging

## Browser cleanup-preview assertions
The targeted browser test verifies that:
1. the preview banner becomes visible,
2. DOM positions visibly change,
3. process data coordinates remain unchanged during preview,
4. cancel restores exact coordinates without adding Undo history,
5. apply changes process coordinates and adds exactly one Undo entry.

## Release status
Push-ready artifact only. Not verified live.
