# Maplini v0.10.25 — Desktop Regression & UI Cleanup

## Fokus
Skydda desktop-layouten efter flera mobil-, state- och performance-releaser samt ta bort verifierad död layout-CSS.

## Genomfört
- Ny explicit desktop-guard för den etablerade layouten: 220 px sidebar + separat scrollande canvas.
- Desktop-toolbar återställs uttryckligen till wrap/visible-beteende utanför mobilbreakpoint.
- Sidebar tvingas tillbaka till normal desktop-position/visibility och kan inte ärva drawer-beteende.
- Canvas-scrollområdet hålls vid desktop-höjd och separat overflow.
- Responsiv resize stänger mobil-drawer och synkar selection-mode deterministiskt när viewport går tillbaka till desktop.
- Tog bort ett gammalt outer-Streamlit CSS-block som försökte styla iframe-klasser (`.p48-main`, `.p48-stage`, `.p48-canvas-wrap`, `#p48-canvas`). Det kunde aldrig påverka editorn inne i `components.html` och var verifierad teknisk skuld.
- Ny separat `tests/test_desktop_contract.py`.

## Oförändrat
Mobilreglerna och den fungerande mobile drawer/canvas-panningen är kvar. Ingen databas, OAuth, secrets eller dependency ändras.

## Inte verifierat här
Ingen fysisk browser/device-session eller live-deployment på Streamlit påstås verifierad.
