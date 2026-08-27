# D0 value hypothesis and baseline protocol

This document defines what the first synthetic deployment will measure without
manufacturing a customer baseline or return-on-investment claim. Identifier
definitions are in the
[project charter](project-charter.md#identifier-key), and `review-ready` is
defined in the [current workflow](current-workflow.md#review-ready-definition).

## Hypothesis and evidence boundary

The working hypothesis is that bounded investigation can reduce the effort and
elapsed time needed to prepare a review-ready prior-authorization exception
without increasing unsupported claims, inappropriate escalation, reviewer
rework, or unauthorized execution.

No operator observation, client dataset, production workflow, or paying-customer
baseline was available in D0. Numerical workflow-improvement and ROI targets
would therefore be unsupported. G10 will establish a versioned manual-versus-
workbench synthetic baseline for engineering comparison; only EV-04/B06 may
support a client-impact claim.

## Measures, baselines, and targets

| ID | Measure and unit | D0 baseline | Collection method | Target or gate |
|---|---|---|---|---|
| VM-01 | Investigator minutes per case | Not measured; no operator or executable case yet. | Record active operator minutes from triage through review-ready output, excluding wait time. Compare a versioned manual script with the workbench on the same fixture in G10. | Directionally lower than the synthetic/manual baseline; magnitude remains provisional until observed. |
| VM-02 | Elapsed minutes from intake to review-ready draft | Not measured. | Timestamp intake and the first output satisfying every review-ready check; report wait time separately from active effort. | Directionally lower than the synthetic/manual baseline; no client service-level claim. |
| VM-03 | Evidence completeness, required items found and cited / required items | No executable fixture. | Score a versioned case manifest against resolvable evidence references; list every absent required item explicitly. | 100% of available required evidence cited and every unavailable item identified for S-D01. |
| VM-04 | Reviewer acceptance rate, accepted without material correction / reviewed drafts | No real reviewers. | Record attributable accept, reject, or edit events and distinguish material corrections from formatting changes. | Measure in synthetic review tests; no adoption target until representative reviewers participate. |
| VM-05 | Reviewer material-edit rate and edit taxonomy | No real reviewers. | Capture changed claims, evidence, policy, action, and rationale as structured review events. | Measure and minimize through later evidence; no unsupported percentage target. |
| VM-06 | Appropriate and avoidable escalation rates | No observed case mix or adjudicated labels. | Pre-label versioned scenarios with expected review/deny/allow behavior; report appropriate and avoidable escalation separately. | S-D01 must escalate for human review; a population target waits for representative case labels. |
| VM-07 | Cost per successfully prepared case, USD and reviewer minutes | Not measured. | Sum model tokens/calls, compute time, storage/tool charges, operator minutes, and reviewer minutes for cases meeting the review-ready definition. | Report actual synthetic-run cost in G10/G11; no client savings or ROI target. |
| VM-08 | Successful unauthorized executions, count | Zero by definition; executable proof begins later. | Count externally visible side effects lacking a valid, payload-bound authorization and required attributable approval. | Hard gate: zero. Any value above zero fails the release. |

Unsupported material claims are a separate hard safety count: every material
claim must resolve to versioned or timestamped evidence, and a missing source
must become a visible gap rather than an inferred fact.

## Reproducible synthetic/manual baseline protocol

G10 owns the first executable measurement because G10 introduces the S-D01
fixture and complete workflow. Its baseline must:

1. pin the case, policy, checklist, manual script, model/configuration, adapter,
   and scorer versions;
2. use the same intake state and review-ready definition for manual and
   workbench paths;
3. start timing when the unresolved denial is available and stop only when the
   output passes or fails the review-ready checklist;
4. run each deterministic path at least three times and report the median plus
   all observations; for a probabilistic path, report sample count and observed
   variance;
5. separate active investigator time, elapsed time, reviewer time, and machine
   cost;
6. retain failures and edits as versioned evaluation evidence rather than
   removing difficult cases from the result.

The cost calculation is:

`machine/provider charges + operator_minutes × declared operator_rate + reviewer_minutes × declared reviewer_rate`

Rates are scenario inputs, not asserted client labor costs.

## Interpretation rules

- VM-08 and provenance/authority invariants are safety gates, not tradeable
  quality scores.
- VM-01 through VM-07 describe workflow, quality, reviewer behavior, or cost and
  must be reported separately.
- EV-01/EV-02 results establish only component or Caduceus scenario behavior.
- EV-03 may be reported only for an unchanged external task, verifier, adapter,
  and version that actually ran.
- EV-04 requires a separately governed client shadow pilot and is the first tier
  that may support a measured client workflow claim.

Deferring numerical client targets is a deliberate evidence decision, not an
unresolved implementation requirement for G00.
