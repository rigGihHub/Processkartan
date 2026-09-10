# QA AUDIT – Maplini v0.20.53

## Scope

Release: **Any Source → Process**. Base: v0.20.52 Source Traceability.

## Added

- Källa → processförslag UI for local documents, pasted arbitrary text, and article/news URL.
- `maplini_any_source_core.js`: deterministic source classification, event-flow extraction, URL normalization/reader helper, markdown cleanup.
- Generic source traceability for `source_import`.
- Browser regression for pasted news/event text → proposal → canvas → source trace.

## Guardrails

- Proposals remain review-first; no source is treated as authoritative truth.
- Local files remain browser-side. URL reading is explicitly disclosed as using an external reader service.
- No Supabase schema, RLS, OAuth, workspace or cloud-write model changes.
- Existing document conflict resolution remains intact.

## Verification

- `python -m py_compile app.py`: PASS
- Python pytest: **419/419 PASS**
- JS test files: **33/33 PASS**
- Core JS `node --check`: **25/25 PASS**
- Chromium desktop interaction smoke: PASS
- Chromium mobile Read/Follow smoke: PASS
- Chromium mobile canvas fit/readability smoke: PASS
- v0.20.52 source traceability browser regression: PASS
- v0.20.53 Any Source pasted-news browser flow: PASS
- Static HTML ids: **367**, duplicates **0**

## Known limitation

URL extraction depends on an external reader endpoint and therefore can fail for blocked/private/authenticated pages. The UI instructs the user to paste the article text instead. This release does not scrape restricted content or bypass access controls.
