# Maplini v0.10.2 — DOM structure fix

Det verkliga layoutfelet var en extra `</div>` före `</aside>`.

Den extra stängtaggen stängde `.p48-body` för tidigt, så `<main id="p48-scroll">`
med canvasen hamnade utanför editor-layouten. Det gav den stora grå ytan och
förskjutna canvasen.

## Fix
- Felaktig extra `</div>` borttagen.
- Sidebar och canvas-main är nu direkta syskon i `.p48-body`.
- Layout-CSS förenklad till vanlig tvåkolumns-grid.
- Tidigare top/left/absolute-hack borttagna.
- Automatisk HTML-strukturtest tillagd i releasebygget.

## Versionsnummer
Visas under loggan och är nu `v. 0.10.2`.
