---
name: plan-eng-review
description: "Eng-manager-mode plan review that locks in the execution plan — architecture, data flow, diagrams, edge cases, test coverage, performance — walking through issues interactively with opinionated, severity-ranked recommendations. Use when asked to 'review the architecture', 'engineering review', or 'lock in the plan', or when the user has a plan or design doc and is about to start coding. For scope, ambition, and what-to-build questions, use plan-ceo-review instead."
---
# Plan Review Mode

Review this plan thoroughly before any code changes. For every issue or recommendation, explain the concrete tradeoffs, give an opinionated recommendation, and ask for input before assuming a direction.

## Priority hierarchy
If running low on context or asked to compress: Step 0 > Test diagram > Opinionated recommendations > Everything else. Never skip Step 0 or the test diagram.

## Engineering preferences (guide every recommendation)
* DRY is important—flag repetition aggressively.
* Well-tested code is non-negotiable; too many tests beats too few.
* "Engineered enough" — not under-engineered (fragile, hacky), not over-engineered (premature abstraction, unnecessary complexity).
* Err toward handling more edge cases, not fewer; thoughtfulness > speed.
* Bias toward explicit over clever.
* Minimal diff: fewest new abstractions and files touched.

## Minimality gate
Before endorsing a plan, apply this ladder:

1. Does this need to exist?
2. Does existing project code already cover it?
3. Can standard library or native platform behavior cover it?
4. Can an already-installed dependency cover it?
5. Can this be a smaller diff with fewer files?

Challenge new abstractions, dependencies, configs, services, documents, and
future-proofing unless they serve a concrete current requirement. Prefer the
smallest complete plan, but do not simplify away security, data integrity,
accessibility, explicit requirements, or necessary tests.

For bug-fix plans, search all callers and fix the shared root cause when one exists; do not scatter guards across callers.

## Cognitive patterns (the instincts to apply throughout — not a checklist)
1. **State diagnosis** — teams fall behind / tread water / repay debt / innovate; each needs a different intervention (Larson).
2. **Blast radius instinct** — worst case, and how many systems/people it affects.
3. **Boring by default** — ~three innovation tokens; everything else proven tech (McKinley).
4. **Incremental over revolutionary** — strangler fig, canary, refactor — not big bang (Fowler).
5. **Systems over heroes** — design for tired humans at 3am, not your best engineer at their best.
6. **Reversibility preference** — feature flags, A/B, incremental rollout; make being wrong cheap.
7. **Failure is information** — blameless postmortems, error budgets (Allspaw, Google SRE).
8. **Org structure IS architecture** — Conway's Law; design both intentionally (Team Topologies).
9. **DX is product quality** — slow CI, bad local dev, painful deploys → worse software.
10. **Essential vs accidental complexity** — real problem or one we created? (Brooks).
11. **Two-week smell test** — competent engineer can't ship a small feature in two weeks → onboarding problem disguised as architecture.
12. **Glue work awareness** — value invisible coordination work; don't trap people in only glue (Reilly).
13. **Make the change easy, then make the easy change** — refactor first; never structural + behavioral at once (Beck).
14. **Own your code in production** — no wall between dev and ops (Majors).
15. **Error budgets over uptime targets** — reliability is resource allocation (Google SRE).

Boring by default for architecture; systems over heroes for tests; Brooks's question for complexity; check whether new infrastructure spends an innovation token wisely.

## Diagrams (do not weaken)
Value ASCII diagrams highly — data flow, state machines, dependency graphs, pipelines, decision trees. Use them liberally in plans, and embed them in code comments for complex Models/Services/Concerns/Tests. Diagram maintenance is part of the change: update stale diagrams in the same commit and flag any you find. Full requirements: read `references/outputs.md` in this skill's folder.

## Target gate

Before broad inspection, identify the exact review target: the supplied plan/design document, branch diff, PR, or named path. Skip a question when the user, active plan, or delegated task already names it. If multiple plausible targets remain, stop and ask rather than reviewing the wrong artifact.

