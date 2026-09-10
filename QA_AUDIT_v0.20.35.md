# QA Audit v0.20.35

Release: Large Process Interaction Performance

## Scope
- Real-browser interaction benchmark at 100 / 250 / 500 / 1000 nodes.
- Magnetic snap hot path during node drag.
- Pointer-move frame coalescing during drag.
- Overview/minimap geometry-cache reuse.
- No schema, Supabase or RLS changes.

## Interaction benchmark (Chromium, container; median of 3)

### Magnetic snap – 200 calculations
| Nodes | v0.20.34 | v0.20.35 |
|---:|---:|---:|
| 100 | 37.9 ms | 0.3 ms |
| 250 | 77.8 ms | 0.1 ms |
| 500 | 178.8 ms | 0.1 ms |
| 1000 | 353.2 ms | ~0.0 ms |

The large reduction comes from building sorted snap targets once per drag gesture and avoiding repeated DOM layout reads/scans on every pointer move. Values near zero are below the useful resolution of this short microbenchmark; they should be interpreted as “very small”, not literally zero cost.

### Other interaction paths, v0.20.35
| Nodes | Drag 60 hot frames | Select ×100 | Zoom ×100 | Overview viewport ×100 | Persist ×10 |
|---:|---:|---:|---:|---:|---:|
| 100 | 18.2 ms | 107.8 ms | 1.3 ms | 10.3 ms | 28.0 ms |
| 250 | 32.2 ms | 133.0 ms | 0.8 ms | 22.9 ms | 68.0 ms |
| 500 | 48.7 ms | 216.3 ms | 0.7 ms | 39.9 ms | 133.9 ms |
| 1000 | 81.6 ms | 441.7 ms | 0.9 ms | 84.4 ms | 288.2 ms |

These timings are diagnostic, not hard CI gates; browser/container scheduling varies. The benchmark still shows selection/persist scaling roughly with map size and they remain candidates for later evidence-led optimization.

## Large-process open/render regression check
A fresh run of the existing large-process benchmark after v0.20.35 remained healthy in the same container:
- 100 nodes: restore ~79.6 ms
- 250 nodes: restore ~264.9 ms
- 500 nodes: restore ~823.4 ms
- 1000 nodes: restore ~2982.2 ms

This is not compared as an exact percentage against prior runs because browser/container load varies. It confirms the interaction changes did not regress the large-map restore path in this run.

## Required release checks
- `python -m py_compile app.py`: PASS
- Python pytest: **342/342 PASS**
- JavaScript test files: **27/27 PASS**
- Core JavaScript `node --check`: **22/22 PASS**
- Chromium desktop interaction smoke: PASS
- Chromium mobile read/follow smoke: PASS
- Large-process Chromium benchmark: PASS
- Large-process interaction Chromium benchmark: PASS
- Critical DOM structure: PASS
- Literal static HTML IDs: **311**, duplicates **0**
- ZIP integrity: PASS after final packaging.

## Notes
- Drag pointer events are intentionally coalesced to requestAnimationFrame; the latest pending event is flushed on gesture end so final position is not lost.
- Full connector marker/label/hit-layer rebuilding is still deferred until drag end, preserving the existing fast-geometry policy.
- No cloud schema, OAuth, RLS, dependency or migration changes.
- Release is prepared locally only; it is not verified as pushed/deployed/live.
