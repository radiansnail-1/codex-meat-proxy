# Governed Loop Packets

Use these templates only when Hound enters governed loop mode, repeated-failure diagnosis, blocker recovery, multi-agent orchestration, or human-feedback propagation. Keep packets inside the benchmark file unless the user asks for separate artifacts.

## Bootstrap Note

Use when context is `seed` or `emerging`.

```text
context_maturity: seed|emerging
how_hound_applies_here:
what_not_to_force_yet:
current_user_intent:
what_success_seems_to_mean_now:
known_non_goals_or_rejections:
accepted_work_or_examples:
unknowns_that_may_change_the_project:
temporary_pipeline_guess:
temporary_evaluator_guess:
protected_boundaries_known_so_far:
evidence_or_artifact_root:
first_likely_human_objections:
minimal_circuit_breaker_threshold:
where_to_save_new_learnings:
what_would_make_this_operational:
```

## Four-Loop Run Packet

Use before scaling workers or after a circuit breaker.

```yaml
context_maturity: "seed|emerging|operational"
objective: ""
real_user_goal: ""
human_acceptance_standard: ""
loop_depth: "fast_path|governed_loop"
invariants:
  - ""
source_truth_loaded: ""
prior_learnings_to_defend:
  - ""
likely_human_objections:
  - ""
pipeline_stages:
  - name: ""
    expected_output: ""
    required_evidence: ""
    likely_blockers: []
    hard_rejects: []
    invariants_preserved: []
    handoff_contract: ""
workers:
  - id: ""
    scope: ""
    status: "pending|running|done|blocked|closed"
raw_evidence:
  - path_or_description: ""
failure_signatures:
  - ""
blocker_hypotheses:
  - ""
intervention_level: "artifact|stage|pipeline|orchestration|evaluation|objective|human_learning"
tiny_proof: ""
scale_decision: "do_not_scale|scale|branch|redesign|ask_user|blocked"
learning_propagation: ""
```

## Pipeline Map

Good stage maps make failure localization possible. Bad stage maps force final-symptom debugging.

```text
stage:
expected_output:
required_evidence:
likely_blockers:
invariant_to_preserve:
handoff_contract:
hard_rejects:
first_failed_stage_signals:
failure_signatures_to_check:
```

## Pre-Artifact Spec

Use before visual, document, UI, diagram, prompt, code, generated asset, or build artifact attempts when structure matters.

```text
artifact_goal:
audience_or_user:
real_user_objective:
concepts_or_invariants_to_preserve:
information_hierarchy:
nested_structure_or_system_topology:
main_flow:
inner_loops_or_failure_routes:
layout_or_build_architecture:
hard_rejects:
acceptance_checks:
tiny_wireframe_or_proof:
stop_condition:
```

## Worker Goal Ledger

Every worker owns a bounded local goal loop.

```text
worker_id:
assigned_scope:
parent_contract:
local_plan:
stage:
attempt_number:
input_used:
output_produced:
artifact_paths:
raw_evidence_paths:
local_check:
local_hypothesis:
tiny_proof_if_any:
predicted_parent_or_human_objection:
pass_fail:
failure_signature:
first_failed_stage:
retry_count_for_stage:
what_changed_from_prior_attempt:
next_allowed_action:
protected_files_or_side_effects:
status:
```

Rule: after two same-stage or same-signature failures, the worker stops and emits a meta-failure packet. Parent decides recovery.

## Orchestrator Dashboard

Use during multi-agent or multi-stage work.

```text
worker | scope | current_stage | attempts | first_failed_stage |
signature | evidence_path | recovery_proof_status | blocker_preflight |
status | open_closed | parent_verdict | likely_human_objection
```

Parent responsibilities:

- verify raw evidence, not only worker summaries;
- compare signatures across workers;
- patch shared contracts when multiple workers fail the same gate;
- run final-context and likely-user-objection checks;
- close workers when complete, blocked, stale, or unnecessary.

