# Live-device attribution verification

Use this runbook when proof depends on a physical phone, a current native build, and one or more provider dashboards. Its purpose is to prevent stale-build claims, wasted clean installs, identifier exposure, and evidence assembled from unrelated sessions.

## Bind the run identity

Record a non-secret run label and the exact:

- authoritative checkout, remote, branch, and commit;
- generated-native-project provenance;
- workspace/project, scheme, configuration, bundle ID, version, and build;
- built product path and installation time;
- physical device label, while keeping any machine identifier needed for control internal and out of reports;
- provider app/event-source records and test environment.

Do not claim that a build is installed merely because compilation succeeded. Confirm installation and launch on the selected physical device.

## Preflight access and control

Before uninstalling, resetting state, or emitting an event:

1. open each required provider view and determine whether its session is authenticated;
2. confirm the intended app/event source is visible;
3. determine whether the device flow contains long-presses, biometrics, permission prompts, QR scanning, account login, purchases, or another gesture the available controller cannot perform;
4. stage one concise user handoff for the unsupported interactions;
5. verify the approved diagnostic path can expose the needed identifier without placing it in screenshots or reports.

Do not repeatedly approximate an unsupported gesture. After one failed capability check, use another authorized control surface or ask for the smallest physical action needed.

## Compare identifiers without disclosure

- Obtain IDFV, IDFA, MMP UID, RevenueCat app-user/customer IDs, and similar values only through approved diagnostic or provider surfaces.
- Keep raw values in the narrowest in-memory scope available. Do not place them in shell arguments, command output, screenshots, source files, patches, checkpoints, or chat.
- Normalize and compare in-process. Report only presence, expected format, and boolean exact-match results.
- Clear a clipboard value after the comparison when the control surface permits it without risking unrelated clipboard contents.
- Treat adding or replacing a provider test-device record as an external, privacy-sensitive mutation. Request approval immediately before submission, then read back only the masked record or boolean match.

If the exact device is not registered, stop the evidence run before using the limited clean-install state or firing the milestone. Registration state is a prerequisite, not evidence of delivery.

## Establish one evidence window

Record the start time, time zone, run label, and app build before the cold launch. Use the same window for local diagnostics, MMP live events, ad-network test events, and downstream RevenueCat evidence.

Classify observations explicitly:

| Evidence class | What it proves |
|---|---|
| Static configuration | The inspected source or built artifact contains the expected non-secret configuration. |
| Local runtime | The selected installed build reached a lifecycle state or emitted a callback/event. |
| Provider receipt | The provider displayed the current run's session or event in the evidence window. |
| Downstream receipt | RevenueCat or an ad partner received the linked identifier or postback for the same run. |
| Historical/proxy | Context only; it does not prove the current run. |

Provider delay is not immediate failure. Use the provider's documented debug latency when known; otherwise poll at a modest interval for a bounded window, record the cutoff, and report `BLOCKED` or `FAIL` according to the observed evidence rather than waiting indefinitely.

## Execute the proof once

After preflight is green:

1. create the approved clean or data-preserving device state;
2. install and launch the attested build;
3. prove initialization, listener registration, readiness, and start ordering;
4. perform one genuine background-to-foreground cycle;
5. emit one property-free allowlisted milestone;
6. inspect local diagnostics for duplicate starts, unhandled rejections, or premature initialized flags;
7. check the MMP, RevenueCat bridge, and expected ad-network surfaces within the same evidence window;
8. verify prohibited automatic logging, revenue duplication, and competing SKAN ownership remain absent;
9. test opt-out or Product Reset, then re-enable/retry if that behavior is in scope.

Do not invent a direct provider event when the architecture intentionally sends none. Mark it `NOT EXPECTED` and identify the actual partner or server-side path.

## Leave a redacted checkpoint

When pausing or moving the run to another task, record:

- run label and source/build/device tuple without private identifiers;
- completed steps and timestamps;
- provider authentication state;
- exact-match booleans and evidence classes, never raw values;
- current app/device state and whether reinstalling would destroy useful evidence;
- outstanding user gesture, approval, provider delay, or access blocker;
- next single concrete action.

The checkpoint is resumability metadata, not proof. Reconfirm any external state that may have changed before continuing.
