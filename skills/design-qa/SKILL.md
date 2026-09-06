---
name: design-qa
description: Independent visual QA, design critique, polish, and implementation verification for an existing interface. Use after a design direction exists when the user asks whether a UI looks good, wants responsive checks, visual polish, hierarchy/spacing critique, browser screenshot review, or fixes to an already chosen design. Use `design` for first-draft ideation or broad design exploration.
---

# Design QA

Use this skill after a design direction exists. It is the independent taste, polish, and verification pass: inspect the implemented UI, name what feels wrong, apply scoped fixes when asked, and verify the result in a browser when practical. Use `design` for new direction, design systems, and unimplemented design plans.

Read the project's `AGENTS.md`, `README`, `DESIGN.md`, design tokens, screenshots, mockups, and component patterns before judging. Use existing project conventions first.

## Modes

Choose the smallest mode:

- `audit`: Inspect a live or implemented interface for visual quality, spacing, hierarchy, responsiveness, state clarity, accessibility, and interaction feel.
- `implement-polish`: Apply scoped polish fixes to an approved or already implemented direction.

If the request wants fresh directions, concepts, a design system, or a premium-experience direction before implementation, route to `design`. For premium audits of an implemented surface, use the conditional premium-audit reference below. A single evidence-backed pass can cover both experience and visual detail.

## Audit standards

- Match the product's domain. Operational tools should be dense, calm, and scannable; games and playful products can be more expressive.
- Use real assets, screenshots, generated bitmap assets, or product imagery when visuals matter. Avoid placeholder-looking decoration.
- Verify desktop and mobile behavior: no overlap, clipping, unexpected resizing, or unusable long text.
- Prefer familiar controls: icons for tools, segmented controls for modes, toggles for binary settings, sliders/inputs for numeric settings, tabs for views, and menus for option sets.
- Check hierarchy, density, spacing rhythm, alignment, contrast, icon weight, typography, empty/loading/error states, hover/focus states, keyboard paths, hit targets, reduced motion, and mobile behavior.
- Use browser screenshots and real interaction when available; inspect console/network errors and broken assets.

## Conditional review lenses

For a broad visual audit, use [visual checklist](references/visual-checklist.md). For a premium-experience critique, use [premium audit](references/premium-audit.md). A narrow spacing fix does not require both catalogs. Apply contextual judgment and distinguish functional defects from taste preferences.

## Implementation rules

- Follow existing codebase patterns and component systems.
- Keep edits scoped to QA/polish. Do not redesign the whole product unless explicitly asked.
- Do not auto-commit design fixes unless explicitly asked.
- For substantial UI changes, verify the affected route and adjacent critical states at desktop and mobile sizes when practical.

## Output

Lead with the highest-impact observed issues or fixes. If no code changed, give a prioritized punch list with evidence and residual risk. If code changed, report files changed, verification performed, skipped checks, and remaining visual risk. Separate observation from preference and hypothesis.
