# Maplini v0.9.8 — Canvas recovery + combined Google Sheets

## Canvas
v0.9.8 är återbaserad på v0.9.4, den sista fungerande editorbasen före
layoutregressionerna i v0.9.5–v0.9.7.

Det innebär att de riskabla senare layoutreglerna inte följer med.
De säkra prestandavinsterna från v0.9.4 finns kvar.

Dessutom finns ett skydd så att ett trasigt sparat processobjekt inte ska
kunna göra hela editorn tom; i så fall öppnas en tom process och felet loggas.

## Google Sheets
De två tidigare knapparna är sammanslagna till en enda meny:

`Google Sheets ▾`

Val:
- `Skapa i Google Drive` — skapar ett riktigt Google Sheet via Google API.
- `Ladda ner .xlsx` — skapar en lokal fil som kan öppnas/importeras i Google Sheets.

Funktionerna är alltså olika, men presenteras nu på ett enda ställe i toolbaren.
