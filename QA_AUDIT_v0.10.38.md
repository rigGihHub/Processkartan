# QA AUDIT v0.10.38

## Scope
Targeted fix for the in-node **+ Lägg till dokumentlänk** action.

## Root cause
The empty-document CTA selected the node and showed a status message, but did not move focus to the actual URL editor. From the user's perspective the CTA therefore appeared to do nothing.

## Fix
The CTA now selects the document node, exposes the document editor, focuses the Dokumentlänk field and scrolls it into view. Existing valid document URLs still open as links in a new tab.

## Verification
- Python compile: PASS
- pytest: 138/138 PASS
- Node JS test suites: PASS
- Embedded JavaScript syntax: PASS
- DOM contract: PASS
- No database/config/dependency changes

## Known limitation
Not physically browser/mobile tested in this environment; live smoke test remains required after deployment.
