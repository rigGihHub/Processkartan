# QA Audit – Maplini v0.20.43

## Release
- Version: `0.20.43`
- Fokus: hård användargranskning och förenkling av kärnflödet Rita → Förstå → Följ.
- Bas: `v0.20.42 – Versionshistorik`.
- Ingen Supabase-, RLS-, OAuth-, schema- eller dependencyändring.
- Inte verifierad live.

## Produktförändringar
- Ny kompakt `Visa ▾` samlar zoom, 100 %, Anpassa, Översikt och Ansvar.
- Följ processen och Läsvy ligger fortsatt på huvudnivå.
- `Analysera process` har bytt namn till `Processkontroll` för konsekvent produktterminologi.
- Avvikelser är kvar men ligger sist under `Övrigt` i Mer-menyn.
- Dubblerad `Processyta`-rubrik borttagen.
- Inga befintliga funktions-ID:n för vyverktygen ändrades.

## QA-resultat
- `python -m py_compile app.py`: PASS
- Python pytest: **377/377 PASS**
- JS-testfiler: **28/28 PASS**
- Core JS `node --check`: **23/23 PASS**
- Desktop Chromium interaction smoke: PASS (uppdaterat för Visa-menyn)
- Mobile Read/Follow Chromium smoke: PASS
- Mobile canvas fit/readability Chromium smoke: PASS
- v0.20.38 fast-building regression: PASS
- v0.20.39 cleanup-preview regression: PASS
- v0.20.40 Follow Process 2.0 regression: PASS
- v0.20.41 Processkontroll regression: PASS
- v0.20.42 Versionshistorik regression: PASS
- Ny v0.20.43 statisk UI/IA-regression: PASS via pytest

## Releasebedömning
Push-klar kandidat. Ska inte beskrivas som live förrän deploy har verifierats.
