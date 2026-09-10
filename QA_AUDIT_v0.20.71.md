# QA AUDIT – Maplini v0.20.71

## Release
Focus Path i Förstå

## Resultat
- py_compile: PASS
- pytest: 461/461 PASS
- JS unit tests: PASS
- node --check för core/static/assets JS: PASS
- Chromium browser_interaction_smoke: PASS
- Chromium browser_v02068_canvas_visual_hierarchy: PASS
- Chromium browser_v02067_canvas_flow_builder: PASS
- Chromium mobile_canvas_fit_readability: PASS
- Processdata/schema: oförändrat
- Ingen deploy/live-verifiering utförd

## Funktionell kontroll
- Fokus aktiveras endast i Förstå-läget med markerat steg.
- Inkommande länk/nod och samtliga direkta utgående länkar/noder lyfts.
- Övrig karta dämpas visuellt.
- Beslut med flera grenar rangordnas inte.
- Fokusfunktionen muterar inte processdata.
