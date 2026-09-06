---
name: spawn
description: Delegate bounded research, implementation, or independent verification when the user invokes /spawn or $spawn, asks for subagents, parallel agents, delegation, or separate reviewers. Do not invoke merely because ordinary work could be divided.
---

# Spawn

Use delegation to improve elapsed time or independent scrutiny. Keep the parent responsible for scope, integration, evidence, and the final answer. A simple task or dependent workflow may have no useful agent lane; say so and complete it locally.

## Choose lanes

Inspect enough context to identify a concrete outcome and bounded ownership. Delegate independent research questions, disjoint implementation slices, or focused review while the parent continues useful non-overlapping work. Do not send several agents to look for the same vague problem.

Use the smallest useful number within the current tool's concurrency limit. Shared files, state, schemas, or generated outputs need one owner or sequential work. Do not delegate deterministic bookkeeping such as Git status, staging, commits, pushes, handoff-file updates, or mechanical Graphify publication.

## Tools and model routing

Use the native delegation tools exposed in the current session and their actual schemas; in Codex this may be `collaboration.spawn_agent`. Do not assume role names or tool namespaces from another harness. Discover a tool only if no suitable callable tool is already available. A skill does not override harness limits or permissions.

Inherit the parent model and reasoning settings by default. Honor a user-selected model or cost route. Use a different route only when explicitly requested or justified by a relevant evaluation and permitted by the tool; do not hardcode a model generation, tier, or maximum effort as a universal default. Verify actual availability rather than silently substituting a tier.

Do not launch a separate CLI just to bypass a native tool limitation. Use a CLI lane only when the requested workflow requires it and its execution scope, model, permissions, and output capture are understood. If delegation is unavailable, continue locally and disclose the limitation.

Account for measured machine pressure when lanes launch browsers, compilers, simulators, or other local processes. Do not assume each remote reasoning agent consumes a fixed amount of local RAM.

## Worker packet

Give each agent:
- the outcome and exact repository/artifact scope;
- the files or responsibility it owns, or a read-only boundary;
- the user constraints and context it cannot otherwise access;
- the evidence required: patch and checks, reproduction, source-backed findings, or concrete counterexample;
- a concise return contract covering result, changed files, verification, and unresolved gaps.

Tell editing workers they share the workspace, must preserve others' changes, and must adapt to concurrent edits. Never give multiple workers overlapping ownership accidentally.

For independent evaluation, provide the task, raw artifact, and acceptance criteria without the builder's proposed answer or confidence. Use isolated fixtures when testing instructions that could trigger writes. Do not expose secrets or authorize new external side effects through delegation.

## Manage and integrate

Continue local work that does not duplicate agent ownership. Inspect results before trusting them, reconcile disagreements against artifacts, and verify the combined result. A child saying a test passed is useful evidence to inspect, not a substitute for the actual result when available.

For difficult research, track distinct hypotheses and redirect converging or stalled lanes toward new evidence. Reopen a failed approach only when the mechanism or evidence changes. Do not create agents merely to satisfy a quota or serialize explorer/worker/verifier handoffs when a single owner is faster.

Wait when a result is on the critical path, use available bounded wait tools, and stop or release agents when their work is no longer useful. Respect the user's time/cost limits and task stopping condition. Never present a pending check as complete.

## Report

Give the integrated result and verification. When material, briefly state which agent roles contributed and any disagreements or gaps. If a requested delegation could not help or could not run, explain why. Do not paste unchecked agent summaries as the final answer.
