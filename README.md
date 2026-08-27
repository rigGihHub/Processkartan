# Processkartan v0.3.0

Streamlit-prototyp för drag-and-drop-baserad processkartläggning.

## Starta lokalt

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Arbetsprincip

Appen ska i första hand styras genom drag-and-drop:
- dra aktiviteter, beslut, delprocesser och grupper till arbetsytan
- dra processsteg mellan swimlanes
- dra från grön anslutningspunkt för att skapa pilar
- dra risker, kontroller, KPI och dokument/bevis direkt på processsteg
- Ctrl/Cmd-klick för multiselect
- kopiera/klistra in markerade steg
- drag-and-drop för swimlane-ordning

## Google Docs-export

Klicka **Exportera till Google Docs (.doc)** i appens högra panel.

1. Appen laddar ner `Processkartan_Google_Docs.doc`.
2. Ladda upp filen till Google Drive.
3. Högerklicka på filen och välj **Öppna med → Google Dokument**.
4. Processbeskrivningen blir redigerbar i Google Docs.

Exporten innehåller processsteg, ansvar, risker, kontroller, KPI och dokument/bevis.
För själva visuella processkartan används **Exportera karta (.svg)** och SVG-filen kan sedan infogas i Google Docs eller Google Slides.

> Direkt skapande av ett Google Docs-dokument i användarens Drive kräver Google OAuth/API och är ett senare integrationssteg.
