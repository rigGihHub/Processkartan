# Maplini v0.9.6 — Stabilization release

Den här versionen backar de riskabla layoutoptimeringarna från v0.9.5 som kunde skapa en stor tom/grå yta och skjuta ned editorn.

## Backat
- content-visibility på noder
- aggressiv CSS contain på sidebar/toolbar/processlista
- contain: layout paint style på canvas

## Behållna prestandavinster
- partial link redraw
- node/link caches
- bounding-box prefilter för kopplingsträff
- idle localStorage serialization
- skip av identiska localStorage writes
- processlist-signatur för att undvika onödiga rerenders
- färre DOM-skrivningar

## Stabilisering
- fast editorhöjd i Streamlit-komponenten
- overflow/min-height normaliseras inne i iframe
- geometri och länkar invalideras vid resize
- extra layout self-heal efter initial render
