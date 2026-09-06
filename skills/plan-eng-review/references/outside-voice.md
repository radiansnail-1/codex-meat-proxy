# Optional independent plan review

Use only when the user requests a second opinion or authorized delegation would materially improve a complex review. It is not a mandatory completion step. Agreement between models is not proof of correctness.

Prefer the current native read-only reviewer. Honor an explicitly selected model and available tooling; do not hardcode a model version, spawn a separate CLI by default, or predict runtime without evidence.

Give the reviewer the actual user goal, plan, relevant raw source, constraints, and acceptance criteria. Withhold the first review's answer and confidence until independent judgment is formed. Do not truncate away material plan sections; narrow the review explicitly or provide the complete artifact through a scoped path.

Require concrete findings, source evidence, failing scenarios, and uncertainty. Inspect the evidence, reconcile disagreements, and return only supported conclusions. Do not paste the output unchecked or require a new question for every disagreement. Ask the user only when a consequential decision remains unresolved.

If independent review cannot run, report the gap and continue with the verified review result. Do not bypass access controls or expand permissions to force a second opinion.
