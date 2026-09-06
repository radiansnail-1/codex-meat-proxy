---
name: investigate
description: |
  Systematic debugging with root-cause investigation. Use when the
  user asks to debug, fix a bug, explain why something is broken, investigate
  an error, or perform root-cause analysis. Proactively invoke when the user
  reports errors, stack traces, regressions, unexpected behavior, or something
  that "was working yesterday."
---

# Investigate

## Setup

```bash
BRANCH=$(git branch --show-current 2>/dev/null || echo "unknown")
echo "BRANCH: $BRANCH"
```

## Protocols

Follow the compact rules below whenever you ask the user something or report status. Full detail (calibration, escalation format, completion states) lives in `references/protocols.md`.

**Asking the user** — use Codex's structured question tool when available; otherwise ask in plain prose, one concise question at a time. Every ask: (1) re-ground in the project path + `BRANCH` + task; (2) explain the problem in plain English a smart 16-year-old could follow (no jargon, no raw function names); (3) give lettered options `A) B) C)` with `Completeness: X/10` each and a `RECOMMENDATION: Choose [X] because [reason]`, always preferring the complete option.

**Completion status** — end work with one of: `DONE` (all steps done, evidence given), `DONE_WITH_CONCERNS` (done but list the issues), `BLOCKED` (state blocker + what was tried), `NEEDS_CONTEXT` (state exactly what is missing).

**Escalation** — it is always OK to stop. Bad work is worse than no work; you are not penalized for escalating. STOP and escalate after 3 failed attempts, on any security-sensitive uncertainty, or when scope exceeds what you can verify.

## Iron Law

**No fixes without root-cause evidence first.**

Do not guess, patch symptoms, or say "this should fix it." Fixing symptoms creates whack-a-mole debugging: every fix that doesn't address the root cause makes the next bug harder to find. Trace the failing path, prove the cause, implement the smallest fix, and verify the original failure no longer reproduces.

Scope boundary: use `code-audit` when the requested deliverable is a read-only correctness review. After root cause is proven, use `reliability-hardening` when the work expands into durable concurrency, idempotency, persistence, adapter, or adversarial-input controls.

## Phase 1: Root-Cause Investigation

Gather context before forming any hypothesis.

0. **Lock source identity:** Confirm the current path, Git remote, branch/worktree, and intended runtime/build. A stale clone, portable drive, archive, generated tree, simulator install, and physical-device build may all contain different code. Do not fix or verify the wrong checkout.
1. **Collect symptoms:** Read the exact error messages, stack traces, logs, screenshots, and reproduction steps. If the user hasn't given enough context and it can't be inferred, ask one concise question (see Protocols).
2. **Build a tight loop:** Before reading broadly, create or identify the smallest command that is red on the user's exact symptom and can turn green after a fix. Prefer a focused test, HTTP probe, CLI fixture, headless browser assertion, device log/repro script, captured-event replay, or differential old-vs-new check. Run it once before changing code.
3. **Read the code:** Trace the code path from the symptom back to potential causes. Use fast search to find all references and read the relevant logic.
4. **Check recent changes:** `git log --oneline -20 -- <affected-files>` and `git diff`. Was this working before? A regression means the root cause is in the diff.
5. **Reproduce:** Can you trigger the bug deterministically? If not, increase the reproduction rate or gather more evidence before proceeding.
6. **For external integrations, prove every seam:** Distinguish source config, built artifact, SDK initialization, current device/session, outbound request, provider receipt, dashboard aggregation, and downstream webhook/entitlement state. Historical counters, a configured dashboard, or an HTTP 200 from another build are not current end-to-end proof.

**Prior investigation notes:** If the project already has notes such as `plan.md` (look for a `## Investigation Notes` section) or `learnings.md`, read them for context — they may capture findings, discarded hypotheses, or durable lessons from prior passes. Reading is fine; do not create or update these files here (see Optional State Files).

Output: **"Root-cause hypothesis: ..."** — a specific, testable claim about what is wrong and why, plus the tight-loop command and authoritative checkout/build identity.

After naming the hypothesis, refresh local history with one sanitized component or bug noun: search relevant project notes, `TODOS.md`, and `git log -S`. Never search with a raw error, customer data, token, hostname, path, or SQL fragment. Reuse prior findings only when current evidence matches them.

## Scope lock

Name the affected module or directory after forming the hypothesis. Treat edits outside it as scope expansion; if new evidence widens the scope, record why before proceeding. Skip the lock only when the failure genuinely spans the repository or the boundary remains unknown.

## Phase 2: Pattern Analysis

Check if this bug matches a known pattern:

