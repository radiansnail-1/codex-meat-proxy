# Required Outputs, Optional Persistence, and Chaining

## How to ask questions
Question format (structured question tool if the harness has one, otherwise plain prose — always: plain-English framing, lettered options with Completeness X/10, and a RECOMMENDATION line). Additional rules for plan reviews:
- **One issue = one question.** Never combine multiple issues into one question.
- Describe the problem concretely, with file and line references.
- Present 2-3 options, including "do nothing" where reasonable.
- For each option: effort, risk, and maintenance burden in one line.
- **Map the reasoning to the engineering preferences (in SKILL.md).** One sentence connecting your recommendation to a specific preference.
- Label with issue NUMBER + option LETTER (e.g., "3A", "3B").
- **Escape hatch:** If a section has no issues, say so and move on. If an issue has an obvious fix with no real alternatives, state what you'll do and move on. Only ask when there is a genuine decision with meaningful tradeoffs.

## Formatting Rules
- NUMBER issues (1, 2, 3...) and LETTERS for options (A, B, C...).
- Label with NUMBER + LETTER (e.g., "3A", "3B").
- One sentence max per option.
- After each section, pause and wait for feedback.
- Use **CRITICAL GAP** / **WARNING** / **OK** for scannability.

## Required Outputs

### "NOT in scope" section
List work considered and explicitly deferred, with one-line rationale each.

### "What already exists" section
List existing code/flows that partially solve sub-problems and whether the plan reuses them.

### "Dream state delta" section
Where this plan leaves us relative to the 12-month ideal.

### Error & Rescue Registry (from Section 2)
Complete table of every method that can fail, every exception class, rescued status, rescue action, user impact.

### Failure Modes Registry
```
  CODEPATH | FAILURE MODE   | RESCUED? | TEST? | USER SEES?     | LOGGED?
  ---------|----------------|----------|-------|----------------|--------
```
Any row with RESCUED=N, TEST=N, USER SEES=Silent → **CRITICAL GAP**.

### TODO proposals
Present each potential TODO as its own individual question. Never batch TODOs — one per question. Write to `TODOS.md` only when the user explicitly chooses that option. Use the format below.

For each TODO, describe:
- **What:** One-line description of the work.
- **Why:** The concrete problem it solves or value it unlocks.
- **Pros:** What you gain by doing this work.
- **Cons:** Cost, complexity, or risks of doing it.
- **Context:** Enough detail that someone picking this up in 3 months understands the motivation, the current state, and where to start.
- **Effort estimate:** S/M/L/XL (human team) → with an agent doing the work: S→S, M→S, L→M, XL→L
- **Priority:** P1/P2/P3
- **Depends on / blocked by:** Any prerequisites or ordering constraints.

Then present options: **A)** Add to TODOS.md **B)** Skip — not valuable enough **C)** Build it now in this PR instead of deferring.

### Scope Expansion Decisions (EXPANSION and SELECTIVE EXPANSION only)
For EXPANSION and SELECTIVE EXPANSION modes: expansion opportunities and delight items were surfaced and decided in Step 0D (opt-in/cherry-pick ceremony). If the user explicitly asked to persist a CEO plan document, reference it for the full record. Otherwise, list the accepted/deferred/skipped decisions in the review output:
- Accepted: {list items added to scope}
- Deferred: {list items sent to TODOS.md}
- Skipped: {list items rejected}

### Diagrams (mandatory, produce all that apply)
1. System architecture
2. Data flow (including shadow paths)
3. State machine
4. Error flow
5. Deployment sequence
6. Rollback flowchart

### Stale Diagram Audit
List every ASCII diagram in files this plan touches. Still accurate?

