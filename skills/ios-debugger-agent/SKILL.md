---
name: ios-debugger-agent
description: "Build, launch, inspect, and debug iOS Simulator apps with XcodeBuildMCP. Use when reproducing iOS runtime behavior, capturing logs, driving simulator UI, or proving which source/build is installed."
license: private
metadata:
  tags: [ios, xcode, simulator, debugging, ui-automation, logs]
  related_skills: [investigate, qa, ios-device-debugger, app-store-connect-operations, mobile-app-attribution-operations]
---

# iOS Debugger Agent

Use the pinned `xcodebuildmcp` connector for simulator discovery, build/run, UI inspection, screenshots, and logs. This is a simulator-debugging skill, not App Store release authorization.

## When to use

Use for:

- building and launching the current iOS scheme on Simulator;
- reproducing runtime/UI bugs with a tight loop;
- inspecting accessibility/UI state and capturing evidence;
- collecting app logs and console output;
- proving which source, scheme, configuration, bundle, version, and build are installed.

For an attached physical iPhone or iPad, use `ios-device-debugger`. For App Store Connect, TestFlight, submission, or public release state, use `app-store-connect-operations`. For attribution or provider delivery, combine the relevant device skill with `mobile-app-attribution-operations`.

## Source and target preflight

Before building or interacting:

1. Confirm authoritative repository/checkout, Git remote, branch/worktree, and dirty state.
2. Read the nearest repository instructions.
3. Identify project versus workspace, exact scheme, build configuration, bundle ID, version/build, and generated-native-project provenance.
4. Use `list_sims` and select the exact simulator by ID. Do not infer identity from a familiar device name.
5. Record whether the requested proof is simulator-only, physical-device, TestFlight, or App Store. Simulator success does not prove the other surfaces.

A stale clone, portable drive, generated `ios/` tree, DerivedData product, existing simulator install, and physical-device build may contain different code. Bind every claim to one source/build/device tuple.

## Core workflow

### 1. Set explicit defaults

Use `session_set_defaults` with the current `projectPath` or `workspacePath`, scheme, simulator ID, and intended configuration. Do not rely on defaults left by another project or session.

### 2. Build a tight loop

Before a broad fix, identify the smallest reproducible sequence:

- focused build target or test;
- clean app launch state when needed;
- exact UI steps;
- expected UI/log/provider signal;
- one command or short tool sequence that can go red and green.

Use `build_run_sim` when a fresh build is required. If the build fails, read the complete current failure, repair only the proven cause, and rebuild the same configuration. Do not interpret stale Xcode issue rows as the latest build result.

### 3. Prove launch identity

After a successful build/run:

- use `describe_ui` or `screenshot` to prove the intended app launched;
- resolve the installed app path and bundle ID when identity is uncertain;
- capture version/build from the product or running app where available;
- distinguish “build succeeded” from “app launched” and “requested flow passed.”

### 4. Drive UI from structure

- Call `describe_ui` before tapping or typing.
- Prefer stable accessibility identifiers or labels over coordinates.
- Re-read UI state after navigation, layout change, keyboard presentation, or asynchronous loading.
- Use screenshots for visual evidence, not as the only functional assertion.
- Treat permission dialogs, ATT, sign-in, purchases, and destructive actions as separate user-visible gates.

### 5. Capture logs narrowly

Use simulator log capture for the exact bundle ID and reproduction window. Enable console capture only when needed. Summarize the relevant lines; do not dump secrets, tokens, device identifiers, customer identifiers, or unrelated personal data.

For external SDKs, correlate the same current run across:

1. local configuration present in the built artifact;
2. initialization/lifecycle logs;
3. exact safe test event or callback;
4. provider receipt;
5. downstream RevenueCat/PostHog/ad-platform state.

Initialization logs alone are not end-to-end proof.

## Safety and mutation boundaries

- Read-only discovery and inspection are preferred first.
- Building, installing, launching, resetting app state, tapping, typing, changing simulator permissions, and generating data are mutations; limit them to the user's requested test scope.
- Never perform a real purchase, submit a build, release an app, change provider dashboards, or launch paid spend from a simulator-debugging request.
- Do not uninstall or erase data unless the task explicitly requires a clean state; confirm the exact bundle and simulator first.
- Keep secrets in existing local build configuration. Never print or copy them into chat, logs, source, or skill files.

## Troubleshooting

- No simulator booted: report the exact state; boot one only when the requested task authorizes simulator execution.
- Wrong app/scheme: re-check session defaults, workspace/project, scheme, bundle ID, and installed app path.
- UI element missing: re-run `describe_ui` after layout/async changes; confirm the app is on the intended screen.
- Build works but provider sees nothing: use the external-integration seam ladder rather than rebuilding blindly.
- Generated native project is stale: establish how the repo regenerates it before editing; do not patch generated files that will be overwritten unless the project contract explicitly owns them.

## Verification report

Report:

- authoritative checkout/branch and source commit;
- workspace/project, scheme, configuration, simulator ID;
- app bundle/version/build;
- exact repro and tool sequence;
- build result, launch proof, UI/log evidence;
- provider evidence or explicit gap;
- files changed and tests run;
- simulator-only versus device/TestFlight/App Store boundaries.
