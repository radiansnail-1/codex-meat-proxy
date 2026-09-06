---
name: handoff-pr-merge
description: "Publish a lightweight handoff through a GitHub PR and authorized merge, then preserve relevant durable project context in the appropriate wiki without mirroring the codebase. Includes compact canonical state, required tracked Graphify, CI gating, merge, remote verification, and a relevance-gated wiki update. Do not use for release, deployment, or product re-verification."
---

# Handoff PR Merge

Extend `handoff` with PR publication, required CI gating, merge, and remote-target verification. This is delivery coordination, not a new validation or release workflow.

## Authorization

An explicit `$handoff-pr-merge` request authorizes the scoped source commit, push, PR, and merge after required checks pass. When the work materially changes durable project context, it also authorizes a narrowly scoped update to the one relevant wiki vault, its required derived-index refresh and leak scan, and a separate wiki commit and push. A user instruction such as “PR only,” “draft,” “do not merge,” or “do not update the wiki” narrows that authority and wins over the skill name. PR-only or unmerged work must not be written to the wiki as completed fact.

The skill never authorizes deployment, App Store/TestFlight upload, release, production configuration changes, credential mutation, or paid-media activity.

Never force-push, bypass branch protection, override failing checks, or merge a different scope without explicit authorization.

## Governing Contracts

Before mutation:

1. Read applicable repository instructions.
2. Load `handoff` and use its compact canonical-file, evidence, commit, Graphify, and push contract.
3. Load `github-yeet` for GitHub publication mechanics.
4. If the repository tracks Graphify, read [references/graphify-publication.md](references/graphify-publication.md).
5. If a wiki update may be relevant, load `wiki` and follow its vault routing, synchronization, privacy, indexing, leak-scan, and repository-instruction contracts.

Repository instructions override this skill when more specific.

## What This Skill Does Not Verify

Do not run new local tests, lint, type checks, builds, native generation, archives, simulators, credential checks, SDK checks, dashboards, live-service probes, browser QA, reviews, or device QA.

Record evidence already produced. If evidence is absent, say so in the PR. Required CI is the merge gate; this skill does not manufacture additional evidence before publishing.

Do not crawl or ingest the whole codebase into the wiki. Source code, file inventories, commit-by-commit history, implementation mechanics, transient debugging notes, CI details, and ordinary refactors belong in Git, the PR, or the compact handoff files.

## Workflow

### 1. Create The Lightweight Source Checkpoint

Use the `handoff` contract to compact the canonical files, keep only the rolling 14-calendar-day changelog window (including the active local date), and commit the scoped source plus handoff files. Before pruning older changelog sections, move unresolved work to `plan.md` and durable lessons to `learnings.md`; never discard unfinished owner TODOs or re-import expired history from another checkout.

If repository instructions require the assigned PR number in tracked handoff state, deliberately defer final Graphify publication. First obtain the real PR identity through the minimal provisional publication flow in Step 3, then update the canonical files once and follow `handoff`'s commit-shape contract. This sequencing overrides the ordinary `handoff` push/Graphify order only for that PR-identity dependency.

Do not guess a PR number or remote status. Do not restage unrelated owner changes. Model the intended post-merge resume state, but record remote facts only after GitHub returns them.

### 2. Confirm Cheap Publication Invariants

Before opening or updating the PR, inspect:

```bash
git status --short --branch
git diff --check
git branch --show-current
git fetch origin --prune
gh auth status
```

Confirm:

- the PR head is the intended checkpoint branch;
- the base is the intended remote target branch;
- the scoped diff contains no unrelated changes, conflict markers, `.env*`, secrets, or generated artifacts that repository rules exclude;
- no requested work remains only in an unstaged or unpushed path;
- the PR is mergeable or has an explicit, reported blocker.

These are publication-scope checks, not product verification.

### 3. Create Or Update The PR And Finalize Tracked Handoff State

When tracked handoff state requires the assigned PR number:

1. Prefer creating or updating the PR from an existing pushed branch commit. If the branch has no unique pushed commit, create and push the minimum scoped provisional checkpoint needed for GitHub to assign a PR number; do not create an empty or Graphify-only commit for this purpose.
2. Create or update the PR and capture its real number and URL.
3. Update the canonical files once with that PR identity and the stable current state: required CI is pending on the final head, merge is intended after required checks pass, and the concrete post-merge next action remains recorded.
4. If required, run only the repository-supported incremental Graphify publication. Prefer generating from the staged snapshot or source digest and include the canonical update and graph in one final checkpoint commit when the repository supports it.
5. If the graph embeds an exact existing commit identity, follow `handoff`'s structurally required source/handoff commit plus graph-only commit. Never create a temporary or unreachable "pretend" commit. Run the normal integrity/freshness check and push the final PR head.

