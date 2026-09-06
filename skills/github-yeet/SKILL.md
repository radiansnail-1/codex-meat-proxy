---
name: github-yeet
description: |
  Publish local changes to GitHub on macOS or Windows: inspect scope, commit
  intentionally, push, and open a draft PR. Includes Brian's Windows GitHub HTTPS
  fallback for Schannel / Git credential-helper failures. Trigger on "yeet".
---

# GitHub Publish Changes

Use this skill when the user asks to publish local changes to GitHub,
push a branch, open a PR, or run a "yeet" flow.

## Before pushing (both platforms)

1. Inspect scope before staging:
   - `git status -sb`
   - `git diff --stat`
   - relevant diffs for changed files
2. If the worktree has unrelated changes, ask which files belong in the PR.
   Stage explicit paths unless the whole worktree is confirmed in scope.
3. Commit with a terse, descriptive message.
4. Run the most relevant local checks that match the change.
5. Never force-push without explicit user approval for the exact branch and
   reason. If a push is rejected with `fetch first`, `non-fast-forward`, or
   similar, treat that as branch-history alignment, not auth.
6. Never write tokens into remotes, Git config, files, commits, logs, or PR text.
7. Default to a draft PR after the branch is on GitHub.

## On macOS

1. Push the current branch:
   ```bash
   git push -u origin "$(git branch --show-current)"
   ```
2. Open a draft PR. Prefer GitHub tooling already available in the session;
   otherwise use `gh pr create --draft`.

## On Windows

1. Push the current branch:
   ```powershell
   git push -u origin $(git branch --show-current)
   ```
2. If normal GitHub HTTPS push/fetch fails with symptoms like
   `SEC_E_NO_CREDENTIALS`, `AcquireCredentialsHandle failed`, Schannel errors,
   private GitHub commands hanging after auth, or `git push` failing while
   `gh auth status` is healthy, use Brian's local wrapper instead of retrying:
   ```powershell
   powershell -ExecutionPolicy Bypass -File E:\5.ProjectIdeas\BeforeScroll\git-gh.ps1 push -u origin $(git branch --show-current)
   ```
   The wrapper must derive auth from `gh auth token` at runtime, use OpenSSL,
   disable Git credential helpers for that command, and pass a transient
   Authorization header. Never write tokens into remotes, Git config, files,
   commits, logs, or PR text.
3. If the wrapper works but Git rejects the push with `fetch first`,
   `non-fast-forward`, or similar, treat that as branch-history alignment,
   not auth. Do not force-push without explicit user approval for the exact
   branch and reason.
4. Open a draft PR after the branch is on GitHub. Prefer GitHub tooling already
   available in the session; otherwise use `gh pr create --draft`.

### Local Lauds Note

For `E:\5.ProjectIdeas\BeforeScroll`, normal Windows Git HTTPS is known to be
unreliable. `lauds-site` and `lauds-android` have repo-local OpenSSL config, and
`E:\5.ProjectIdeas\BeforeScroll\git-gh.ps1` is the verified transport path.