| Pattern | Signature | Where to look |
|---------|-----------|---------------|
| Race condition | Intermittent, timing-dependent | Concurrent access to shared state |
| Nil/null propagation | NoMethodError, TypeError | Missing guards on optional values |
| State corruption | Inconsistent data, partial updates | Transactions, callbacks, hooks |
| Integration failure | Timeout, unexpected response | External API calls, service boundaries |
| Configuration drift | Works locally, fails in staging/prod | Env vars, feature flags, DB state |
| Stale cache | Shows old data, fixes on cache clear | Redis, CDN, browser cache, Turbo |

Also check:
- `TODOS.md` (if present) for related known issues
- `git log` for prior fixes in the same area — **recurring bugs in the same files are an architectural smell**, not a coincidence

**External pattern search:** If the bug doesn't match a known pattern, search the web for "{framework} {generic error type}" and "{library} {component} known issues". **Sanitize first:** strip hostnames, IPs, file paths, SQL, and customer data. Search the error category, not the raw message. If web search is unavailable, skip and proceed. If a documented solution or known dependency bug surfaces, present it as a candidate hypothesis in Phase 3.

## Phase 3: Hypothesis Testing

Before writing ANY fix, verify your hypothesis.

1. **Confirm the hypothesis:** Add a temporary log statement, assertion, or inspection command at the suspected root cause. Run the reproduction. Does the evidence match?
2. **If the hypothesis is wrong:** Before forming the next one, consider searching for the error. **Sanitize first** — strip hostnames, IPs, file paths, SQL fragments, customer identifiers, and any internal/proprietary data. Search only the generic error type and framework context: "{component} {sanitized error type} {framework version}". If the message is too specific to sanitize safely, or web search is unavailable, skip it. Then return to Phase 1, gather more evidence. Do not guess.
3. **3-strike rule:** If 3 hypotheses fail, **STOP** and ask the user (see Protocols) with what was tried and what evidence is missing. Present the options:
   ```
   3 hypotheses tested, none match. This may be an architectural issue
   rather than a simple bug.

   A) Continue investigating — I have a new hypothesis: [describe]
   B) Escalate for human review — this needs someone who knows the system
   C) Add logging and wait — instrument the area and catch it next time
   ```

**Red flags** — if you see any of these, slow down:
- "Quick fix for now" — there is no "for now." Fix it right or escalate.
- Proposing a fix before tracing data flow — you're guessing.
- Each fix reveals a new problem elsewhere — wrong layer, not wrong code.

## Phase 4: Implementation

Once the root cause is confirmed:

1. **Fix the root cause, not the symptom.** The smallest change that eliminates the actual problem.
2. **Minimal diff:** Fewest files touched, fewest lines changed. Do not refactor unrelated code. Do not revert user changes.
3. **Regression check:** When the bug is non-trivial and the repo has a reasonable test path, add or update a check that **fails** without the fix (proves it is meaningful) and **passes** with it (proves the fix works).
4. **Run tests:** Run focused tests or checks for the touched area, and broader checks when shared behavior changed. Paste the output. No regressions allowed.
5. **If the fix touches more than five files:** pause and ask the user, explaining why the blast radius is necessary before continuing:
   ```
   This fix touches N files. That's a large blast radius for a bug fix.
   A) Proceed — the root cause genuinely spans these files
   B) Split — fix the critical path now, defer the rest
   C) Rethink — maybe there's a more targeted approach
   ```

## Phase 5: Verification & Report

**Fresh verification:** Re-run the original reproduction and confirm it's fixed. This is not optional. Run the relevant tests/checks and paste the output.

Output a structured debug report:
```text
DEBUG REPORT
Symptom:         <what the user observed>
Root cause:      <the actual cause and the evidence for it>
Fix:             <files changed and behavior changed, with file:line refs>
Verification:    <reproduction re-run + test output showing the fix works>
Regression test: <file:line of the new/updated check, or "none — <why>">
Related:         <TODOS.md items, prior bugs in same area, architectural notes>
Status:          DONE | DONE_WITH_CONCERNS | BLOCKED
```

Use `DONE_WITH_CONCERNS` when the fix is applied but verification is partial (list each concern). Use `BLOCKED` only when the root cause cannot be proven with available context (state what was tried and what is missing).

## Optional State Files

Do not create or update `plan.md`, `changelog.md`, `learnings.md`, `TODOS.md`,
or other Markdown state files unless the user explicitly asks for a handoff,
checkpoint, TODO capture, or persistent investigation note.

When persistence is requested, use the `handoff` skill if available.

## Important Rules

- **3+ failed fix attempts -> STOP and question the architecture.** Wrong architecture, not failed hypothesis.
- **Never apply a fix you cannot verify.** If you can't reproduce and confirm, don't ship it.
- **Never say "this should fix it."** Verify and prove it. Run the tests.
- **If the fix touches more than five files -> pause** and justify the blast radius before proceeding.
