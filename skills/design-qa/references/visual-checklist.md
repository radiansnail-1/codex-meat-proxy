# Visual checklist

Use the [Impeccable slop catalog](https://impeccable.style/slop/) as a standing QA lens. Treat a quality defect as a fix; treat an AI-default pattern as a prompt for contextual judgment, not a universal ban. A flagged choice may be valid when it is intentional, fits the product and brand, and is executed consistently. Do not replace one fashionable default with another.

Check the following during `audit` and `implement-polish` when relevant:

### Design-system drift

- Flag fonts, literal colors, corner radii, and font sizes that fall outside `DESIGN.md` or the project's documented tokens. Use an existing token or document the intentional addition.

### Visual details

- Decorative grids without a canvas, mapping, or measurement purpose.
- Thick accent borders fighting rounded corners, especially one-sided "tab" borders on cards.
- Glass, blur, glow borders, and frosted surfaces used without a real layering purpose.
- Hairline borders combined with wide diffuse shadows; choose a clear edge or soft elevation.
- Repeating-gradient stripes used as generic surface decoration.
- Small cards and controls rounded into indistinct blobs; reserve pills for suitable controls and tags.
- Crude hand-built SVG mascots or scenes standing in for finished imagery.

### Typography

- Decorative kicker or eyebrow labels above headings, especially uppercase tracked labels and hero pills.
- Functional text below 11px and body text below 14px.
- Flat type scales whose adjacent steps lack enough contrast; aim for roughly a 1.25 ratio where appropriate.
- Rounded-square icon tiles stacked above feature headings as a repeated card formula.
- Oversized italic-serif hero headlines used as a generic taste signal rather than an editorial choice.
- Long sentence-length hero headlines blown up until they dominate the first viewport.
- Tracking tightened enough to damage letterforms or widened above 0.05em in body copy.
- Reflexive use of ubiquitous AI-era typefaces without brand rationale.
- One font treatment used for every role when it produces no hierarchy or personality.
- Long passages in all caps.

### Color and contrast

- Saturated radial halos or faint spotlight hazes added behind sections without compositional purpose.
- Reflexive purple-to-blue gradients, cyan-on-dark palettes, or dark themes with glowing accents.
- Gradient-filled text, particularly headings and metrics; prefer solid, readable text color.
- Gray text on colored surfaces; use a tonal shade of the surface or an accessible near-white.
- Defaulting to warm cream or beige merely to imply taste rather than deriving color from the brand.
- Text below WCAG AA contrast: 4.5:1 for body text and 3:1 for large text.

### Layout and spacing

- Tiny numbered section markers that imitate editorial sequencing without adding meaning.
- Scroller cards flush to one edge because the container lacks matching gutters.
- Text covered by opaque overlapping elements.
- Unbalanced opening columns where one column extends far beyond its neighbor and creates dead space.
- Headings closer to the preceding block than to the content they introduce.
- Generic hero-metric arrangements: one giant number, a small label, and a row of decorative supporting stats.
- Endless identical icon-heading-copy card grids.
- Monotonous spacing values that erase grouping and section rhythm.
- Cards nested inside cards; flatten with spacing, type, and dividers.
- Prose lines beyond roughly 65–80 characters without a deliberate reading measure.
- Content spilling outside its container or producing accidental horizontal scroll.
- Tooltips, menus, popovers, and other positioned children clipped by an overflow container.

### Motion

- Pulsing status indicators when the underlying state is static.
- Fake blinking terminal cursors attached to non-editable copy.
- Auto-scrolling marquees that demand attention and prevent self-paced reading.
- Bounce or elastic easing on ordinary interface transitions; favor restrained ease-out motion.
- Animation of width, height, padding, or margin when transform, opacity, or grid transitions can avoid layout thrash.
- Images that scale or rotate on hover without a meaningful interaction purpose.

### Copy

- The same label repeated in multiple slots within one component.
- Repeated em-dashes used as a synthetic conversational cadence.
- Generic SaaS claims such as "supercharge," "streamline," "world-class," or "enterprise-grade" where concrete verbs and nouns would be clearer.
- Repeated manufactured-contrast aphorisms or terse rebuttals used as section endings.
- Dismissing alternatives as "theater" instead of explaining the concrete limitation.

### Imagery

- Hero illustrations assembled from generic geometric SVG shapes when real illustration, photography, product imagery, or a purposeful graphic is needed.
- Images with empty, missing, or placeholder `src` values.

### General quality

- Uncaught errors on load, broken assets, or failed requests that compromise the page.
- Content left invisible because a reveal or hydration path failed; content should remain visible without enhancement.
- Bordered or colored controls with cramped padding; use at least 8px and generally 12–16px where density permits.
- Body text touching the viewport edge; keep at least 16px horizontal padding on small screens.
- Justified screen text without robust hyphenation.
- Heading levels that skip and break the document outline.
- Multi-line body copy with line-height below about 1.3; usually use 1.5–1.7.

When the project already includes Impeccable or its CLI is available, use `npx impeccable detect <target>` as supporting evidence for web code or rendered URLs. Do not install a new dependency solely for QA without user approval. The detector complements screenshot review and contextual judgment; it does not replace them and does not apply to native UI code.

