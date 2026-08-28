# v0.10.12 — MOBILE SCROLL FIX

- Rättar mobilproblemet där sidan inte gick att scrolla upp och ned.
- Tar bort vertikal scroll-lock från html/body, #pk48 och .p48-body.
- Canvasbehållaren behåller horisontell panorering men fångar inte längre normal sidscroll.
- Streamlit-komponentens höjd höjs från 1000 till 1650 px så yttersidan kan scrollas naturligt.
- Vänsterpanelen via Verktyg behålls.
- Mobilens logga använder contain/overflow-visible så den inte kapas.
- Nya regressionstester för mobilscroll, canvaspanorering, logga och komponenthöjd.
