# Maplini v0.10.11
Mobil- och connector-stabilisering.

Mobil:
- Verktyg ligger först i toppraden.
- Toppraden scrollas horisontellt istället för att radbrytas.
- Canvasen ligger direkt under header/topprad.
- Vänsterpanelen öppnas som drawer.
- Touchytor och iPhone safe-area behålls.

Teknik:
- Connector helpers ligger i `maplini_connector_core.js`.
- Regressionstester skyddar mobilens riktiga DOM/CSS och connector wiring.
