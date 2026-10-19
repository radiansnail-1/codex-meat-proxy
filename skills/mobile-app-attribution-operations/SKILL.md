---
name: mobile-app-attribution-operations
description: "Mobile attribution, ad-SDK, SKAN, ATT, deep-link, and revenue-postback implementation and live-device verification. Use when adding, auditing, or proving AppsFlyer, TikTok, Meta, Apple Ads, or another mobile acquisition integration."
license: private
metadata:
  tags: [mobile, attribution, appsflyer, tiktok, meta, skan, att, revenuecat]
  related_skills: [investigate, qa, ios-debugger-agent, ios-device-debugger, posthog-analytics, revenuecat-operations, app-store-connect-operations]
---

# Mobile App Attribution Operations

Design, implement, and verify paid mobile acquisition without confusing product analytics, MMP attribution, ad-platform reporting, RevenueCat subscription truth, or Apple privacy mechanisms.

## When to use

Use for:

- AppsFlyer, Adjust, Branch, Singular, Kochava, TikTok, Meta, Apple Ads, or Google Ads mobile integration;
- missing installs, app events, campaign dimensions, subscriptions, or revenue postbacks;
- SDK lifecycle, IDFV/IDFA, deep-link, ATT, SKAN, or AdAttributionKit debugging;
- verifying a fresh build end to end before paid spend.

## Establish the authoritative source and build

Before editing or testing:

1. Confirm the authoritative repository/checkout, remote, branch, and clean worktree. A portable, archived, or stale checkout is not automatically the source of the installed build.
2. Record bundle/package ID, numeric store ID, app/version/build, platform, native-build path, and signing target.
3. Inventory existing analytics, RevenueCat, MMP, ad SDKs, event allowlist, privacy manifest, store disclosures, deep links, and consent/reset behavior.
4. Resolve advertiser, business, app/event-source, MMP, RevenueCat, and store identifiers as distinct fields.
5. Never print or persist SDK keys, tokens, IDFV/IDFA values, customer IDs, transaction IDs, or device identifiers.

For a physical-device proof run, read [references/live-device-verification.md](references/live-device-verification.md) before operating the device or provider dashboards.

## Choose one coherent architecture

Default:

```text
Ad networks -> one MMP -> attribution and campaign dimensions
                     -> PostHog for product behavior
RevenueCat -> server-side lifecycle and revenue events -> MMP/ad network
Apple/Google privacy attribution -> aggregate measurement
```

- Keep one MMP as attribution authority.
- Keep PostHog as product-behavior analytics.
- Keep RevenueCat/store receipts as subscription and revenue truth.
- Choose exactly one SKAN/AdAttributionKit conversion-value owner.
- Do not add several SDKs that all claim installs, purchases, or revenue without a documented hybrid design.

## Freeze a privacy-safe event contract

Map existing canonical app milestones; do not invent a second vocabulary at call sites.

A typical subscription funnel:

1. install / first launch;
2. onboarding/tutorial complete;
3. one genuine activation milestone;
4. paywall/offer view;
5. trial start;
6. subscription/purchase;
7. renewal, cancellation, refund, expiration, and billing issue from RevenueCat.

Use standard partner events only when semantically true. Do not map onboarding to registration if no registration occurred. Never send health/body data, precise location, race identity/date, plans, free text, images, raw URLs, credentials, or support identifiers through attribution properties.

## Implement behind one adapter

One attribution module should own:

- native-safe initialization and environment configuration;
- lifecycle start/stop/foreground behavior;
- install-conversion and deep-link callbacks;
- canonical event mapping;
- consent and sharing controls;
- production-disabled diagnostic logging;
- reset/opt-out behavior;
- forwarding the MMP identifier to RevenueCat.

Avoid screen-level SDK calls. Preserve existing analytics code. A native development/release build is required; Expo Go is not verification.

## Debug lifecycle with a tight loop

For initialization or delivery bugs, prove each seam:

1. current build contains non-secret configuration;
2. initialization/listener/start ordering is deterministic;
3. cold start and background -> foreground produce the intended session behavior without duplicate starts;
4. failures do not create unhandled rejections or silently mark initialization complete;
5. the exact test device is registered through the provider's approved diagnostic flow;
6. a safe allowlisted event appears in live/debug evidence for the current build.

Historical counters, dashboard configuration, HTTP 200s from an older build, or SDK initialization logs do not prove current end-to-end delivery.

Check provider authentication, device-registration state, and automation limitations before spending a fresh install or emitting the test event. Bind every runtime claim to one source commit, native build, installed app, physical device, and evidence window.

## RevenueCat bridge

After both SDKs are configured:

1. obtain the MMP stable identifier without displaying it;
2. attach it to the RevenueCat customer before the first purchase where required;
3. collect only identifiers allowed by policy and consent;
4. configure production and sandbox integrations separately;
5. map trial, purchase, renewal, refund/cancellation, expiration, and billing issue;
6. remove duplicate client-side monetary revenue logging.

A privacy-safe client event may record purchase outcome for UX analysis, but one server-side source owns money. Check complete routes per destination: direct RevenueCat-to-network delivery plus RevenueCat-to-MMP-to-network forwarding can duplicate the same purchase even when RevenueCat owns both routes. Retain one monetary route to each destination.

