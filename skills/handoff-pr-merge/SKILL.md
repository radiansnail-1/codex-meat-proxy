---
name: handoff-pr-merge
description: Close a work session by preserving resume state, reviewing how the user worked, and updating relevant skills, project guidance and canonical wiki knowledge. Publish a scoped checkpoint or GitHub PR and merge when the request and session require delivery; complete relevant knowledge updates even when there is no code to publish. Use for handoff, session closeout, checkpoint, save-state, or PR-and-merge requests. Summary-only requests return text. Do not use for deployment, release or product re-verification.
---

# Session Closeout, Checkpoint and Publication

Use one closeout workflow for session learning, durable knowledge and optional repository delivery. A missing repository or source PR does not prevent relevant skill or wiki updates.

## Scope and authority

- An explicit `$handoff-pr-merge` invocation authorizes relevant skill/project-guidance updates, canonical wiki writeback and their existing validation/backup workflows. When the session has scoped repository work to deliver, it also authorizes commit, push, PR and merge after required checks and reviews pass.
- Natural-language closeout or checkpoint requests select the matching scope; automatic skill selection does not grant a merge. A requested checkpoint authorizes its scoped commit/push; a guidance closeout follows the affected skills' and wikis' existing publication rules.
- Honor narrower instructions such as summary-only, note-only, local-only, checkpoint-only, PR-only, draft, no merge, no wiki or no skill updates. A summary/resume-note request alone returns text without durable writes.
- No source changes to deliver: skip source publication and still complete relevant guidance/wiki updates. Do not create an empty PR to make the skill name fit.
- Deployment, release, uploads, live-service changes, spending, messages to others, sharing changes and new schedules retain their own authorization boundaries. Never force-push or bypass failed checks or branch protection.

## Review the session

Use the conversation and evidence already produced. Follow [session closeout](references/session-closeout.md) on every substantive closeout:

1. Identify completed work, explicit corrections, accepted choices, repeated friction, unresolved work and the next action. Distinguish proposed, applied, verified and pending states.
2. Decide which lessons are reusable workflow changes and which are project/company facts. Update only affected skills, project guidance and owning knowledge pages; skip any destination with no material delta.
3. Preserve accepted preferences at their actual scope. Do not infer a permanent rule from an unaccepted suggestion or one ambiguous example.
4. Apply relevant skill and project-guidance edits before the final checkpoint when they belong in that repository. Defer wiki claims that depend on source delivery until its actual outcome is verified; independent decisions or lessons can be written without a source merge.

## Preserve project state when relevant

For a real project checkpoint or repository delivery, use [checkpoint](references/checkpoint.md). A guidance-only closeout does not create three project files in an arbitrary projectless directory.

Maintain compact `plan.md`, `learnings.md` and a rolling 14-calendar-day `changelog.md`; preserve unfinished user TODOs. Read [templates](references/templates.md) only when creating or substantially restructuring those files.

Record product checks already completed; mark absent or stale evidence unverified. Do not run fresh product tests, lint, builds, simulators, dashboards, live probes or a release audit. Validation of changed instructions, mandatory wiki/privacy/backup checks and a repository-required graph integrity check remain part of the authorized edits.

## Deliver repository work when applicable

Skip this section when there is no scoped repository work to publish or the selected mode excludes publication.

1. Read applicable repository instructions; inspect Git state and the scoped staged/unstaged diff. Preserve unrelated changes, use explicit paths, and never push directly to the remote default branch unless requested. If on that branch, create a non-default checkpoint branch.
2. Use `github-yeet` when available for publication mechanics; reuse session verification evidence. For required tracked Graphify, follow [graph publication](references/graphify-publication.md), including supported semantic refresh/recovery and exact source identity. Do not delegate deterministic bookkeeping.
3. Stage the scoped source and canonical state; run whitespace/scope checks. Prefer one commit when the graph supports a staged snapshot/source digest; an exact existing commit identity requires a source/checkpoint commit followed by a graph-only commit. Never use a temporary or unreachable pretend commit.
4. Push the final branch and create or update the matching PR. If tracked state requires the real PR number, use the graph reference's provisional-publication exception before the final graph pass. Attach created/updated PRs using the host's attachment tool when available.
5. Keep the PR body concise: resulting behavior, existing evidence, unverified work, excluded changes and material risks. Keep credentials, private source material and transient CI timestamps out of tracked handoff files.
6. For PR-only/draft requests, leave the PR open as requested. Otherwise, wait for required CI and review gates on the final head. On a failed/cancelled check or conflict, report the blocker; repair it only when already authorized by the active request. Do not start unrelated investigations.
7. When merge is authorized and actual checks/reviews permit it, mark ready if needed, use the repository's merge method (otherwise squash), verify GitHub reports merged, then fetch and verify the merge commit on the remote target.
8. Do not create a post-merge/status-only checkpoint or Graphify cycle merely to record CI or merge timestamps.

## Complete relevant skill and wiki writeback

Always finish the material writeback selected by the session review, including when source publication was skipped, left draft or blocked.

- **Skills:** capture reusable corrections in the existing affected skill/resources. Use the available authoring/maintenance workflow; reconcile installed counterparts without overwriting private adaptations, and follow their public-update preference. Validate changed instructions and links. Report draft/publication state separately.
- **Wiki:** use the available wiki adapter and the scope's live entry instructions, directory and owning pages. Preserve its library/topic-guide layout, file IDs, source dates, concurrent changes and privacy boundaries. Reconcile against the agreed version; Git recovery and search results do not override a cloud-canonical page.
- Keep current facts in their owning record, dated evidence with its subject/work, and agreed actions in the existing task system. Write only supported changes; never describe unmerged code as shipped or paste repository inventories, raw diffs or whole handoff files into the wiki.
- Verify canonical readback/location/relevant access, run required privacy/focused checks, complete the reviewed backup, seal agreement only when both copies match, then refresh only that scope's documented index. Do not turn manual upkeep into a schedule.

A source-publication blocker does not block independent skill or knowledge updates. If wiki/skill access or reconciliation fails, preserve the prepared change and report that portion as pending; never claim completion or bypass its safeguards.

## Report the outcome

Lead with what was completed. Include the relevant project resume state, skills/guidance and wiki pages updated, validation, source/public-skill PR states, merge/backup evidence, preserved unrelated changes and concrete blockers. State why source publication or a writeback destination was skipped when relevant. A local edit, a draft PR, a saved plugin release and merged main are different states.
