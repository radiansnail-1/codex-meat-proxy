# Pre-Review System Audit and Full Step 0

Substitute the detected base branch (from SKILL.md Step 0) wherever a command references `<base>` or "the base branch."

## PRE-REVIEW SYSTEM AUDIT (before Step 0)

Before doing anything else, run a system audit. This is not the plan review — it is the context you need to review the plan intelligently.

Run the following commands:
```
git log --oneline -30                          # Recent history
git diff <base> --stat                           # What's already changed
git stash list                                 # Any stashed work
grep -r "TODO\|FIXME\|HACK\|XXX" -l --exclude-dir=node_modules --exclude-dir=vendor --exclude-dir=.git . | head -30
git log --since=30.days --name-only --format="" | sort | uniq -c | sort -rn | head -20  # Recently touched files
```
Then read the project instructions file (`CLAUDE.md` / `AGENTS.md`), TODOS.md, and any existing architecture docs.

**Plan doc check:**
```bash
[ -f plan.md ] && echo "Plan found: plan.md" || echo "No plan.md found"
[ -f learnings.md ] && echo "Learnings found: learnings.md"
[ -f changelog.md ] && echo "Changelog found: changelog.md"
```
If `plan.md` exists, read it. Also inspect `DESIGN.md` and the newest relevant `docs/designs/*.md` when present. State which document is authoritative: explicit user direction and a document marked canonical outrank timestamps; otherwise use the newest relevant source and name the evidence. Read `learnings.md` for decisions and gotchas, but never let stale notes override newer source or the user's latest written correction.

### Standard Project Resume Block

When reviewing a project plan, require the plan or handoff to expose a small resume block before implementation starts. If it is missing, flag it as a documentation gap and recommend adding it to `plan.md` or the nearest handoff file:

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

Use this block to prevent stale wiki/project drift. Do not create or update it unless the user explicitly requests persistence; when requested, keep it concise and current.

**Prior review check:** If `plan.md` already contains a `## CEO Review Notes` section from a prior run, read it. This contains system audit findings and discussion from a prior CEO review session — use it as additional context to avoid re-asking questions the user already answered. Do NOT skip any steps — run the full review, but let the prior notes inform your analysis.

If you find prior notes, tell the user: "Found prior CEO review notes in plan.md. I'll use that context to pick up where we left off."

When reading TODOS.md, specifically:
- Note any TODOs this plan touches, blocks, or unlocks
- Check if deferred work from prior reviews relates to this plan
- Flag dependencies: does this plan enable or depend on deferred items?
- Map known pain points (from TODOS) to this plan's scope

Map:
- What is the current system state?
- What is already in flight (other open PRs, branches, stashed changes)?
- What are the existing known pain points most relevant to this plan?
- Are there any FIXME/TODO comments in files this plan touches?

### Retrospective Check
Check the git log for this branch. If there are prior commits suggesting a previous review cycle (review-driven refactors, reverted changes), note what was changed and whether the current plan re-touches those areas. Be MORE aggressive reviewing areas that were previously problematic. Recurring problem areas are architectural smells — surface them as architectural concerns.

### Frontend/UI Scope Detection
Analyze the plan. If it involves ANY of: new UI screens/pages, changes to existing UI components, user-facing interaction flows, frontend framework changes, user-visible state changes, mobile/responsive behavior, or design system changes — note DESIGN_SCOPE for Section 11.

### Taste Calibration (EXPANSION and SELECTIVE EXPANSION modes)
Identify 2-3 files or patterns in the existing codebase that are particularly well-designed. Note them as style references for the review. Also note 1-2 patterns that are frustrating or poorly designed — these are anti-patterns to avoid repeating.
Report findings before proceeding to Step 0.

### Landscape Check

If `ETHOS.md` exists, read its Search Before Building guidance. Otherwise apply the same principle directly. Before challenging scope, use the available web-search tool for:
- "[product category] landscape {current year}"
- "[key feature] alternatives"
- "why [incumbent/conventional approach] [succeeds/fails]"

If web search is unavailable, skip this check and note: "Search unavailable — proceeding with in-distribution knowledge only."

Run the three-layer synthesis:
- **[Layer 1]** What's the tried-and-true approach in this space?
- **[Layer 2]** What are the search results saying?
- **[Layer 3]** First-principles reasoning — where might the conventional wisdom be wrong?

Feed into the Premise Challenge (0A) and Dream State Mapping (0C). If you find a eureka moment, surface it during the Expansion opt-in ceremony as a differentiation opportunity.

## Step 0: Nuclear Scope Challenge + Mode Selection

### 0A. Premise Challenge
1. Is this the right problem to solve? Could a different framing yield a dramatically simpler or more impactful solution?
2. What is the actual user/business outcome? Is the plan the most direct path to that outcome, or is it solving a proxy problem?
3. What would happen if we did nothing? Real pain point or hypothetical one?

### 0B. Existing Code Leverage
1. What existing code already partially or fully solves each sub-problem? Map every sub-problem to existing code. Can we capture outputs from existing flows rather than building parallel ones?
2. Is this plan rebuilding anything that already exists? If yes, explain why rebuilding is better than refactoring.