## Pause Packet

Use before a third same-stage/signature attempt.

```text
visible_repeated_failure:
first_failed_stage:
why_this_stage_is_first:
failure_signature:
attempts_already_made:
what_changed_between_attempts:
raw_evidence_inspected:
evidence_still_missing:
local_proxy_at_risk:
accepted_invariant_at_risk:
current_diagnosis:
what_would_falsify_it:
likely_user_objection:
next_materially_different_move:
stop_condition_if_repeated:
```

## Blocker Hypothesis Packet

A blocker diagnosis must be falsifiable.

```text
visible_failure:
worker_block_scope:
is_worker_block_terminal_for_parent:
first_suspected_failed_stage:
why_this_stage_is_first:
alternate_hypotheses:
raw_evidence_inspected:
evidence_still_missing:
existing_artifact_reconciliation_result:
local_control_surface_available:
recovery_proof_to_run:
recovery_proof_result:
why_blocker_is_user_facing_now:
what_would_prove_this_wrong:
local_proxy_at_risk:
accepted_invariant_at_risk:
failure_signature:
smallest_useful_probe:
```

Report blocked only when blocker preflight is complete, no proof path exists, a recovery proof repeats the failure, or a real user/tool/credential/policy decision is required.

## Step-Back Audits

Use `second_step_back` when a prior step-back still leads to the same path.

```text
current_diagnosis:
meta_failure_signature:
intervention_level:
did_diagnosis_change_evidence:
did_diagnosis_change_action:
did_diagnosis_preserve_user_words:
alternate_hypothesis:
what_would_falsify_current_diagnosis:
why_next_action_is_materially_different:
stop_condition_if_repeated:
```

Use `post_proof_step_back` before scaling a passing proof.

```text
proof_that_passed:
what_it_actually_proved:
real_user_objective_rechecked:
local_proxy_still_at_risk:
accepted_invariant_regression_check:
prior_failure_mode_that_could_recur:
likely_human_objection_after_proof:
evidence_that_would_show_proxy_success:
scale_decision:
required_patch_before_scale:
```

## Human Learning Packet

Use when the human catches a miss, changes a standard, rejects an output, or changes the target.

```text
exact_human_objection:
what_agent_optimized_instead:
true_failure_layer: artifact|stage|pipeline|orchestration|evaluation|objective|human_learning
failure_signature:
new_rule_or_standard:
invariant_or_standard_to_preserve:
proof_needed_before_scale:
where_learning_is_saved:
should_this_be_promoted: yes|no
scope: local_run|project|cross_project_skill
```

If the correction changes the project frame, record:

```text
old_objective_or_frame:
new_objective_or_frame:
which_prior_artifacts_or_decisions_are_superseded:
which_accepted_artifacts_still_survive:
pipeline_changes_required:
evaluator_changes_required:
worker_contract_changes_required:
next_tiny_proof_under_new_frame:
```

## Learning Propagation Gate

Learning is not complete just because one artifact, prompt, or file changed.

```text
learning_id:
exact_user_feedback:
what_changed:
generalized_rule:
failure_signature:
invariant_to_preserve:
affected_layers:
  goal_or_objective:
  pipeline_map:
  artifact_design_spec:
  worker_prompt_or_contract:
  orchestrator_dashboard:
  evaluator_stack:
  tiny_proof_harness:
  handoff_or_wiki_memory:
  skill_or_reusable_protocol:
proof_of_propagation:
remaining_risk:
```

Every affected layer must be synced or explicitly scoped out before scaling or final handoff.

## Evaluator Stack

Use more than one evaluator class when stakes or ambiguity are high.

```text
hard_checks:
semantic_checks:
artifact_checks:
presentation_checks:
user_objection_check:
regression_check:
```

If hard checks pass but semantic, artifact, presentation, or user-objection checks fail, classify the issue as metric laundering or proxy success.
