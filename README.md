# Processkartan v0.4.0

## Nytt
- ISO-information borttagen helt.
- En enda stor canvas, 2400 × 1400 px.
- Flera separata processer i samma app.
- `Ny process` skapar en tom canvas.
- `Spara process` bevarar den aktuella processen.
- Processväljare för att växla mellan sparade processer.
- Lokal lagring i webbläsaren.
- Export/import av hela processbiblioteket som JSON.
- Google Docs-export (.doc).
- SVG-export.
- Drag-and-drop, pilar, multiselect, undo/redo, kopiera/klistra in och snap-to-grid.

## Starta lokalt
```bash
pip install -r requirements.txt
streamlit run app.py
```

## GitHub Desktop
1. Packa upp ZIP-filen.
2. GitHub Desktop → Repository → Show in Explorer.
3. Kopiera innehållet från den uppackade ZIP-mappen till repository-mappen.
4. Ersätt befintliga filer.
5. Commit to main.
6. Push origin.
7. Streamlit uppdaterar appen automatiskt.

## Sparning
`Spara process` sparar i webbläsarens lokala lagring.
`Spara alla (.json)` skapar en portabel backup av hela processbiblioteket.
