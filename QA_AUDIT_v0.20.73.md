# QA Audit v0.20.73 – Floating Tools & Canvas First

## Resultat
- `pytest -q`: **465 passed**
- `python -m py_compile app.py`: PASS
- `node --check` på samtliga 30 `maplini_*_core.js`: PASS
- Riktad Chromium UI-regression: PASS
  - desktop-brand = 72 px
  - öppning av `Mer` ändrar inte toppfältets eller canvasens bounding box
  - `Mer` renderas som en fast högerpanel (360 px i 1500 px viewport)
  - panelen överlappar inte sin egen `Mer`-knapp
  - snabbkontrollen `A4 stående · Auto` är dold i standardvyn
- Ingen ändring av processdata, sparformat eller kopplingslogik.

## Notering
Det generella historiska browser-smoketestet innehåller sekvenser som förutsätter äldre placering av `Visa` utanför `Mer`. v0.20.73 har därför verifierats med en riktad Chromium-regression för den nya avsiktliga navigationsstrukturen, samtidigt som Python- och JS-regressionerna är helt gröna.