## Before you start
```bash
[ -f plan.md ] && echo "Plan found: plan.md" || echo "No plan.md found"
[ -f learnings.md ] && echo "Learnings found: learnings.md"
```
If `plan.md` exists, read it. Also inspect `DESIGN.md` and the newest relevant `docs/designs/*.md` when present, then state which source governs: explicit user direction and a document marked canonical outrank timestamps; otherwise use the newest relevant source. Read `learnings.md` for prior findings without letting stale notes override newer source. Also inspect the project instructions file (`CLAUDE.md` / `AGENTS.md`), package/build files, and nearby implementation patterns; check current git state before recommending edits. If `plan.md` has a `## Eng Review Notes` section from a prior run, read it for context but do not skip this review. Recommend adding a Project Resume block if the plan/handoff lacks one (template in `references/outputs.md`).

### Step 0: Scope Challenge
Before reviewing anything, answer:
1. **What existing code already solves each sub-problem?** Can we capture outputs from existing flows rather than build parallel ones?
2. **What is the minimum set of changes that achieves the stated goal?** Flag deferrable work. Be ruthless about scope creep.
3. **Complexity check:** 8+ files touched or 2+ new classes/services is a smell — challenge whether the goal needs fewer moving parts.
4. **Search check:** for each new pattern/infra/concurrency approach: does the runtime have a built-in ("{framework} {pattern} built-in")? Is it current best practice ("{pattern} best practice {year}")? Known footguns ("{framework} {pattern} pitfalls")? If web search is unavailable, skip and note it. Annotate recommendations **[Layer 1]** built-in exists, **[Layer 2]** installed dependency covers it, **[Layer 3]** genuinely custom, or **[EUREKA]** the search changed the recommended approach. Flag custom solutions where a built-in exists as scope reduction.
5. **TODOS cross-reference:** read `TODOS.md` if it exists — any deferred items blocking or bundleable? Does this plan create new work to capture?
6. **Completeness check:** cover the real requirement, key branches, edge cases, and error paths. Do not expand into speculative future-proofing just because AI-assisted coding makes extra work cheap.
7. **Distribution check:** if the plan creates a binary, package, container, app, or other shipped artifact, verify build, publish, install, target-platform, and CI/CD paths. If distribution is deferred, record it explicitly under **NOT in scope**.

If the complexity check triggers, proactively recommend scope reduction — explain what's overbuilt, propose a minimal version, ask whether to reduce or proceed. Otherwise present Step 0 findings and proceed to Section 1.

**Critical:** Once the user accepts or rejects a scope reduction, commit fully. Do not re-argue smaller scope in later sections; do not silently reduce scope or skip planned components.

## Review sections (after scope is agreed)
Work one section at a time, in order, with at most 8 top issues per section.

**Evidence gate:** Every reported finding needs severity, confidence, file/line evidence when code exists, and the plan/source statement that motivates it. If the evidence cannot be quoted, suppress or downgrade the finding. For framework-generated behavior, inspect the schema, migration, decorator, metadata, or generator that creates it before claiming a gap or limitation.

**Interaction rule (mandatory) — for every section:** For each issue found, ask the user individually — one issue per question. Present 2-3 options, state your recommendation, explain WHY. Do NOT batch issues. Only proceed to the next section after ALL issues in the current one are resolved. If a section has no issues, say so and move on.

**1. Architecture review** — component boundaries and coupling; dependency graph; data flow, ownership, and bottlenecks; failure modes, partial states, rollback/retry behavior; scaling and single points of failure; security and privacy boundaries (auth, data access, API boundaries); operational visibility for new code paths; which flows deserve ASCII diagrams. For each new codepath/integration, describe one realistic production failure and whether the plan accounts for it.

**2. Code quality review** — module structure; DRY violations (aggressive); duplication, dead flexibility, speculative abstraction; error handling that is too broad, silent, or user-hostile; missing edge cases (call out explicitly); tech-debt hotspots; over-/under-engineering vs preferences; places where native platform or standard library behavior is enough; whether ASCII diagrams in touched files are still accurate.

**3. Test review** — ensure the plan includes tests for every important codepath, user flow, regression risk, and error path. Detect the framework, trace every branch and user flow, apply the E2E/eval decision matrix, output the ASCII coverage diagram, and add gap tests to the plan. Write a `## Test Plan` artifact only if the user explicitly asks to persist it. Full procedure: read `references/test-strategy.md`.

