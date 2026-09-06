# Compact Handoff Templates

Use these only when creating or substantially restructuring the canonical files. Rewrite existing files in place and keep each fact in one file.

## `plan.md`

```markdown
# Plan

**Goal:** <one sentence>
**Status:** <one sentence>
**Next action:** <first concrete action>

## Resume State

- **Path:** <absolute project path>
- **Branch:** <branch and latest relevant commit>
- **Last action:** <last concrete completed action>
- **Evidence:** <checks already run and outcomes, or unverified>
- **Blockers:** <current blockers or none>
- **Do not:** <scope traps or unsafe assumptions>
- **Resume:** `<literal first command>`

## TODO

- [ ] <current concrete task>
- [ ] <unfinished user-authored TODO to preserve>

## Context

- <small set of key file, PR, dashboard, or evidence pointers>

**Last updated:** YYYY-MM-DD
```

Target 30–80 lines excluding the user's TODO pile. Do not add historical narratives, repeated verification logs, or review tables unless a live review decision changes the next action.

## `learnings.md`

```markdown
# Learnings

- **<short hook>.** <durable non-obvious rule, decision, or root cause and why it matters.>

**Last updated:** YYYY-MM-DD
```

Target at most 20–40 active bullets. Remove superseded, duplicated, transient, and code-obvious entries whenever updating the file.

## `changelog.md`

```markdown
# Changelog

## YYYY-MM-DD — <short scope>

- <material change, decision, or fix>
- <important existing verification outcome, if any>

**Last updated:** YYYY-MM-DD
```

Keep only entries dated within the latest 14 calendar days. Use roughly 3–6 bullets for a meaningful scope and omit routine mechanics. Older context remains available through Git history.

