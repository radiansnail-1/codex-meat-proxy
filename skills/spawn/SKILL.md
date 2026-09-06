---
name: spawn
description: Delegation-first subagent orchestration for research, code inspection, implementation shards, fixes, verification, and review. Use when the user invokes /spawn or $spawn, asks to spawn subagents, delegate work, use parallel agents, run independent reviewers, split implementation across agents, or cross-check a task with separate agents.
---

# Spawn

## Purpose

When this skill is active, default to using subagents for meaningful research, investigation, fixes, implementation, and verification. Keep the main agent focused on scoping, delegation, conflict management, inspecting results, integrating work, final verification, and the final answer.

The main thread should do substantive research or code changes only when the task is a super simple one-shot, no subagent tool is available, RAM pressure makes delegation impractical, or immediate local inspection is needed to write good subagent prompts.

This skill is for explicit delegation. Do not treat it as permission to spawn agents silently when `$spawn` or an equivalent user request is absent.

## Speed Boundary

Delegation must shorten the critical path. Scope only until the first bounded lane is clear, then dispatch it; do not spend several minutes designing a parallel program before useful work starts.

Do not spawn agents for deterministic local bookkeeping such as git status, staging, handoff-file refreshes, commits, pushes, Graphify AST/update/check commands, or routine tool/version checks. The parent runs those directly. Semantic Graphify agents are allowed only when the user explicitly requested Graphify work and a full semantic workflow is genuinely the task—not when Graphify appears incidentally during handoff.

When progress is blocked on one brief owner action, finish safe staging and ask for that action. Do not invent speculative background lanes merely to satisfy `$spawn`. If no independent lane will reduce elapsed time, say so and continue single-agent.

## Tool Discovery

- **Claude Code:** the `Agent` tool is built in. Send multiple Agent calls in one message to run subagents concurrently; use `run_in_background` for long tasks.
- **Codex:** if `multi_agent_v1.spawn_agent` is not already in the tool list, call `tool_search` for `multi-agent spawn subagent`.

If no subagent tool is available, say so briefly and continue with the best single-agent workflow.

## Resource Check

Before spawning, check current memory pressure. On Windows, this PowerShell command is sufficient:

```powershell
$os = Get-CimInstance Win32_OperatingSystem
$used = 100 - (($os.FreePhysicalMemory / $os.TotalVisibleMemorySize) * 100)
[math]::Round($used, 1)
```

On macOS, do not count cached/file-backed pages toward the `87%` threshold. Use anonymous app memory, wired memory, and compressor memory:

```sh
vm_stat | awk -v total="$(sysctl -n hw.memsize)" '
  /page size of/ { page = $8; gsub(/[^0-9]/, "", page) }
  /Anonymous pages:/ { anon = $3 }
  /Pages wired down:/ { wired = $4 }
  /Pages occupied by compressor:/ { compressor = $5 }
  END { printf "%.1f\n", ((anon + wired + compressor) * page / total) * 100 }
'
```

Use RAM pressure to choose concurrency:

- For planning, assume each concurrent subagent adds about `0.5-1 GB` RAM pressure depending on task size. Compare `current_used_gb + (subagents * estimated_gb)` against `total_ram_gb * 0.87`.
- Under `70%`: spawn the useful independent agents in parallel, up to the natural split of the task.
- `70-87%`: use fewer concurrent agents, usually one or two.
- Near or above `87%`: do not run several agents at once. Spawn one focused agent, wait/close it, then spawn the next agent only if the next step still needs delegation.

Prefer sequential subagents over main-thread implementation when the task is still substantive but RAM is tight.

## When To Spawn

When this skill is active, spawn when at least one of these is true:

- Research or problem investigation requires more than a tiny one-shot lookup.
- Independent codebase questions can be answered in parallel or sequentially by focused agents.
- Any fix or code change is nontrivial and can be assigned a bounded ownership scope.
- Implementation can be split into disjoint files, modules, responsibilities, or phases.
- A separate verification pass can run while the main agent continues implementation.
- Research requires multiple independent angles or source checks.
- The task is risky enough that an independent reviewer is likely to catch a real issue.

