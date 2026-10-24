# Reusable project verification

Use when reusable verification is requested or repeated QA keeps rediscovering the same setup. Extend the project's existing runbook or harness; create another skill only when requested. A one-off check can stay in the task's evidence. Respect read-only scope and existing permission boundaries.

## Keep one proven recipe

Discover commands and stable UI handles from the repo and current tools. Reuse working scripts before adding helpers. Keep these details together, linking existing owners instead of copying them:

| Part | What the next agent needs |
| --- | --- |
| Target | Authoritative checkout, app/build identity, surface, and required device/account state. |
| Start | Exact launch/build command, required fixtures or migrations, and a readiness signal that means the feature is usable. |
| Health check | A read-only way to confirm the intended version, instance, port/device, and auth before driving it. |
| User flow | Entry point, preconditions, real user actions with stable selectors/commands, and the observable pass condition. |
| Evidence | Action plus resulting state, relevant side effects, and where screenshots/logs/results survive teardown. |
| Cleanup | Only processes, sessions, and scratch data created by this run; retain evidence and user-owned state. |

For several recurring flows, keep a compact index of the relevant features and link each recipe. Cover the requested surface; do not generate a whole-app inventory for a narrow task. Name physical-device, entitlement, external-service, and inaccessible-state prerequisites explicitly.

## Prove and maintain the recipe

Run the documented instructions through one relevant real flow, capture the proof, and clean up. Verify evidence still exists afterward. A recipe that has not run is a draft; a simulator or mock proves only the behavior that surface can exercise. Do not infer harmlessness from a command named dry-run or test mode.

Use isolated instances when available. Otherwise give the shared runtime one driver. After a surprising failure, check instance health and restore a known state before retrying. Never terminate by process name or reset user data to make the recipe pass.

When instructions drift, correct and re-exercise them within scope. When the app breaks an expected behavior, report the regression rather than weakening the pass condition. Persistent recipe edits follow the task's edit scope; read-only QA can return a proposed correction without changing repo files.

Workflow reference: [Lauren Tan's pstack verification generator](https://github.com/cursor/plugins/blob/main/pstack/skills/create-verification-skill/SKILL.md).
