---
name: make-proposals
description: Generates up to two solution proposals grounded in a research document and a feature or project request. Use when the user asks for solution proposals, approaches, or invokes /make-proposals. Requires a research document produced by /research-codebase.
disable-model-invocation: true
---

Generate up to two solution proposals grounded in an existing research document and a new feature or project request

## Behavior
- Treat the provided research-codebase md as the canonical reference for intake expectations and documentation structure.
- Require a research document produced by `/research-codebase`
- Produce two distinct solution approaches tailored to the provided request, each tied back to the research findings.
- Highlight trade-offs, impacted systems, validation steps, and open questions per proposal.

## Steps
1. Intake
   - Capture the user’s request and optional research document path.
2. Parse research
   - Read the research document fully.
   - Extract constraints, relevant modules, dependencies, data flows, and prior decisions.
3. Synthesize solution space
   - Derive candidate approaches grounded in the research findings.
   - For each approach, note primary changes, affected code paths, required migrations/config updates, and rollout considerations.
   - Keep the list to two or three distinct proposals, ordered from most to least aligned with constraints.
4. Validation planning
   - Identify verification strategies (tests, experiments, observability) necessary to prove each approach.
   - Surface critical unknowns or prerequisite research.
5. Deliver response using the template below.

## Output template
```
## Solution Proposals

Context:
- Request: <short restatement of the ask>
- Research Source: <filename and key sections used>

Proposal 1 — <title>
- Overview: <2-3 sentences>
- Key Changes: <components/modules>
- Trade-offs: <risks vs benefits>
- Validation: <tests/experiments/metrics>
- Open Questions: <gaps or follow-ups>

Proposal 2 — <title>

```

## Notes
- Reference code and sections in backticks using `path/to/file.py:lines` when citing specifics from the research.
- When the research does not directly address the request, call out the gaps and suggest additional research before proposing solutions.
- Stay concise; favor clarity over exhaustive detail while maintaining actionable guidance.