Do not spawn for trivial one-step tasks, unclear tasks where delegation would multiply confusion, or changes where no bounded agent-owned scope exists. If multiple agents would likely edit the same files, run them sequentially or assign only one worker to those files.

## Agent Count

Default to the smallest useful number that preserves delegation-first execution:

- `1` agent for one bounded investigation, implementation, fix, or review.
- `2-3` agents for independent exploration, split implementation, or one worker plus one verifier.
- Up to `5` only when the work naturally separates into five valuable, non-overlapping tracks and RAM allows it.

If RAM is short, run the same plan sequentially: agent 1 investigates, close it; agent 2 fixes, close it; agent 3 verifies, close it.

## Delegation-First Workflow

Use this sequence for substantive tasks:

1. Main agent scopes the task just enough to identify the first useful delegation split.
2. Spawn explorer agents for research/investigation unless the question is a tiny one-shot.
3. Main agent reads the explorer results and decides the fix/implementation plan.
4. Spawn worker agents for code changes when the work can be bounded. Use sequential workers when RAM or file overlap prevents parallelism.
5. Main agent inspects patches, resolves conflicts, and makes only small glue edits when needed.
6. Spawn verifier/reviewer agents for focused checks when useful and RAM allows. If RAM is tight, run verification after workers finish.
7. Main agent runs or reviews final tests/checks and owns the final response.

The main agent may perform super simple edits directly: typo fixes, one-line config changes, obvious small text changes, or tiny targeted research needed to write an accurate subagent prompt.

## Strategy Diversity, Evidence, and Iteration

Use this control loop for difficult, open-ended, or hypothesis-rich work—not routine split-by-file implementation.

1. **Maintain an approach registry.** Group lanes by their underlying hypothesis, mechanism, or evaluation method—not superficial wording. The parent tracks active, blocked, rejected, and underexplored lanes.
2. **Act on convergence.** When agents converge on one approach family, retain the strongest representative and redirect later agents toward materially distinct formulations, evidence sources, or failure modes.
3. **Block with a reason.** Record the exact missing proof, dependency, reproduction, or test failure. Reopen a blocked lane only for a genuinely new mechanism, evidence source, or implementation path; do not churn on the same dead end.
4. **Cross-pollinate late.** Let independent lanes expose concrete strengths and gaps before combining ideas. Avoid early blending into a single untested consensus.
5. **Require artifacts, not status.** Each lane returns task-appropriate evidence: patch/diff plus tests, minimal reproduction, exact citations, decision table, counterexample, or concrete next experiment. Reject vague optimism and unexplained confidence.
6. **Use adversarial checks.** Assign a focused reviewer to test task-specific invalid assumptions, regressions, circular reasoning, missing edge cases, source gaps, and duplicate work.
7. **Run parent synthesis rounds.** The parent periodically synthesizes, challenges, redirects, and launches only the next highest-value lanes. A failed first wave updates the registry; it is not an automatic stop condition.
8. **Use explicit stop conditions.** Continue only while a new lane has expected value within the user’s time, cost, and deadline budget. At the stop point, deliver the strongest verified result and its precise remaining gap—never present partial work as complete.

## Role Selection

Use the read-only explorer role (`explorer` in Codex; the `Explore` agent type in Claude Code) for specific codebase questions. Ask narrow questions and avoid duplicating the main agent's work.

Use the worker role (`worker` in Codex; `general-purpose` in Claude Code) for bounded implementation or test-fix work. Give each worker explicit ownership of files, modules, or responsibility. Tell workers they are not alone in the codebase, must not revert others' edits, and must adapt to concurrent changes.

Use the default agent type when the task does not fit a specialized role.

## Model Routing

