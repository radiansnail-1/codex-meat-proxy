---
name: handoff
description: Create and push a lightweight, resumable project checkpoint by refreshing plan.md, learnings.md, and a rolling 14-day changelog, updating a required tracked Graphify graph, and committing only the scoped work. Use for handoff, checkpoint, save-state, or resume-note requests. Use handoff-pr-merge when a PR and merge are also requested.
---

# Handoff

Preserve the current working state quickly enough that a fresh session can resume it. A handoff records evidence already produced; it does not re-verify the product or repair repository tooling.

## Checkpoint Boundary

A full handoff is one durable session boundary, not per-action telemetry. During one live turn, batch nearby owner gestures, logins, approvals, or other short interactions into the next durable checkpoint. Do not create a commit, Graphify refresh, and push merely because the workflow is about to ask the user for a brief action and expects to resume immediately afterward.

Run the full workflow when the user explicitly asks to save/checkpoint now, when the task is genuinely stopping, or when context/session continuity is at risk. If the canonical files already describe the same material state, do not rewrite or recommit them.

## Authorization

An explicit `$handoff` or full checkpoint/publish request authorizes:

- updating the three canonical handoff files;
- committing the clearly scoped current work and handoff files;
- performing a repository-required incremental Graphify refresh;
- pushing the checkpoint branch.

A request only for a resume note or summary calls for the requested note, without committing or pushing. Automatic skill selection does not expand authority. For note-only work, stop after producing the note; the full canonical-file and publication workflow below applies to checkpoints.

It does not authorize a PR, merge, deployment, release, upload, or live-service mutation. An explicit request such as “local only” or “do not push” narrows the workflow.

Do not push directly to the remote default branch unless the user explicitly requests that. If the active branch is the default branch, create a non-default `codex/handoff-<short-scope>` checkpoint branch before committing.

## Canonical Files

Maintain exactly these project-root files:

- `plan.md`: current goal, status, next action, blockers, resume command, and unfinished user TODOs. Target 30–80 lines excluding the user's TODO pile; do not exceed roughly 150 lines without a concrete need.
- `learnings.md`: durable, non-obvious rules, decisions, and root causes that will still matter later. Target at most 20–40 active bullets; delete superseded, duplicated, transient, or code-obvious entries.
- `changelog.md`: short chronological continuity for a rolling 14-calendar-day window, including the active local date. Keep each meaningful entry to roughly 3–6 bullets. Before removing an older section, migrate any still-open work to `plan.md` and any still-durable lesson to `learnings.md`; then delete the old section. Git history is the archive.

Do not duplicate a fact across all three files. Do not create `handoff.md`, dated handoff files, backup copies, separate TODO files, wiki stubs, or cleanup reports.

If `changelog.md` is an established product/release changelog rather than a handoff file, ask before repurposing it.

Read [references/templates.md](references/templates.md) when creating or substantially restructuring the canonical files.

## Evidence Rule

Record verification already completed in the active session, including exact commands and outcomes when useful. Do not run new:

- tests, lint, type checks, builds, native generation, archives, or simulators;
- credential, SDK, dashboard, production, or live-service checks;
- reviews, audits, investigations, browser QA, or device QA.

If evidence is missing, stale, or incomplete, write `unverified` and preserve it as a next step. Never turn a handoff into a release audit.

## Lightweight Repository Check

Use only cheap state inspection needed to avoid saving the wrong work:

```bash
git status --short --branch
git branch --show-current
git diff --stat
git log --oneline -5
git diff --check
```

Inspect the relevant staged and unstaged diff. Determine the current task's paths from the conversation and repository state. Preserve unrelated owner changes and never use `git add -A` in a mixed worktree.

If scope is ambiguous, commit the canonical handoff files and other clearly scoped paths only, then report every excluded uncommitted path. Do not stall the checkpoint by investigating unrelated work.

## Commit Shape

Prefer one checkpoint commit. When a repository can generate and validate its tracked graph from the staged source snapshot or a source-content digest, stage the scoped source and canonical files, run the supported incremental graph publication, stage the graph, and commit everything once.

Do not create a temporary or "pretend" commit merely to obtain a hash and then squash/amend it away. A tracked graph that embeds an exact `built_at_commit` cannot safely name the same commit that contains it: adding the graph changes the commit hash, and an abandoned temporary hash will be unavailable in fresh clones and CI. For that repository format, a source/handoff commit followed by one graph-only commit is structurally required until the repository changes its graph metadata to a staged-tree or source-digest identity. Follow the repository's declared format and report this constraint plainly.

## Workflow

1. Confirm the real project root and read existing canonical files.
2. Inspect the lightweight repository state above.
3. Rewrite `plan.md` as current resume state while preserving unfinished user-authored TODOs.
4. Prune and update `learnings.md` with only durable knowledge.
5. Add the current material delta to `changelog.md`, deduplicate it, migrate surviving TODOs/lessons to their canonical files, and remove every entry outside the rolling 14-day window. Do not restore expired history from another branch or checkout during conflict resolution.
6. Record existing evidence without generating new evidence.
7. Stage only explicit scoped paths and the canonical files, then run `git diff --cached --check`.
8. If repository instructions require a tracked Graphify graph **and scoped non-document source changes are staged**, use the repository's supported incremental publication command once. Prefer generating from the staged snapshot and including the graph in the same commit when the repository supports it. Canonical handoff-file edits alone do not justify a graph refresh unless the repository explicitly says otherwise. Do not perform graph exploration, a full corpus rebuild, semantic extraction, or visualization work as part of handoff.
9. Commit once when the graph format permits it. If the graph requires an existing exact commit identity, commit the scoped source/handoff first, publish the graph from that commit, and create one graph-only commit; never simulate a commit that will not remain reachable.
10. Push the current checkpoint branch with upstream tracking. If authentication, remote state, or branch protection blocks the push, retain the local commits and report the exact blocker.

Once Graphify begins, do not edit the canonical files for transient push or CI status. Live hosting state belongs in the final response or PR, not another handoff cycle.

### Graphify fast-fail boundary

Graph publication must remain mechanical. Run only the repository-defined incremental command (for example, `npm run graphify:update`) and its normal check when required.

If that command is missing or refuses because of a version mismatch, missing manifest/baseline, semantic-update marker, unavailable tool, shrink guard, or request for a full rebuild:

- stop the Graphify step and report the exact command and blocker;
- keep any already-created scoped commit—or the staged scoped work in a one-commit flow—intact, and push an existing commit when otherwise safe;
- do not inspect Graphify internals, reconstruct manifests or historical baselines, create temporary worktrees, invoke a full/semantic workflow, or spawn agents to finish Graphify.

Graphify recovery is a separate task, not handoff bookkeeping.

## Guardrails

- Never delete source, evidence, screenshots, logs, ignored files, or temporary artifacts as part of a normal handoff.
- Never install dependencies or bootstrap tools merely to complete a handoff.
- Never delegate deterministic handoff bookkeeping or Graphify publication to subagents.
- Never amend a source/handoff commit after a tracked graph has been generated from it.
- Never invent review, verification, release, or remote status.
- Keep the checkpoint scoped and reversible; leave unrelated dirty state untouched.

## Completion Report

Report only:

- the checkpoint branch and pushed commit(s);
- one short line for each canonical file;
- Graphify update/check result when required;
- excluded/uncommitted paths preserved;
- unverified or blocked next actions.
