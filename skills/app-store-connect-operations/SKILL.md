---
name: app-store-connect-operations
description: "App Store Connect build, metadata, pricing, screenshot, review, TestFlight, and release operations. Use when inspecting or changing iOS app versions, builds, localizations, in-app purchases, subscriptions, or release state."
license: private
metadata:
  author: "Codex Meat Proxy"
  version: "1.0.0"
  tags: [app-store-connect, ios, testflight, release, metadata, screenshots]
  related_skills: [deploy, qa, ios-debugger-agent, revenuecat-operations, mobile-app-attribution-operations]
---

# App Store Connect Operations

Use the configured `asc` MCP first for structured App Store Connect reads and supported writes. Use the installed iOS skills for simulator/debugging work and the repository's declared Expo/EAS path when applicable. Use the visible browser only when Apple exposes no structured route or requires user-controlled sign-in, MFA, agreements, or a UI-only release control.

## When to use

Use for:

- version/build inventory, processing state, TestFlight, and pre-release train errors;
- metadata, localization, keywords, screenshots, previews, pricing, IAPs, and subscriptions;
- attaching a build, creating a version, submitting for review, or checking release state;
- reconciling an approved build with the public storefront;
- diagnosing App Store upload or validation failures.

## Identity preflight

Before any read that drives a decision—and immediately before every mutation—verify:

1. Apple organization/account;
2. exact app name, App Store Connect app ID, bundle ID, and SKU;
3. platform, version, and build number;
4. environment and territory/storefront when relevant;
5. intended action: local build, upload, attach, submit, release, schedule, metadata-only, pricing, or product change.

Separate apps must remain strictly isolated. Never carry an app ID, build, localization, or product from one into the other.

## State model

Keep these gates separate:

1. source and version configuration;
2. local archive/build success;
3. upload accepted;
4. Apple processing complete;
5. build attached to a version;
6. metadata and compliance complete;
7. submitted for review;
8. approved / Ready for Distribution;
9. released / Ready for Sale;
10. public storefront propagated.

A successful archive is not an upload. An accepted upload is not a processed build. Approval is not release. The public listing is a cache/propagation surface and cannot identify which approved build is awaiting release.

## Structured workflow

### 1. Check connector and target

Run the local ASC self-test through the configured MCP environment when connector health is in doubt. Then use read tools such as `list_apps`, `get_app`, `list_app_store_versions`, `list_builds`, and relevant localization, screenshot, price, IAP, or subscription reads.

Do not use cancelled AppSprint services as a live connector. Imported AppSprint files are historical/local reference data only.

### 2. Diagnose upload/build errors from exact evidence

Read the complete Apple/Xcode error and map it to the exact source setting and uploaded state. Common classes:

- closed pre-release train or marketing version not greater than the approved version;
- duplicate build number;
- signing, entitlement, privacy manifest, architecture, symbol, or dSYM problems;
- metadata, compliance, export, or package validation failures.

Verify `CFBundleShortVersionString` and build number from the archive/build product, not only source config. Build the exact Release configuration again after a fix and require `BUILD SUCCEEDED`; old Xcode Issue Navigator rows are not fresh failures.

### 3. Prepare the mutation

Read the current entity first and send only intended fields. For replacement-style operations such as price schedules or screenshot order, include every row/item that must remain. Preview the target state and list any destructive consequence.

### 4. Approval gates

These are separate approvals unless the user's request explicitly includes them:

- local code/version fix;
- build/archive;
- upload to App Store Connect/TestFlight;
- attach build or change metadata/media/pricing;
- submit for review;
- release to the public App Store;
- paid Apple Ads changes.

Never treat “fix the upload error” as authorization to upload or submit. Never treat “upload” as authorization to submit or release.

### 5. Execute and verify

After an approved mutation:

- read the exact version/build/entity back;
- verify app, version/build, locale/territory, changed fields, and state;
- for uploads, wait for Apple processing and confirm the build appears;
- for submissions, confirm the review submission/state;
- for releases, confirm App Store Connect's durable released state separately from storefront propagation.

For browser-only actions, keep credentials, passkeys, MFA, CAPTCHA, agreements, and payment confirmation user-controlled.

## Metadata and media

- Preserve locale sets across app-info and version metadata when required.
- Validate keyword length and comma-separated formatting.
- Verify screenshot display type, dimensions, locale, count, checksums, and final order.
- Screenshot deletion and preview deletion are irreversible; require explicit approval for exact IDs/files.
- Label simulator/static renders separately from source-app and physical-device evidence.

## IAP, subscriptions, and pricing

- Verify store product IDs against source and RevenueCat before changes.
- Treat app, IAP, and subscription price schedules as replacement operations where the tool says so.
- Require explicit base territory, customer price/price-point IDs, effective dates, and retained rows.
- Read back App Store Connect and RevenueCat independently after changes.
- Product creation or submission is not proof the product is purchasable in every territory.

## Apple Ads boundary

The `asc` MCP also has Apple Ads reads and guarded dry-run write tools. Reads may diagnose delivery, bids, keywords, and ROAS. Any spend-affecting mutation requires exact campaign/ad-group/keyword identity, a reviewed dry run, explicit budget caps, and approval. Never enable spend from an App Store release request.

## Verification report

End with:

- target app/version/build and organization;
- pre-action state;
- local build/archive evidence;
- exact authorized action performed;
- durable App Store Connect read-back state;
- public storefront state separately;
- remaining processing, propagation, permission, or approval gate.

Use `references/release-state-checklist.md` for the compact release checklist.
