---
name: grilling
description: "Use when the user asks to be grilled or interviewed about a coding plan, design, specification, or implementation decision. Research discoverable facts first, then ask consequential unresolved questions. Do not impose an interview on ordinary implementation."
---

# Grilling

Stress-test the user's thinking before implementation. Expose hidden assumptions, force concrete choices, and leave a decision record another coding pass can execute.

Adapted for standalone Codex from Matt Pocock's `grilling` skill.

## Prime directive

Interview the user about blind spots, edge cases, tradeoffs, scope, failure modes, and success criteria. Keep the requested interview focused on material decisions. Conclude when the user ends it or all material branches are resolved; continue implementation only if the user also requested it. Honor an explicit request to wait for confirmation before implementing.

## Decision-frontier loop

1. **Inspect context first.** Read the relevant plan, repository instructions, source files, prior decisions, and evidence before asking questions.
2. **Remove researchable questions.** Answer questions about the codebase, external facts, or existing state with tools. Batch independent lookups or delegate them when useful; do not make the user supply facts you can discover.
3. **Build the question tree.** Separate independent branches and identify the earliest unresolved question on each branch.
4. **Ask one frontier question.** Ask the highest-value unresolved question whose prerequisites are settled, include a concise recommended choice, and wait for the user's response. Ask the whole frontier as a numbered round only when the user explicitly requests batching.
5. **Update and prune.** Incorporate the answer, close dead branches, expose new dependencies, and recompute the frontier.
6. **Repeat until done.** Stop only when the user confirms completion or every material branch is resolved enough to act.

## What to push on

- vague words such as "fast," "simple," "premium," "secure," or "done";
- unstated users, environments, owners, or source-of-truth files;
- canonical repository, branch, worktree, generated project, build, device, and provider identity;
- data shape, state transitions, concurrency, retries, idempotency, durability, and rollback;
- privacy, authorization, spend, release, migration, and other approval gates;
- happy-path assumptions, adversarial input, degraded dependencies, partial success, and recovery;
- validation evidence: what would prove the change works end to end rather than only in source or tests;
- scope boundaries, explicitly rejected alternatives, and the cost of being wrong.

## Question quality

- Ask concrete questions whose answers would change implementation or acceptance criteria.
- Explain a non-obvious tradeoff briefly, but do not preload the answer.
- Avoid generic questionnaires, repeated questions, and questions already answered by context.
- If the user is uncertain, offer two or three materially distinct choices with consequences.
- If a branch is low impact and reversible, choose a reasonable default and label it instead of prolonging the interview.

## Exit handoff

When the interview concludes, return:

1. settled decisions;
2. explicit defaults and assumptions;
3. unresolved risks or approval gates;
4. acceptance evidence required;
5. the next implementation or planning action.

Do not implement unless the user has also asked for implementation.
