# QA Audit – Maplini v0.20.20

## Release
- Version: `0.20.20`
- Namn: **Flow Readability Polish**
- Bas: v0.20.19 Connector Label Clarity
- Datamodell/Supabase: ingen ändring eller migrering

## Funktionell avgränsning
- Auto-managed connectorer klassas visuellt som huvudflöde eller sidogren.
- Direkt Ja/Nej-koppling och fortsatt enkel gren klassas som sidogren.
- Huvud- och grenflöden skiljs enbart med diskret opacitet; användarens connector-färg skrivs inte över.
- Vid markering av exakt en ruta förstärks anslutna auto-managed pilar och övriga auto-managed pilar tonas tillfälligt ned.
- Manuella connectorer påverkas inte av den automatiska läsbarhetshierarkin.
- Routing, connector labels och Follow Process-logik ändras inte.

## Automatiska kontroller
- `python -m py_compile app.py`: PASS
- Python pytest: 272/272 PASS
- JavaScript testfiler: 27/27 PASS
- `node --check` core-JS: 22/22 PASS
- Chromium browser interaction smoke: PASS
- Kritisk DOM-hierarki: PASS
- Dubbla DOM-id:n: 0
- ZIP-integritet: PASS
