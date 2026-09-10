# QA Audit – Maplini v0.20.44

## Scope
Releasefokus: göra vägen från **Ny process** till första riktiga steget så kort och självklar som möjligt utan tutorial, AI eller ny processlogik.

## Förändringar verifierade
- Ny process-dialog börjar tom och visar exempelplaceholder.
- Tom, redigerbar process visar en kompakt startyta med direkt textfält.
- Enter skapar första aktiviteten med exakt användarens text.
- Den skapade rutan behåller fokus så Tab fortsätter befintligt snabbbyggande.
- Objekt in och Start finns som sekundära startvägar.
- Startytan döljs när processen innehåller steg samt i shared/read mode.
- Ingen schema-, Supabase-, RLS-, OAuth- eller dependencyändring.

## Automatiska tester
- `python -m py_compile app.py`: PASS
- Python/pytest: **380/380 PASS**
- JS-testfiler: **28/28 PASS**
- Core JS `node --check`: **23/23 PASS**
- Desktop Chromium interaction smoke: PASS
- Mobile Read/Follow smoke: PASS
- Mobile canvas fit/readability smoke: PASS
- v0.20.38 fast-building regression: PASS
- v0.20.39 safe cleanup preview regression: PASS
- v0.20.40 Follow Process 2 regression: PASS
- v0.20.41 Process Control regression: PASS
- v0.20.42 Version History regression: PASS
- Nytt `browser_v02044_first_process_flow.py`: PASS

## Browserflöde v0.20.44
Chromiumtestet verifierar:
1. Ny process öppnar namndialogen med tomt namn.
2. Enter skapar processen.
3. Första-steg-fältet får fokus.
4. `Ta emot beställning` + Enter skapar exakt en Aktivitet.
5. Startytan försvinner.
6. Den nya aktiviteten behåller fokus.
7. Tab skapar nästa steg via befintligt snabbbyggarflöde.

## Riskbedömning
Låg. Förändringen ligger ovanpå befintliga `addNode`, selection och Tab-flöden. Den introducerar ingen ny persisterad data och ändrar inte processers semantik.

## Release status
Push-klar ZIP. Inte verifierad live.
