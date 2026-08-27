# D0 current workflow and system map

This is a sourced but unvalidated provider-side workflow hypothesis. It is not
an interview-derived service blueprint. The identifier definitions are in the
[project charter](project-charter.md#identifier-key).

## Evidence basis and limits

- The [HL7 Da Vinci PAS workflow](https://hl7.org/fhir/us/davinci-pas/2022May/usecases.html)
  describes determining whether authorization is required, gathering required
  documentation, submitting it, responding to requests for more information,
  and checking status.
- The [CMS prior-authorization API fact sheet](https://www.cms.gov/newsroom/fact-sheets/cms-interoperability-prior-authorization-final-rule-cms-0057-f)
  requires affected payers to support requests/responses, specific denial
  reasons, and requests for additional information on applicable timelines.
- The [2024 AMA physician survey](https://www.ama-assn.org/system/files/prior-authorization-survey.pdf)
  documents material physician/practice burden and limited staff capacity, but
  it does not validate this project's buyer, operator, or software design.

These sources establish a credible administrative problem and common flow. They
do not reveal one client's actual screens, handoffs, staffing, data quality,
exception mix, or purchasing process.

## Current-state hypothesis

| Step | Primary actor | Typical system or artifact | Work and handoff | Failure point |
|---|---|---|---|---|
| 1. Receive denial or request | Payer endpoint, intake staff | Portal, fax, email, work queue, EHR/task system | Create or update the case and attach the payer response. | Duplicate intake, missing identifier, unclear denial reason, deadline not captured. |
| 2. Triage exception | ACT-02 | Work queue, payer portal, notes | Confirm member, coverage, service, requester, payer, status, and due date. | Records disagree, status is stale, or prior submission cannot be found. |
| 3. Determine requirement | ACT-02 | Payer portal, policy repository, CRD-like response | Identify whether authorization applies and which documentation/policy governs. | Requirement differs by payer/product or multiple policies appear applicable. |
| 4. Gather documentation | ACT-02, care-team staff | EHR/FHIR resources, scanned notes, procedure and therapy records | Search approved sources and request missing material. | Information is fragmented, malformed, stale, duplicated, or absent. |
| 5. Reconcile evidence and policy | ACT-02 | Records plus exact policy version | Map each relevant fact to evidence and policy sections; expose conflicts. | Staff must interpret ambiguous language or clinical significance beyond administrative authority. |
| 6. Assemble review-ready case | ACT-02 | Case packet, draft, checklist | Package identifiers, cited evidence, policy, contradictions, gaps, and proposed next action. | Reviewer must repeat search because evidence or rationale is not attributable. |
| 7. Review and decide | ACT-03/ACT-04 | Review queue and source systems | Approve, reject, edit, or escalate within existing authority. | Approval identity, rationale, or payload binding is missing; model confidence substitutes for authority. |
| 8. Submit or request information | Authorized endpoint | PAS/payer API, portal, fax, or other approved channel | Execute only the action authorized for the same case and payload. | Premature, duplicate, stale, or mismatched submission. |
| 9. Monitor and resolve | ACT-02 and payer endpoint | Work queue, status inquiry, payer response | Track pending status, additional-information request, appeal, approval, denial, or closure. | Polling loops, missed updates, inconsistent states, or untraceable commitment. |

## First product intervention

The first slice enters after step 1 with a denial already received. It assists
steps 2–6 and prepares a typed proposal for step 7. It does not automate clinical
or coverage judgment and stops before step 8 because S-D01 requires human
review.

The workbench should reduce search and assembly work by:

1. retrieving declared synthetic FHIR R4 records and payer-policy material;
2. validating identifiers, source versions, and workflow state;
3. linking every material claim to evidence;
4. listing contradictions, missing information, and stale material;
5. drafting a structured appeal proposal;
6. sending that proposal to independent deterministic authorization;
7. presenting the review-required result and complete trace.

## Review-ready definition

A case is review-ready only when all of the following are visible and
machine-checkable where applicable:

- case, patient/member, coverage, payer, service, requester, and deadline
  identifiers;
- current workflow state and prior-submission status;
- exact payer policy ID, version, and cited sections;
- every material administrative assertion linked to a resolvable source;
- required documentation present or explicitly listed as missing;
- stale, duplicate, malformed, irrelevant, or conflicting evidence identified;
- clinical, coverage, or policy ambiguity marked for the correct authority;
- one typed proposed next action with reason and evidence references;
- authorization result, reason codes, and required reviewer role;
- no external side effect before valid authorization and any required review.

Review-ready does not mean clinically correct, covered, approved, or authorized
for execution.

## System boundary map

| Boundary | Portfolio representation | Future client question |
|---|---|---|
| Patient/coverage/encounter record | Synthea-derived FHIR R4 fixtures behind an adapter | Which EHR/FHIR endpoints, profiles, access scopes, and data-quality constraints apply? |
| Payer behavior | Deterministic Da Vinci-aligned simulator | Which payer APIs, portals, clearinghouses, and fallback channels are actually used? |
| Policy | Versioned local repository | What is authoritative, how are updates detected, and who interprets ambiguity? |
| Workflow state | Deterministic service | Which existing queue owns state and how are races/duplicates resolved? |
| Human review | Synthetic attributable identity and review record | Which roles can approve, reject, edit, or escalate? |
| Consequential action | Guarded test executor | Which organizational endpoint may submit and what authorization proof does it require? |
| Observability | Correlated structured trace | What retention, redaction, audit, and incident requirements apply? |

## Discovery questions retained for external validation

- Which exceptions consume the most operator time and which are most frequent?
- What exact event starts and ends an exception specialist's work?
- Which sources are authoritative when records or policies disagree?
- What makes a case review-ready to the operator and reviewer?
- Which edits are administrative corrections versus clinical judgment?
- Which handoffs, deadlines, and system limitations cause rework?
- What baseline time, cost, acceptance, and escalation data already exists?
- What would cause operators, reviewers, security, or integration owners to reject
  the workflow?

These questions are routed to B07 and must be answered before making a client
workflow-fit or ROI claim.
