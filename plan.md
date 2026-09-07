# Plan

**Goal:** Keep reusable skill updates aligned between personal installations and this public repository.
**Status:** Maintenance documentation is implemented; PR #2 is prepared for authorized merge.
**Next action:** Use the paired-update workflow for the next shared skill revision.

## Resume state

- Read AGENTS.md and CONTRIBUTING.md before editing skills.
- Publication branch: codex/paired-skill-maintenance.
- PR: https://github.com/radiansnail-1/codex-meat-proxy/pull/2
- Existing evidence: all 24 public skills passed `python3 scripts/validate.py`; the companion local maintenance skill passed its installed validator.
- No executable behavior changed. Behavioral synchronization across future tasks remains untested.
- No tracked Graphify graph or graph refresh requirement applies to this documentation checkpoint.
- Resume: `git fetch origin --prune`, then inspect the current branch and PR state before new work.

## Pending

- Future shared skill changes should reconcile both variants and publish a scoped draft PR.
- Merged state is authoritative on GitHub; do not infer it from this pre-merge checkpoint.

**Last updated:** 2026-09-07
