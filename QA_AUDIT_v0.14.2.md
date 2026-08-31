# QA Audit v0.14.2

## Scope
Layout & Formatting Polish.

## Changes verified
- Vertical Smart Layout resets internal connector anchors to auto and clears stale via points so connectors use centered bottom/top anchors.
- Desktop body/sidebar/scroll viewport uses `--p48-desktop-body-h`, calculated from available screen/parent height; component height reduced to keep the whole sidebar scrollbar reachable.
- Node styles have visibly differentiated 3D, raised, glass and flat treatments without moving node geometry.
- Typography controls are grouped in `.p48-text-format-block`: font, size, bold, italic, underline and alignment.

## QA
- Python compile: PASS
- pytest: 174/174 PASS
- JavaScript suites: 24/24 PASS
- `node --check` all `maplini_*_core.js`: PASS
- Embedded editor JavaScript: PASS
- Critical DOM nesting: PASS
- ZIP integrity: pending packaging
