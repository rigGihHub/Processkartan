# QA Audit – Maplini v0.20.19

## Release
- Version: `0.20.19`
- Namn: **Connector Label Clarity**
- Bas: v0.20.18 Connector Lane Separation
- Datamodell/Supabase: ingen ändring eller migrering

## Funktionell avgränsning
- Connector-etiketter väljer ren position längs befintlig rutt; själva connector-rutten ändras inte.
- Node-obstacles och redan renderade etiketter vägs in.
- Längre raka segment och luft från böjar föredras.
- Etiketten får byta sida om standardläget är blockerat.
- Markerad pils snabbverktyg speglas mot etikettens faktiska position.
- Manuella connector-inställningar påverkas inte.

## Automatiska kontroller
- `python -m py_compile app.py`: PASS
- Python pytest: 268/268 PASS
- JavaScript testfiler: 27/27 PASS
- `node --check` core-JS: 22/22 PASS
- Chromium browser interaction smoke: PASS
- Kritisk DOM-hierarki: PASS
- Dubbla DOM-id:n: 0
- ZIP-integritet: PASS
