# QA Audit v0.20.34

Release: Large Process Performance

## Scope
- Real-browser benchmark: 100 / 250 / 500 / 1000 nodes.
- Large-map connector routing policy.
- Persist duplicate-comparison removal.
- No schema, Supabase or RLS changes.

## Performance baseline (Chromium, container; median of 3)
| Nodes | Links | Restore | Serialize | Save flush | Overview |
|---:|---:|---:|---:|---:|---:|
| 100 | 96 | 107.2 ms | 4.8 ms | 2.4 ms | 9.4 ms |
| 250 | 240 | 362.4 ms | 6.3 ms | 4.4 ms | 39.5 ms |
| 500 | 480 | 1076.2 ms | 11.1 ms | 8.7 ms | 165.0 ms |
| 1000 | 960 | 3752.8 ms | 21.8 ms | 19.9 ms | 688.6 ms |

Previous v0.20.33 baseline in the same environment was approximately 153.7 / 573.6 / 1297.9 / 4557.9 ms restore time, so the final v0.20.34 routing changes reduced restore time at all four sizes in this run. Timing is diagnostic rather than a hard CI gate because browser/container load varies.

## Required release checks
- `python -m py_compile app.py`: PASS
- Python pytest: **337/337 PASS**
- JavaScript test files: **27/27 PASS**
- Core JavaScript `node --check`: **22/22 PASS**
- Chromium desktop interaction smoke: PASS
- Chromium mobile read/follow smoke: PASS
- Critical DOM structure: PASS
- Literal HTML/DOM IDs: **0 duplicates**
- ZIP integrity: verified after packaging.