Recheck the current RevenueCat customer across asynchronous identifier writes and confirm the attribute sync succeeds before claiming the purchase bridge is ready. Failed syncs must remain retryable. Missing or restricted acquisition data stays unknown; it does not establish organic acquisition.

## ATT and aggregate attribution

- Do not add ATT merely to make attribution “work”; aggregate attribution may be sufficient.
- If ATT is approved, request contextually, honor denial, refresh identifiers after changes, update usage description/privacy manifest/store disclosures, and preserve opt-out/reset.
- Record identified tracking and anonymous aggregate reporting separately. ATT denial does not establish that aggregate reporting must stop; verify the approved consent behavior and the aggregate paid-event path independently.
- Re-check current Apple and provider documentation before release; SKAN/AdAttributionKit behavior and partner requirements change.

## Dashboard configuration is a separate gate

Verify the exact:

- app record, store ID, and bundle/package ID;
- advertiser and app/event-source connection;
- current partner integration generation;
- truthful event mappings;
- attribution windows and privacy mode;
- SKAN/AdAttributionKit schema owner and publication;
- RevenueCat production/sandbox credentials;
- deep links when required by the campaign.

Separate sandbox/debug receipts from production event eligibility. A received test purchase proves that test route, not that Purchase is selectable for production optimization; do not promise that one real purchase will unlock it.

Eligibility is time-sensitive and specific to an event/objective pair. Before launch, re-read that exact live eligibility row and diagnostic; an older eligible snapshot, a saved event label or text typed into a picker does not prove current eligibility. Distinguish a selectable option from a disabled result, then verify publication succeeds for the ad set and ads before reporting that the goal can run.

Keep delivery, acceptance, qualification and attribution counts separate. A server integration's Sent status or HTTP200 does not establish how many events the ad platform processed, deduplicated or qualified for optimisation. Compare matched time zones, delivery/event dates, event types, unique events and response acceptance fields where available. A count mismatch alone does not prove lost events or justify changing consent flags, adding duplicate SDK events or inventing a volume threshold.

When the request is to enable measurement, implemented-but-disabled is incomplete. Before submitting the release, verify the non-secret activation markers and fixed cutover in the signed artifact against the published provider decoder. A passing build or a declined device test does not establish activation. If activation remains blocked, explain what is inactive and why before proceeding with any separately authorized partial release.

Apple aggregate conversion updates and Meta AEM eligibility are separate gates. Read the exact eligibility diagnostic; do not promise that a SKAN mapping change clears an ATE-volume requirement or alter consent flags to make it pass.

Code completion does not authorize provider configuration, campaign launch, or spend.

## End-to-end proof

Using a fresh test identity/device state where possible:

1. authenticate the required provider views and confirm the exact device is registered;
2. install from a controlled attribution test flow;
3. confirm install/session in the MMP;
4. complete onboarding and activation;
5. verify the mapped product events in PostHog and the MMP;
6. view the paywall and perform an explicitly approved sandbox purchase;
7. verify RevenueCat customer attributes contain the MMP identifier;
8. verify one server-side revenue event reaches the MMP;
9. verify the ad platform receives the mapped postback;
10. compare timestamps, currency, gross/net policy, install date, and campaign dimensions;
11. test opt-out/reset and an existing-user upgrade path.

Gate the selected optimization goal on its own evidence. Do not optimize to purchase until production event eligibility and the paid transaction/postback path are verified. If the user explicitly chooses a bounded install or activation campaign while the paid path remains unresolved, verify that selected goal and disclose the remaining paid-measurement gap; do not silently substitute objectives or report the paid path fixed.

Use `references/expo-appsflyer-tiktok-revenuecat.md` for the current Expo/React Native pattern, and re-check its first-party links before implementation.

## Campaign performance review

- If the user requests a pause, publish and verify Off on the exact campaign before analyzing results. Do not resume it while debugging without authorization.
- Reconcile ad-network spend/results, the MMP's normal and aggregate attribution views, and receipt-based subscription revenue separately. Confirm the selected app/campaign, currency, time zone and each reporting window; shared dashboards can retain another app's filter.
- Blank install results are not verified zero installs. SKAN cutoffs can lag; do not add normal and aggregate counts without verified deduplication. Label cost per reported install by its measurement basis rather than presenting it as complete acquisition cost.
- Missing postback copies, null conversion values and volume/rate diagnostics are observations, not a proven payload or source-code defect. Check the provider's current diagnostic definition before changing consent flags, event parameters or the SDK.

## Campaign launch and handoff

- Verify the account currency, daily-budget average and any displayed daily/weekly maximums. A daily average is not a hard daily cap.
- Match the minimum OS targeting to the current store requirement; a privacy campaign label such as iOS 14+ is not proof of app compatibility.
- Preview the saved creative with the current Facebook/Instagram identities. After a user stops launch for branding changes, keep the campaign paused until they authorize resuming.
- Read back campaign, ad-set and ad switches plus delivery status. Published, Processing, In review, Active and measured delivery are distinct states; an approval notification alone is not delivery proof.

## Completion report

Report each provider separately:

- code/config state;
- current build identity;
- live device/session evidence;
- event and RevenueCat delivery evidence;
- dashboard mapping state;
- privacy/ATT/SKAN state;
- evidence class and current-run timestamp for each claim;
- what remains unverified;
- whether spend is still blocked.

When the run pauses or moves to another task, leave the redacted checkpoint defined in the live-device reference. Do not put identifiers or secrets in the checkpoint.