### 0C. Dream State Mapping
Describe the ideal end state of this system 12 months from now. Does this plan move toward that state or away from it?
```
  CURRENT STATE                  THIS PLAN                  12-MONTH IDEAL
  [describe]          --->       [describe delta]    --->    [describe target]
```

### 0C-bis. Implementation Alternatives (MANDATORY)

Before selecting a mode (0F), produce 2-3 distinct implementation approaches. This is NOT optional — every plan must consider alternatives.

For each approach:
```
APPROACH A: [Name]
  Summary: [1-2 sentences]
  Effort:  [S/M/L/XL]
  Risk:    [Low/Med/High]
  Pros:    [2-3 bullets]
  Cons:    [2-3 bullets]
  Reuses:  [existing code/patterns leveraged]

APPROACH B: [Name]
  ...

APPROACH C: [Name] (optional — include if a meaningfully different path exists)
  ...
```

**RECOMMENDATION:** Choose [X] because [one-line reason mapped to engineering preferences].

Rules:
- At least 2 approaches required. 3 preferred for non-trivial plans.
- One approach must be the "minimal viable" (fewest files, smallest diff).
- One approach must be the "ideal architecture" (best long-term trajectory).
- Give the minimal and ideal approaches equal consideration; choose from user outcome and trajectory, not simply the smallest diff.
- If only one approach exists, explain concretely why alternatives were eliminated.
- Do NOT proceed to mode selection (0F) without user approval of the chosen approach.

### 0D. Mode-Specific Analysis
**For SCOPE EXPANSION** — run all three, then the opt-in ceremony:
1. 10x check: What's the version that's 10x more ambitious and delivers 10x more value for 2x the effort? Describe it concretely.
2. Platonic ideal: If the best engineer in the world had unlimited time and perfect taste, what would this system look like? What would the user feel when using it? Start from experience, not architecture.
3. Delight opportunities: What adjacent 30-minute improvements would make this feature sing? Things where a user would think "oh nice, they thought of that." List at least 5.
4. **Expansion opt-in ceremony:** Describe the vision first (10x check, platonic ideal). Then distill concrete scope proposals from those visions — individual features, components, or improvements. Present each proposal as its own structured question when the harness supports one, otherwise in plain prose. Recommend enthusiastically — explain why it's worth doing. But the user decides. Options: **A)** Add to this plan's scope **B)** Defer for later (write to TODOS.md only if the user explicitly asks) **C)** Skip. Accepted items become plan scope for all remaining review sections. Rejected items go to "NOT in scope."

**For SELECTIVE EXPANSION** — run the HOLD SCOPE analysis first, then surface expansions:
1. Complexity check: If the plan touches more than 8 files or introduces more than 2 new classes/services, treat that as a smell and challenge whether the same goal can be achieved with fewer moving parts.
2. What is the minimum set of changes that achieves the stated goal? Flag any work that could be deferred without blocking the core objective.
3. Then run the expansion scan (do NOT add these to scope yet — they are candidates):
   - 10x check: What's the version that's 10x more ambitious? Describe it concretely.
   - Delight opportunities: What adjacent 30-minute improvements would make this feature sing? List at least 5.
   - Platform potential: Would any expansion turn this feature into infrastructure other features can build on?
4. **Cherry-pick ceremony:** Present each expansion opportunity as its own structured question when available, otherwise in plain prose. Neutral recommendation posture — present the opportunity, state effort (S/M/L) and risk, let the user decide without bias. Options: **A)** Add to this plan's scope **B)** Defer for later (write to TODOS.md only if the user explicitly asks) **C)** Skip. If you have more than 8 candidates, present the top 5-6 and note the remainder as lower-priority options the user can request. Accepted items become plan scope for all remaining review sections. Rejected items go to "NOT in scope."

**For HOLD SCOPE** — run this:
1. Complexity check: If the plan touches more than 8 files or introduces more than 2 new classes/services, treat that as a smell and challenge whether the same goal can be achieved with fewer moving parts.
2. What is the minimum set of changes that achieves the stated goal? Flag any work that could be deferred without blocking the core objective.

**For SCOPE REDUCTION** — run this:
1. Ruthless cut: What is the absolute minimum that ships value to a user? Everything else is deferred. No exceptions.
2. What can be a follow-up PR? Separate "must ship together" from "nice to ship together."

### 0D-POST. Optional CEO Plan Persistence (EXPANSION and SELECTIVE EXPANSION only)

Do not write files by default. After the opt-in/cherry-pick ceremony, ask
whether the user wants the vision and decisions persisted. If they decline or do
not answer, keep the decisions in the review output only.

If the user explicitly asks to persist, add or rewrite a `## CEO Plan` section
in `plan.md` (in the project root) using this format:

```markdown
## CEO Plan
Generated by plan-ceo-review on {date}
Mode: {EXPANSION / SELECTIVE EXPANSION}

### Vision

#### 10x Check
{10x vision description}

#### Platonic Ideal
{platonic ideal description — EXPANSION mode only}

### Scope Decisions

| # | Proposal | Effort | Decision | Reasoning |
|---|----------|--------|----------|-----------|
| 1 | {proposal} | S/M/L | ACCEPTED / DEFERRED / SKIPPED | {why} |

### Accepted Scope (added to this plan)
- {bullet list of what's now in scope}

### Deferred to TODOS.md
- {items with context}
```

