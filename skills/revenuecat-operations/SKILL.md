---
name: revenuecat-operations
description: "RevenueCat configuration, entitlement, paywall, purchase, Web Purchase Link, and redemption debugging for subscription apps. Use when inspecting or changing native or web-to-app subscription configuration, customers, transactions, integrations, or store synchronization."
license: private
metadata:
  tags: [revenuecat, subscriptions, entitlements, offerings, paywalls, purchases]
  related_skills: [posthog-analytics, app-store-connect-operations, mobile-app-attribution-operations]
---

# RevenueCat Operations

Use the configured `revenuecat` MCP as the primary structured route. The local `asc` MCP also exposes a smaller read-only RevenueCat surface; treat it as a diagnostic fallback, not proof that every RevenueCat project is available.

## When to use

Use for:

- subscription and entitlement bugs;
- product, offering, package, and paywall configuration checks;
- customer purchase, renewal, refund, cancellation, expiration, or billing-issue investigations;
- RevenueCat analytics and monetization checks;
- App Store product synchronization and store-state debugging;
- Web Purchase Links, Redemption Links, success redirects, and web-to-app entitlement handoff;
- attribution identifier and server-side revenue delivery verification.

## Identity preflight

`140.6` and `Prayer First` are separate products. Before every operation:

1. List accessible RevenueCat projects.
2. Select the exact project and app/store target.
3. Record whether the target is production, sandbox, or both.
4. Resolve the app's bundle/package ID and store product identifiers from live data or source.
5. Distinguish product, package, offering, entitlement, paywall, customer, app user ID, and store transaction identifiers.

Do not infer that two apps share a project, offering, or entitlement. If the intended project is not visible, stop and report the access gap.

## Source-of-truth model

- **App Store / Play Store:** store product existence, availability, pricing, transaction receipt, review, and storefront state.
- **RevenueCat:** customer subscription lifecycle, entitlement evaluation, offerings/packages, integrations, and recognized subscription metrics.
- **PostHog:** behavioral funnel and UX telemetry.
- **MMP/ad platform:** acquisition attribution and campaign dimensions.

A PostHog purchase event is not a RevenueCat transaction. A configured RevenueCat product is not proof the store product is purchasable. An HTTP 200 or historical event is not proof the current build completed the flow.

## Read-first workflow

### 1. Connectivity and scope

- Confirm the RevenueCat MCP is authenticated.
- List projects and apps; select explicitly.
- If using the `asc` fallback, run `rc_connection_status` and treat returned scope as limited to the credentials configured there.

### 2. Reconstruct the configuration graph

Read, in order:

1. apps and store identities;
2. products and their store identifiers;
3. entitlements and attached products;
4. offerings and packages;
5. paywalls and targeting rules, when relevant;
6. webhook/integration state;
7. store-state and synchronization status.

Verify every link rather than assuming a product appearing in one list is attached everywhere it needs to be.

### 3. Diagnose customer state

For a named test customer or app user:

- resolve the exact customer without exposing identifiers;
- inspect active and historical subscriptions, entitlements, purchases, expiration, ownership, and store environment;
- check aliases/anonymous-to-identified transitions when account identity changed;
- compare event timestamps with the app session and provider receipt;
- distinguish stale cache/UI state from server-side entitlement state.

Never grant an entitlement to make a bug disappear unless Brian explicitly requests that exact customer mutation.

### 4. Reconcile purchase failures

Check four seams separately:

1. store product is available to the exact app, territory, and build;
2. SDK fetch returns the intended offering/package;
3. store transaction completes or returns a concrete error;
4. RevenueCat receives the transaction and evaluates the intended entitlement.

Then compare PostHog telemetry and source capture points. Missing `purchase_failed` telemetry is inconclusive until the purchase callbacks and RevenueCat customer/event history are checked.

### 5. Monetization analysis

Use RevenueCat overview metrics, charts, revenue metrics, subscriptions, and purchases for subscription truth. State currency, gross/net policy, date window, refund treatment, and sandbox exclusion. Use PostHog only for behavior around the paywall and conversion path.

## Attribution and integrations

For AppsFlyer or another MMP:

- obtain the MMP identifier only through the app's approved diagnostic path;
- attach it to the RevenueCat customer before the first purchase where the integration requires it;
- configure production and sandbox credentials separately;
- verify delivery from the customer's event history or integration delivery state;
- send monetary revenue from one authoritative server-side path; remove duplicate client-side revenue logging.

Do not print or persist raw device IDs, app user IDs, transaction IDs, keys, or customer identifiers in chat or skills.

## Web purchase and redemption

For Web Purchase Links, Redemption Links, callback URL schemes, or web-to-app onboarding, read [references/web-purchase-redemption.md](references/web-purchase-redemption.md). Treat the browser checkout, RevenueCat web app, native app, handoff service, and store app as distinct identities until verified. A successful web checkout or configured redirect does not prove that a fresh physical device redeemed the entitlement.

## Mutation gates

Explicit approval for the exact project/app is required before:

- creating, updating, attaching, detaching, archiving, or unarchiving products, entitlements, offerings, packages, paywalls, or virtual currencies;
- changing targeting rules, pricing, store state, webhook integrations, or project configuration;
- changing Web Purchase Links, Redemption Links, success redirects, callback configuration, or web-app settings;
- granting customer entitlements;
- publishing or unpublishing a paywall;
- submitting products to a store;
- starting, pausing, resuming, or stopping experiments.

Preview/dry-run when available. Set fields explicitly. After every approved write, read back the exact entity and verify its project, app, links, status, and user-visible effect.

## Verification report

Report:

- project, app, store, and environment verified;
- configuration graph checked;
- customer/provider evidence checked without identifiers;
- authoritative versus proxy evidence;
- exact mutation performed, if any, plus read-back state;
- remaining store, SDK, webhook, or access blocker.
