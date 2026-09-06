---
name: trim
description: Audit your entire agent setup — the instructions file (CLAUDE.md or AGENTS.md), all skills, all context files — and produce a list of everything to cut with reasons, any conflicts between files, and a cleaned-up instructions file. Run this whenever outputs start feeling worse or your setup feels bloated.
---

Read the active instruction files before producing recommendations:
- The harness instructions file: `~/.claude/CLAUDE.md` (Claude Code) or `$CODEX_HOME/AGENTS.md` (Codex)
- Every `SKILL.md` under the corresponding `skills/` directory (skip `node_modules/`)
- Plugin skill manifests exposed in the current session
- Other user-authored context files under the harness home (`~/.claude` or `$CODEX_HOME`), excluding caches, `node_modules/`, generated runtime folders, and plugin/vendor internals unless the user explicitly asks

Then go through every rule, instruction, and preference you found. For each one, evaluate:

1. **Default?** Is this something you already do without being told?
2. **Conflict?** Does this contradict or tension with another rule elsewhere?
3. **Duplicate?** Is this already covered by a different rule or file?
4. **Patch?** Does this read like it was added to fix one specific bad output rather than improve outputs generally?
5. **Vague?** Is this so non-specific you'd interpret it differently every time? (e.g. "be more natural", "use a good tone")

Then output three things:

**1. Cut list** — everything you'd remove, one-line reason each

**2. Conflicts** — any rules fighting each other across files, with both sides quoted

**3. Cleaned instructions file** — rewrite of the active `CLAUDE.md`/`AGENTS.md` with dead weight removed, conflicts resolved, and nothing that's already default behaviour

---

After getting results, the process:
1. Read what was flagged and why
2. Delete flagged rules only after user approval
3. Run your 3 most common tasks
4. Output same or better → the deleted rules were dead weight
5. Something specific broke → add back just that one rule
