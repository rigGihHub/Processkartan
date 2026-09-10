# QA Audit – Maplini v0.20.45

## Scope
Releasefokus: **Förstå processen på 30 sekunder**. Läsvyn ska ge omedelbar orientering utan dashboard, AI eller ny processdata.

## Förändringar verifierade
- Läsvyn visar en kompakt processöverblick ovanför canvasen.
- Överblicken visar **Börjar med**, **Leder till**, **Ansvar** och **Omfattning**.
- Start/slut härleds deterministiskt från befintlig processgraf; ingen generativ tolkning.
- Ansvar hämtas från befintligt `responsibleRole` och dubbletter tas bort.
- Omfattning visar antal steg och beslut.
- Ingen ny persisterad data, schema-, Supabase-, RLS-, OAuth- eller dependencyändring.
- Mobil visar samma överblick som en horisontellt skrollbar kompakt rad.

## Automatiska tester
- `python -m py_compile app.py`: PASS
- Python/pytest: **381/381 PASS**
- JS-testfiler: **28/28 PASS**
- Core JS `node --check`: **23/23 PASS**
- Desktop Chromium interaction smoke: PASS
- Mobile Read/Follow smoke: PASS
- Mobile canvas fit/readability smoke: PASS
- v0.20.44 first-process regression: PASS
- Kritisk HTML: **330 ID:n, 0 dubbletter**

## Riskbedömning
Låg. Funktionen är en läslins ovanpå befintlig graf och befintlig metadata. Den flyttar inga noder, ändrar ingen logik och sparar inget nytt till processdata.

## Release status
Push-klar ZIP. Inte verifierad live.
