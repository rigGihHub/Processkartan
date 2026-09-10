# QA Audit – Maplini v0.20.42

## Release
- Version: `0.20.42`
- Fokus: Versionshistorik
- Bas: `v0.20.41 – Processkontroll`
- Ingen Supabase-, RLS-, OAuth- eller schemaändring.
- Inte verifierad live.

## Funktionell omfattning
- Lokal versionshistorik per process.
- Max 20 versioner per process.
- Vanligt Spara skapar kontrollpunkt endast vid verklig innehållsändring.
- Manuell kontrollpunkt via `+ Spara version nu`.
- Konkret diff mot nuvarande process: tillagda/borttagna/ändrade steg samt tillagda/borttagna kopplingar.
- Säker återställning: nuläget sparas först som kontrollpunkt.
- Molnanvändare får tydlig instruktion att trycka Spara efter lokal återställning.
- Versionsdata lagras separat i `maplini_version_history_v1` och ingår inte i processens normala autosave/state-signatur.

## QA-resultat
- `python -m py_compile app.py`: PASS
- Python pytest: **373/373 PASS**
- JS-testfiler: **28/28 PASS**
- Core JS `node --check`: **23/23 PASS**
- Desktop Chromium interaction smoke: PASS
- Mobile Read/Follow Chromium smoke: PASS
- Mobile canvas fit/readability Chromium smoke: PASS
- v0.20.38 fast-building regression: PASS
- v0.20.39 cleanup-preview regression: PASS
- v0.20.40 Follow Process 2.0 regression: PASS
- v0.20.41 Processkontroll regression: PASS
- v0.20.42 Versionshistorik Chromium smoke: PASS
- Kritisk desktop-DOM via regressionstest: PASS
- Statiska HTML-ID:n: **319**, dubbletter: **0**

## Medvetna begränsningar
- Historiken är lokal per webbläsare/enhet i denna release. Den synkas inte mellan enheter.
- Fulla process-snapshots används för kontrollpunkter; max 20 versioner begränsar tillväxten.
- Ingen automatisk merge av versioner.
- Ingen separat visuellt sida-vid-sida-jämförelse ännu; varje historikkort visar däremot konkret diff mot nuläget.

## Releasebedömning
Push-klar kandidat. Ska inte beskrivas som live förrän deploy har verifierats.
