# Hound Benchmark Template

Use this template when creating or repairing a hound benchmark file. Keep entries concise and update it after every accepted, failed, blocked, or rolled-back experiment.

## Goal

- Outcome:
- Target artifact:
- Allowed edit surface:
- Constraints:
- Task shape:
- Non-goals:
- Stop criteria:

## Target Priority

- Primary metric:
- Fallback priority when unspecified:
- Acceptance rule:
- Evidence standard:

## Benchmark

- Command, script, rubric, checklist, or evaluation method:
- How to run it:
- What evidence to save:
- How to compare before and after:

## Metric

| Metric | Command or source | Baseline | Current best | Target | Noise | Guardrail |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |

## Baseline

- Starting score:
- Artifact snapshot or reference:
- Command output summary:
- Screenshots, traces, or artifacts:
- Known risks:

## Rubric Or Checklist

Use this section for qualitative or mixed goals. Delete it only when the metric is purely mechanical.

| Criterion | Weight | Baseline | Current best | Evidence |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## Scope Exclusions

- Generated files:
- Migrations:
- Lockfiles:
- Vendored code:
- Snapshots:
- Other excluded surfaces:

## Invariants

| Area | Invariant | Evidence |
| --- | --- | --- |
| Behavior |  |  |
| Public APIs, schemas, or data formats |  |  |
| UI, accessibility, or interaction states |  |  |
| Factual claims, citations, tone, or policy |  |  |
| Compatibility constraints |  |  |

## Bug Checks

| Check | Command or flow | Required before accept? | Result |
| --- | --- | --- | --- |
| Focused tests |  | yes |  |
| Broad checks |  |  |  |
| Browser/computer-use flows |  |  |  |
| Adversarial probes |  |  |  |
| Console, network, or error-path checks |  |  |  |
| Skipped checks and reasons |  |  |  |

## Candidate Angles

- Largest files or modules:
- Most imported modules:
- Slowest tests, routes, or actions:
- Duplicate shapes or repeated work:
- Missing assumptions or unsupported claims:
- Confusing order, naming, or audience fit:
- Prompt, rubric, or eval failure cases:
- Data, formula, or reconciliation risks:
- Dependency cost:
- Hydration warnings, waterfalls, or profiles:
- TODO/HACK clusters:

## Candidate Queue

| Status | Candidate | Expected gain | Risk | Verification | Rollback |
| --- | --- | --- | --- | --- | --- |
| pending |  |  |  |  |  |

Statuses: `pending`, `accepted`, `failed`, `blocked`, `deferred`.

## Attempts

### Attempt 1

- Hypothesis:
- Files changed:
- Evaluation result:
- Metric delta:
- Bug checks:
- Decision:
- Rollback note:
- Consecutive failure count:

## Current State

- Best known score:
- Accepted changes:
- Failed attempts since last accepted improvement:
- Next candidate:
- Remaining blind spots:
- Continue or stop:
