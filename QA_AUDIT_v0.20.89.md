# QA audit – Maplini v0.20.89

## Omfattning

Samlad Editor Reset efter visuell granskning av v0.20.88: stegredigering, markerad nod, snabbskapande, rutstorlek och sidopanelens fokus.

## Automatiska kontroller

- `pytest`: 501 godkända
- JavaScript: 38 testfiler godkända
- Core JavaScript: 30 filer syntaxkontrollerade
- `python -m py_compile app.py`: godkänd
- `git diff --check`: godkänd

## Skyddade kontrakt

- Befintliga processdata och sparformat ändras inte.
- Fri storleksändring och storlekspresets använder befintliga width/height-fält.
- Processfärger, typsnitt, nodpositioner och kopplingslogik bevaras.
- Förstå och Följ använder oförändrad processlogik.
- Responsiv layout, livscykelsparning och initial canvasjustering körs inom editorns runtime-scope.

## Livekontroll efter deploy

Verifiera särskilt att snabbskapandets plus ligger utanför noden, att endast ett resize-handtag syns, att sidopanelen börjar högst upp vid nytt nodval och att den dubblerade sammanhangssektionen är dold i Rita.
