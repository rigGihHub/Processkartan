# Maplini v0.9.5 — Ultra performance pass

Det här varvet fokuserar på större processkartor.

- Bounding-box-cache före exakt länkträfftestning.
- Node→link-index cache vid drag/resize.
- Cache av formateringskontroller.
- localStorage-serialisering via requestIdleCallback när möjligt.
- Sparade-processer-listan byggs bara om när den faktiskt ändrats.
- Färre DOM-style-skrivningar för kopplingspunkter.
- Idle-persist för vissa processinställningar.
- Mer aggressiv CSS containment/content-visibility.

Funktionaliteten är oförändrad.
