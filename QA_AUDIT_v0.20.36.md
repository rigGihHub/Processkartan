# QA Audit v0.20.36

Release: Mobile Canvas Fit & Readability

## Scope
- Fix the mobile Read-mode composition shown in the user-provided screenshot.
- Prevent small/medium process maps from opening as unreadable thumbnails.
- Reduce mobile reader chrome and excess empty canvas height.
- Keep the existing explicit "Anpassa" behaviour available for whole-process overview.
- No schema, Supabase, RLS, OAuth or cloud-data changes.

## Reproduced before/after reference (Chromium, 390 × 844 CSS px, touch/mobile context)

| Metric | v0.20.35 | v0.20.36 |
|---|---:|---:|
| Initial mobile read scale | 25 % | 76 % |
| First step rendered width | ~53 px | ~162 px |
| Mobile reader bar height | ~60 px | ~52 px |
| Read canvas viewport height | ~574 px | 540 px |

The previous behaviour used the desktop "fit everything" calculation with a large margin. On a 390 px viewport the horizontal process therefore hit the 25 % minimum scale and became thumbnail-sized. v0.20.36 deliberately prefers readable scale and starts at the process Start/left-most step when the whole process cannot remain readable at once.

## Mobile viewport geometry checks
New Chromium geometry smoke ran at:
- 360 × 844
- 390 × 844
- 430 × 844

For each viewport the test verifies:
- Read mode activates.
- Initial process scale is at least 74 % for the four-step starter process.
- Reader chrome height stays at or below 54 px.
- Read canvas stays within the intended compact height band.
- The first process step is immediately visible.
- The first step is visually substantial rather than thumbnail-sized.

## Required release checks
- `python -m py_compile app.py`: PASS
- Python pytest: **346/346 PASS**
- JavaScript test files: **27/27 PASS**
- Core JavaScript `node --check`: **22/22 PASS**
- Chromium desktop interaction smoke: PASS
- Chromium mobile read/follow smoke: PASS
- Chromium mobile canvas fit/readability smoke (360 / 390 / 430 px): PASS
- Critical DOM structure: PASS
- Parsed embedded HTML IDs: **306**, duplicates **0**
- ZIP integrity: PASS after final packaging.

## Product decision
Mobile Read mode should not try to display the entire desktop process at any cost. **Readable process steps take priority over whole-map overview.** Users can still press **Anpassa** to see the whole process, and can pan naturally when the readable default view shows only part of a wider process.

## Notes
- No process data is modified by the mobile fit strategy.
- No node positions are moved.
- No database migration is required.
- Release is prepared locally only; it is not verified as pushed/deployed/live.
