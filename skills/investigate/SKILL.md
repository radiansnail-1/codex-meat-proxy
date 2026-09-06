---
name: investigate
description: Investigate errors, regressions, stack traces, and unexpected behavior; find the root cause and implement a verified fix when requested. Use code-audit for a read-only correctness review.
---

# Investigate

Trace the actual failing path before fixing it. A request to explain a problem calls for an explanation; a request to fix it authorizes the necessary scoped implementation and verification.

## Establish evidence

1. Confirm the authoritative checkout, applicable repository instructions, current Git state, and intended runtime/build. Preserve unrelated work. Generated trees, archives, installed apps, and source checkouts may differ.
2. Read the symptoms and relevant source. Identify the smallest reproduction, focused test, safe probe, or captured evidence that distinguishes correct from failing behavior. Run it before editing when feasible; if reproduction is unavailable, state the limitation and use the strongest available evidence.
3. Trace callers, state owners, data flow, and recent relevant changes. Regressions can originate in source, dependencies, configuration, data, or external services; do not assume the cause must be in the local diff.
4. For integrations, distinguish configuration, built artifact, initialization, current run, outbound request, provider receipt, and downstream state. Initialization logs, historical counters, and an HTTP success alone do not prove the requested end-to-end outcome.

## Test hypotheses

State a specific causal hypothesis and choose a probe that can disprove it. Use targeted inspection, temporary instrumentation, a fixture, or a focused test. Update the hypothesis when evidence disagrees instead of accumulating symptom patches.

Search relevant existing notes and history when useful. For external searches, sanitize proprietary data, hostnames, identifiers, paths, credentials, and raw error details; query generic error categories and exact framework versions. Consult current first-party documentation when API behavior matters.

Failed hypotheses should change the evidence source or approach. Continue while a concrete next experiment can advance the task within scope and budget. Stop when required evidence, access, authorization, or consequential user judgment is missing, or no useful next experiment remains. Neither three failed hypotheses nor a fixed file count is an automatic stop condition.

## Fix and verify

Once evidence supports the cause, implement the smallest complete fix. Trace all affected callers; explain a wider edit boundary when necessary without treating mechanical multi-file updates as a permission gate. Do not refactor unrelated code or overwrite owner changes.

For a non-trivial bug with a reasonable test path, add or update a check that fails for the real defect and passes with the fix. Rerun the original reproduction where possible, the focused checks, and required project checks; broaden verification when shared behavior changes. Summarize results and link useful evidence instead of dumping logs.

If the task needs durable concurrency, idempotency, persistence, or adversarial-input controls, use `reliability-hardening` for that boundary. Runtime UI verification may use `qa` and the appropriate platform skill. Routing does not require asking again about work already authorized.

Do not claim a fix is verified if the original failure or an equivalent decisive check could not be exercised. Separate a supported source correction from its remaining runtime/provider verification gap. A debugging request does not itself authorize production release or unrelated provider writes.

## Communication

Ask only for missing information or a consequential decision that tools and context cannot resolve. Give a concise explanation and recommendation; do not require completeness ratings, repeated path/branch introductions, or special status labels. See [protocols](references/protocols.md) only for reporting examples.

Report the outcome, cause and evidence, changed behavior/files, checks performed, and material remaining gaps. Persist investigation notes or handoff files only when requested; reuse existing notes as evidence without letting stale notes override current source.
