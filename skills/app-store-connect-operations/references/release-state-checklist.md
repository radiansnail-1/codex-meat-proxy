# App Store Connect release-state checklist

## Preflight

- [ ] Exact Apple organization and app identity verified.
- [ ] App Store Connect app ID, bundle ID, version, and build recorded.
- [ ] User's visual target, when any, matched against the candidate build's artwork/screenshots.
- [ ] Current state read from App Store Connect rather than inferred from the public listing.
- [ ] Release mode understood: upload, TestFlight, submit, release now, schedule, pre-order, territory/date change, or metadata-only.
- [ ] The exact stage is authorized; adjacent stages remain blocked unless explicitly included.
- [ ] User-controlled sign-in, passkey, MFA, CAPTCHA, agreements, and payment steps remain with the user.

## Action

1. Read the exact app/version/build immediately before mutation.
2. Re-check app identity, version/build, locale/territory, and state.
3. Execute only the approved stage through the structured ASC tool when available.
4. For replacement operations, include every row/item that must remain.
5. Do not report success from an accepted request or click alone.

## Verification

- Build/upload: exact build appears and finishes processing.
- Attach/TestFlight: exact build is attached/distributed to the intended target.
- Review: review submission and version state read back.
- Release: App Store Connect says Released/Ready for Sale or current equivalent.
- Public: exact App Store ID and relevant storefronts reflect the intended version/artwork after propagation.

Record App Store Connect state and public storefront state separately. If they disagree, report the propagation gap.
