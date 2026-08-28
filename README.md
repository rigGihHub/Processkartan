# Maplini v0.8.1 — Google Sheets export

## Nytt
- Ny knapp `Exportera Google Sheets`.
- Exporten skapar en `.xlsx` som kan öppnas direkt i Google Sheets.
- Filen innehåller två flikar:

### Processsteg
Varje processsteg blir en rad med:
- Ordning
- ID
- Typ
- Text
- Inputs
- Outputs
- Nästa steg
- Föregående steg
- X/Y-position
- Bredd/höjd

### Kopplingar
Varje pil/koppling blir en rad med:
- Från ID
- Från steg
- Till ID
- Till steg
- Anslutningssida

## Varför tabellformat?
PDF och DOCX är visuella exporter. Google Sheets-exporten är avsedd för analys, sortering, filtrering och vidare processarbete.

Google Sheets kan öppna `.xlsx` direkt via Arkiv → Importera eller genom att ladda upp filen i Google Drive.
