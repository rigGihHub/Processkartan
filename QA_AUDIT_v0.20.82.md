# QA Audit – Maplini v0.20.82

## Omfattning

Riktad release efter livegranskning av v0.20.81. Fokus är Canvas Calm, sidformatets grundläge och läsbarhet i kontextpanelen. Ingen datamodell eller processlogik ändras.

## Verifierat

- GitHub `main` matchade `588aa9ac4b8b38dfc1345e0bdd212274233fdf1b` före arbetet.
- Livegranskning visade att PDF-guiden var avstängd men att äldre CSS fortfarande vann över plusknappens hotfix.
- De nya `#pk48`-scopade reglerna har högre specificitet än den äldre Canvas First-regeln och finns även i huvudstilen, så resultatet är oberoende av när core-scriptet körs.
- HTML och runtime initierar båda PDF-vyn som `off`.
- `482/482` pytest passerar.
- `38/38` JavaScript-testfiler passerar.
- `node --check maplini_ui_core.js` passerar.
- `python -m py_compile app.py` passerar.

## Browserstatus

Liveversionen före ändringen granskades i Chromium på desktop. Den lokala Playwright-installationen kunde inte hämta sin browserbinär i denna miljö, så den nya renderingen måste slutverifieras efter deploy. Ett riktat browserskript finns i `tests/browser_v02082_canvas_calm.py` för samma kontroll i ordinarie QA-miljö.

## Kvarvarande risk

Den enda öppna releasekontrollen är visuell verifiering av den deployade CSS-regeln och mobilregression efter push. Ingen release ska beskrivas som liveverifierad innan detta är gjort.
