## Mobile and generated-build audits

- Verify canonical checkout and generated native-project provenance.
- Reconcile app config, native project settings, Info.plist/manifest, extensions/widgets, signing target, marketing version, and build number.
- Bind simulator/device evidence to the exact source commit and artifact.
- Separate local build, upload, provider processing, TestFlight/App Store state, and public-storefront state.
- Treat stale Xcode issue rows and historical provider counters as non-current evidence.

## Analytics, attribution, and subscription audits

- Trace event emission and semantics in source before accepting dashboard labels.
- Verify order, duplicate guards, identity/session fields, app version/build, placement, and taxonomy generation.
- For checkout, inspect one attempt identifier, callback-specific lifecycle events, retry properties, once-guards, and entitlement confirmation before completion.
- Keep PostHog behavior, MMP attribution, RevenueCat/store revenue, and ad-platform delivery as separate authorities.
- An organic sandbox purchase proves only the observed app-to-billing/MMP path; it does not prove partner-attributed install or ad-network receipt.

