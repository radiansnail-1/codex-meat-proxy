# RevenueCat web purchase and app redemption

Use this reference for a subscription flow that begins on the web and is expected to produce an entitlement in a native app.

## Reconstruct the identity graph

Resolve these independently before editing anything:

- RevenueCat project;
- native iOS/Android app record and bundle/package ID;
- RevenueCat web app record and its generated identifier;
- entitlement, offering, package, and store product;
- Web Purchase Link for each plan;
- Redemption Link behavior;
- success redirect origin and path;
- native callback URL scheme or universal link;
- handoff seal/unseal endpoints and deployment environment.

Do not assume a callback scheme belongs to the native app because it resembles a previous value. Inspect the live RevenueCat field and current documentation. If RevenueCat generates the scheme from the web-app identity and the field is read-only, record that as an invariant and change the native registration only when the user authorizes the required app change.

## Verify plan links independently

For every visible plan:

1. resolve the exact package and product;
2. inspect the complete generated Web Purchase Link, including package selection and success behavior;
3. verify runtime configuration preserves defaults for plans that are not overridden;
4. confirm displayed price and billing period agree with the store/RevenueCat source of truth;
5. keep production and sandbox paths distinct.

Do not treat one working annual link as proof that weekly or another plan survived configuration merging.

## Trace the complete handoff

Model the flow as separate seams:

```text
website plan selection
  -> RevenueCat web checkout
  -> successful web purchase
  -> Redemption Link or handoff payload
  -> configured success redirect
  -> native callback/universal link
  -> RevenueCat customer reconciliation
  -> native entitlement refresh
```

At each seam, distinguish configuration from a current transaction receipt. Preserve anonymous-to-identified alias behavior and do not expose customer, transaction, or redemption identifiers.

If the site uses a signed handoff:

- verify the deployed secret exists without displaying it;
- verify seal and unseal use compatible schemas and expiry rules;
- allow only intended origins and methods;
- test canonical and preview origins separately when both are supported;
- ensure CORS failures do not get misreported as checkout failures.

## Deployment boundary

Before promoting a web-to-app change:

- prove serverless functions include their complete runtime dependency closure;
- test the deployed preview rather than relying only on a local server;
- read deployment logs for function-load or module-resolution failures;
- preserve the last known-good production deployment and know the rollback target;
- verify DNS/custom-domain attachment separately from application routing;
- keep public CTAs and temporary redirects unchanged when the repository has a dormant-funnel or activation gate.

A passing static test, successful Vercel build, or browser redirect does not prove that the serverless function loaded or the native app redeemed an entitlement.

## Activation proof

Before declaring the funnel ready, require evidence for:

| Surface | Required proof |
|---|---|
| RevenueCat | Production links for every offered plan, Redemption Link behavior, and success redirect verified. |
| Deployment | Correct environment secrets, CORS, function loading, and intended domain routing. |
| Native app | Current build registers the exact callback mechanism and handles the payload safely. |
| Physical device | Fresh-device cases complete through entitlement refresh without a real charge unless explicitly authorized. |
| Safety | Existing public download flow remains available until every project-specific gate and owner approval is satisfied. |

Use sandbox or no-charge evidence where possible. Never trigger a real purchase merely to complete verification without explicit authorization immediately before the transaction.

Report which seam is `PASS`, `FAIL`, `BLOCKED`, or `NOT TESTED`, the evidence for that seam, and the next concrete action. Do not collapse partial browser success into end-to-end readiness.
