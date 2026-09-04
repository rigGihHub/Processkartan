# QA Audit – Maplini v0.20.18

## Release
- Version: `0.20.18`
- Namn: **Connector Lane Separation**
- Bas: v0.20.17 Connector Crossing Reduction
- Datamodell/Supabase: ingen ändring eller migrering

## Funktionell avgränsning
- Längre parallell eller nästan parallell överlappning mellan auto-managed orthogonal connectors får routingkostnad.
- Kort gemensam stam vid delad källa/mål undantas via en 30 px tolerans.
- Befintlig prioritet bevaras: nodkollision >> riktig korsning >> parallell överlappning >> längd/svängar.
- Manuella/fixed/free connectors påverkas inte.

## Automatiska kontroller
- `python -m py_compile app.py`: PASS
- Python pytest: 267/267 PASS
- JavaScript testfiler: 27/27 PASS
- `node --check` core-JS: 22/22 PASS
- Chromium browser interaction smoke: PASS
- Connector core integration: smart route väljer separat korridor när naturlig lane redan används: PASS
- Kritisk DOM-hierarki: PASS
- Dubbla literal HTML-id:n: 0
- ZIP-integritet: PASS
