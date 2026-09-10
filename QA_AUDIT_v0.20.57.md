# QA AUDIT – Maplini v0.20.57

Release: **v0.20.57 – Export som faktiskt ser ut som processen**
Datum: 2026-09-07

## Omfattning
- PDF-export på flera sidor komponerar separata sidor och upprepar exporthuvudet.
- DOCX använder valt A4/A3-format och valt/automatiskt sidantal.
- Stora processer kan delas över flera DOCX-sidor i stället för att pressas till en sida.
- Befintlig snapshot-rendering för noder, kopplingar, etiketter, bakgrund och logotyp behålls.
- Ingen schema-, RLS-, workspace- eller editorrewrite.

## Automatiserad QA
- python -m py_compile app.py: PASS
- pytest: **424 passed**
- JS unit/regression files: **35 PASS**
- node --check maplini_export_core.js: PASS
- tests/browser_interaction_smoke.py: PASS
- tests/browser_v02055_source_change.py: PASS
- tests/browser_v02056_source_support.py: PASS
- tests/browser_v02057_export_fidelity.py: PASS
- Kritiska DOM ancestor-relationer: PASS
- Duplicerade id:n i renderad Chromium-DOM: inga

## Exportverifiering i Chromium
Ett deterministiskt tvåsidigt A4 landscape-test verifierar att:
- PDF har giltig PDF-signatur.
- PDF innehåller exakt 2 Page-objekt och 2 image-objekt.
- DOCX är en giltig ZIP-container.
- DOCX innehåller två separata processbilder.
- DOCX innehåller riktig sidbrytning mellan bilderna.
- DOCX använder landscape-orientering.

## Bedömning
PASS för push-kandidat. Inte live-verifierad och inte deployad.
