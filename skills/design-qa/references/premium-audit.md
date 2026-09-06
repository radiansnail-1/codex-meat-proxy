# Premium-experience audit

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