If `plan.md` does not exist, create it only after the user has explicitly asked
for persistence. If a `## CEO Plan` section already exists, replace it in place.

After writing, run the spec review loop on the updated `plan.md`.

#### Spec Review Loop

Before presenting the document to the user for approval, run an adversarial review.

**Step 1: Dispatch reviewer subagent**

Use the Agent tool to dispatch an independent reviewer. The reviewer has fresh context and cannot see the brainstorming conversation — only the document. This ensures genuine adversarial independence.

Prompt the subagent with:
- The file path of the document just written
- "Read this document and review it on 5 dimensions. For each dimension, note PASS or list specific issues with suggested fixes. At the end, output a quality score (1-10) across all dimensions."

**Dimensions:**
1. **Completeness** — Are all requirements addressed? Missing edge cases?
2. **Consistency** — Do parts of the document agree with each other? Contradictions?
3. **Clarity** — Could an engineer implement this without asking questions? Ambiguous language?
4. **Scope** — Does the document creep beyond the original problem? YAGNI violations?
5. **Feasibility** — Can this actually be built with the stated approach? Hidden complexity?

The subagent should return a quality score (1-10) and PASS if no issues, or a numbered list of issues with dimension, description, and fix.

**Step 2: Fix and re-dispatch**

If the reviewer returns issues:
1. Fix each issue in the document on disk (use Edit tool)
2. Re-dispatch the reviewer subagent with the updated document
3. Maximum 3 iterations total

**Convergence guard:** If the reviewer returns the same issues on consecutive iterations (the fix didn't resolve them or the reviewer disagrees with the fix), stop the loop and persist those issues as "Reviewer Concerns" in the document rather than looping further.

If the subagent fails, times out, or is unavailable — skip the review loop entirely. Tell the user: "Spec review unavailable — presenting unreviewed doc." If no document was written because persistence was not requested, skip this loop.

**Step 3: Report and persist metrics**

After the loop completes (PASS, max iterations, or convergence guard):

1. Tell the user the result — summary by default: "Your doc survived N rounds of adversarial review. M issues caught and fixed. Quality score: X/10." If they ask "what did the reviewer find?", show the full reviewer output.
2. If issues remain after max iterations or convergence and a document exists, add a "## Reviewer Concerns" section to the document listing each unresolved issue. If no document exists, list the concerns in the review output.

### 0E. Temporal Interrogation (EXPANSION, SELECTIVE EXPANSION, and HOLD modes)
Think ahead to implementation: What decisions will need to be made during implementation that should be resolved NOW in the plan?
```
  HOUR 1 (foundations):     What does the implementer need to know?
  HOUR 2-3 (core logic):   What ambiguities will they hit?
  HOUR 4-5 (integration):  What will surprise them?
  HOUR 6+ (polish/tests):  What will they wish they'd planned for?
```
NOTE: These represent human-team implementation hours. With Claude Code, 6 hours of human implementation compresses to ~30-60 minutes. The decisions are identical — the implementation speed is 10-20x faster. Always present both scales when discussing effort.

Surface these as questions for the user NOW, not as "figure it out later."

### 0F. Mode Selection
In every mode, you are 100% in control. No scope is added without your explicit approval.

Present four options:
1. **SCOPE EXPANSION:** The plan is good but could be great. Dream big — propose the ambitious version. Every expansion is presented individually for your approval. You opt in to each one.
2. **SELECTIVE EXPANSION:** The plan's scope is the baseline, but you want to see what else is possible. Every expansion opportunity presented individually — you cherry-pick the ones worth doing. Neutral recommendations.
3. **HOLD SCOPE:** The plan's scope is right. Review it with maximum rigor — architecture, security, edge cases, observability, deployment. Make it bulletproof. No expansions surfaced.
4. **SCOPE REDUCTION:** The plan is overbuilt or wrong-headed. Propose a minimal version that achieves the core goal, then review that.

Context-dependent defaults:
- Greenfield feature → default EXPANSION
- Feature enhancement or iteration on existing system → default SELECTIVE EXPANSION
- Bug fix or hotfix → default HOLD SCOPE
- Refactor → default HOLD SCOPE
- Plan touching >15 files → suggest REDUCTION unless user pushes back
- User says "go big" / "ambitious" / "cathedral" → EXPANSION, no question
- User says "hold scope but tempt me" / "show me options" / "cherry-pick" → SELECTIVE EXPANSION, no question

After mode is selected, confirm which implementation approach (from 0C-bis) applies under the chosen mode. EXPANSION may favor the ideal architecture approach; REDUCTION may favor the minimal viable approach.

Once selected, commit fully. Do not silently drift.
**STOP.** Ask one question per issue using the harness's structured question tool when available. Do NOT batch. Recommend + WHY. If no issues or the fix is obvious, state it and move on — don't waste a question. Do NOT proceed until the user responds.
