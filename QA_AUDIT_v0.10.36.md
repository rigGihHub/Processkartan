# QA v0.10.36

Verifierat:
- markerad connector kan starta drag både via linjens hit-area och draghandtaget
- connector bend sparas via befintlig `setVia`
- zoomkontroller − / 100% / +
- all canvasgrafik skalar via gemensam transform
- node drag, resize, drop, connector drag och logo drag använder zoomkorrigerade koordinater
- desktop/mobile DOM-kontrakt
- Python- och JS-syntax
- full pytest och samtliga Node-sviter

Ej hävdat verifierat:
- live Streamlit
- fysisk Android/iPhone
