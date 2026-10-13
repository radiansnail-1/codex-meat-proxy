# Expo + AppsFlyer + TikTok + RevenueCat pattern

Concrete reference for an Expo/React Native subscription app that already has product analytics and RevenueCat. Re-check current provider and Expo documentation before implementation; SDK APIs and dashboard labels change.

## Smallest coherent addition

When the app already has a privacy-gated analytics client, typed event allowlist, RevenueCat, and an Expo prebuild/native path:

1. one supported MMP SDK;
2. one attribution adapter mapping existing canonical events;
3. a RevenueCat identifier bridge;
4. provider-dashboard configuration;
5. SKAN/AdAttributionKit and privacy review;
6. fresh-install and sandbox-purchase verification.

## AppsFlyer + TikTok boundary

TikTok supports MMP-based app attribution. Re-check current first-party setup and event support:

- TikTok MMP overview: <https://ads.tiktok.com/resources/help/article/mobile-measurement-partner-mmp-tracking>
- AppsFlyer TikTok integration: <https://support.appsflyer.com/hc/en-us/articles/6722785184913-TikTok-for-Business-Advanced-SRN-integration-setup>
- TikTok AppsFlyer events: <https://ads.tiktok.com/help/article/list-of-supported-events-by-appsflyer>
- AppsFlyer React Native: <https://dev.appsflyer.com/hc/docs/rn_integration>

Verify the current integration identifier in first-party docs; do not reuse a deprecated identifier from old configuration.

## Code shape

- Add `react-native-appsflyer` through the project's package manager.
- Keep developer key, Apple numeric app ID, bundle ID, advertiser ID, and TikTok App ID distinct.
- Initialize in one native-safe adapter, not screen components.
- Require a native build; Expo Go cannot verify the SDK.
- Forward existing allowlisted milestones instead of adding network-specific calls throughout the app.

Truthful mapping example:

| Canonical milestone | Partner direction |
|---|---|
| install / first launch | automatic |
| onboarding complete | tutorial-complete standard event |
| first durable value | custom activation or honest supported event |
| paywall shown | content/offer view |
| trial begins | server-side from RevenueCat when supported |
| subscription begins | subscribe |
| purchase/revenue | server-side from RevenueCat |

Do not map onboarding to registration when no registration occurred.

## RevenueCat bridge

RevenueCat's AppsFlyer integration requires the AppsFlyer identifier and may use approved device identifiers to improve matching. Set identifiers after both SDKs are configured and before the first purchase. Configure production and sandbox credentials separately and verify delivery from customer/integration event history.

RevenueCat can send trial, purchase, renewal, refund, expiration, and billing-issue events server-side. Remove duplicate client-side monetary revenue logging.

Reference: <https://www.revenuecat.com/docs/integrations/attribution/appsflyer>

### Final campaign values and Meta restrictions

AppsFlyer SDK conversion callbacks may arrive before attribution is final. Do not persist provisional labels into RevenueCat's write-once campaign fields or fill blanks with Organic, Unknown or No Consent. Use permitted settled reports or an authenticated final-data feed; verify access, allowed fields/recipients and customer binding before implementing it. See [AppsFlyer's conversion-data limitations](https://support.appsflyer.com/hc/en-us/articles/4410481069969-Get-conversion-data-using-AppsFlyer-SDK-Overview).

Meta partner activation, Advanced data sharing, Advanced Matching and AMM agreement acceptance are separate settings and gates. Read the current [Meta integration requirements](https://support.appsflyer.com/hc/en-us/articles/207033826-Meta-Ads-integration-setup) and exact agreement before using its data. Acceptance does not retroactively unrestrict old installs or authorise exporting restricted measurement data to RevenueCat/PostHog user profiles. Review restrictions per recipient instead of assuming every campaign field can be forwarded.

Check the direct RevenueCat-to-Meta route against AppsFlyer-to-Meta purchase mappings before enabling the MMP. A received HTTP 200 or event count proves ingestion, not campaign matching or one-postback delivery. Prove those separately through one controlled campaign/install/purchase identity.


## TikTok dashboard sequence

1. Select the exact app event source.
2. Activate the current TikTok partner integration for the exact app in AppsFlyer.
3. Put advertiser ID and TikTok App ID in their own fields; URL query parameters are not app IDs.
4. Map only supported, truthful events.
5. Decide privacy mode and unattributed/organic postback policy.
6. Select and publish one SKAN/AdAttributionKit owner.
7. Attach the event source to the intended advertiser/campaign.

## ATT and privacy

Do not add ATT solely because an MMP was installed. If IDFA access is approved later, use the current Expo tracking-transparency module, add a contextual usage description, honor denial, refresh identifiers after changes, and update privacy disclosures and reset/opt-out behavior.

Health/body values, precise location, race identity/date, plans, free text, images, raw URLs, credentials, and support identifiers stay outside attribution properties.

## Complete proof

- fresh install observed in AppsFlyer;
- canonical activation event observed and mapped;
- RevenueCat customer has the AppsFlyer identifier;
- sandbox purchase produces one RevenueCat-to-AppsFlyer revenue event;
- TikTok receives the mapped postback;
- no duplicate revenue;
- currency and gross/net policy match;
- existing-user update and opt-out/reset paths pass.

Configuration screenshots alone are not transaction evidence and do not authorize spend.
