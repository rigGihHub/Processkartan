# v0.10.11 — MOBILE + CONNECTOR STABILIZATION
- Rättar mobilgrundorsaken: v0.10.9 använde CSS-selektorer som inte motsvarade den riktiga DOM:en.
- Mobil-CSS använder nu `.p48-top`, `.p48-brand`, `.p48-logo-crop` och `#p48-name`.
- Toppraden kan inte radbrytas och skjuta canvasen ur bild; den scrollas horisontellt.
- Verktyg ligger först på mobil och öppnar vänsterpanelen som drawer.
- Canvasen hålls synlig och panorerbar med touch.
- Connector utilities är utbrutna till `maplini_connector_core.js`.
- Utökade regressions- och syntaxkontroller.
