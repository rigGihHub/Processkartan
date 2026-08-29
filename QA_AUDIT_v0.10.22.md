# Maplini v0.10.22 — Performance & Modularization Audit

## Focus
Reduce repeated DOM/style work and resize scheduling without changing product behavior.

## Implemented
- New pure `maplini_performance_core.js`.
- Keyed `rafOnce()` scheduling for responsive layout and editor alignment.
- Process background/logo styling uses a signature cache and skips identical rewrites.
- Process-list rendering uses a signature cache and skips identical DOM rebuilds.
- Destructive process deletion forces list refresh so memoization cannot hide mutations.
- Existing workflow, connector, state, reliability and export modules are preserved.

## Architecture
Another cross-cutting concern—performance scheduling/signatures—is extracted from `app.py` into a testable module.

## Not claimed
No physical-device profiling, browser Performance-panel trace, live deployed timing or network benchmarking is claimed in this offline release.
