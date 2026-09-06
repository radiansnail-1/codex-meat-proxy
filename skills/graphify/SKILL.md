---
name: graphify
description: "Use when the user explicitly invokes /graphify, asks to build, update, query, path, or explain a Graphify graph, or identifies graphify-out as the intended evidence source. Do not load for ordinary codebase questions merely because they concern architecture."
---

# Graphify

Compact Codex adapter for Graphify-Labs/graphify v0.9.53. Graphify is an evidence index, not a substitute for current source files or revision identity.

## Route the request

1. **Existing graph question:** if `graphify-out/graph.json` exists, use `graphify query`, `path`, or `explain`. Load `references/query.md` only when its vocabulary expansion or traversal details are needed.
2. **Code-only refresh:** use `graphify update <path>` when the user asks, when repo instructions require it, or after code changes in a repository that already tracks a graph. Load `references/update.md` only for incremental edge cases or `--cluster-only`.
3. **First full build or mixed semantic rebuild:** load `references/full-workflow.md`; load `references/extraction-spec.md` only when docs, papers, or images actually require semantic chunks.
4. **Optional features:** load only the matching reference: `github-and-merge.md`, `transcribe.md`, `exports.md`, `hooks.md`, or `add-watch.md`.

## Existing-graph fast path

- Confirm the graph path and, when available, its recorded commit or build metadata against the current repository HEAD.
- If the graph is stale, say so. Run the cheap code-only update only when requested or required; do not silently start a semantic rebuild.
- Prefer:
  - `graphify query "<question>"`
  - `graphify path "<node-a>" "<node-b>"`
  - `graphify explain "<node>"`
  - `graphify affected "<node>"`
- Use graph output to locate relationships, then inspect cited source locations before editing code or making correctness claims.
- Never invent an edge or hide a missing path. Preserve `EXTRACTED`, `INFERRED`, and `AMBIGUOUS` distinctions.

## Build and update rules

- Run `graphify --version` before a full build. This adapter targets 0.9.53; if the executable and `.graphify_version` disagree, stop and reconcile them before following the full workflow.
- Do not install or upgrade packages silently. If Graphify is absent or stale, state the required `uv tool` action and obtain approval unless the user already asked for the upgrade.
- A code-only corpus uses deterministic AST extraction and needs no model or API key.
- For docs, papers, or images, use Codex subagents with `gpt-5.6-luna`, `xhigh`, and `fork_turns="none"`. Never inspect, request, print, or reuse provider API keys.
- Review `.graphifyignore` and sensitive-file exclusions before broad scans. Report sensitive skips by count, not filename, unless the user explicitly asks to troubleshoot them.
- Do not upload a corpus or switch to the hosted Graphify service without explicit approval.
- Preserve the prior graph on partial extraction failure; never force past a shrink guard without evidence that source deletion was intentional.

## Completion evidence

Report the exact graph path, repository revision, Graphify version, operation run, node/edge counts, stale or partial state, skipped-sensitive count, and any semantic chunks that failed. Treat generated HTML/report files and the underlying `graph.json` as separate artifacts.