Do not wait for or memorialize checks on the provisional head. After final Graphify publication starts, keep passing/failing CI timestamps in GitHub and the completion report; do not create another handoff/Graphify cycle merely to replace “pending” with “passed.” If incremental Graphify refuses because it needs semantic extraction, a full rebuild, version repair, manifest/baseline reconstruction, or other recovery, stop publication and report the blocker; do not expand PR delivery into Graphify recovery. If a real blocker or scope change alters resume state, follow the repository's explicit rules.

When the repository does not require a real PR identity in tracked files, use the ordinary `handoff` sequence: Graphify and push the complete checkpoint before creating the PR.

Keep the PR body concise:

- what changed and why;
- existing verification evidence;
- what remains unverified;
- deliberately excluded local changes;
- remaining risks or external gates.

Do not include raw environment values, credentials, tokens, unsupported claims, or the entire handoff documents.

If the user requested PR-only, leave it open or draft as requested and stop after reporting the URL.

### 4. Wait Only For Required CI

Wait for required GitHub checks to settle, for example:

```bash
gh pr checks <number> --watch --interval 10
```

If a required check fails, is cancelled, or the PR becomes non-mergeable, stop and report the exact blocker. Do not automatically expand the task into debugging, code changes, local verification, or repeated Graphify cycles. Continue only when the user asks to fix the blocker or the fix is already explicitly within the active request.

### 5. Merge And Verify

When merge is authorized, the PR is mergeable, and required checks pass:

1. Inspect the live PR state and review requirements.
2. Mark a draft ready if necessary.
3. Use the repository's requested merge method; otherwise prefer squash merge.
4. Verify GitHub reports the PR merged.
5. Fetch and verify the merge commit is present on the remote target branch.

Do not create a post-merge handoff commit merely to record the merge; GitHub and the remote branch are the durable authority.

### 6. Preserve Relevant Project Context In The Wiki

After the merge and remote-target verification, decide whether the completed work changed knowledge that should survive outside the repository. A wiki update is relevant when the merge materially changes one or more of:

- what the product, company, or team does;
- a user-facing capability, offering, workflow, or operating model;
- a durable product, business, architecture, or integration decision and its rationale;
- an important external dependency, ownership boundary, constraint, or recurring operating procedure;
- the high-level status of a meaningful initiative when that status is already tracked in the wiki.

Skip the wiki update for internal refactors, formatting, dependency churn, routine bug fixes with no durable lesson, generated changes, test-only work, and other implementation detail. When uncertain, prefer no edit and report that no durable wiki delta was identified.

When relevant:

1. Select exactly one vault using the `wiki` routing contract. Cross-vault updates require an explicit user request.
2. Synchronize the vault and read its instructions and routing index before editing.
3. Extend the smallest set of existing entity or project pages; create a page only when the vault's conventions clearly require one.
4. Write a concise, human-level summary of the durable change: what it is, why it matters, current status, important constraints or decisions, and a source link to the merged PR when useful.
5. Preserve uncertainty and distinguish shipped/current behavior from plans. Do not paste the PR body, handoff files, code, diffs, file paths, Graphify output, or a general repository summary.
6. Refresh only that vault's derived index, run its mandatory leak scan, inspect the scoped wiki diff, then commit and push the wiki change separately under the vault's repository rules.

A wiki sync, auth, conflict, routing, index, or leak-scan failure does not undo a verified source merge. Stop the wiki portion, preserve all local work, and report the exact partial-completion blocker. Never force-push, bypass vault safeguards, or write to a guessed vault.

## Completion Report

Lead with the result and include:

- PR URL and final state;
- remote target branch and merge commit when merged;
- required CI result;
- checkpoint commit(s), plus the Graphify result and graph-only commit only when the repository format required one;
- canonical files included;
- wiki vault and pages updated, with the wiki commit, or a one-line reason no durable wiki update was relevant;
- unrelated local changes preserved;
- remaining unverified work or blockers.

Never call the source-delivery workflow complete until GitHub and the remote target branch agree. Report wiki completion separately so a post-merge wiki blocker is visible rather than misrepresenting the source merge.
