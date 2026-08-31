# QA Audit v0.16.3

## Scope
- Desktop drag-to-pan navigation on blank canvas.
- Slider-based whole-process scaling.
- Make visible node rectangles truly follow process scaling.

## Verified behavior
- Blank-canvas mouse drag pans horizontal and vertical scroll.
- Nodes and other interactive controls do not initiate desktop pan.
- Process scale is a 50–150% slider with live percentage.
- Slider remains open while scaling.
- Chromium verified 100% → 70% visibly reduces both node width and height.
- Chromium verified 70% → 120% visibly increases node dimensions again.
- CSS min/max constraints are overridden for scaled nodes.
- Stored scaled dimensions reopen using border-box sizing and the same min/max overrides.
- Fit-to-page remains available.

## Verified release gates
- `py_compile`: passed.
- `pytest`: 201/201 passed.
- JavaScript suites: 25/25 passed.
- Focused Chromium pan + scale-slider smoke: passed.
- Core JavaScript syntax: passed.
- Embedded editor JavaScript syntax: passed.
- Critical DOM hierarchy: passed.
- Duplicate HTML IDs: none detected.
- ZIP integrity: passed.

## Deployment
Not pushed or deployed.
