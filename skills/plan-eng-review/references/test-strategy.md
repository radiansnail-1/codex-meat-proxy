# Proportionate test strategy

Read repository instructions, package/build configuration, and existing tests to identify the supported verification path. Trace affected behavior from entry to outcome, including failure modes whose impact or likelihood matters.

Distinguish:
- demonstrated regression: unintended loss of previously correct behavior;
- coverage gap: relevant behavior lacks a meaningful check;
- intentional change: expected behavior changes by design;
- hypothesis: a suspected failure that still needs evidence.

For each material gap, recommend a concrete assertion and the smallest reliable test level:
- unit tests for pure transformations and local branching;
- integration tests for persistence, concurrency, adapters, and boundaries mocks would conceal;
- UI or end-to-end checks for critical user-visible journeys and interaction failures;
- behavioral evaluations for instruction, prompt, and tool-definition changes where output judgment matters.

Prefer checks that would detect the actual failure. For a demonstrated regression, establish that the check fails without the fix and passes with it when practical. Avoid mirroring implementation, testing wording alone, or adding redundant tests merely to increase count. A component count does not determine test level.

Inspect existing coverage before proposing more. Recommend targeted checks first, then required repository checks and broader verification where shared behavior changes. Record unavailable infrastructure and verification gaps rather than claiming untested paths passed. Do not create a new test framework for a low-impact reversible change without a concrete benefit.

A compact table of behavior, existing evidence, gap, and recommended check often suffices. Draw a coverage diagram only if it explains complex flow. Do not manufacture coverage percentages from an informal path inventory.

Only write a persistent test-plan artifact when requested. For a substantial prompt change, compare original and revised instructions on representative raw tasks with the same model, tools, and effort where feasible; grade outcomes and side effects before comparing speed or token use. Do not claim a gain from shorter instructions alone.
