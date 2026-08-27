# Maplini v0.5.1

## Nytt
- Rutor kan förstoras/förminskas genom att dra i hörnen.
- `Grupp / område` är borttagen.
- Inputs och Outputs kan läggas till på varje markerad ruta.
- Inputs/Outputs sparas med processen och visas kompakt i rutan.
- UI-upprensning och större Maplini-header.
- Inline-redigering och textformatering finns kvar.
- DOCX-export finns kvar.
- Riktig Google OAuth + Google Docs API-integration finns med.

## Google Docs
För direkt skapande av dokument behöver Streamlit Secrets:

```toml
[google_oauth]
client_id = "..."
client_secret = "..."
redirect_uri = "https://DIN-APP.streamlit.app"
```

Du behöver skapa OAuth-klienten i Google Cloud Console och aktivera Google Docs API + Google Drive API.

Obs: direktintegrationen kan skapa riktiga Google Docs. I denna version är canvasdata ännu inte automatiskt bryggad från den inbäddade JS-canvasen till Streamlit-backend, så Google-panelen använder textfält. Den lokala DOCX-exporten innehåller aktuell processdata.
