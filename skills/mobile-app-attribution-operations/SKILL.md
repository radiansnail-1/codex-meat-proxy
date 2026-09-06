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

A privacy-safe client event may record purchase outcome for UX analysis, but one server-side source owns money.

## ATT and aggregate attribution

- Do not add ATT merely to make attribution “work”; aggregate attribution may be sufficient.
- If ATT is approved, request contextually, honor denial, refresh identifiers after changes, update usage description/privacy manifest/store disclosures, and preserve opt-out/reset.
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

Do not authorize spend or optimize to purchase until this chain is green. Small launch budgets should normally optimize first for a reachable event such as install or a well-defined activation—not subscriptions without sufficient volume.

Use `references/expo-appsflyer-tiktok-revenuecat.md` for the current Expo/React Native pattern, and re-check its first-party links before implementation.

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
