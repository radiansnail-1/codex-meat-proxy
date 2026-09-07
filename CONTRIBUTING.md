# Keeping skill updates together

Keep the standard skill folder format:

```text
skills/<name>/
  SKILL.md
  agents/openai.yaml     # when present
  references/           # when needed
  scripts/              # when needed
```

The repository owns the public, portable version. A personal installation may retain private project routing, device details, and operational conventions. Synchronize reusable changes by reviewing diffs rather than copying entire directories.

## Update workflow

1. Identify the named skill and its public counterpart. Inspect repository state and fetch remote changes before editing; preserve unrelated work. Base new work on current remote main or continue the matching open update branch.
2. Make the requested change in the relevant variant. Carry reusable behavior changes into its counterpart. Keep local paths, private account/product details, credentials, and personal-only references out of the public patch. Preserve public substitutions and license/attribution metadata.
3. Update affected references, executable helpers, and invocation metadata together. A local-only preference can have no public delta; say so. An absent public counterpart requires an explicit decision to publish a new skill.
4. Validate with `python3 scripts/validate.py`, inspect changed local references, and run relevant helper tests when executable behavior changes. Validate the personal counterpart with the installed skill validator when available. Report skipped behavioral testing honestly.
5. Inspect the complete scoped diff, commit, push an update branch, and create or update a draft PR when publication is authorized. Include what changed, why, verification, and any intentionally local-only difference. Do not merge without authorization.
6. Report the local result and GitHub PR separately. A local edit, a pushed branch, and a merged main branch are different completion states.

If GitHub access fails, preserve the local change and prepared public diff, and report publication pending. Do not claim the repository was updated until the push is verified. Do not create a recurring background watcher merely to maintain skills.

## Installation choices

`./scripts/install.sh --link` makes edits in an intentionally shared installation modify this checkout directly; Git commit and push are still required to update GitHub. Existing non-symlink folders are skipped. Do not replace a customized personal installation with symlinks without reconciling its differences.

`./scripts/install.sh --copy` replaces destination skill directories. Use it for an intentional installation, not as a synchronization command for private adaptations.

The validator requires PyYAML (`python3 -m pip install PyYAML` in your chosen Python environment). It validates skill metadata and scaffold placeholders; it does not prove link correctness, script behavior, or task quality.
