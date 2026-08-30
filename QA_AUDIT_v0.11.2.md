# QA Audit v0.11.2

Fokus: **Quick Next Step / Faster Editing**.

## Verifierat
- `APP_VERSION = 0.11.2`.
- Markerad Start/Aktivitet/Beslut/Dokument/Delprocess får **＋ Nästa steg** på canvasen.
- Typval: Aktivitet, Beslut, Dokument, Slut.
- Nytt steg placeras via testbar `MapliniEditingCore.nextStepPosition()` med högerprioritet och kollisionsundvikande fallback.
- Ny koppling använder befintlig smart connector-routing och automatiska Ja/Nej-förslag från beslut.
- Nya steget markeras och öppnas direkt för inline-redigering.
- Enter avslutar redigering; Shift+Enter kan användas för radbrytning.
- Skapande + koppling är en Undo-operation.
- Quick-next-kontrollen ignoreras av nodens drag-handler och menyer stängs vid klick utanför.

## QA-resultat
- Python compile: godkänd (`app.py`, `google_docs.py`, `maplini_google_ui.py`).
- Pytest: **157/157 godkända**.
- Node.js: **21/21 testsviter godkända**.
- Extraherad huvud-JavaScript: `node --check` godkänd.
- BeautifulSoup desktop-DOM-kontrakt: godkänt.
- Ingen databas-, OAuth-, secret- eller dependencyändring.

## Känd begränsning
- Exakt placering och touchkänsla bör smoke-testas i riktig desktop-/mobilwebbläsare efter push.
