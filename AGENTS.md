# Maintaining Codex Meat Proxy

Read CONTRIBUTING.md before changing skills. This repository contains public, portable skill variants; installations can contain private adaptations. Preserve that distinction.

For a skill update, inspect its complete folder, including references, scripts and agents/openai.yaml. Update the smallest relevant public change and validate it. Preserve upstream attribution and license metadata. Do not overwrite a public variant with a personal directory or import private skills without an explicit request.

When working from an installation with a matching local skill, reconcile the reusable behavioral change in both locations while retaining local operational details. Report local validation and public publication separately. Use scoped commits and draft PRs; do not merge unless authorized. Follow the user's narrower scope, including local-only or repo-only requests.

Do not run scripts/install.sh --copy to reconcile an existing personal installation: it replaces destination directories. Symlinking is appropriate only when the installed variant is intentionally identical to the public one.
