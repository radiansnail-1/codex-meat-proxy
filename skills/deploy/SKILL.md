---
name: deploy
description: Deploy projects to production, preview, staging, or app/device targets with preflight checks, provider-specific publishing, live verification, rollback awareness, and honest blocked-state reporting. Use when asked to deploy, publish, ship, release, push live, update a live website/config/API, install a fresh device build, run a Vercel/Netlify/Fly/Render/cloud deploy, or verify whether a deploy actually went live.
---

# Deploy

## Core Rule

Treat deployment as complete only after the intended live target is verified. A provider URL, successful upload, green local build, or CLI command returning without error is not enough.

If any check is inconclusive, say the deploy is blocked or unverified. Do not alias, promote, or announce success for deployments whose provider status is failed, pending, unknown, inaccessible, or mismatched against the expected live output.

## Workflow

1. Identify the target, environment, and success condition.
   - Target examples: production website, preview URL, staging API, physical iPhone install, Android APK install, app-store build.
   - Success examples: live URL serves new config version, provider status is Ready, app installs and launches, health endpoint passes, app build appears in TestFlight.
   - If the user did not specify an environment, infer the safest likely target from project context and state the assumption.
   - Route App Store Connect metadata, build processing, TestFlight, review, and release-state work through `app-store-connect-operations`. For Expo/React Native, use the repository's declared EAS profiles/scripts and current first-party Expo documentation; preserve upload, submission, and release as separate gates.

2. Inspect project context before publishing.
   - Read local deploy docs, package scripts, provider config, previous handoff notes, and current git status.
   - Prefer existing project scripts over improvised deploy commands.
   - Note dirty worktree scope. Do not revert unrelated changes.
   - Check whether the deploy target depends on secrets, account selection, scope/team, branch, or local runtime version.

3. Run preflight verification.
   - Run the project's declared validation/build/test commands needed for this deploy.
   - For config-only or static-site deploys, run schema checks and targeted content scans.
   - For mobile installs, build the exact variant to be installed and confirm signing/device identity.
   - Stop before publishing if preflight fails unless the user explicitly asks to deploy despite failure.

4. Deploy with explicit target selection.
   - Use explicit provider scope/team/project flags when available.
   - Capture deployment IDs, inspect URLs, production/preview URLs, build logs, aliases, and provider status.
   - If a command hangs, inspect the provider status from a second command before deciding whether to wait, interrupt, or report blocked.

5. Verify the live target independently.
   - Fetch the public URL, API endpoint, config file, app install state, or provider status directly.
   - Compare against expected version, content, headers, health output, or app behavior.
   - Bypass or account for caches when relevant, but do not assume cache staleness explains a mismatch without evidence.

6. Report the result precisely.
   - Complete: provider status is good and live verification matches expected output.
   - Deployed but unverified: provider accepted/published, but live checks are missing or inconclusive.
   - Blocked: provider status failed/unknown/stuck, preflight failed, account/permission is missing, or live target still serves old content.
   - Include exact next action, not generic advice.

7. Update handoff only after deploy work if the user asks for handoff or the session state is important to preserve.
   - Use the handoff skill separately.
   - Record deployed URLs, provider status, verification commands, and blocked state.

## Vercel Guardrails

Use these checks for Vercel projects:

- Prefer the authenticated `vercel` MCP for read-only team/project/deployment/domain/log inspection and current provider documentation. Use the repository's Vercel CLI path for local builds and approved deployments; confirm the exact team/project before either route.
- Run project-local validation first.
- Use explicit scope/team when known: `--scope <team-or-account>`.
- Prefer project-local build commands or `vercel build --prod --scope <scope>` before `vercel deploy --prebuilt --prod --scope <scope>` when prior handoff/docs recommend prebuilt deployment.
- Inspect the returned deployment:

```bash
vercel inspect <deployment-url> --scope <scope>
vercel list <project> --prod --scope <scope>
```

- A Vercel deployment with `status UNKNOWN` is not successfully deployed. Do not alias it to the production domain.
- Verify the custom domain, not only the generated deployment URL:

```bash
curl -fsS https://example.com/path
```

- For public JSON/config deploys, compare the live response to local expected values and headers. If a project has a script like `check-mobile-config-live`, use it.

## Mobile Device Installs

For physical iOS or Android installs:

- Confirm the connected device identity before uninstalling or installing.
- If the user asks to clear data, uninstall the app/package before reinstalling.
- Build the exact configuration requested or implied by QA needs.
- Install with platform tools, then launch the app and report whether launch succeeded.
- Do not call it done if signing failed, install failed, the wrong bundle/package was installed, or launch was not attempted.

## App Store and TestFlight Boundary

- A local build/archive is not an upload; an accepted upload is not a processed build; a processed build is not attached/submitted/released.
- Treat local version fix, archive, upload, build attachment, TestFlight distribution, App Review submission, and public release as separate authorization gates unless the user's request explicitly combines them.
- "Fix the upload error" never authorizes upload. "Upload" never authorizes App Review submission or release.
- After an approved upload, verify the exact app/version/build appears and completes Apple processing. After submission or release, read back the durable App Store Connect state separately from public-storefront propagation.

## Failure Handling

When deploy fails or is stuck:

- Preserve the deployment ID/URL and provider status.
- Read logs/status if available.
- Do not retry endlessly without new information.
- Try the documented deploy path if an old handoff or project doc names one.
- Stop and report blocked when repeated attempts produce the same provider-side state.
- Leave any generated build output or evidence that may help debug unless it is clearly transient and safe to remove.

## Output

Keep the user-facing report short and factual:

- What was deployed or attempted.
- Exact live verification result.
- Any URLs or device IDs that matter.
- Whether the deploy is complete, unverified, or blocked.
- First concrete next step.
