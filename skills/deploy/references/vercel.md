## Vercel Guardrails

Use these checks for Vercel projects:

- Prefer the authenticated `vercel` MCP for read-only team/project/deployment/domain/log inspection and current provider documentation. Use the repository's Vercel CLI path for local builds and approved deployments; confirm the exact team/project before either route.
- Run project-local validation first.
- Use explicit scope/team when known: `--scope <team-or-account>`.
- For `vercel curl`, check the installed CLI's help and verify the checkout's linked team/project first. Some versions forward `--scope` and `--non-interactive` to native curl, causing failures. Use the supported `vercel curl /path --deployment <id> -- <curl-options>` form in that verified checkout; do not silently relink another project.
- Before adding upload exclusions, inspect which files the browser serves from those directories. A scripts folder can contain public assets as well as build tools; verify the affected asset URLs on the staged deployment before promotion.
- Prefer project-local build commands or `vercel build --prod --scope <scope>` before `vercel deploy --prebuilt --prod --scope <scope>` when prior handoff/docs recommend prebuilt deployment.
- Inspect the returned deployment:

```bash
vercel inspect <deployment-url> --scope <scope>
vercel list <project> --prod --scope <scope>
```

- A Vercel deployment with `status UNKNOWN` is not successfully deployed. Do not alias it to the production domain.
- Verify the custom domain, not only the generated deployment URL. After promotion, confirm each custom domain's alias resolves to the intended deployment ID and that the promotion completed. The deployment's embedded alias list can lag; use the alias lookup and promotion status to resolve disagreement. Compare release-specific content or assets too: an unchanged health response alone cannot identify the deployed version.

```bash
curl -fsS https://example.com/path
```

- For public JSON/config deploys, compare the live response to local expected values and headers. If a project has a script like `check-mobile-config-live`, use it.

