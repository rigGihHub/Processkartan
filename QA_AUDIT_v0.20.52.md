# QA AUDIT v0.20.52 – Källspårning på processkartan

## Omfattning
Release byggd från v0.20.51. Fokus: bevara och visa källdokument + källtext på dokumentgenererade processsteg utan ny databasmodell eller AI-gissningar.

## Funktionell kontroll
- Dokumentgenererade noder får `sourceTrace` med dokumentnamn och relevant evidence-text.
- Enkeldokumentimport dekoreras med verkligt filnamn och evidence innan canvas skapas.
- Flerdokumentimport bevarar alla källor som stöder ett sammanslaget steg.
- Markerat dokumentgenererat steg visar skrivskyddad panel **Källa till steget**.
- Vanligt manuellt skapat steg visar ingen tom källpanel.
- Källspåret sparas i nodens befintliga dataobjekt och kräver ingen schemaändring.

## Automatiska tester
- `python -m py_compile app.py`: PASS
- Python pytest: **417/417 PASS**
- JS testfiler: **32/32 PASS**
- Core JS `node --check`: **24/24 PASS**
- Desktop Chromium interaction smoke: PASS
- Mobile Read/Follow smoke: PASS
- Mobile canvas fit/readability smoke: PASS
- Dokumenttolkning v0.20.48 regression: PASS
- Verkligt dokumentflöde v0.20.49 regression: PASS
- Flerdokument v0.20.50 regression: PASS
- Konfliktlösning v0.20.51 regression: PASS
- Ny browser smoke för källspårning: PASS

## DOM / struktur
- Statiska HTML-ID:n: 363
- Dubbletter: 0
- Kritisk editorstruktur lämnas oförändrad (`.p48-body`, sidebar, scroll, controls, canvas).

## Data / säkerhet
- Ingen ny Supabase-tabell eller migration.
- Ingen RLS/OAuth/workspace-ändring.
- Ingen dokumenttext skickas till ny backendfunktion.
- Källtext visas via `textContent`, inte injicerad HTML.
- Källspårningen är läsbar metadata, inte ett påstående om att tolkningen är korrekt.

## Begränsningar
- Källspårningen pekar på dokumentnamn + extraherad text, inte sidnummer/Word-paragraf-ID ännu.
- Om originalfilen flyttas eller byter namn finns ingen automatisk länk tillbaka till filen i denna release.
- Ingen jämförelse mellan senare manuellt ändrad nodtext och ursprunglig källtext ännu.

## Slutsats
PASS – releasekandidat för senare Commit/Push efter användarens manuella deployfönster.
