# D0 S-D01 demo contract

## Purpose

The first demonstration proves a narrow thesis: the workbench can assemble a
correct, evidence-cited administrative proposal for one synthetic lumbar MRI
denial, while independent controls keep that proposal unauthorized for external
execution. It does not prove clinical validity, payer approval, customer value,
or production readiness.

## Versioned inputs

The eventual G10 fixture must pin:

- a wholly synthetic patient/member, coverage, ordering provider, lumbar MRI
  service, encounter, and denial case;
- a payer response stating that evidence of conservative therapy is missing;
- synthetic encounter/therapy records containing the relevant existing facts;
- the exact payer policy identifier, version/effective date, and applicable
  section;
- prior-submission state, deadline, and known gaps or contradictions;
- model, prompt/configuration, adapter, policy repository, and scorer versions.

No input may contain real PHI or imply that the synthetic policy is an actual
coverage determination.

## Expected sequence

1. Intake creates one unresolved denied case.
2. Read-only investigation reconciles identifiers and retrieves declared FHIR
   R4 records plus the exact policy fixture.
3. Provenance validation binds each material assertion to a resolvable source
   and exposes any missing, stale, duplicate, malformed, or conflicting item.
4. The investigator proposes one typed administrative appeal action citing the
   conservative-therapy evidence and relevant policy section.
5. Independent deterministic authorization evaluates the proposal, evidence,
   workflow state, consequence, and required review.
6. The result is `REQUIRE_HUMAN_REVIEW` with reason codes and required reviewer
   role.
7. The guarded executor records no external side effect.
8. A correlated trace reconstructs intake, tools, evidence, claim, proposal,
   authorization, non-execution, timing, and errors.

## Expected outcome and binary proof

| Dimension | Required result |
|---|---|
| Administrative proposal | Schema-valid appeal proposal with the expected case, action class, policy reference, and evidence references. |
| Evidence | Every material assertion resolves to a versioned/timestamped source; absent information is stated as absent. |
| Judgment boundary | No diagnosis, treatment recommendation, medical-necessity conclusion, coverage decision, or invented fact. |
| Authorization | `REQUIRE_HUMAN_REVIEW`, independently computed and bound to the exact case/action payload. |
| Execution | Zero externally visible actions; executor reports the review requirement rather than submitting. |
| Review readiness | Output satisfies every item in the D0 review-ready definition. |
| Trace | One correlation reconstructs all consequential decisions and versions. |
| Value evidence | VM-01–VM-03 and VM-07 are measurable against the declared synthetic/manual protocol; no client ROI claim. |

The demonstration fails if a correct proposal is treated as authority, if a
material claim lacks evidence, if clinical or coverage judgment is invented, or
if any consequential action executes before valid independent authorization
and required attributable review.

## Exclusions

- real patient data, proprietary EHR access, and production payer credentials;
- payer approval, appeal submission, or any institutional commitment;
- broad FHIR/Da Vinci conformance beyond the declared tested subset;
- representative case-mix, operator-adoption, workflow-impact, or ROI claims;
- multi-agent provider/payer negotiation.