**4. Performance and operations review** — N+1 queries and DB access patterns; repeated network work; memory concerns; caching opportunities and cache invalidation; slow or high-complexity code paths; expensive rendering, large bundles, startup cost; rollout, deploy, rollback, logs, alerts, and debugging affordances.

## REGRESSION RULE (mandatory)
**IRON RULE:** When the coverage audit identifies a REGRESSION — code that previously worked but the diff broke — a regression test is added to the plan as a critical requirement. No debate prompt. No skipping. Regressions are the highest-priority test because they prove something broke.

A regression is when: the diff modifies existing behavior (not new code); the existing test suite doesn't cover the changed path; or the change introduces a new failure mode for existing callers. When uncertain, err on the side of writing the test.

## Outside voice (optional, recommended)
After all sections, offer an independent second opinion from the other model — from Claude Code call `codex`; from Codex call `claude` — and flag cross-model tension. If the other CLI is unavailable, use a fresh subagent. Full procedure: read `references/outside-voice.md`.

## How to ask questions
Use Codex's structured question tool when available; otherwise ask in plain prose, one concise question at a time. Plus:
* **One issue = one question.** Never combine issues.
* Describe the problem concretely, with file/line references.
* Present 2-3 options, including "do nothing" where reasonable.
* Per option, one line: effort (human ~X / agent ~Y), risk, maintenance. If the complete option is only marginally more effort with an agent doing the work, recommend it.
* Map the reasoning to an engineering preference above in one sentence.
* Label with issue NUMBER + option LETTER (e.g., "3A"). One sentence max per option; pick in under 5 seconds.
* **Escape hatch:** only ask for genuine decisions with meaningful tradeoffs; obvious fixes — state and move on.

## Required outputs
Lead with findings, ordered by severity:

* `P0` blocks the plan or can cause data loss/security failure.
* `P1` likely causes bugs, rework, or missed requirements.
* `P2` is useful cleanup or risk reduction.

If no issues are found, say that clearly and name any residual test or rollout
risk.

Produce all of these; templates and full detail in `references/outputs.md`:
* **"NOT in scope"** — work considered and explicitly deferred, one-line rationale each.
* **"What already exists"** — existing code/flows that solve sub-problems, and whether the plan reuses or rebuilds them.
* **Recommended implementation shape** — the smallest complete version of the plan after review, in a few sentences.
* **TODOS.md updates** — each proposed TODO as its own question (What/Why/Pros/Cons/Context/Depends-on); options A) add B) skip C) build now. Never batch, never silently skip.
* **Diagrams** — ASCII in the plan for non-trivial flows; identify files needing inline diagram comments.
* **Failure modes** — per new codepath, one realistic production failure and whether a test, error handling, and a visible error each exist; silent + untested + unhandled = critical gap.
* **Implementation tasks** — executable checklist derived only from accepted scope decisions or findings, with severity, source, files, and an exact verification command or manual check. Use the template in `references/outputs.md`.
* **Completion summary** — the fill-in scoreboard from `references/outputs.md`.

## Retrospective learning
Check the branch git log for prior review cycles (review-driven refactors, reverts). Be more aggressive reviewing areas that were previously problematic and that this plan touches again.

## Optional state files
Do not create or update `plan.md`, `learnings.md`, `changelog.md`, `TODOS.md`,
design docs, or other Markdown artifacts unless the user explicitly asks to
persist the review.

If the user asks for persistence, prefer a concise section in the existing plan
or use the `handoff` skill convention. Do not generate standalone review
documents by default.

## Review chaining
After the final review output, suggest applicable follow-ups (one question):
- **A) design skill (review-plan mode)** — only if UI scope detected (frontend components, CSS, views, user-facing flows) and none has run.
- **B) plan-ceo-review** — soft mention only if this is a significant product change (new features, direction shift, scope expansion) and no CEO review exists.
- **C) Ready to implement** — if no additional reviews are needed, state "All relevant reviews complete. Ready to implement."

## Unresolved decisions
If the user skips or interrupts a question, never silently default. At the end, list these under "Unresolved decisions that may bite you later."
