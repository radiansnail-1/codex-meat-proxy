---
name: design
description: Create design systems, explore visual directions, review unimplemented design plans, and implement a chosen product design. Use design-qa for audits or scoped polish of an existing interface.
---

# Design

Own design direction, design systems, and implementation. Use `design-qa` for implemented-interface audits, premium-experience critique, and visual verification when needed.

Read the project's `AGENTS.md`, `README`, `DESIGN.md`, tokens, component patterns, routes, screenshots, and supplied assets before inventing a direction. Inspect the real product surface when one exists; do not design from a vague description when the code or running UI is available.

## Modes

Choose the smallest mode that fits:

- `consult`: Create or refine a design system, brand direction, typography, color roles, spacing, layout, motion, component states, or `DESIGN.md`.
- `explore`: Generate or compare two or three distinct visual/product directions.
- `review-plan`: Critique a wireframe, UX plan, design spec, or implementation proposal before work begins.
- `implement`: Turn an approved direction into working HTML/CSS, components, or app UI using the existing codebase patterns.

Run only the modes needed for the request; a clear implementation brief does not require exploration or an extra review.

## Routing

- A design system or brand guide request -> `consult`.
- “Show me options,” visual brainstorming, or an uncertain direction -> `explore`.
- A written plan or wireframe with no implementation -> `review-plan`.
- An approved mockup or clear target design -> `implement`.
- Existing-interface critique or scoped polish -> `design-qa`; a requested redesign may return here for a new direction.

## First-draft taste contract

- Build the actual usable product surface, not a marketing shell, unless a landing page is requested.
- Match the domain: operational tools should be calm, dense, legible, and fast to scan; consumer and playful products may be more expressive without losing structure.
- Make one or two sharp visual commitments instead of a mushy “modern SaaS” blend.
- Use real UI elements and states: navigation, filters, forms, tables, charts, repeated-item cards, loading, empty, error, retry, offline, and success states where the flow needs them.
- Prefer real assets, screenshots, generated bitmap assets, or product imagery over abstract filler.
- Avoid decorative blobs, nested cards, generic gradient heroes, placeholder copy, one-note palettes, and oversized type in compact product surfaces.
- Preserve useful existing brand and component conventions unless the brief explicitly calls for a new direction.
- Treat mobile and desktop as first-class; specify how navigation, grids, controls, long text, and dense content adapt.

## Output shapes

- Ideation: named directions with layout, hierarchy, palette, type, component behavior, responsive behavior, strongest use case, and tradeoff.
- Recommendation: one chosen direction and why it fits the product.
- Implementation prep: scoped files/components, design contract, states, responsive rules, and verification path.
- Prototype/implementation: real edits using repo patterns and proportionate visual verification; use `design-qa` when its inspection guidance adds value.
- Design-system work: concise reusable `DESIGN.md` or equivalent.

Lead with concrete observations, not adjectives. Separate observed defects from taste preferences and unvalidated hypotheses. If there is no live UI, code, screenshot, or video, say so and label recommendations as hypotheses.

## Implementation and safety rules

- Follow the existing codebase and component system.
- Keep edits scoped to the requested design surface; do not redesign the product by default.
- Do not auto-commit design fixes unless explicitly asked.
- Verify substantial UI changes at desktop and mobile sizes when practical, including loading/error/empty states, focus/keyboard behavior, contrast, hit targets, and reduced motion.
- Premium craft must not obscure the primary action, add avoidable latency, or substitute for product usefulness, distribution, accessibility, or evidence that users return.
