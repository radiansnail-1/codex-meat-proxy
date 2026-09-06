---
name: wiki
description: Route Brian's four Obsidian knowledge vaults. Use when the user asks to query, summarize, ingest, update, lint, or health-check personal, Sandbox, RMS, or All Square wiki content; asks what the wiki says; says “fold this into the wiki,” “wiki ingest,” “search my notes,” “lint the wiki,” or invokes /wiki.
---

# Wiki — four-vault router

This skill routes between four separate Obsidian vaults. Markdown under each vault's `wiki/` directory is the source of truth; GBrain or other indexes are derived search state. Do not treat the four vaults as one undifferentiated corpus.

## Vault map

| scope | vault root | use for |
|---|---|---|
| `personal` | `/Users/brian/Obsidian_Wikis/personal` | Brian's personal knowledge, relationships, life, decisions, and personal finance/investing context |
| `sandbox` | `/Users/brian/Obsidian_Wikis/sandbox` | Sandbox / edutainment, corporate development, diligence, and Sandbox operations |
| `rms` | `/Users/brian/Obsidian_Wikis/rms` | Radiant Management Systems, Prayer First, 140.6, CalPal, D2C product, growth, and app operations |
| `all-square` | `/Users/brian/Obsidian_Wikis/all-square` | All Squares, B2B AI clients, proposals, proof decks, sales pipeline, content, and brand work |

`personal` is the default only when no company scope is evident. Do not route to `riftbound` or any other vault unless Brian explicitly adds that scope.

## Required startup

1. Choose exactly one vault from the map using the user's topic. If the request explicitly spans scopes, search each named vault separately and label the sources; do not silently merge indexes.
2. Confirm that the selected root exists before reading or writing. If it is absent, report the missing path and stop; do not guess alternate paths.
3. Read that vault's root `AGENTS.md` before any non-trivial work. Read `CLAUDE.md` too when present (currently the personal vault has one). Follow the vault files if they conflict with this router.
4. Make the selected vault current before relying on it: run `git fetch --prune`, then inspect `git status --short --branch`. If the worktree is clean and behind, use `git pull --ff-only`. If it is dirty and behind, preserve the local work: for a read-only query/audit, inspect the newest remote files with `git show origin/main:<path>` (or an isolated temporary worktree) alongside local changes; for an edit, use a safe autostash/rebase workflow and resolve only unambiguous conflicts while retaining the safety stash until the merged tree is verified. Never discard, overwrite, or misattribute existing edits. If sync/auth fails or a conflict is ambiguous, report it and stop rather than answering from stale state as though current.
5. Read `wiki/index.md` for routing and current structure when the task is broad, ambiguous, or not covered by the vault's operating manual. Do not crawl the whole vault by default.

## Routing

- **Query / summarize:** select the vault, run its documented GBrain/index search first, treat hits as pointers, then open the matched Markdown pages and cite them as `[[WikiLinks]]`. Search literal topic terms and page-title words before trying a synonym. If search is unavailable or misses, use that vault's `wiki/index.md` and at most the relevant sub-indexes.
- **Ingest / fold in:** follow the selected vault's `AGENTS.md` and, for personal, `CLAUDE.md` ingest workflow exactly. Extend existing entities before creating duplicates. Preserve provenance, uncertainty, evidence gaps, status, gates, and next steps.
- **Update a page:** identify the correct vault and page/category first; preserve frontmatter, naming, links, index conventions, and append-only logs. If category is genuinely ambiguous, ask one focused decision question rather than writing to the default.
- **Lint / health-check:** follow the vault-specific lint and leak-scan instructions; report findings before fixing. Do not silently auto-fix.
- **After edits:** refresh only the selected vault's derived index using its documented command. Personal uses `/Users/brian/.hermes/scripts/gbrain_refresh_wiki.sh` or deliberate offline `gbrain import /Users/brian/Obsidian_Wikis/personal --no-embed`; Sandbox has an isolated rebuild tool documented in its `AGENTS.md`. Do not guess commands for RMS or All Square—read their local instructions/config first.

## Index and privacy boundaries

- Personal GBrain is the local `brian-wiki` layer under `~/.gbrain`; Sandbox uses an isolated layer under `~/.gbrain-layers/sandbox`. Keep company indexes and private source roots isolated.
- Never use a search result as the final answer without opening the source page. If the file on disk disagrees with an index, the file wins; refresh the selected index rather than editing index state directly.
- Do not copy private personal, company, client, financial, or credential-bearing material between vaults without explicit scope and page-level review.
- Cite durable claims with `[[WikiLinks]]`; preserve source dates and confidence rather than flattening them into unsupported assertions.

## Hard guardrails

- Never touch `.obsidian/`, `.trash/`, or Notion `*.base` files; never move files inside `Notion/`.
- Never read, print, copy, or expose credential/token/`.env`/OAuth contents, API keys, passwords, passport or ID numbers, or raw credential paths paired with contents. Do not hunt for secrets with GBrain search.
- Treat generated Drive/source-index directories as read-only unless the selected vault's sanctioned script explicitly regenerates them. Never hand-edit generated output.
- Do not commit or push without Brian's explicit approval. Before any commit touching generated wiki/Drive data, run the selected vault's mandatory leak scan.
- If a Drive/authentication step fails, report the error and stop; do not bypass access controls or invent a fallback identity.

If Brian is merely chatting or asking a generic question unrelated to the vaults, do not search them; wiki context is private and retrieval should be intentional.
