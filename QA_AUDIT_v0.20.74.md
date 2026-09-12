# QA Audit v0.20.74 – Editor Coherence

## Resultat
- `pytest -q`: **469 passed**
- `python -m py_compile app.py`: PASS
- `node --check` på samtliga `maplini_*_core.js`: PASS
- Chromium v0.20.74 riktad UI-regression: PASS
  - logotyp/brand och huvudtoolbar börjar på samma Y-position på desktop
  - vänsterpanel = 304 px vid 1500 px viewport
  - markerad single-node visar inte längre den duplicerade flytande `p48-node-quick`-toolbaren
  - nodens gröna `+`-kontroll finns kvar som primär canvasåtgärd
  - kontextpanelen ligger före byggpaletten när ett steg är markerat
- Befintlig contextual-sidebar Chromium-regression: PASS
- Ingen ändring av processdata, sparformat, kopplingslogik, Supabase eller RLS.

## Fångad regression under QA
Första browserkörningen visade att en äldre CSS-regel låg senare i dokumentet och därför vann över den nya desktop-headern. v0.20.74-stilarna flyttades till sista override-lagret och testades om i Chromium innan paketering.
