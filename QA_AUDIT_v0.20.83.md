# QA Audit – Maplini v0.20.83

## Omfattning

Fokuserad förenkling av stegredigeringen efter livegranskning av v0.20.82. Ingen ny produktfunktion eller datamodell införs.

## Förändringar

- Redigeringsformuläret visas före sammanhangsöversikten.
- Input/Output använder inte längre ett separat kort inuti redigeringskortet.
- Redundant fotnot har tagits bort.
- Sammanhangsöversikten finns kvar men har lägre visuell vikt.
- Bred desktop får 320 px sidopanel; mindre desktop behåller den kompaktare layouten.

## Testresultat

- `486/486` pytest passerar.
- `38/38` JavaScript-testfiler passerar.
- `node --check maplini_ui_core.js` passerar.
- `python -m py_compile app.py` passerar.
- `git diff --check` passerar.

## Livekontroll efter deploy

Verifiera att redigeringsfältet är först, att Input/Output saknar dubbel kortinramning och att canvasen fortfarande har tillräcklig bredd på desktop. Mobilens befintliga brytpunkt ändras inte men ska ändå snabbkontrolleras visuellt.
