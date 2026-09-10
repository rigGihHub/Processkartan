# QA Audit – Maplini v0.20.49

## Release
**v0.20.49 – Dokument → verkligt flöde**

## Scope
Bygger vidare på v0.20.48 Smart dokumenttolkning och gör uttryckliga villkor och återkopplingar till ett granskningsbart graf-förslag utan att hitta på processlogik.

## Funktionellt verifierat
- `Om …, gör …, annars …` kan bli ett beslut med separata Ja/Nej-grenar.
- Ja/Nej-vägar skapas bara när båda vägarna uttryckligen finns i texten.
- Grenarna återansluter till nästa tydliga huvudsteg när dokumenttexten fortsätter efter villkoret.
- Uttryckliga `tillbaka till …`-formuleringar kan skapa en `Tillbaka`-loop när målsteget är entydigt.
- Tvetydigt återkopplingsmål lämnas utan automatisk pil och markeras för kontroll.
- Möjliga delprocessreferenser markeras som förslag men omvandlas inte automatiskt.
- Granskningsvyn visar Vägar, Loopar och konkret nästa mål för upptäckta grenlänkar.
- Den ritade canvasen använder dokumentets föreslagna graf och märkta länkar.
- Ingen Supabase-, RLS-, schema- eller molnsäkerhetsförändring.

## QA-resultat
- `python -m py_compile app.py`: PASS
- Python pytest: **400/400 PASS**
- JS-testfiler: **30/30 PASS**
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
- v0.20.48 document interpretation regression: PASS
- v0.20.49 dedicated document real-flow browser test: PASS
- Runtime DOM IDs: **355**, duplicate IDs: **0**
- Critical DOM ancestor contract: PASS

## Guardrails
- Dokumentet läses lokalt i webbläsaren i denna version.
- All dokumenttolkning är ett förslag och måste kontrolleras mot källan.
- Tvetydiga återkopplingar kopplas inte automatiskt.
- Möjliga delprocesser markeras men skapas inte utan mänskligt beslut.
- Ingen generativ AI eller extern dokumentanalys har lagts till.
- Ingen avvikelse-/adminexpansion.

## Kända begränsningar
- Regelbaserade villkor täcker främst tydliga svenska `om/ifall … annars …`-formuleringar.
- Mer komplexa nästlade villkor och parallella flöden kräver fortsatt manuell kontroll.
- Skannade PDF:er utan textlager kräver OCR, vilket inte ingår.
- DOCX/PDF-läsarbibliotek laddas från CDN vid behov.

## Release status
Push-klar ZIP. Inte pushad och inte verifierad live.
