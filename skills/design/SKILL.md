---
name: design
description: Unified product-design workflow for design systems, visual exploration, implementation, visual QA, and premium-experience audits. Use when the user wants better frontend direction, design variants, a design critique, an approved design built, or an existing interface made clearer, more distinctive, or more crafted.
---

# Design

This is the canonical design router. It covers first-draft direction, implementation preparation, and audits of existing interfaces. Use `design-qa` for the final independent visual verification pass after implementation.

Read the project's `AGENTS.md`, `README`, `DESIGN.md`, tokens, component patterns, routes, screenshots, and supplied assets before inventing a direction. Inspect the real product surface when one exists; do not design from a vague description when the code or running UI is available.

## Modes

Choose the smallest mode that fits:

- `consult`: Create or refine a design system, brand direction, typography, color roles, spacing, layout, motion, component states, or `DESIGN.md`.
- `explore`: Generate or compare two or three distinct visual/product directions.
- `review-plan`: Critique a wireframe, UX plan, design spec, or implementation proposal before work begins.
- `implement`: Turn an approved direction into working HTML/CSS, components, or app UI using the existing codebase patterns.
- `audit`: Inspect an existing interface for visual quality, usability, responsiveness, interaction feel, and premium craft.

When a request spans modes, run them in order: `explore -> review-plan -> implement -> audit`.

## Routing

- A design system or brand guide request -> `consult`.
- “Show me options,” visual brainstorming, or an uncertain direction -> `explore`.
- A written plan or wireframe with no implementation -> `review-plan`.
- An approved mockup or clear target design -> `implement`.
- An existing UI that feels generic, abrupt, flat, unfinished, or not premium -> `audit`.

## First-draft taste contract

- Build the actual usable product surface, not a marketing shell, unless a landing page is requested.
- Match the domain: operational tools should be calm, dense, legible, and fast to scan; consumer and playful products may be more expressive without losing structure.
- Make one or two sharp visual commitments instead of a mushy “modern SaaS” blend.
- Use real UI elements and states: navigation, filters, forms, tables, charts, repeated-item cards, loading, empty, error, retry, offline, and success states where the flow needs them.
- Prefer real assets, screenshots, generated bitmap assets, or product imagery over abstract filler.
- Avoid decorative blobs, nested cards, generic gradient heroes, placeholder copy, one-note palettes, and oversized type in compact product surfaces.
- Preserve useful existing brand and component conventions unless the brief explicitly calls for a new direction.
- Treat mobile and desktop as first-class; specify how navigation, grids, controls, long text, and dense content adapt.

## Premium-experience audit

Use this as the `audit` lens when an implemented app should feel more premium, distinctive, crafted, or memorable. Premium is not “more decoration, animation, or complexity.” Inspect repeated moments where users gain or lose confidence, clarity, delight, or trust.

### Establish the boundary

1. Identify the exact build, route, device, viewport, audience, and core user journey.
2. Read the repository guidance and design contract; record the commit/build and missing evidence.
3. Run the app or inspect supplied screenshots/video. Do not claim a live finding without implementation evidence.
4. Concentrate on high-frequency, high-emotion, high-risk, and high-value moments rather than every screen.

### Audit five layers

1. **Feedback and state clarity** — idle, loading, progress, success, partial success, empty, offline, permission, error, retry, and undo. The user should know what started, what is waiting, what happened, and how to recover.
2. **Motion and transitions** — timing, easing, interruption, reduced motion, causality, hierarchy, continuity, and control. Animation must not delay common actions or exist only because it is technically possible.
3. **Illustration and visual language** — whether an illustration or mascot orients, explains, reassures, celebrates, humanizes, or warms an empty state. Recommend a small intentional state set and a coherent base style, not a dump of generic AI assets.
4. **Invisible interaction craft** — launch/framing/return behavior, focus, gestures, haptics, permissions, forgiving input, undo/retry, optimistic updates, latency, jank, defaults, refresh, dismissal, back behavior, and interruption recovery.
5. **Coherence and taste** — typography, spacing rhythm, alignment, hierarchy, color roles, icon weight, copy tone, radii, shadows, empty states, and asset treatment. Look for one-off exceptions, noisy hierarchy, generic defaults, and polished hero moments followed by unfinished states.

For each finding record evidence, user effect, frequency, importance to the core job, smallest recommendation, confidence (observed fact/inference/hypothesis), effort, and accessibility/performance risk. Prioritize with `importance × frequency × confidence ÷ effort`, then use judgment.

Keep three buckets:

- **Fix now:** clarity, recovery, responsiveness, accessibility, or repeated-flow defects.
- **Craft next:** high-leverage motion, illustration, mascot states, or interaction polish attached to a meaningful working surface.
- **Delight bets:** expressive experiments whose value needs user or behavioral feedback.

## Output shapes

- Ideation: named directions with layout, hierarchy, palette, type, component behavior, responsive behavior, strongest use case, and tradeoff.
- Recommendation: one chosen direction and why it fits the product.
- Implementation prep: scoped files/components, design contract, states, responsive rules, and verification path.
- Prototype/implementation: real edits using repo patterns, followed by a handoff to `design-qa` for independent visual verification.
- Design-system work: concise reusable `DESIGN.md` or equivalent.
- Audit: verdict; scope/evidence; three to seven ranked opportunities; interaction/motion changes; illustration/mascot opportunity; invisible craft; fix-now/craft-next/delight-bets plan; what not to do; validation plan.

Lead with concrete observations, not adjectives. Separate observed defects from taste preferences and unvalidated hypotheses. If there is no live UI, code, screenshot, or video, say so and label recommendations as hypotheses.

## Implementation and safety rules

- Follow the existing codebase and component system.
- Keep edits scoped to the requested design surface; do not redesign the product by default.
- Do not auto-commit design fixes unless explicitly asked.
- Verify substantial UI changes at desktop and mobile sizes when practical, including loading/error/empty states, focus/keyboard behavior, contrast, hit targets, and reduced motion.
- Premium craft must not obscure the primary action, add avoidable latency, or substitute for product usefulness, distribution, accessibility, or evidence that users return.
