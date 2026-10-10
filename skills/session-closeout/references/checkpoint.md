# Project checkpoint

Use for a requested project checkpoint or scoped repository delivery. Identify the real project from the session; a generated projectless folder is not automatically its root.

## Canonical state

Maintain exactly these project-root files when checkpoint state is needed:

- `plan.md`: current goal, status, next action, blockers, resume command and unfinished user TODOs. Target 30–80 lines excluding the user's TODO pile; exceed roughly 150 only for a concrete need.
- `learnings.md`: durable, non-obvious rules, decisions and root causes. Target 20–40 active bullets; remove superseded, duplicated, transient or code-obvious entries.
- `changelog.md`: short continuity for the latest 14 calendar days, including the user's active local date. Keep meaningful entries to roughly 3–6 bullets. Before pruning older sections, move open work to the plan and durable lessons to learnings; Git history is the archive.

Read existing files first. Preserve unfinished user-authored TODOs and record each fact once. Do not create dated handoff files, separate TODO files, raw wiki stubs or cleanup reports. If the existing changelog is a product/release record, ask before repurposing it.

Use [templates](templates.md) when creating or substantially restructuring these files. Wiki/project facts follow their actual canonical owner; a newer Git timestamp does not make a recovery copy authoritative.

## Checkpoint boundary

Batch the session's material state into one durable checkpoint. Do not commit, refresh a graph and push for every brief login, owner gesture or approval. If the existing files already describe the same material state, do not rewrite/recommit them.

Keep pending work and existing verification evidence in resume state. Never invent a review, build, release or remote result. Missing/stale evidence stays unverified with a concrete next step.

## Cheap repository inspection

Use only the state needed to save the right work:

```bash
git status --short --branch
git branch --show-current
git diff --stat
git log --oneline -5
git diff --check
```

Inspect relevant staged/unstaged changes. Stage explicit task paths and canonical files; never use `git add -A` in a mixed worktree. If source scope is ambiguous, save clearly scoped state and report excluded paths without investigating unrelated owner work.

## Prepare the checkpoint

1. Confirm the project and read its instructions and canonical files.
2. Update the plan with current resume state and preserve unfinished user TODOs.
3. Prune/update durable learnings; add the material changelog delta, migrate surviving open work/lessons and remove entries outside the rolling window. Do not restore expired history from another checkout during conflict resolution.
4. Record existing evidence without rerunning product verification.
5. Stage only authorized paths and run `git diff --cached --check`.
6. If repository instructions require a tracked Graphify refresh for the staged change, follow [graph publication](graphify-publication.md). Canonical-file edits alone do not justify a graph refresh unless the repository explicitly requires one.
7. Commit/push only within the requested mode and publication authority. Prefer one commit when the graph supports it; preserve the retained source identity when a separate graph commit is required.
8. If authentication, remote state or branch protection blocks publication, retain local commits and report the exact pending step.

Once the final graph pass starts, keep transient push/CI/merge timestamps in GitHub and the completion report. Do not edit canonical state again unless a real blocker or scope change changes the next action.

## Preservation

Do not delete source, evidence, screenshots, logs, ignored files or temporary artifacts during a normal checkpoint. Do not install dependencies or bootstrap tools merely to hand off. Preserve unrelated dirty state and existing stashes; never amend a source/checkpoint commit after a tracked graph has been generated from it.
