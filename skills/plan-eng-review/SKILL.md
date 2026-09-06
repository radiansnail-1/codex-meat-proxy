---
name: plan-eng-review
description: Review a requested engineering plan, architecture proposal, or implementation design for correctness, reuse, failure modes, test coverage, and rollout. Use for engineering review or stress-testing a plan; do not interrupt ordinary implementation merely because a plan exists. Use plan-ceo-review for product scope and strategy.
---

# Engineering Plan Review

Review the supplied plan in one pass by default. Deliver a practical recommendation another engineer can implement. A review request alone does not authorize implementation or persistent state files; when the user requests review followed by implementation, continue with the authorized work after resolving material decisions.

## Establish the target

Identify the supplied plan, PR, branch diff, or named path. Inspect applicable repository instructions, current Git state, canonical design/plan documents, and nearby implementation patterns. User direction and explicit canonical markers outrank timestamps. Ask only if multiple plausible targets remain and selection would materially change the review.

## Review

- **Scope and reuse:** What already solves the problem? Prefer existing code, native behavior, or installed dependencies where they meet the requirement. Challenge unnecessary abstractions without reducing the user's chosen scope. File count is a signal to inspect, not a reason to stop.
- **Architecture and behavior:** Trace affected inputs, ownership, state transitions, dependencies, and durable outcomes. Inspect generated behavior before claiming it is missing. Identify realistic concurrency, partial-failure, cancellation, retry, security, and recovery risks relevant to the feature.
- **Implementation shape:** Recommend the smallest complete change consistent with repository conventions. For bug fixes, trace callers and address a shared cause when evidence supports it.
- **Verification:** Compare important behaviors and failure modes with existing checks. A regression is an unintended loss of previously correct behavior; an intentional behavior change or missing test is not by itself a regression. Recommend a meaningful failing-before/passing-after check for demonstrated regressions when feasible. Use [test strategy](references/test-strategy.md) for substantial coverage planning.
- **Performance and delivery:** Inspect likely bottlenecks and relevant build, publish, install, rollout, observability, and rollback paths. Do not expand a local change into speculative scaling work.

Research framework or provider behavior when correctness depends on current facts. Prefer first-party documentation and identify uncertainty. Use a diagram when it clarifies non-trivial flow; no diagram or branch-by-branch inventory is required for a simple plan.

## Decisions and evidence

Ask only when an unresolved decision materially changes scope, architecture, externally visible behavior, or authorization. Research discoverable facts yourself. Recommend a choice with its tradeoff; continue independent review while awaiting an answer. Honor an explicitly requested interactive review format.

Do not ask about obvious corrections, invent numeric completeness scores, or repeatedly reopen settled decisions. Existing authorization continues to count. If a material decision remains unanswered, report it without treating elapsed time as agreement.

Each finding needs the concrete scenario, impact, severity, and supporting plan statement or source location. Distinguish verified defects, supported risks, and unresolved hypotheses. Do not classify a coverage gap as a proven bug or invent findings to fill sections.

## Output

Lead with ranked findings and the recommended implementation shape. Include relevant verification, material decisions, and residual gaps. If there are no findings, say so. Scale detail to the plan; optional output examples are in [outputs](references/outputs.md).

Persist review notes or TODOs only when requested, using existing project conventions. Do not require a follow-up review, outside model, or subagent pass merely to finish this review. Use independent review when requested or when available delegation is authorized and materially useful; see [independent review](references/outside-voice.md) for that workflow.
