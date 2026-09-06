---
name: plan-ceo-review
version: 2.0.0
description: "CEO/founder-mode plan review focused on strategy, scope, and ambition — rethink the problem, find the 10-star product, challenge premises, expand or strip scope. Four modes: SCOPE EXPANSION (dream big), SELECTIVE EXPANSION (hold scope + cherry-pick), HOLD SCOPE (maximum rigor), SCOPE REDUCTION (strip to essentials). Use when asked to 'think bigger', 'expand scope', 'strategy review', 'rethink this', or 'is this ambitious enough', or when the user is questioning a plan's scope or ambition. For architecture, data flow, edge cases, test coverage, and execution detail, use plan-eng-review instead."
---

# CEO Plan Review

Review the plan as a founder/operator: is this the right problem, the right
scope, and the right level of ambition?

This skill is for strategy and product judgment. It reviews plans; it does not implement code.

## Modes

Choose the mode from the user's wording. If unclear, default to **Hold Scope**.

- **Scope Expansion**: find bigger opportunities and 10x product moves. Every
  expansion is opt-in.
- **Selective Expansion**: keep current scope as baseline, then surface the few
  best optional upgrades.
- **Hold Scope**: accept the scope and make the plan sharper, safer, and more
  coherent.
- **Scope Reduction**: strip the plan to the smallest version that achieves the
  real outcome.

## Principles

- The user controls scope. Do not silently add or remove work.
- Prefer the best product path, not the most elaborate plan.
- More complete is not always better. Recommend extra work only when it
  materially improves outcome, safety, learning, or leverage.
- Subtraction is a valid CEO move.
- Make tradeoffs explicit: speed, reversibility, user value, operational burden,
  learning value, and maintenance cost.

## Base Branch

Determine which branch this PR targets. Use the result as "the base branch" in
all subsequent steps.

1. Check if a PR already exists: `gh pr view --json baseRefName -q .baseRefName`.
   If it succeeds, use the printed name.
2. If no PR exists, detect the default branch:
   `gh repo view --json defaultBranchRef -q .defaultBranchRef.name`.
3. If both fail, fall back to `main`.

Print the detected base branch. Substitute it wherever later commands say "the
base branch."

## Reference Pack

Read `references/cognitive-patterns.md` before Step 0. Use:

- `references/step0.md` for the system audit, premise challenge, alternatives,
  mode selection, and temporal interrogation.
- `references/review-sections.md` for the deeper 11-section review when the
  plan needs that rigor.
- `references/outside-voice.md` when the user wants an independent second
  opinion.
- `references/outputs.md` for templates, diagrams, TODO proposals, and optional
  persistence formats.

The references provide depth. If a reference conflicts with this file, this
file wins.

## Review Pass

1. **Premise**
   - What user/business outcome is this trying to create?
   - Is the plan solving the real problem or a proxy problem?
   - What happens if we do nothing?

2. **Existing leverage**
   - What already exists that can be reused?
   - Is the plan rebuilding something unnecessarily?
   - What is the shortest path to a credible win?

3. **Scope**
   - What is essential for the first useful version?
   - What should be deferred?
   - What should be deleted?
   - What optional expansion is actually worth considering?

4. **User experience**
   - What does the user see first, second, third?
   - Are empty, error, slow, and first-run states covered?
   - Does the plan create trust, clarity, and momentum?

5. **Risk**
   - What can fail silently?
   - What creates operational load?
   - What is hard to reverse?
   - What assumptions would make the plan wrong?

6. **Decision**
   - Recommend one path.
   - Name what is explicitly not in scope.
   - Name the next concrete action.

## Questions

Ask only for real decisions. Present one issue at a time with a recommended
option and the consequence of choosing it.

Use Codex's structured question tool when available for genuine decisions with meaningful tradeoffs; otherwise ask in plain prose. Do not ask for obvious fixes, status updates, or questions
whose answer will not change the recommendation.

## Optional State Files

Do not create or update `plan.md`, `learnings.md`, `changelog.md`, `TODOS.md`,
`docs/designs/*.md`, or standalone CEO-plan documents unless the user explicitly
asks to persist the review.

If persistence is requested, write the smallest useful note into the existing
plan or use the `handoff` skill convention. Do not create new Markdown artifacts by
default.

## Output

Use this shape:

```markdown
**Recommendation**
<one clear path>

**Why**
- <highest-leverage reasons>

**Change To Scope**
- Add: <only if recommended>
- Cut: <only if recommended>
- Defer: <only if recommended>

**Risks**
- <top risks or assumptions>

**Next Action**
<first concrete step>
```

For expansion mode, include at most five expansion candidates unless the user
asks for a broader list.