- **Default child route:** unless the user specifies another route, spawn Codex execution agents with `gpt-5.6-luna` and `model_reasoning_effort="xhigh"`. If the built-in subagent tool cannot select a model, invoke a separate Codex execution lane with those exact settings; keep the built-in child only when its role-specific capabilities are required.
- **Choose model size before reasoning effort:** use **Luna** for clear, bounded, low-risk execution or bulk work where speed/limits matter; **Terra** for everyday business reasoning and moderate implementation; **Sol** only for genuinely hard, ambiguous, high-stakes, or quality-gated work. A prior third-party benchmark makes Luna/xhigh worth testing for a bounded execution lane; it is not a universal default.
- **Use the minimum adequate reasoning level:** start at the previous successful effort—or one level lower—and escalate only after a concrete quality, correctness, or test failure. Reserve provider-specific Max/Pro modes for cases where the expected quality gain justifies the latency and limit cost.
- **Verify once per route:** run a tiny real, read-only smoke test with the exact model and reasoning setting before changing a default or reporting the routing change complete. Example: `codex exec --skip-git-repo-check -s read-only -m gpt-5.6-luna -c 'model_reasoning_effort="xhigh"' 'Reply with exactly: LUNA_OK'`.
- **Fallback:** if the chosen model or setting is unavailable, errors, or is unsuitable for the task, retain the existing configured model; do not substitute an unverified tier name.
- **Claude boundary:** Claude Code's native `Agent` tool accepts Claude model aliases, not GPT identifiers. Use a Claude-native child there, or invoke Codex as a separate GPT execution lane; never pass `gpt-5.6-luna` as an Agent model.
- Keep the parent session on its planning/orchestration model unless the whole task needs a switch. Use the execution model for the bounded child, then inspect and integrate its result.

## Prompt Shape and Economy

Every subagent prompt must include:

- The exact outcome needed.
- The repo/path or artifact scope.
- The files/modules it may edit, or that it must stay read-only.
- Relevant constraints from the user request.
- Expected final output: findings, changed files, tests run, blockers, and confidence.
- **One source of truth for each instruction.** Do not repeat a global rule in multiple prompt sections; give the child only context it cannot otherwise access.
- **An explicit response contract, not “be concise.”** Name the facts/artifacts that must remain and the detail that may be omitted.
- **Programmatic reduction for large tool data.** Filter, join, count, diff, or summarize large structured results in code before returning them to the model; return the smallest verifiable result plus the artifact/query needed to reproduce it.

For coding workers, include:

```text
You are not alone in this codebase. Do not revert edits you did not make. Work only in your assigned scope and adapt to concurrent changes.
```

## Parallel Patterns

Good patterns:

- Explorer A maps auth flow, Explorer B maps data model, main agent inspects UI.
- Worker A owns frontend files, Worker B owns backend files, main agent owns integration and final verification.
- Explorer finds root cause, Worker fixes the assigned files, Verifier checks the regression.
- Under high RAM pressure: Explorer runs first, then Worker, then Verifier, each closed before the next starts.
- Separate reviewers check security, performance, and product behavior when each has distinct evidence to inspect.

Bad patterns:

- Five agents all looking for "anything wrong".
- Multiple workers editing the same files without a clear owner.
- Main agent doing all implementation while subagents only give vague advice.
- Delegating final judgment to subagents.
- Waiting idly for agents when useful orchestration, prompt prep, or result inspection can continue.

## Main-Agent Responsibilities

After spawning:

1. Manage the queue of agents according to RAM and file-overlap constraints.
2. Continue orchestration, prompt prep, or non-overlapping checks instead of waiting by default.
3. Wait when the result is on the critical path or when sequential low-RAM delegation requires it.
4. Inspect completed findings or patches before relying on them.
5. Reconcile disagreements explicitly.
6. Make only small glue edits directly unless the remaining change is a super simple one-shot.
7. Run the final verification yourself when feasible.
8. Close agents when they are no longer needed.

Never paste subagent output as the final answer without checking it. Summarize what was used, what was rejected, and what remains uncertain.

## Reporting

When subagents were used, include a concise final note with:

- Number and role of agents spawned.
- What each agent was assigned.
- Which findings or changes were accepted.
- Verification performed by the main agent.

When subagents were not used despite `$spawn`, state the reason: no available tool, high RAM pressure, no useful parallel split, or risk of conflicting edits.
