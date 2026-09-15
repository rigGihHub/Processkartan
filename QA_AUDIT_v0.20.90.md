# QA audit – Maplini v0.20.90

## Fokus

Canvas Stage rättar den visuella skalan och nybörjarflödet för små processer efter livegranskning av v0.20.89.

## Verifierat

- Små kartor förstoras aldrig automatiskt över 100 procent.
- Kompakt, Normal och Stor använder de nya mindre dimensionerna och beslut förblir kvadratiska.
- Fri resize ned till 120 px är oförändrad.
- Ett palettklick fortsätter automatiskt en process som bara har ett steg.
- Småkartor döljer visuella scrollbars utan att blockera panorering eller stora kartor.
- Endast vit, enfärgad standardcanvas får den rena neutrala arbetsytan; användarvalda bakgrunder lämnas orörda.
- Äldre systemstandard för nodkant migreras till en tunnare, lugnare standard utan att skriva över andra användarvalda färger.

## Automatiska kontroller

- `pytest`: 507 godkända
- JavaScript: 38 testfiler godkända
- Core JavaScript: 30 filer syntaxkontrollerade
- Python-kompilering och `git diff --check`: godkända
