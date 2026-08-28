# Maplini v0.9.7 — Canvas visibility + export toolbar fix

## Canvas
- Återställer synlig processyta efter regressionen i v0.9.6.
- Editor-scroll får fast, synlig höjd.
- Canvas hålls på 2400 × 1400 px.
- Overflow normaliseras så innehållet inte döljs bakom en grå yta.
- Full länk/geometri-refresh körs efter initial layoutstabilisering.

## Exportknappar
`Skapa Google Sheet` ligger nu tillsammans med:
- Exportera PDF
- Exportera DOCX
- Ladda ner Sheets-fil

Alla exporter är samlade till höger i toolbaren.