### Completion Summary
```
  +====================================================================+
  |            MEGA PLAN REVIEW — COMPLETION SUMMARY                   |
  +====================================================================+
  | Mode selected        | EXPANSION / SELECTIVE / HOLD / REDUCTION     |
  | System Audit         | [key findings]                              |
  | Step 0               | [mode + key decisions]                      |
  | Section 1  (Arch)    | ___ issues found                            |
  | Section 2  (Errors)  | ___ error paths mapped, ___ GAPS            |
  | Section 3  (Security)| ___ issues found, ___ High severity         |
  | Section 4  (Data/UX) | ___ edge cases mapped, ___ unhandled        |
  | Section 5  (Quality) | ___ issues found                            |
  | Section 6  (Tests)   | Diagram produced, ___ gaps                  |
  | Section 7  (Perf)    | ___ issues found                            |
  | Section 8  (Observ)  | ___ gaps found                              |
  | Section 9  (Deploy)  | ___ risks flagged                           |
  | Section 10 (Future)  | Reversibility: _/5, debt items: ___         |
  | Section 11 (Design)  | ___ issues / SKIPPED (no UI scope)          |
  +--------------------------------------------------------------------+
  | NOT in scope         | written (___ items)                          |
  | What already exists  | written                                     |
  | Dream state delta    | written                                     |
  | Error/rescue registry| ___ methods, ___ CRITICAL GAPS              |
  | Failure modes        | ___ total, ___ CRITICAL GAPS                |
  | TODOS.md updates     | ___ items proposed                          |
  | Scope proposals      | ___ proposed, ___ accepted (EXP + SEL)      |
  | CEO plan             | written / skipped (HOLD/REDUCTION)           |
  | Outside voice        | ran (other model / subagent) / skipped       |
  | Lake Score           | X/Y recommendations chose complete option   |
  | Diagrams produced    | ___ (list types)                            |
  | Stale diagrams found | ___                                         |
  | Unresolved decisions | ___ (listed below)                          |
  +====================================================================+
```

### Unresolved Decisions
If any question goes unanswered, note it here. Never silently default.

## Optional Persist Review to plan.md and changelog.md

Do not write files by default. After producing the Completion Summary, ask
whether the user wants the review persisted. If they decline or do not answer,
stop at the chat output.

If the user explicitly asks to persist the review, write the results into the
canonical project files (per the `handoff` convention):

1. **Update `plan.md`** — add or rewrite a `## CEO Review Notes` section in `plan.md`. Include:
   - Date of review and current commit (`git rev-parse --short HEAD`)
   - Mode selected (SCOPE_EXPANSION / SELECTIVE_EXPANSION / HOLD_SCOPE / SCOPE_REDUCTION)
   - Scope proposals: number proposed, accepted, deferred (for EXPANSION/SELECTIVE; 0 for HOLD/REDUCTION)
   - Critical gaps from Failure Modes
   - Unresolved decisions
   - Outside voice result if it ran

   Note: in EXPANSION/SELECTIVE EXPANSION modes, the `## CEO Plan` section (vision + scope decisions) exists only if the user requested Step 0D-POST persistence. The `## CEO Review Notes` section is a separate, shorter status entry. Both live in `plan.md` when persistence is requested.

   If a `## CEO Review Notes` section already exists, replace it in place. If `plan.md` does not exist, create it only because the user requested persistence.

2. **Append to `changelog.md`** — one line: `{date} — ceo review ({mode}): {N} proposals, {M} accepted, {K} critical gaps`. Create `changelog.md` if it does not exist.

## Next Steps — Review Chaining

After the review output, recommend the next review(s) based on what this CEO review discovered.

**Recommend plan-eng-review** — eng review covers architecture, tests, and code quality. If this CEO review expanded scope, changed architectural direction, or accepted scope expansions, emphasize that a fresh eng review is needed.

**Recommend the `design` skill's review-plan mode if UI scope was detected** — specifically if Section 11 (Design & UX Review) was NOT skipped, or if accepted scope expansions included UI-facing features. In SCOPE REDUCTION mode, skip this recommendation.

**If both are needed, recommend eng review first**, then design review.

Present the next step as one question. Include only applicable options:
- **A)** Run plan-eng-review next
- **B)** Run the `design` skill's review-plan mode next (only if UI scope detected)
- **C)** Skip — I'll handle reviews manually

## docs/designs Promotion (EXPANSION and SELECTIVE EXPANSION only)

At the end of the review, if the vision produced a compelling feature direction and the user explicitly wants persistence, offer to promote the `## CEO Plan` section from `plan.md` to a standalone design doc in the project repo. Ask:

"The vision from this review produced {N} accepted scope expansions. Want to promote it to a design doc in the repo?"
- **A)** Promote to `docs/designs/{FEATURE}.md` (committed to repo, visible to the team)
- **B)** Skip — keep it in `plan.md` only

If promoted, copy the `## CEO Plan` content from `plan.md` to `docs/designs/{FEATURE}.md` (create the directory if needed). Do not create this doc without the user's explicit approval.

## Post-Implementation Design Audit (if UI scope detected)

After implementation, run the `design` skill's audit mode on the live site to catch visual issues that can only be evaluated with rendered output.
