---
name: ios-device-debugger
description: "Build, install, launch, inspect, and debug apps on an attached physical iPhone or iPad. Use when device-only SDKs, identifiers, permissions, hardware behavior, or release-build behavior cannot be proven in Simulator; do not use for App Store submission."
license: private
metadata:
  tags: [ios, iphone, ipad, physical-device, devicectl, debugging, logs, mirroring]
  related_skills: [ios-debugger-agent, mobile-app-attribution-operations, qa, app-store-connect-operations]
---

# iOS Device Debugger

Build and verify one attested app build on one exact attached physical iOS device. Keep device-only proof separate from Simulator, TestFlight, and App Store evidence.

## When to use

Use for:

- installing and launching a development, ad hoc, or locally signed release build on an attached device;
- reproducing physical-device-only SDK, lifecycle, notification, camera, sensor, identifier, deep-link, or performance behavior;
- capturing a narrow device log window;
- driving an app through iPhone Mirroring or another approved control surface;
- proving which source and build are installed on the device.

Use `ios-debugger-agent` for Simulator-first work. Use `app-store-connect-operations` for TestFlight, submission, or release state. Combine with the relevant domain skill for attribution, purchases, analytics, or another external provider.

## Attest source, build, and device

Before building or interacting:

1. confirm the authoritative checkout, remote, branch, commit, dirty state, and nearest repository instructions;
2. identify the workspace/project, scheme, configuration, signing target, bundle ID, version/build, and generated-native-project provenance;
3. enumerate attached devices with the available structured tool or `xcrun devicectl list devices`, parse the result without echoing private identifiers, and select the exact record;
4. determine whether the requested proof requires a clean install, preserved app data, or merely a relaunch;
5. record the built product path and installation time without exposing signing or device identifiers.

A successful compile, a product in DerivedData, and an existing device installation are three different states. Bind claims to one source commit, native build, installed bundle, and physical device.

Prefer a structured device tool. When a command returns private machine identifiers, process the result in the narrowest local scope and emit only safe fields such as device name, platform version, connection state, and the boolean identity checks needed for the task.

## Preserve or reset state deliberately

- Default to preserving device data unless the requested proof requires first-install state.
- Before uninstalling, confirm the exact bundle and explain what useful test state will be lost.
- A request for a clean-install test authorizes resetting only the scoped app on the selected device, not erasing the device or unrelated apps.
- Reinstall only when it changes the evidence. Avoid repeated clean installs while provider access, device registration, or a required user gesture is still blocked.

## Build, install, and launch

Use the repository's established build command when one exists. Otherwise use explicit Xcode settings for the attested workspace/project, scheme, configuration, and device destination.

After building:

1. resolve the actual `.app` product;
2. install it on the selected device using the structured device tool or `xcrun devicectl device install app`;
3. launch the exact bundle ID and terminate an older process when the test requires it;
4. confirm the expected app UI is visible;
5. capture the installed/running version and build where available.

Do not infer installed-build identity from the app icon or project name alone.

## Preflight the control surface

Before a long UI sequence, determine whether automation can perform every required interaction. Pay special attention to:

- press-and-hold or multi-touch gestures;
- biometrics, passcode, trust, and permission dialogs;
- QR scanning, camera capture, hardware buttons, and backgrounding;
- account login, CAPTCHA, and browser-to-app switching;
- clipboard transfer containing sensitive values;
- purchase confirmation.

Prefer accessibility labels and structural inspection when available. With coordinate-only mirroring, re-read the visible state after navigation, keyboard changes, scrolling, or asynchronous loading.

After one failed capability check, do not keep approximating an unsupported gesture. Stage the app at the correct screen and ask the user for one precise physical action, then resume from the resulting state.

## Capture evidence narrowly

Define the reproduction window before launch. Collect only the logs and screenshots needed for the exact bundle and interval.

For each claim, separate:

- build/install success;
- app launch and visible state;
- local lifecycle, callback, or diagnostic evidence;
- external provider receipt;
- historical or proxy evidence.

Initialization logs do not prove provider delivery. A provider dashboard does not prove which local build emitted an event unless timestamps and run identity align.

## Sensitive identifiers

- Never print or persist device UDIDs, IDFV/IDFA values, SDK keys, tokens, diagnostic passwords, customer IDs, or transaction IDs.
- Keep raw values in the narrowest in-memory scope and report only presence, format validity, or boolean comparisons.
- Do not place secrets in shell arguments, filenames, screenshots, patches, task checkpoints, or final reports.
- Treat registering a device identifier with an external provider as a separate privacy-sensitive mutation requiring explicit approval immediately before submission.

## Safety boundaries

- Building, installing, launching, backgrounding, tapping, typing, changing app permissions, and generating test data are limited to the requested device test.
- Do not perform a real purchase, change provider configuration, upload a build, publish to TestFlight, submit to App Review, release publicly, or erase the device without explicit authorization for that action.
- Preserve unrelated owner work and existing device data.
- If signing, trust, device lock, authentication, or a physical gesture blocks progress, report the exact smallest user action needed.

## Completion report

Report:

- authoritative checkout, commit, workspace/project, scheme, and configuration;
- selected physical device in non-sensitive terms;
- bundle, version/build, product path, installation, and launch result;
- whether app data was preserved or reset;
- exact reproduction sequence and evidence window;
- local runtime and external provider evidence as separate claims;
- user-assisted interactions and why they were necessary;
- files changed and focused checks run;
- remaining physical-device, TestFlight, or App Store uncertainty.
