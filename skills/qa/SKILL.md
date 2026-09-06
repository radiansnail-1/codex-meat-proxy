---
name: qa
description: "Surface-level QA for web and mobile apps plus light code-quality QA routing: drive browser/device flows, reproduce issues, capture screenshots/logs/DOM/UI-tree evidence, classify bugs/design/product/code-quality issues, apply a minimal simplification lens to code smells, document repro steps, and verify fixes across relevant viewports/devices. Use when the user asks to test, QA, inspect, click/tap through, reproduce, verify a local or deployed app UI, or perform code QA connected to user-facing app behavior."
---

# QA

## Role

Own the user-facing test surface. Drive the app like a user, capture evidence, classify issues, and verify final behavior.

Route work that belongs elsewhere:

- Source root-cause or non-trivial fixes -> `investigate`. QA may reproduce first and verify after. Only make a tiny local fix when the user explicitly asks QA to do it and the root cause is obvious.
- Visual polish or design critique/fixes -> `design-qa` when available.
- Launch, deploy, security, or production preflight -> `deploy` when available.
- Subagents -> use subagents (Agent tool in Claude Code; `spawn` skill in Codex) only when the user explicitly asks or parallel independent passes are clearly useful.
- Android/iOS platform debugging -> use the relevant platform tooling; for iOS Simulator build/run/log work, use `ios-debugger-agent`.
- Mobile attribution, ad SDK, SKAN/ATT, or revenue-postback verification -> `mobile-app-attribution-operations`; require a current native build, fresh device/session evidence, and provider receipt rather than initialization logs alone.
- App Store Connect build processing, metadata, TestFlight, review, or release state -> `app-store-connect-operations`; keep build, upload, submission, and public release as separate gates.
- PostHog telemetry or RevenueCat subscription truth -> `posthog-analytics` or `revenuecat-operations`; QA may reproduce the user flow, but provider data owns the external state.
- Read-only implementation correctness or regression audit -> `code-audit`.
- Proven durability, idempotency, concurrency, adapter, persistence, or adversarial-input hardening -> `reliability-hardening`.
- Pure code QA: over-engineering/bloat -> the harness code-review skill (`/code-review` in Claude Code; `ponytail:ponytail-review` in Codex), cleanup -> `/simplify` in Claude Code; root-cause debugging or non-trivial fixes -> `investigate`; architecture/plan review -> `plan-eng-review` when available; measurable optimization loops -> `hound` when available.

## Inputs

Extract the target URL or app launch command, scope, user-provided repro steps, auth/session needs, expected surface, and required devices/viewports. If scope is vague, test the main path a real user would hit first.

Default web viewports: desktop `1440x900`, laptop `1280x720`, mobile `390x844`. For mobile apps, use portrait and landscape when practical.

## Surface Selection

For web QA, prefer the harness in-app browser (Claude Browser Use in Claude Code; the Codex in-app browser in Codex — there, read `browser:control-in-app-browser` before the first browser action when available). If it is unavailable or blocked, use the strongest available fallback such as Playwright, another browser surface, screenshots, console output, DOM inspection, or static checks, and state the verification gap clearly.

Detect mobile apps before defaulting to web:

- React Native / Expo: `react-native`, `expo`, or Expo config.
- Flutter: `pubspec.yaml`.
- Capacitor / Ionic: `capacitor.config.*` or `ionic.config.json`.
- Native: `android/` or `ios/` platform projects.

For mobile apps, prefer a real attached device, then an emulator/simulator, then static/build checks. Use `adb devices` for Android availability. For iOS-only projects, check the platform before declaring device QA impossible:

- On macOS: discover simulators through `ios-debugger-agent`/XcodeBuildMCP first; if a simulator is booted or bootable, build and drive the app there instead of falling back.
- On Windows: iOS device/simulator QA is not possible from this machine. Fall back to responsive browser emulation, and run whatever subset is doable (lint, typecheck, unit tests, web preview if available).

