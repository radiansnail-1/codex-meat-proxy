# Outside Voice — Independent Plan Challenge (optional, recommended)

After all review sections are complete, offer an independent second opinion from the OTHER model. Two different models agreeing on a plan is stronger signal than one model's thorough review.

**The symmetric rule:** call the other model's CLI, whichever harness you are in.

- Running in Claude Code → call `codex` (gpt-5.5).
- Running in Codex → call `claude`.
- If the other CLI is unavailable or errors → fall back to a fresh subagent in the current harness (Agent tool in Claude Code; spawn_agent in Codex). Same-model, but fresh context still buys genuine independence.

**Check availability of the other CLI:**

```bash
# from Claude Code:
which codex 2>/dev/null && echo "OTHER_AVAILABLE" || echo "OTHER_NOT_AVAILABLE"
# from Codex:
which claude 2>/dev/null && echo "OTHER_AVAILABLE" || echo "OTHER_NOT_AVAILABLE"
```

(On Windows without `which`, use `where codex` / `where claude`.)

**Offer it** (structured question tool if available, otherwise plain prose):

> "All review sections are complete. Want an outside voice? A different AI model can
> give a brutally honest, independent challenge of this plan — logical gaps, feasibility
> risks, and blind spots that are hard to catch from inside the review. Takes about 2
> minutes."
>
> RECOMMENDATION: Choose A — an independent second opinion catches structural blind
> spots. Completeness: A=9/10, B=7/10.

Options:
- A) Get the outside voice (recommended)
- B) Skip — proceed to outputs

**If B:** Print "Skipping outside voice." and continue to the next section.

**If A:** Construct the plan review prompt. Read the plan file being reviewed (the file the user pointed this review at, or the branch diff scope). If a CEO plan document was written earlier, read that too — it contains the scope decisions and vision.

Construct this prompt (substitute the actual plan content — if plan content exceeds 30KB, truncate to the first 30KB and note "Plan truncated for size"):

"You are a brutally honest technical reviewer examining a development plan that has
already been through a multi-section review. Your job is NOT to repeat that review.
Instead, find what it missed. Look for: logical gaps and unstated assumptions that
survived the review scrutiny, overcomplexity (is there a fundamentally simpler
approach the review was too deep in the weeds to see?), feasibility risks the review
took for granted, missing dependencies or sequencing issues, and strategic
miscalibration (is this the right thing to build at all?). Be direct. Be terse. No
compliments. Just the problems.

THE PLAN:
<plan content>"

**Invoke the other CLI:**

Pick a temp file for stderr per platform:
- On macOS/Linux: `TMPERR_PV=$(mktemp /tmp/planreview-XXXXXXXX)`
- On Windows (Git Bash): `TMPERR_PV=$(mktemp "${TEMP:-/tmp}/planreview-XXXXXXXX")`

```bash
# from Claude Code:
codex exec --skip-git-repo-check -s read-only "<prompt>" 2>"$TMPERR_PV"
# from Codex:
claude -p "<prompt>" 2>"$TMPERR_PV"
```

Use a 5-minute timeout (`timeout: 300000`). After the command completes, read stderr:
```bash
cat "$TMPERR_PV"
```

Present the full output verbatim:

```
OUTSIDE VOICE (<other model> — plan review):
════════════════════════════════════════════════════════════
<full output, verbatim — do not truncate or summarize>
════════════════════════════════════════════════════════════
```

**Error handling:** All errors are non-blocking — the outside voice is informational.
- Auth failure (stderr contains "auth", "login", "unauthorized"): report it and name the login command (`codex login` / `claude` then `/login`).
- Timeout: "Outside voice timed out after 5 minutes."
- Empty response: "Outside voice returned no response."

On any error, fall back to the fresh-subagent option; if that also fails: "Outside voice unavailable. Continuing to outputs."

**Cross-model tension:**

After presenting the outside voice findings, note any points where the outside voice disagrees with the review findings from earlier sections. Flag these as:

```
CROSS-MODEL TENSION:
  [Topic]: Review said X. Outside voice says Y. [Your assessment of who's right.]
```

For each substantive tension point, auto-propose as a TODO (one question each):

> "Cross-model disagreement on [topic]. The review found [X] but the outside voice
> argues [Y]. Worth investigating further?"

Options:
- A) Add to TODOS.md
- B) Skip — not substantive

If no tension points exist, note: "No cross-model tension — both reviewers agree."

**Cleanup:** Run `rm -f "$TMPERR_PV"` after processing.
