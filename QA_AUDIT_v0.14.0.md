# QA Audit v0.14.0 – Process Intelligence

## Scope
First Process Intelligence release: deterministic structural process checking.

## Functional coverage
- Missing Start / missing End.
- Isolated structural nodes.
- Missing incoming flow / dead ends.
- Decision nodes with fewer than two outgoing branches.
- Directed loops / feedback components.
- Long sequential chains.
- High fan-in / fan-out insights.
- Notes/groups excluded from structural-error rules.
- Clickable findings select and center affected nodes.
- Health score and severity counts rendered in analysis panel.

## Safety / data
- Read-only analysis: no changes to process state, Supabase schema, or dependencies.
- No AI inference or external calls.

## Required regression checks
- Python syntax and pytest.
- All Node JS suites and `node --check` on all core modules.
- Fully substituted embedded scripts syntax checked.
- Critical `.p48-body` DOM hierarchy retained.
- ZIP integrity verified.