Do not imply physical iOS QA is possible without macOS, Xcode provisioning, and enabled device tooling.

## Workflow

1. Inspect enough repo context to identify framework, package manager, scripts, dev URL, and likely source areas.
2. Check `git status` before any allowed edit; preserve unrelated user changes.
3. Start or reuse the dev server, build, simulator, or device install using the project's standard command.
4. Open the target surface and capture baseline evidence: screenshot plus DOM, UI tree, console, device logs, or visible state when useful.
5. Exercise real user flows: navigation, forms, auth, primary actions, back behavior, search/filter/sort, settings, empty/loading/error states, permissions, and supplied repro steps.
6. Repeat critical flows on the required viewports/devices unless the user narrows coverage.
7. Record each issue with surface/device, URL/screen, viewport/orientation, screenshot path or capture reference, repro steps, visible symptom, and any useful log/DOM/UI-tree clue.
8. Route out-of-scope work to the right skill, then return to QA for verification. For SDK/provider flows, record the exact app/version/build and compare the same test session across device logs, PostHog, RevenueCat/MMP, and store/provider state.

Prioritize blocked user flows, crashes, console-visible failures, broken navigation, failing forms, auth problems, layout overlap, unreadable text, and mobile regressions before cosmetic polish.

## Code QA And Simplification Routing

When QA exposes code-quality issues, inspect only enough source to classify the
risk and support the finding. Apply a small simplification lens:

1. Does this code need to exist?
2. Does existing project code already cover it?
3. Can standard library or native platform behavior cover it?
4. Can an already-installed dependency cover it?
5. Can this be a smaller diff with fewer files?

Surface code-quality issues with file paths, symptoms, and likely user impact.
Do not refactor inside QA unless the user explicitly asks and the fix is tiny,
obvious, and can be verified through the failing user flow.

Route pure code QA as follows:

- Over-engineering, bloat, duplication, dead flexibility -> the harness code-review skill (`/code-review` in Claude Code; `ponytail:ponytail-review` in Codex); cleanup -> `/simplify` in Claude Code.
- Correctness, regression, integration, or release-artifact audit without edits -> `code-audit`.
- Implementation hardening after root cause is proven -> `reliability-hardening`.
- Root-cause debugging or non-trivial fixes -> `investigate`.
- Architecture or implementation-plan review -> `plan-eng-review` when available.
- Measurable optimization loops -> `hound` when available.

## Classification

- Bugs: functional breakage, crashes, broken navigation, failing forms, state corruption, network/auth failures, mobile regressions, or layout that blocks a task. Reproduce, document, and verify. Route source fixes to `investigate` unless the user explicitly requested a tiny QA-local fix.
- Design issues: spacing, hierarchy, alignment, typography, contrast, clutter, awkward empty states, weak affordances, microcopy, or motion quality. Surface with evidence and route fixes to `design-qa` when available.
- Product issues: confusing flow order, missing obvious affordances, bad defaults, misleading labels, redundant screens, or behavior that works but does not make sense. Surface with evidence and a suggested decision.
- Code-quality issues: smells noticed while inspecting for QA, such as bloated files, duplication, dead code, suspicious `any`, unused exports, or commented-out scaffolding. Surface and route; do not refactor inside QA unless the tiny-fix rule above applies.

When unsure: task blocked -> bug; product feels worse -> design issue; product is confusing despite working -> product issue; future maintenance is worse -> code-quality issue.

## Verification And Report

After a fix or routed change, re-test the failing flow on the failing surface, then check the other required viewports/devices for regressions when practical.

End with:

- Bugs found, grouped by verified-fixed, best-effort, deferred, and not reproducible.
- Design, product, and code-quality issues surfaced, with evidence.
- Repro steps and evidence links/paths for meaningful issues.
- Files changed, if any, and commit hashes only when the user requested commits.
- Desktop, laptop, mobile web, Android, and iOS verification status as applicable.
- Tests/checks run and remaining verification gaps.
