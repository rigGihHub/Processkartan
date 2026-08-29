# v0.10.34 — DOCUMENT NODE

- Ny canvasruta: **Dokument**.
- Dokumentrutan kan länkas till en http/https-adress, t.ex. Google Drive, SharePoint, OneDrive eller en PDF/webbsida.
- Markerad dokumentruta visar fältet **Dokumentlänk** i formateringspanelen.
- Dokumentrutan visar en tydlig **Öppna dokument**-knapp när en giltig länk finns.
- Länken öppnas i ny flik med `noopener,noreferrer`.
- Endast http/https accepteras för att undvika osäkra URL-scheman.
- Dokumentrutor fungerar med befintlig drag, resize, kopplingar, undo/redo, save/reload, cloud state och read-only.
- Dokumentlänk följer med Google Sheets/XLSX-export.
- Ingen databas-, OAuth-, secret- eller dependency-ändring.
