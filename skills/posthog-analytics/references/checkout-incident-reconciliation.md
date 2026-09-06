# Checkout Incident Reconciliation

Use when purchase conversion appears to collapse around an app release. Separate telemetry facts, release identity, store reports, and code hypotheses so a low-intent cohort is not mislabeled as a checkout defect.

## 1. Lock identity and time

- Resolve and switch to the exact PostHog project; read the taxonomy again after switching.
- State project timezone and explicit calendar bounds.
- Discover events and exact property values before filtering.

## 2. Map releases from observed telemetry

Use the incident event's observed `$app_build`, `$app_version`, and platform values. Do not infer the cohort from an App Store marketing version, branch name, or one upload record.

## 3. Run four reconciliations

For the same daily window and build:

1. **Exposure:** distinct onboarding-complete or paywall-presented users.
2. **Outcome:** paywall result by outcome and placement.
3. **Lifecycle:** attempt-started -> presented -> purchase-started -> terminal result.
4. **Completion:** verified purchase-completed plus RevenueCat/store transaction evidence.

Keep daily values visible. Distinct users per interval may not equal unique people across the whole window.

## 4. Interpret conservatively

- `dismissed` may be user cancellation or sheet closure, not a technical failure.
- No `failed` rows does not prove checkout health if SDK callbacks collapse errors into dismissal.
- Purchase starts without completions remain inconclusive until callbacks and provider transactions are checked.
- Sparse lifecycle events may mean instrumentation shipped mid-window.
- Repeated hard-paywall dismissals may come from the same person; report events and distinct users separately.
- Validate breakdown properties on every event; missing values can silently omit series.

## 5. Reconcile source and deployment

- Use Git pickaxe search for event names to find when telemetry appeared.
- Inspect the source path mapping SDK results to purchased, pending, failed, and dismissed.
- Compare fix commit, archive/upload, first-seen telemetry, and exact build provenance.
- A commit before upload means likely included, not proven. Require exact provenance or a real-device sandbox transaction.

## 6. Keep store facts separate

- Exact first-time downloads come from App Store Connect, not PostHog.
- App-open/onboarding counts are proxies when store reports are unavailable.
- Never use PostHog alone to declare revenue loss or zero transactions; corroborate with RevenueCat/store records.

## 7. Evidence-grade conclusion

Report:

- confirmed telemetry;
- confirmed instrumentation limitation;
- authoritative provider/store evidence;
- root-cause status: proven, supported hypothesis, or unresolved;
- next verification: provider transactions, store report, replay, exception match, or sandbox purchase on the candidate build.
