# QA audit – Maplini v0.20.93

## Fokus

Vänsterflanken i Förstå ska beskriva processlogiken, inte den visuella placeringen av rutor.

## Verifierat

- Sammanhängande steg följer riktade kopplingar.
- Explicita Ja/Nej-etiketter visas och ingen huvudgren utses.
- Sammanfogningar läggs efter sina inkommande grenar.
- Cykler terminerar utan dubblerade steg.
- Den huvudsakliga komponenten väljs deterministiskt; övriga delflöden märks Okopplade steg.
- Klick, aktiv markering och mobilbeteende från v0.20.92 är bevarade.

## Automatiska kontroller

- `pytest`: 516 godkända
- JavaScript: 38 testfiler godkända
- Core JavaScript: 30 filer syntaxkontrollerade
- Python-kompilering och `git diff --check`: godkända
