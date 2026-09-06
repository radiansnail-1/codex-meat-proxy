---
name: trim
description: Audit agent instructions and personal skills for conflicts, unnecessary overhead, overlapping triggers, and stale tool assumptions. Recommend concrete cuts and validate requested revisions. Use when asked to audit or simplify the agent setup.
---

# Trim

Start with active harness instructions and personal skill entrypoints plus their invocation metadata. Inventory vendor/plugin descriptions separately; inspect overlapping vendor entrypoints only when relevant. Exclude backups, archives, caches, generated runtime state, secrets, and unrelated personal content from broad scans.

For each substantive rule, assess whether it contributes non-obvious knowledge, duplicates a default, conflicts with another instruction, overgeneralizes a past incident, or triggers unrelated work. Inspect supporting references when needed to verify a finding or prevent an old rule from being reintroduced through a link.

Preserve operational invariants, user-selected conventions, authorization boundaries, and evidence standards. Prefer clear outcomes and decision criteria over mandatory interviews, numeric thresholds without evidence, and rigid reporting. Keep normal skill discovery enabled unless the user asks to change invocation policy.

Report ranked findings with exact source evidence and replacement direction, a per-skill cut/move/preserve list, and a cleaned global instructions proposal when useful. If the active global file is empty, leave it empty rather than adding defaults. Distinguish structural defects from behavioral hypotheses.

An audit alone does not authorize installing revisions. An explicit request to revise or apply the recommendations authorizes scoped edits and deletion of flagged rules; do not ask again. Preserve a recoverable original, update affected references/metadata consistently, and leave vendor caches alone unless specifically requested.

Run the installed skill validator and check linked local resources for changed skills. For substantial behavioral changes, evaluate realistic tasks and side effects when feasible; structural validation alone does not prove better behavior. Record what was actually tested and compare outcomes before claiming quality, speed, or token improvements.
