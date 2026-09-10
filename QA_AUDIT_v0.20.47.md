# QA AUDIT v0.20.47

Scope: Dokument → processförslag.

- APP_VERSION: 0.20.47
- Python compile: PASS
- Python pytest: 389/389 PASS
- JS tests: 28/28 files PASS
- core JS syntax: 23/23 PASS
- ZIP integrity: PASS after packaging

Guardrails: review-before-draw, no automatic Yes/No invention, no Supabase/RLS change. PDF/DOCX parsing runs client-side via external parsing libraries; TXT/MD/CSV use browser File API.
