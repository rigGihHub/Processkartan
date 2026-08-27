# Processkartan – Streamlit-prototyp v0.1

## Starta

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Ingår

- drag-and-drop-processkarta
- start, aktivitet, beslut och slut
- pilar mellan processsteg
- swimlanes: Bid/Sälj, Region, Kalkyl, Juridik, Ledning
- metadata per steg: ansvar, input, output, risk, kontroll, KPI, dokument/bevis
- undo/redo
- spara/öppna projekt som JSON
- Google Docs-kompatibel `.doc`-export av processbeskrivningen
- flikar för risker, dokument, revisioner, rapport/export och administration

## Medveten begränsning

Ritmotorn ligger i en inbäddad HTML/JavaScript-komponent. Det ger en betydligt bättre rityta än rena Streamlit-widgetar, men data är ännu inte synkad till en gemensam backend/databas.

## Rekommenderad v0.2

1. Gemensam datamodell i SQLite/Turso/PostgreSQL
2. Synkning mellan ritmotor och backend
3. Redigerbara swimlanes och egna roller
4. Piltext: Ja/Nej, återkoppling, villkor
5. Riskmatris och kontrollregister
6. Versionshistorik och audit log
7. Rollbaserade behörigheter
8. Google OAuth
9. Direkt export till Google Docs och Google Slides
10. Processhierarki och klickbara delprocesser
