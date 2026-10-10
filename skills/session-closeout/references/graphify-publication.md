# Graphify During Handoff And Publication

Read this reference only when repository instructions require a tracked
Graphify graph or `graphify-out/graph.json` is part of the delivery contract.
Prefer the repository's named incremental update and check commands over generic CLI calls. Handoff publication is graph maintenance, not graph exploration.

## Commit Shape And Ordering

Prefer one checkpoint commit when the repository can generate and validate its tracked graph from a staged source snapshot or source-content digest:

1. Stage the scoped source/config/docs and canonical handoff files.
2. Run the repository's incremental Graphify publication against that staged snapshot.
3. Inspect and stage only the tracked graph artifacts required by repository instructions.
4. Run the repository's supported integrity/freshness check when it supports the pending snapshot.
5. Commit the scoped work, canonical files, and graph once.
6. Run any required post-commit check and push only after it passes.

Never create a temporary or "pretend" commit to obtain a hash and then squash or amend it away. If the tracked graph embeds an exact `built_at_commit`, it cannot safely name the same commit that contains the graph because adding the graph changes the commit hash. In that format, use the structurally required sequence:

1. Commit the scoped source/config/docs and canonical handoff files.
2. Run the repository's incremental Graphify update command from that retained commit.
3. Inspect and stage only the required tracked graph artifacts.
4. Commit the graph refresh separately.
5. Run the repository's integrity/freshness check and push after it passes.

This two-commit fallback remains necessary only until the repository changes graph freshness metadata to a staged-tree or source-digest identity.

### PR-identity exception

Some repositories require the assigned PR number in tracked handoff files. In that case, avoid an immediate second semantic Graphify cycle by obtaining the real PR identity before the final graph pass:

1. Prefer an existing unique pushed branch commit for PR creation. If none exists, commit the minimum scoped checkpoint, run cheap publication invariants, and push it provisionally.
2. Create or update the PR.
3. Record the real PR number and URL once. Describe required CI as pending on the final Graphify head; do not copy transient check timestamps from the provisional head.
4. Follow the commit-shape rules above: include the final canonical state and graph in one commit when staged-snapshot/source-digest publication is supported; otherwise use the exact-commit two-commit fallback.
5. Run the normal integrity/freshness check and push the final head.
6. Wait for required CI and merge without another status-only handoff/Graphify cycle.

This is an ordering exception, not permission to invent a future PR number or check result. The provisional push exists only to obtain GitHub's durable PR identity; it is not the CI acceptance head.

Start with incremental publication. When it requires a semantic refresh or
local rebuild, the handoff request authorizes that required work without an
additional permission pause. Load the Graphify skill and follow its documented
workflow. Keep the work limited to producing a valid required graph; unrelated
query/explain exploration and visualization remain outside this scope.

A separate graph commit is required in the exact-commit format because graph
metadata records the retained source commit that was current when generation
began. Amending, squashing, or replacing that source commit can make freshness
metadata dishonest or leave it pointing to an object unavailable in CI.

## Documentation And Semantic Markers

Documentation, media, and the canonical handoff files may create a semantic
update marker. Do not ignore or delete the marker to make validation pass.
Resolve it through the Graphify skill's supported semantic-update workflow,
using bounded semantic subagents when required. Continue normal publication
and integrity checks after that workflow succeeds.

Once the final Graphify pass starts, avoid editing handoff files for transient
CI events. A repository that requires the PR number should already contain it,
with final-head CI truthfully recorded as pending. If a failed check, blocker,
review decision, or scope change really does change resume state:

1. update and stage the canonical files with any scoped change;
2. rerun the supported incremental Graphify publication;
3. follow the commit-shape rules above—one commit for staged-snapshot/source-digest repositories, or the exact-commit fallback when structurally required;
4. run the integrity check;
5. push and wait for CI again.

Passing-check snapshots and merge timestamps belong in GitHub and the final
response, not in another handoff/graph commit cycle. Record a PR number in the
repository only when repository instructions require it, using the PR-identity
exception above.

## Integrity Failure

If the update command succeeds but the integrity check fails:

- stop publication of the invalid graph;
- preserve the last known-good graph and the scoped checkpoint work;
- report the exact update/check command and diagnostic blocker;
- follow documented Graphify recovery when it can safely resolve the failure;
  stop and report a concrete blocker when recovery would require ambiguous
  source deletion, unavailable access, or bypassing an integrity safeguard.

After supported recovery, rerun the repository-supported publication path
normally. Required local recovery does not require a separate permission pause.

Do not hand-edit `graphify-out/graph.json`, discard semantic markers, or invent
ad hoc graph-building code merely to obtain a passing exit code. If the tracked
base graph is already invalid on the remote default branch, distinguish that
pre-existing defect from the requested change and report it rather than hiding
it.

## Final Evidence

Record the incremental update command, integrity-check result, and graph-only
commit when the repository format required one. A generated graph is not
complete delivery evidence until the repository's check confirms integrity and
source freshness.
