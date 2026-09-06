---
name: hound
description: Unified evidence-driven improvement loop. Use when the user asks to hound, autoresearch, relentlessly optimize, or iteratively improve code, apps, prompts, docs, plans, research, UI, or another artifact against a measurable benchmark, rubric, test suite, or named reference.
license: private
metadata:
  tags: [hound, gauntlet, iterative-improvement, benchmark, independent-review, optimization, evaluation]
  related_skills: [agentic-engineering-system, spawn, code-audit]
---

# Hound

Hound is the canonical improvement-loop skill. It has two modes:

- **Metric mode:** optimize against a trustworthy benchmark, metric, rubric, or test suite.
- **Reference mode:** improve toward a named reference, exemplar, competitor, or production bar using fresh independent critics.

Both modes use the same contract:

> **goal + inspectable bar -> bounded decomposition -> builder -> real evidence -> measure/critic -> largest gap -> small repair -> repeat**

Do not ask a model to “try harder” without an inspectable bar. A benchmark gain or enthusiastic critique never outranks correctness, accessibility, factual accuracy, privacy, security, compatibility, or user behavior.

## When to use

Use for requests to:

- hound, autoresearch, optimize, reduce lag/latency/startup/render time, reduce LOC/bundle/query/memory cost, or keep improving until progress stalls;
- make a product, UI, game, design, article, plan, research output, prompt, or codebase as good as a reference;
- split work, build parts, compare them independently, and iterate;
- run a bounded autonomous quality-improvement workflow in Codex, Claude Code, or Hermes.

Do not treat this as permission for unbounded background work, production writes, paid actions, destructive rewrites, copying protected references, or changing auth. Stop or escalate at those boundaries.

## Startup contract

Before editing, establish:

1. **Goal:** outcome in user terms, not an unnecessary implementation recipe.
2. **Bar:** primary metric, repeatable benchmark, rubric, test suite, or reference with provenance.
3. **Artifact:** exact files/surface and command, route, URL, evaluator, or device used to inspect it.
4. **Scope:** allowed edits, exclusions, constraints, invariants, and guardrails.
5. **Stop rule:** target reached, no meaningful improvement, budget/time limit, repeated failures, user acceptance, or blocker.

Then:

1. Inspect current files, repository state, docs, routes, tests, benchmarks, and existing evidence.
2. Run the narrowest real path before changing anything. Capture baseline screenshots, timings, tests, samples, draft, score, or other durable evidence.
3. Read the benchmark file named by the user; otherwise create `hound-benchmark.md` in the target project root (or the dedicated work area when appropriate), using `references/benchmark-template.md`.
4. Confirm the inspection path works and record noise/variance, known limitations, candidate queue, current round, and next action.
5. Decompose only where slices are independently judgeable. Shared rendering, state, schemas, timing, APIs, or design language usually require sequential ownership.

A fresh agent should be able to reproduce the baseline and know exactly what evidence decides the next pass.

## Benchmark mode

Use one primary metric whenever possible; use guardrails rather than averaging unrelated goals. The benchmark should record:

- Goal, allowed edits, target metric, and stop criteria.
- Target priority and acceptance rule.
- Exact command, script, rubric, checklist, or scorecard.
- Metric direction, threshold, guardrails, and known noise.
- Baseline evidence and current best score.
- Invariants: behavior, APIs, visual states, factual claims, data formats, policy, tone, compatibility, and accessibility.
- Bug checks: tests, browser/computer-use flows, edge cases, console/network checks, and regression probes.
- Candidate queue with `pending`, `accepted`, `failed`, `blocked`, or `deferred` status.
- One concise attempt entry per experiment: hypothesis, files, result, delta, decision, rollback note, and consecutive failure count.
- Current state: accepted changes, next candidate, blind spots, and why to continue or stop.

Prefer small, reversible experiments. For vague code optimization, start with safe simplification, then user-visible latency. Prove removals with search, types, tests, route coverage, runtime evidence, and checks for dynamic/config-driven usage; never delete code merely because it looks unused.

## Reference mode

Select a concrete reference artifact, implementation, golden output, reproducible suite, measurable target, or weighted rubric. The reference is a judgment bar, not permission to imitate protected code, art, text, branding, or private data.

Create or update a small `hound-run.md`, `workbench.md`, or project worksheet containing goal, bar/provenance, baseline evidence, invariants, exclusions, workstreams, round, owner, stop rule, and next action.

The lead agent should choose the smallest judgeable slices. Use parallel builders only when ownership is disjoint, each slice has a local bar and inspection path, changes cannot invalidate one another, and integration preserves evidence. Otherwise use one sequential owner.

