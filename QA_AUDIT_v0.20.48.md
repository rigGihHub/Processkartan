# QA Audit – Maplini v0.20.48

## Release
**v0.20.48 – Smart dokumenttolkning**

## Scope
Bygger vidare på v0.20.47 Dokument → processförslag. Dokumentflödet får en strukturerad, granskningsbar tolkning av verksamhetsprocessen utan databasändring eller automatisk AI-sanning.

## Funktionellt verifierat
- Dokumenttolkning kan föreslå aktivitet/beslut.
- Ansvarig roll kan identifieras ur tydliga formuleringar.
- System kan identifieras ur tydliga systemfraser.
- Möjliga input/output kan följa med till noden.
- Varje kandidat visar källtext och tolkningsnivå.
- Sammanfattning visar steg, beslut, roller, system och kontrollpunkter.
- Växling mellan strukturerad vy och enkel redigerbar lista fungerar.
- Strukturerat förslag ritas med metadata i vanliga Maplini-noder.
- Beslut markeras för kontroll; Maplini hittar inte på Ja/Nej-vägar.
- Ingen ny Supabase-tabell/migration/RLS-förändring.

## QA-resultat
- `python -m py_compile app.py`: PASS
- Python pytest: **395/395 PASS**
- JS-testfiler: **29/29 PASS**
- Core-JS `node --check`: **24/24 PASS**
- Desktop Chromium interaction smoke: PASS
- Mobile Read/Follow smoke: PASS
- Mobile canvas fit/readability smoke: PASS
- v0.20.38 fast building regression: PASS
- v0.20.39 safe cleanup regression: PASS
- v0.20.40 Follow Process 2.0 regression: PASS
- v0.20.41 Processkontroll regression: PASS
- v0.20.42 Versionshistorik regression: PASS
- v0.20.44 First Process regression: PASS
- v0.20.46 Paste → Process regression: PASS
- v0.20.48 dedicated document interpretation browser test: PASS
- Runtime DOM IDs: **355**, duplicate IDs: **0**

## Guardrails
- Dokumentet läses lokalt i webbläsaren i denna version.
- Förslag måste granskas mot källdokumentet.
- Ingen generativ AI eller extern dokumentanalys har lagts till.
- Ingen avvikelse-/adminexpansion.
- Ingen automatisk molnsynk av dokumentinnehåll.

## Kända begränsningar
- Regelbaserad tolkning kan missa roller/system eller feltolka otydliga formuleringar.
- Komplexa beslut och återkopplingsloopar visualiseras ännu inte automatiskt som grenar.
- Skannade PDF:er utan textlager kräver OCR, vilket inte ingår här.
- DOCX/PDF-läsarbibliotek laddas från CDN vid behov.

## Release status
Push-klar ZIP. Inte pushad och inte verifierad live.
