# Maplini v0.10.1 — Layout recovery + visible version

## Layout
v0.10.0 använde absolut positionering för sidebar/canvas. Det löste ett problem
men gjorde att canvasen kunde lägga sig ovanpå header och toolbar.

v0.10.1 återgår till en stabil grid:
- toolbar/header ligger normalt ovanför editorn
- sidebar och canvas ligger i samma grid-rad
- båda startar direkt under toolbaren
- sidebar har egen scroll
- canvasområdet har egen scroll
- inga absoluta top/left-positioner används

## Versionsnummer
Aktuell version visas nu under Maplini-payoffen, exempelvis:

`v. 0.10.1`