Builder packet:

- goal and owned slice;
- bar, guardrails, and exclusions;
- exact files/surface and real inspection command/path;
- invariants and constraints;
- response contract: changed files, checks, evidence paths, blockers, and uncertainty.

Critic packet:

- give a fresh-context critic only the goal, bar, guardrails, inspection instructions, and real artifact;
- withhold builder history, rationale, confidence, and self-assessment until judgment is formed;
- compare directly with the bar and use blind A/B when practical;
- identify the single largest meaningful gap first;
- distinguish observation from inference and uncertainty;
- return one minimal repair direction and a regression concern.

Critic response shape:

```text
verdict: PASS | GAP | BLOCKED
bar: <one sentence>
blind_choice: OURS | REFERENCE | TIE | NOT_POSSIBLE
largest_gap: <one concrete observation>
evidence: <paths, commands, screenshots, tests, or citations>
repair: <smallest high-leverage next change>
regression_risk: <what could break>
confidence: high | medium | low
```

Critic surface by artifact: running pixels and real viewports for UI; tests/traces/failure behavior/security checks for code; full draft/source/citation/calculation checks for writing/research; actual workbook/schema/formulas/rows for data; representative cases and grader variance for prompts/evals.

## Loop

1. **Baseline.** Run the benchmark or real inspection path exactly as written. Record skipped checks and why.
2. **Generate candidates.** Rank small hypotheses by expected gain, confidence, blast radius, verification cost, and rollback path. Do not repeat a failed idea without new evidence.
3. **One experiment.** Implement one coherent, attributable change inside the assigned scope.
4. **Verify.** Re-run the metric and all relevant bug checks. For reference mode, run the same inspection and critic path.
5. **Decide.** Keep only a verified improvement that preserves all guardrails. Revert only the failed experiment's changes when safe; never revert unrelated user work.
6. **Record.** Update the benchmark/worksheet with evidence, delta, accepted or rejected decision, risks, and next candidate.
7. **Repeat.** Continue while a plausible candidate, trustworthy inspection path, and budget remain.

For browser-facing work, run the app and inspect real pixels at representative desktop/mobile viewports. Exercise key flows, loading/error/empty states, focus/keyboard behavior, console and network output, assets, responsive behavior, and reduced motion when relevant. For noisy performance, use repeated measurements and report distributions rather than a flattering single run.

Optional creativity passes after obvious wins run out: subtraction, latency archaeology, dependency diet, cache/precompute, boundary tightening, and mining discovered invariants into tests.

## Acceptance and stop rules

Accept only when the primary metric improves or target is reached, the real artifact was inspected, guardrails/invariants hold, changes are attributable, and the evidence is recorded. A reference-mode pass requires `PASS` or a documented residual gap explicitly accepted by the lead.

Stop when:

- target/bar is met or the remaining gap is immaterial;
- five consecutive metric attempts fail to produce a verified improvement;
- the benchmark/evaluator is broken or untrustworthy after reasonable repair;
- improvements flatten relative to cost;
- the next action requires product judgment, credentials, paid resources, production-only data, destructive changes, or broader scope;
- a regression or safety boundary cannot be fixed without widening scope;
- Brian asks to stop.

Never claim completion while required critics, tests, or live verification are pending. Partial or blocked results are preferable to invented confidence.

## Harness adapters

- **Hermes:** the lead owns routing, scope, integration, and final verification. Use bounded delegation for builders, critics, research, and verification; inspect child evidence rather than trusting summaries. Keep auth, money, production writes, and irreversible choices in the parent session.
- **Claude Code:** use native fresh-context subagents for critics and explicit ownership for builders. `/loop` is only a harness convenience; this contract and worksheet remain authoritative.
- **Codex:** use native Codex subagents/tooling for bounded lanes. If unavailable, use a separate self-contained `codex exec` lane and inspect its output. Use Codex-native model/effort settings only; do not pass Claude aliases across runtimes.

## Safety and rollback

- Every run needs a budget, stop rule, and resumable worksheet; never run an infinite loop.
- Do not overlap edits or overwrite unrelated user changes.
- Do not execute production writes, send messages, spend money, alter subscriptions, delete data, or change auth without required approval.
- Do not expose secrets to workers or place credentials in worksheets.
- Use version control or a recoverable baseline before rewriting non-code artifacts.
- If a failed experiment overlaps user edits, undo only the experiment's diff or stop for help.

## Final report

Report the benchmark/worksheet path, baseline versus final metric or verdict, accepted improvements and safety rationale, failed attempts since the last accepted improvement, verification and skipped checks, deferred ideas, confidence, and residual risk.
