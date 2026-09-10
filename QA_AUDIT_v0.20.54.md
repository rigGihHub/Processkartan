# QA AUDIT v0.20.54 – Förstå samband

## Resultat

- `python -m py_compile app.py`: PASS
- `node --check` på samtliga `maplini_*_core.js`: PASS
- Samtliga core-JS-test + background state: PASS
- `pytest -q`: **420 passed**
- Chromium `browser_interaction_smoke.py`: PASS
- Chromium `browser_v02053_any_source.py` regression: PASS
- Chromium `browser_v02054_understand_relations.py`: PASS
- Kritisk DOM ancestor-kontroll: PASS
- Duplicate HTML/DOM IDs i extraherad editor-HTML: PASS

## Ny funktion verifierad

- Explicit orsak → konsekvens upptäcks och visas i granskningsflödet.
- Relationsantal visas kompakt i statusraden.
- Neutral sekvens får ingen påhittad semantisk relation.
- Källspårning från Any Source → Process är kvar.

## Avgränsning

Relationsmotorn är medvetet konservativ och regelbaserad. Den märker bara relationer när tydliga språkliga signaler finns; den försöker inte semantiskt gissa dolda kausala samband. Ingen Supabase-/schema-/RLS-/OAuth-förändring gjordes.

## Releasebedömning

Push-klar ZIP kan skapas. Release är inte verifierad live och ska därför inte beskrivas som live.
