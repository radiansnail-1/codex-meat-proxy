---
name: design-qa
description: Independent visual QA, design critique, polish, and implementation verification for an existing interface. Use after a design direction exists when the user asks whether a UI looks good, wants responsive checks, visual polish, hierarchy/spacing critique, browser screenshot review, or fixes to an already chosen design. Use `design` for first-draft ideation or broad design exploration.
---

# Design QA

Use this skill after a design direction exists. It is the independent taste, polish, and verification pass: inspect the implemented UI, name what feels wrong, apply scoped fixes when asked, and verify the result in a browser when practical. Use `design` for new direction, design systems, and unimplemented design plans.

Read the project's `AGENTS.md`, `README`, `DESIGN.md`, design tokens, screenshots, mockups, and component patterns before judging. Use existing project conventions first, but flag conventions that produce the observed problem; consistency alone does not establish quality.

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

## Visual judgment

For every broad visual audit or anti-slop review, read and apply the [visual checklist](references/visual-checklist.md), including its whole-screen review. Assess composition and product specificity before individual CSS details. Working controls, consistent tokens, and clean screenshots do not establish that the design is good.

- Inspect the rendered opening view and the rest of the affected flow, including a representative content-heavy or secondary state. Use desktop and mobile evidence for responsive claims. If only code or supplied screenshots are available, limit the verdict to what they show.
- Name the dominant visual idea and whether it helps this audience understand or do something specific. Check cumulative repetition, generic copy, decorative filler, and whether the real product is displaced by presentation.
- For a flagged pattern, state the visible evidence, its effect, and the smallest useful correction. Retain it when a concrete product, brand, content, or interaction reason supports it. Do not invent intent or dismiss a finding merely as "intentional," "modern," or "on-brand."
- Prefer removing redundant elements and clarifying hierarchy before adding decoration. Preserve purposeful expression and familiar controls; a common font, card, or gradient is not by itself a defect.

For premium-experience critiques, also use [premium audit](references/premium-audit.md). For a narrow polish request, inspect the changed component in context and use only relevant checklist sections; do not expand it into a full redesign.

## Implementation rules

- Follow existing codebase patterns and component systems.
- Keep edits scoped to QA/polish. Do not redesign the whole product unless explicitly asked.
- Do not auto-commit design fixes unless explicitly asked.
- For substantial UI changes, verify the affected route and adjacent critical states at desktop and mobile sizes when practical.

## Output

Lead with the highest-impact observed issues or fixes. If no code changed, give a prioritized punch list with evidence and residual risk. If code changed, report files changed, verification performed, skipped checks, and remaining visual risk. Separate observation from preference and hypothesis.

For broad audits, report usability/implementation quality and visual distinctiveness separately, with a brief evidence-backed conclusion for each. Surface unresolved generic composition or copy even when functional checks pass. Summarize any consequential retained pattern and its reason; mark uninspected surfaces as unverified. Do not infer that AI authored a design from its appearance.
