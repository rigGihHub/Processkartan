# Maplini v0.10.23 — Mobile Touch & Interaction Hardening

Real issues fixed:
- Mobile CSS targeted nonexistent `.p48-resize-handle`; real class is `.p48-resize`.
- Blank canvas retained `touch-action:none`; it now pans naturally on mobile, while selection mode explicitly disables native pan.
- Connector preview, area selection and dropped-node coordinates double-counted scroll offsets after horizontal scrolling. A single tested client-to-canvas conversion now handles these paths.
- Touch node drag now ignores normal finger jitter with a larger pointer-type threshold.
- Connector and marquee gestures clean up on `pointercancel`.
- Connector/resize controls get larger invisible touch hit areas without changing their visible size.

Automated QA covers mobile primitives, full critical-flow E2E, DOM contract, Python/JS syntax and existing regressions.
Physical Android/iPhone gesture verification is not claimed offline.
