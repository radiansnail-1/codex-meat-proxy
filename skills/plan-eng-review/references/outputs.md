# Outputs — Templates, Diagram Requirements, Resume Block, Completion Summary

## Documentation and diagrams

* Value ASCII art diagrams highly — for data flow, state machines, dependency graphs, processing pipelines, and decision trees. Use them liberally in plans and design docs.
* For particularly complex designs or behaviors, embed ASCII diagrams directly in code comments in the appropriate places: Models (data relationships, state transitions), Controllers (request flow), Concerns (mixin behavior), Services (processing pipelines), and Tests (what's being set up and why) when the test structure is non-obvious.
* **Diagram maintenance is part of the change.** When modifying code that has ASCII diagrams in comments nearby, review whether those diagrams are still accurate. Update them in the same commit. Stale diagrams are worse than no diagrams — they actively mislead. Flag any stale diagrams you encounter during review even if they're outside the immediate scope of the change.

## Standard Project Resume Block

Before locking an execution plan, check that `plan.md` or the handoff has a small resume block. If absent, recommend adding it so the next agent can resume without rediscovery:

```markdown
## Project Resume

**Project:** <canonical project/product name>
**Path:** <absolute local path>
**Source of truth:** <explicitly designated canonical source, otherwise newest relevant source; include date>
**Status:** <one sentence>
**Next action:** <first concrete action>
**Verification command:** <exact command or "none yet">
**Do-not-do:** <scope traps / unsafe actions / stale assumptions>
**Freshness rule:** Explicit user direction and canonical markers outrank timestamps; otherwise use the newest relevant source and say which one won.
```

Treat this as execution hygiene, not ceremony. The resume block should be short, current, and more useful than a long narrative.

## Required output sections

### "NOT in scope" section
Every plan review MUST produce a "NOT in scope" section listing work that was considered and explicitly deferred, with a one-line rationale for each item.

### "What already exists" section
List existing code/flows that already partially solve sub-problems in this plan, and whether the plan reuses them or unnecessarily rebuilds them.

### TODOS.md updates
After all review sections are complete, present each potential TODO as its own individual question (structured question tool if available, otherwise plain prose). Never batch TODOs — one per question. Never silently skip this step. Use the format below.

For each TODO, describe:
* **What:** One-line description of the work.
* **Why:** The concrete problem it solves or value it unlocks.
* **Pros:** What you gain by doing this work.
* **Cons:** Cost, complexity, or risks of doing it.
* **Context:** Enough detail that someone picking this up in 3 months understands the motivation, the current state, and where to start.
* **Depends on / blocked by:** Any prerequisites or ordering constraints.

Then present options: **A)** Add to TODOS.md **B)** Skip — not valuable enough **C)** Build it now in this PR instead of deferring.

Do NOT just append vague bullet points. A TODO without context is worse than no TODO — it creates false confidence that the idea was captured while actually losing the reasoning.

### Diagrams
The plan itself should use ASCII diagrams for any non-trivial data flow, state machine, or processing pipeline. Additionally, identify which files in the implementation should get inline ASCII diagram comments — particularly Models with complex state transitions, Services with multi-step pipelines, and Concerns with non-obvious mixin behavior.

### Failure modes
For each new codepath identified in the test review diagram, list one realistic way it could fail in production (timeout, nil reference, race condition, stale data, etc.) and whether:
1. A test covers that failure
2. Error handling exists for it
3. The user would see a clear error or a silent failure

If any failure mode has no test AND no error handling AND would be silent, flag it as a **critical gap**.

### Implementation tasks

Translate accepted scope decisions and findings into executable tasks. Do not add work that lacks a source finding or decision.

```markdown
## Implementation Tasks

- [ ] T1 (P0/P1/P2, human: ~X / agent: ~Y) — <component> — <imperative task>
  - Source: <review section and finding or accepted decision>
  - Files: <paths>
  - Verify: <exact test command or manual check>
```

### Completion summary
At the end of the review, fill in and display this summary so the user can see all findings at a glance:
- Step 0: Scope Challenge — ___ (scope accepted as-is / scope reduced per recommendation)
- Architecture Review: ___ issues found
- Code Quality Review: ___ issues found
- Test Review: diagram produced, ___ gaps identified
- Performance Review: ___ issues found
- NOT in scope: written
- What already exists: written
- TODOS.md updates: ___ items proposed to user
- Failure modes: ___ critical gaps flagged
- Outside voice: ran (other model / subagent) / skipped
- Lake Score: X/Y recommendations chose complete option
