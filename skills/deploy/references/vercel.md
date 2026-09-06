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

