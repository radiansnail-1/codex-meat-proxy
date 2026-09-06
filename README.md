# Codex Meat Proxy 🥩🤖

> Battle-tested agent skills and operational protocols for OpenAI Codex and AI coding agents collaborating with a human operator.

Autonomous AI coding agents are extraordinarily capable, but real-world software engineering requires a human operator—the "meat proxy"—for sensitive access, product discernment, physical hardware, and high-stakes release gates.

**Codex Meat Proxy** is a curated, verified, and plug-and-play collection of **24 agent skills**. Each skill follows the official Codex / AI agent skill format (`SKILL.md` frontmatter, progressive references, and bounded agent delegation).

---

## Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/radiansnail-1/codex-meat-proxy.git
cd codex-meat-proxy
```

### 2. Install skills into Codex
Use the included installer to symlink or copy the skills directly into your local Codex directory (`~/.codex/skills`):

```bash
# Symlink skills (recommended for active updates)
./scripts/install.sh --link

# Or copy folders directly
./scripts/install.sh --copy
```

### 3. Validate
Run the bundled skill validator to ensure all skill frontmatter, schemas, and references conform to the specification:

```bash
python3 scripts/validate.py
```

### 4. Configure environment (Optional)
If your workflow uses external services (PostHog, RevenueCat, App Store Connect, or Neo4j):

```bash
cp .env.example .env
# Edit .env with your environment settings
```

---

## Skills Catalog

The 24 skills are organized into focused operational domains:

### 🏗️ Planning & Architecture
| Skill | Description | Primary Triggers |
|---|---|---|
| [`grilling`](skills/grilling) | Rigorous Socratic interview on plan design, edge cases, and architectural trade-offs before implementation. | "grill me", "interview me on this plan" |
| [`plan-ceo-review`](skills/plan-ceo-review) | Founder/CEO perspective plan review focused on product vision, user leverage, and non-linear leverage. | "ceo review", "founder review", "rethink problem" |
| [`plan-eng-review`](skills/plan-eng-review) | One-pass engineering review for correctness, regression risk, test strategy, and boundary conditions. | "eng review", "architecture review", "plan review" |

### ⚡ Execution & Delegation
| Skill | Description | Primary Triggers |
|---|---|---|
| [`spawn`](skills/spawn) | Safe, bounded delegation to autonomous subagents with separate context, clean tool scopes, and artifact verification. | `/spawn`, "delegate task", "spawn subagent" |
| [`handoff`](skills/handoff) | Generates crisp, resumable project checkpoints (`plan.md`, `learnings.md`) so work can pause and resume cleanly. | "create handoff", "checkpoint state" |
| [`handoff-pr-merge`](skills/handoff-pr-merge) | Publishes handoff checkpoints via a structured GitHub PR and authorized merge workflow. | "pr handoff", "publish handoff" |
| [`github-yeet`](skills/github-yeet) | Fast git staging, scoped commit, branch push, and draft PR flow with Windows Schannel fallback. | "yeet", "publish to github" |

### 🔍 Debugging, Auditing & Quality
| Skill | Description | Primary Triggers |
|---|---|---|
| [`investigate`](skills/investigate) | Evidence-led root cause debugging across source, dependencies, configuration, data, and services. | "investigate bug", "debug crash", "find root cause" |
| [`code-audit`](skills/code-audit) | Read-only correctness and security audit across integrations, dependencies, builds, and release boundaries. | "audit code", "security audit" |
| [`reliability-hardening`](skills/reliability-hardening) | Hardens code against concurrency races, idempotency issues, retries, and partial failure modes. | "harden code", "concurrency fix" |
| [`qa`](skills/qa) | Surface-level functional and UI QA testing across web and mobile platforms with concrete failure capture. | "run qa", "test ui flow" |
| [`hound`](skills/hound) | Relentless, automated metric-driven optimization and benchmark feedback loop. | "hound", "autoresearch", "optimize metric" |

### 📱 Mobile & Deployment Operations
| Skill | Description | Primary Triggers |
|---|---|---|
| [`app-store-connect-operations`](skills/app-store-connect-operations) | App Store Connect builds, TestFlight, pricing, screenshots, metadata, and release gates. | "testflight", "app store release", "submit review" |
| [`revenuecat-operations`](skills/revenuecat-operations) | In-app purchase, paywall, subscription, Web Purchase Link, and entitlement debugging. | "revenuecat", "verify entitlement", "paywall debug" |
| [`posthog-analytics`](skills/posthog-analytics) | Telemetry verification, event instrumentation, funnel debugging, and release behavior correlation. | "posthog query", "check events", "funnel telemetry" |
| [`mobile-app-attribution-operations`](skills/mobile-app-attribution-operations) | Mobile ad-SDKs, AppsFlyer, SKAN, ATT, deep-links, and revenue postback verification. | "attribution test", "appsflyer debug", "skan verify" |
| [`ios-debugger-agent`](skills/ios-debugger-agent) | iOS Simulator build, launch, inspection, UI driving, and log diagnosis with XcodeBuildMCP. | "debug ios simulator", "run in simulator" |
| [`ios-device-debugger`](skills/ios-device-debugger) | Physical connected iOS device debugging, installation, system log collection, and crash inspection. | "debug physical iphone", "device crash log" |
| [`deploy`](skills/deploy) | Multi-target deployment (Vercel, staging, production) with preflight checks and safety verification. | "deploy to vercel", "production deploy" |

### 🎨 Design & Polish
| Skill | Description | Primary Triggers |
|---|---|---|
| [`design`](skills/design) | Design system synthesis, visual exploration, component architecture, and UI implementation. | "design system", "visual exploration", "build ui" |
| [`design-qa`](skills/design-qa) | Visual inspection, typography, micro-interactions, layout polish, and premium feel audit. | "design qa", "visual polish", "review ui" |

### 🛠️ Codebase Intelligence & Utilities
| Skill | Description | Primary Triggers |
|---|---|---|
| [`graphify`](skills/graphify) | Extracts structural knowledge graphs of repos to provide instant AST, dependency, and concept lookup. | `/graphify`, "build knowledge graph" |
| [`text-output-cleaner`](skills/text-output-cleaner) | Strips hidden zero-width spaces, RTL overrides, and bad control characters without breaking markdown. | "clean text output", "strip zero-width" |
| [`trim`](skills/trim) | Audits agent instructions and skills for instruction bloat, circular rules, and conflicting triggers. | "trim skills", "audit instructions" |

---

## Upstream Lineage & Tracking

Several skills in this repository adapt ideas and patterns from the open-source agent ecosystem:

- **`grilling`**: Adapted from [mattpocock/skills](https://github.com/mattpocock/skills) with decision-frontier preservation.
- **`graphify`**: Packaged with [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) CLI and semantic retrieval.
- **`investigate`, `plan-ceo-review`, `plan-eng-review`**: Adapted from [garrytan/gstack](https://github.com/garrytan/gstack) into compact, standalone, protocol-driven skills.

All upstreams, licenses, and tracking notes are recorded in [`skill-upstreams.json`](skill-upstreams.json).

---

## Validation & Compatibility

All skills in this repository:
- Pass the standard skill schema validator (`quick_validate.py`).
- Use valid YAML frontmatter properties (`name`, `description`, `license`, `metadata`, `allowed-tools`).
- Have bounded, progressive references (loading deep details on demand rather than clogging agent context).
- Are fully decoupled from local filesystem paths or machine-specific usernames.

---

## License

Individual skills retain the licenses of their upstreams where applicable (MIT / Apache-2.0 as documented in [`skill-upstreams.json`](skill-upstreams.json)). The wrapper collection, installer, and synthesized skills are available under the [MIT License](LICENSE).
