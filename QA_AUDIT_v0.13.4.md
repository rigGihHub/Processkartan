# QA Audit v0.13.4

## Scope
Desktop left-sidebar scroll reachability regression.

## Fix
- `.p48-side` keeps its existing 900px editor viewport.
- `overflow-y: scroll` ensures a real scroll container.
- `min-height:0` prevents grid-item minimum sizing from blocking scroll.
- `scrollbar-gutter:stable` keeps layout stable.
- bottom padding provides clearance below the final sidebar controls.
- `.p48-body` DOM/layout contract is unchanged.

## Regression intent
Verify Python/JS syntax, full pytest/JS suites, critical editor DOM, and ZIP integrity.
