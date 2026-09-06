---
name: code-audit
description: "Read-only correctness audits of code, integrations, builds, and release artifacts. Use when reviewing an implementation or commit without changing it."
version: 1.0.0
author: Brian Tan + Codex
license: private
metadata:
  tags: [audit, correctness, regression, mobile, integrations, review]
  related_skills: [investigate, qa, reliability-hardening, plan-eng-review]
---

# Code Audit

Perform a read-only, evidence-backed correctness audit of one pinned implementation target. Do not edit target source, reset branches, merge, deploy, or silently repair findings.

## When to use

Use when the user asks to:

- audit or review an implementation, commit, PR, integration, build, or release artifact;
- determine whether acceptance criteria are actually satisfied;
- inspect correctness, regressions, error paths, concurrency, state, or provider boundaries without fixing them;
- independently verify another agent's implementation claims.

Use `investigate` when the task is to find and fix a root cause. Use `reliability-hardening` when implementing durability or safety improvements. Use `qa` for user-facing runtime and visual verification.

## Pin the target

Before judging anything, record:

1. repository path and nearest project instructions;
2. remote, branch/worktree, commit, and dirty state;
3. exact requested behavior and acceptance criteria;
4. build/runtime/deployment identity when the audit involves generated artifacts or external state;
5. excluded surfaces and unavailable evidence.

Never mix evidence from a stale checkout, generated workspace, simulator install, physical-device build, TestFlight build, or production revision.

## Evidence classes

Label conclusions as:

- **Verified current** — observed in a focused test, current runtime, provider read, or exact artifact.
- **Implementation-backed** — directly supported by source/config at the pinned revision but not exercised end to end.
- **Documented/intended** — described by instructions or provider docs without matching current implementation evidence.
- **Unknown / not verified** — unavailable, ambiguous, credential-gated, or outside scope.

A source-level test, configured dashboard, successful HTTP response, uploaded build, or merged PR is not automatically end-to-end proof.

## Audit workflow

1. Map the affected control and data flow from entry point to durable outcome.
2. Read the changed files plus neighboring callers, state owners, error paths, retries, and cleanup.
3. Compare the implementation with working project patterns and current first-party APIs when necessary.
4. Run focused existing tests or temporary read-only probes. Record exact commands and results; never invent output.
5. Inspect boundary cases: missing/duplicate/out-of-order input, retry, partial failure, concurrency, stale state, migration, cancellation, and rollback.
6. Reconcile code claims with the exact build/runtime/provider surface when the feature crosses a system boundary.
7. Rank findings by severity and return findings before narrative.

## Mobile and generated-build audits

- Verify canonical checkout and generated native-project provenance.
- Reconcile app config, native project settings, Info.plist/manifest, extensions/widgets, signing target, marketing version, and build number.
- Bind simulator/device evidence to the exact source commit and artifact.
- Separate local build, upload, provider processing, TestFlight/App Store state, and public-storefront state.
- Treat stale Xcode issue rows and historical provider counters as non-current evidence.

## Analytics, attribution, and subscription audits

- Trace event emission and semantics in source before accepting dashboard labels.
- Verify order, duplicate guards, identity/session fields, app version/build, placement, and taxonomy generation.
- For checkout, inspect one attempt identifier, callback-specific lifecycle events, retry properties, once-guards, and entitlement confirmation before completion.
- Keep PostHog behavior, MMP attribution, RevenueCat/store revenue, and ad-platform delivery as separate authorities.
- An organic sandbox purchase proves only the observed app-to-billing/MMP path; it does not prove partner-attributed install or ad-network receipt.

## Integration and security checks

- Verify exact project/account/environment selection and configuration precedence without printing secret values.
- Check retry/idempotency, duplicate suppression, timeouts, partial failure, error propagation, and webhook/event ownership.
- Inspect untrusted-input handling, dynamic code/package loading, persistence, network egress, and credential boundaries.
- Never use live mutations merely to make an audit conclusive. State the approval-gated verification step instead.

## Finding quality

Every finding must include:

- severity;
- exact `path:line` or external entity/build reference;
- evidence and reproduction;
- user/operational impact;
- concrete fix direction;
- confidence and remaining verification gap.

Do not list style preferences as correctness defects. Distinguish confirmed defects, material risks, and hypotheses.

## Output

1. Verdict and pinned scope.
2. Severity-ranked findings.
3. Tests/probes actually run and results.
4. Evidence classes and provider/build reconciliation.
5. Coverage gaps and residual risk.
6. Recommended owner: `investigate`, `reliability-hardening`, `qa`, or release/deploy workflow.
