# D0 deployment brief

This brief fixes the customer, workflow, authority, integration, evidence, and
handoff boundaries needed to begin the synthetic portfolio implementation. The
identifier definitions are in the
[project charter](project-charter.md#identifier-key).

## Decision status

| Field | Decision |
|---|---|
| Evidence basis | External document and repository review completed August 26, 2026. No domain-expert or prospective-user interview was accessible. |
| Validation status | Buyer demand, workflow fit, adoption, and willingness to pay remain unvalidated. The review is the D0-AC3 substitute, not customer discovery evidence. |
| Initial organization | Provider organization with a prior-authorization or revenue-cycle operations function. |
| Economic buyer | Director or VP accountable for prior-authorization operations, revenue-cycle performance, or both. |
| Daily operator | Prior-authorization exception specialist. |
| First deployment | Local, synthetic, portfolio-quality demonstration for one lumbar MRI denial. |
| Authority | Administrative preparation only; the reference action remains human-review-required and unexecuted. |
| Next eligible goal | G00, proposed only after D0 verification. |

## Buyer and operator profile

The economic-buyer hypothesis is ACT-01. This person needs visibility into
exception throughput, handling cost, reviewer burden, failure modes, and control
effectiveness. The portfolio does not claim that this title, budget owner, or
purchase motivation has been validated.

The daily-operator hypothesis is ACT-02. The operator:

- reconciles case, member, payer, service, deadline, and submission status;
- finds administrative and clinical documentation already present in approved
  systems;
- identifies the exact payer requirement and policy version;
- surfaces missing, stale, duplicate, or conflicting information;
- assembles a review-ready case and a proposed administrative next action;
- routes clinical, coverage, or institutional judgment to its existing owner.

The operator does not determine clinical appropriateness, medical necessity, or
coverage and does not acquire authority merely by using the workbench.

## Stakeholder map

| Charter actor | Role in the first deployment | Engagement or handoff need |
|---|---|---|
| ACT-01 | Sponsors and evaluates the operational hypothesis. | Review value measures, limitations, and rollout criteria. |
| ACT-02 | Primary user represented by the synthetic workflow. | Validate workflow, review-ready definition, usability, and escalation fit when access becomes available. |
| ACT-03 | Reviews the proposed action and evidence. | Confirm audit fields, decision binding, and material-edit capture. |
| ACT-04 | Owns clinical or coverage judgment. | Receive bounded escalation; never be replaced by model opinion. |
| ACT-05 | Owns integration, identity, data, security, and operations. | Approve interfaces and runtime before any client environment. |
| ACT-06 | Supplies requirements and receives authorized transactions. | Represented by a deterministic simulator in the core portfolio. |
| ACT-07 | Experiences downstream delay or resolution. | No direct product or authorization role is assumed. |

## First deployment contract

The workbench receives one unresolved synthetic lumbar MRI denial stating that
conservative therapy was not demonstrated. Relevant therapy evidence exists in
versioned synthetic FHIR R4 records. The workbench gathers and cites that
evidence, retrieves the exact payer-policy version, exposes contradictions or
missing information, and proposes an appeal action.

The proposal is not authority. The deterministic authorization layer returns
`REQUIRE_HUMAN_REVIEW`; the guarded executor proves that no external action is
performed. The complete demonstration contract is in
[demo-contract.md](demo-contract.md).

## Authority boundary

| Activity | Agent | Deterministic services | Attributable human or institution |
|---|---|---|---|
| Search approved records and policy | May propose tool calls through declared read-only tools. | Enforce tool, identity, scope, and workflow limits. | Approves source access and operating envelope. |
| State a material fact | May propose only with evidence references. | Validate schema, provenance, freshness, and required fields. | Resolves genuine clinical or policy ambiguity. |
| Draft an appeal or information request | May produce a typed proposal. | Evaluate action, policy, workflow, and evidence requirements. | Reviews when rules or consequence require it. |
| Make a clinical or coverage determination | Prohibited. | Deny or require escalation. | Existing clinical or payer authority retains the decision. |
| Create an external commitment | Prohibited directly. | Only the guarded executor can act on valid authorization. | Existing delegated authority approves when required. |
| Expand permissions or operating envelope | Prohibited. | Deny by default and version all envelope changes. | Explicit approver and passing evidence are required later. |

## Integration and deployment boundaries

- Use synthetic data only; no real PHI or proprietary EHR dependency.
- Isolate FHIR R4, Da Vinci-aligned payer behavior, policy retrieval, workflow
  state, model provider, and consequential execution behind replaceable adapters.
- Keep a deterministic fake-model path and a local Docker path without paid
  cloud or model credentials.
- Select a cloud only in G19, based on what the bounded deployment must prove.
- Treat all retrieved content and external responses as untrusted data.
- Make internal authorization and executor services unreachable from the agent
  and from public interfaces.

## Adoption and handoff hypothesis

Adoption begins with a read-only, review-required exception workflow rather
than autonomous submission. The operator should see evidence, policy version,
contradictions, missing information, proposed action, and authorization result
in one review-ready package. Reviewer acceptance is not inherently good: edits,
rejections, handling time, and appropriate escalation must be visible.

Handoff requires a reproducible local setup, architecture and authority decision
records, adapter contracts and deviation logs, versioned eval evidence, release
gate, operating envelope, incident exercise, deployment runbook, and explicit
limitations. A client shadow pilot remains EV-04/B06 and requires separate
governance.

## Testing and data-vetting split

| Question | Testable without client data? | Evidence destination |
|---|---|---|
| Typed contracts, workflow transitions, authorization, executor guards, provenance, replay/idempotency, and trace reconstruction | Yes | TV-01–TV-04 across G01–G18. |
| Declared FHIR R4 and Da Vinci subset behavior and deviations | Yes, against synthetic/reference fixtures | TV-02 in G03, G04, G10, and G12. |
| Probabilistic investigation quality on declared synthetic cases | Yes, but not representative of client performance | TV-05 in G09, G11, G12, and G14. |
| End-to-end and release behavior | Yes, for the synthetic deployment | TV-06 and TV-07 in G10–G19. |
| Real case mix, missingness, coding conventions, policy variation, system latency, and exception base rates | No | Future client discovery and governed EV-04/B06 pilot. |
| Operator workflow fit, reviewer behavior, adoption, cost improvement, and ROI | No | Interviews when accessible and governed EV-04/B06 pilot. |
| Client identity, access, PHI handling, retention, security, and production integration | No | Client-approved architecture and governance before EV-04. |

Synthetic findings may support EV-01 or EV-02 only. An unchanged external
fixture may support EV-03. None of those establish EV-04 client value.

## Material ambiguity decisions

| Topic | D0 decision | Blocking status |
|---|---|---|
| Buyer and operator | Retain the provider-side ACT-01/ACT-02 hypotheses. | Non-blocking for a synthetic portfolio; unvalidated for a client pitch. |
| Workflow | Exception handling after denial, not happy-path submission. | Resolved for G00. |
| Authority | Administrative preparation only; first external action is review-required. | Resolved and mandatory. |
| Data | Synthetic FHIR R4 and policy fixtures only. | Resolved and mandatory. |
| Standards | Recognizable declared subset with adapters, validation, and deviations. | Resolved; exact fixtures selected in G03/G04. |
| Orchestration | Minimal deterministic control flow first; framework only by recorded need. | Resolved for G00. |
| Authorization engine | Typed Python rules first behind a stable decision interface. | Resolved for G00/G07. |
| Runtime | Local deterministic path first; cloud deferred to G19. | Resolved for G00. |
| Value claims | Measure synthetic/manual workflow data; make no client ROI claim. | Resolved and mandatory. |

There is no unresolved decision that changes G00's project shell, local test
foundation, adapter boundaries, or synthetic-data guard. G00 may be proposed as
the next goal. Customer validation remains a routed external finding, not an
implementation assumption.
