# Project charter and product contract

This charter is the project's acceptance-driven PRD and stable product-level
contract. It extracts durable intent from
[`bounded_healthcare_agency_project.md`](../bounded_healthcare_agency_project.md).
The original specification remains the intent source; this file supplies a
customer, value, deployment, evidence, and acceptance model plus stable
identifiers that roadmap goals can reference without copying project-wide
prose.

## Identifier key

Identifiers are stable references, not priority rankings. Numbers are local to
their namespace and are not reused for a different meaning.

| Pattern | Meaning |
|---|---|
| `ACT-##` | Product actor or stakeholder. |
| `VM-##` | Value or workflow measure. |
| `DH-##` | Deployment hypothesis. |
| `EV-##` | Evidence tier. |
| `BR-##` | Build-versus-reuse decision subject. |
| `AS-##` | Assumption or open product decision. |
| `O##` | Canonical project outcome. |
| `C##` | Architecture or product constraint. |
| `TV-##` | Testing and vetting layer. |
| `S-{category}##` | Single-institution acceptance scenario. |
| `M-{category}##` | Multi-agent acceptance scenario. |
| `D0` | Discovery and deployment-definition goal. |
| `G##` | Core implementation goal. |
| `MA-#` | Future multi-agent goal. |
| `{goal}-AC#` | Binary acceptance criterion local to a goal, such as `G11-AC8` or `MA7-AC4`. |
| `FP-#` | Entry criterion for the future multi-agent phase. |
| `B##` | Backlog item outside the ordered roadmap. |

Scenario category codes are `R` for routine, `A` for ambiguous, `S` for
safety-sensitive, `F` for system or operational failure, `X` for adversarial,
and `D` for a thesis-defining demonstration. For example, `S-A05` is
single-institution ambiguous scenario 05 and `M-X03` is multi-agent adversarial
scenario 03. Example payload identifiers such as `CASE-0083`, `CLAIM-17`, or
`AUTH-9911` are domain data, not planning namespaces.

## Thesis

Build a provider-side prior-authorization exception workbench showing that
probabilistic systems can investigate and propose useful work while
deterministic policy, provenance, workflow constraints, evaluation evidence,
and human approval bound consequential actions.

> Probabilistic systems propose. Deterministic systems authorize.

The first buyer hypothesis is a provider prior-authorization or revenue-cycle
operations organization; the daily operator is an exception specialist. The
core reference workflow is one lumbar MRI denial that produces the correct
administrative proposal but remains review-required and unexecuted. This buyer
hypothesis was retained after D0's external evidence review and remains
unvalidated until direct domain-expert or prospective-user evidence is
available.

The differentiated contribution is evidence-aware institutional authorization,
not generic agent orchestration, prior-authorization automation, synthetic FHIR,
allow/review/deny policy, or multi-agent messaging. The portfolio uses synthetic
data only and should reuse recognizable standards and existing systems around
that control plane.

## Product problem and promise

Provider prior-authorization denials create high-variance exception work across
fragmented records, payer requirements, policy versions, workflow systems, and
organizational handoffs. An exception specialist must assemble a review-ready
case without inventing missing facts, applying stale policy, making a clinical
or coverage decision, or creating an unauthorized external commitment.

The product hypothesis is that a bounded investigation system can perform the
mechanical search, reconciliation, citation, and drafting work while independent
controls preserve institutional authority.

> A policy-enforced exception workbench that assembles cited evidence and
> drafts prior-authorization actions, while deterministic controls and
> attributable human review govern every external commitment.

The initial product is not a happy-path form-submission tool. It concentrates on
cases that are unresolved, incomplete, contradictory, stale, or otherwise
unsafe to automate without explicit evidence and authority checks.

## Target actors and decision rights

These actors were retained as bounded design hypotheses after D0's external
evidence review; they have not been customer-validated. The authority column
defines product boundaries, and organizational titles may change without
changing those boundaries.

| ID | Actor | Primary need | Decision right or boundary |
|---|---|---|---|
| ACT-01 | Economic buyer: provider prior-authorization or revenue-cycle director/VP | Improve exception throughput, consistency, cost visibility, and control. | Sets deployment priorities and acceptable operational risk; does not gain clinical or payer authority through the product. |
| ACT-02 | Daily operator: prior-authorization exception specialist | Find the right administrative evidence, reconcile requirements, and prepare a complete next action. | Prepares and routes administrative work; does not decide clinical appropriateness or payer coverage. |
| ACT-03 | Attributable reviewer or operations supervisor | Inspect cited evidence, contradictions, policy, and the proposed action efficiently. | Approves, rejects, or edits work only within existing delegated institutional authority. |
| ACT-04 | Clinical or coverage authority | Receive genuine judgment questions with adequate context. | Retains clinical, medical-necessity, and coverage decisions outside the agent's authority. |
| ACT-05 | Integration, security, and platform owner | Deploy and operate a bounded, observable system against approved interfaces. | Approves technical access, data handling, identity, security, and operational controls. |
| ACT-06 | Payer or external organizational endpoint | Exchange requirements, status, evidence requests, and authorized submissions. | Remains a separate and untrusted authority domain; the core portfolio uses a deterministic simulator. |
| ACT-07 | Patient and care team | Avoid preventable administrative delay and opaque case handling. | Are affected stakeholders, not an implied source of product or institutional authorization. |

## Current workflow and product intervention

The hypothesized current-state workflow is:

1. Receive and classify an unresolved denial or documentation request.
2. Reconcile identifiers, case status, deadlines, and prior submissions.
3. Search encounters, procedures, notes, and other administrative evidence.
4. Identify the applicable payer requirement and exact policy version.
5. Surface missing, stale, duplicated, or contradictory information.
6. Assemble a review-ready case and draft a structured next action.
7. Route judgment to an attributable reviewer and execute only an independently
   authorized action.

D0 replaced this outline with a sourced workflow map covering likely handoffs,
systems, failure points, and a testable review-ready definition. Because no
interviews were accessible, those operational details remain hypotheses routed
to B07 for direct validation. The product intervention is bounded as follows:

| Current failure mode | Product capability | Preserved boundary |
|---|---|---|
| Evidence is fragmented or difficult to locate. | Search approved sources and connect every material claim to cited evidence. | The system does not infer missing clinical facts. |
| Requirements are ambiguous, overlapping, or stale. | Retrieve and compare exact, versioned policy material. | The system does not make a clinical or coverage determination. |
| Drafting is inconsistent or difficult to review. | Produce a typed proposed action with contradictions and missing information visible. | The proposal carries no authority by itself. |
| External actions can outpace review or workflow state. | Apply deterministic policy, workflow, disclosure, and human-review gates. | Authority is deny-by-default and cannot be granted by the model. |
| Decisions are hard to explain after the fact. | Preserve a correlated, structured decision trace. | Explanatory text cannot replace source evidence or authorization records. |

## Value and success hypothesis

The initial value hypothesis is that bounded automation can reduce the time and
effort required to produce a review-ready exception case without increasing
unsupported claims, inappropriate escalation, or unauthorized action.

| ID | Measure | Intended interpretation |
|---|---|---|
| VM-01 | Investigator minutes per case | Operator effort required to prepare a case. |
| VM-02 | Elapsed time from intake to review-ready draft | Workflow speed, reported separately from operator effort. |
| VM-03 | Evidence completeness | Required evidence found, cited, and made reviewable. |
| VM-04 | Reviewer acceptance rate | Share of drafts accepted without a material correction. |
| VM-05 | Reviewer material-edit rate | Frequency and type of changes needed before approval. |
| VM-06 | Appropriate and avoidable escalation rates | Whether the system routes genuine judgment and avoids unnecessary review. |
| VM-07 | Cost per successfully prepared case | Model, infrastructure, and review cost for a case meeting the review-ready definition. |
| VM-08 | Successful unauthorized executions | Hard safety guardrail; the required value is zero. |

Goal D0 owns the baseline and target definitions. Until operator or client data
exists, workflow targets must use a reproducible synthetic/manual baseline and
remain explicitly provisional. A component score, project scenario, or
standards fixture does not establish customer value or ROI.

## Deployment hypothesis

| ID | Dimension | Initial hypothesis |
|---|---|---|
| DH-01 | Organization | A provider-side prior-authorization or revenue-cycle operation. |
| DH-02 | First workflow | One lumbar MRI denial in which conservative-therapy evidence may exist across fragmented synthetic records. |
| DH-03 | Data mode | Synthetic FHIR R4 data only for the portfolio; no real PHI or proprietary EHR dependency. |
| DH-04 | Integration boundary | Replaceable adapters for FHIR records, Da Vinci-aligned payer behavior, policy retrieval, and workflow state. |
| DH-05 | Operator interaction | An exception workbench that returns a cited, review-ready case rather than an autonomous coverage decision. |
| DH-06 | Initial authority | The reference demonstration ends correct-but-not-authorized, with the external action review-required and unexecuted. |
| DH-07 | Runtime | A reproducible local Docker path first; select a cloud target only when the deployment brief identifies what it must prove. |
| DH-08 | Handoff | Documentation, decision records, evaluation evidence, operating-envelope controls, incident proof, and a runbook sufficient for another team to operate the bounded system. |

The first deployment is a portfolio-quality synthetic demonstration. Client
discovery is workflow mapping and architecture work only. A shadow pilot is a
separately governed future engagement and inherits no authority or readiness
claim from the synthetic deployment.

## Evidence and validation plan

Product, safety, standards, and customer-value claims use different evidence
tiers and may not be collapsed into one score.

| Tier | Evidence | Claim permitted |
|---|---|---|
| EV-01 | Component tests | A schema, rule, state transition, or adapter behaves as specified. |
| EV-02 | Caduceus project scenarios | The documented synthetic thin slice behaves correctly across its declared cases. |
| EV-03 | Unchanged external benchmark or standards fixture | Only the exact task, verifier, adapter, and version that actually ran may be reported. |
| EV-04 | Governed client shadow pilot | A measured client workflow result under client-approved data, access, and operating controls. |

EV-01 and EV-02 are required for the core portfolio. EV-03 is conditional on
semantic comparability and actual execution. EV-04 is outside the core roadmap
and cannot be inferred from synthetic results.

Customer discovery is also evidence. Goal D0 should incorporate at least three
domain-expert or prospective-user conversations when accessible. A sourced
document review may substitute for momentum, but it must be labeled unvalidated
and cannot validate buyer demand, workflow fit, adoption, or willingness to pay.

## Build-versus-reuse decision policy

The following are initial postures, not completed architecture decisions. Goal
D0 records a reasoned adopt, adapt, interoperate, or reimplement decision for
each; later goals verify those choices against working contracts.

| ID | Adjacent capability | Initial posture |
|---|---|---|
| BR-01 | Synthea synthetic records | Adopt or adapt generated records; do not build a competing synthetic-patient generator. |
| BR-02 | FHIR R4 | Interoperate through a declared, validated profile subset and isolate deviations behind an adapter. |
| BR-03 | Da Vinci PAS/DTR/CRD concepts and reference implementations | Adapt or interoperate for recognizable provider/payer contracts; do not claim broad conformance from a thin slice. |
| BR-04 | OPA, OpenLeash, AgentGate, or adjacent authorization tools | Evaluate reuse, but implement only the thesis-specific evidence and institutional-authority controls that are not supplied. |
| BR-05 | LangGraph or another durable workflow runtime | Start with the simplest deterministic orchestration that satisfies the workflow; adopt a runtime when durability or human-review requirements justify it. |
| BR-06 | HealthAdminBench | Crosswalk or adapt only when task and verifier semantics are compatible; never publish a benchmark score for changed tasks. |
| BR-07 | A2A | Defer to the gated multi-agent phase and interoperate through a healthcare transaction profile rather than recreating a generic protocol. |
| BR-08 | Existing healthcare-agent demonstrations | Use as comparison baselines and integration references; do not reproduce generic agent orchestration as the project's claimed contribution. |

## Assumptions and open product decisions

| ID | Assumption or decision | Current status | Resolution gate |
|---|---|---|---|
| AS-01 | Provider prior-authorization leadership is the initial economic buyer. | Retained but unvalidated after D0 evidence review. | B07 direct discovery evidence. |
| AS-02 | An exception specialist is the daily operator and the documented workflow reflects their highest-friction work. | Retained but unvalidated after D0 evidence review. | B07 workflow and operator evidence. |
| AS-03 | Reducing effort and time to a review-ready case is valuable without increasing risk or review burden. | Retained but unvalidated after D0 evidence review. | G10 synthetic baseline; EV-04/B06 for a client claim. |
| AS-04 | Operators and reviewers agree on a testable definition of review-ready. | Definition specified in D0 but user agreement is unvalidated. | B07 operator/reviewer evidence. |
| AS-05 | A narrow FHIR R4 and Da Vinci-aligned adapter surface can be recognizable without overstating conformance. | D0 design decision; not yet contract-tested. | G03/G04 contract tests, then G12 external alignment. |
| AS-06 | Some external evaluation tasks can be compared without changing their verifier semantics. | Unknown. | G12 crosswalk and evidence report. |
| AS-07 | The selected deployment footprint, adoption model, and handoff package fit a prospective client environment. | Unknown. | D0 hypothesis, G19 deployment proof, and future client validation. |
| AS-08 | The project creates sufficient interview or client interest to justify a governed shadow pilot. | Unknown. | G20 portfolio feedback and backlog item B06. |

AS-01 through AS-04 remain material inputs to a real deployment. D0 bounded
them sufficiently for the synthetic portfolio shell; B07 or later client
evidence may revise them, in which case the charter and affected roadmap goals
must be updated before making customer-fit claims.

## Canonical project outcomes

| ID | Outcome |
|---|---|
| O01 | Model a consequential enterprise workflow. |
| O02 | Give an investigation agent multiple tools and data sources. |
| O03 | Let the agent investigate cases and propose structured actions. |
| O04 | Prevent the agent from granting itself authority. |
| O05 | Evaluate proposed actions with an independent deterministic policy layer. |
| O06 | Require attributable human review when rules, evidence, or consequence demand it. |
| O07 | Preserve provenance for material claims and actions. |
| O08 | Reconstruct every consequential decision from structured traces. |
| O09 | Evaluate normal, ambiguous, safety-sensitive, system-failure, and adversarial cases. |
| O10 | Convert important failures into regression tests. |
| O11 | Produce measurable release criteria and a deterministic release decision. |
| O12 | Expand or contract a versioned operating envelope only from deployment evidence and approval. |
| O13 | Translate a named operator's workflow and constraints into a bounded technical deployment. |
| O14 | Integrate recognizable healthcare standards and existing reference systems instead of replacing them with bespoke approximations. |
| O15 | Measure workflow impact, reviewer adoption, and cost per successful case separately from model quality and safety. |
| O16 | Produce a repeatable discovery, deployment, evaluation, adoption, and handoff playbook. |
| O17 | Represent provider and payer as mutually untrusted institutional identity and authority domains. |
| O18 | Exchange typed, authenticated institutional transactions instead of free-form agent conversation. |
| O19 | Independently gate outbound messages, commitments, and minimum-necessary disclosure. |
| O20 | Independently verify inbound identity, integrity, authorization metadata, schema, and replay protection. |
| O21 | Represent sourced agreement and disagreement structurally and bound negotiation with deterministic stop conditions. |
| O22 | Escalate unresolved or high-consequence disputes to attributable humans and separately authorize binding commitments. |
| O23 | Evaluate, release-gate, and reconstruct governed transactions across institutional audit boundaries. |

## Canonical acceptance scenarios

These are project scenarios, not automatically goal-level acceptance criteria.
Goals reference the scenario IDs they advance. Executable fixtures receive their
own IDs when the evaluation harness is introduced.

| ID | Category | Scenario |
|---|---|---|
| S-R01 | Routine | All required documentation is present. |
| S-R02 | Routine | A required identifier is missing. |
| S-R03 | Routine | The payer requests a known document. |
| S-R04 | Routine | A submission is duplicated. |
| S-A01 | Ambiguous | Encounter dates conflict. |
| S-A02 | Ambiguous | Therapy history is incomplete. |
| S-A03 | Ambiguous | Applicable policy language is ambiguous. |
| S-A04 | Ambiguous | Multiple policies may apply. |
| S-A05 | Ambiguous | The selected policy version is stale. |
| S-S01 | Safety | The case requires clinical interpretation. |
| S-S02 | Safety | Evidence conflicts with physician assessment. |
| S-S03 | Safety | The agent attempts to infer missing clinical facts. |
| S-S04 | Safety | A correct proposed action still requires human approval. |
| S-F01 | Failure | The synthetic FHIR R4 adapter times out. |
| S-F02 | Failure | A retrieved resource is malformed. |
| S-F03 | Failure | The payer API times out. |
| S-F04 | Failure | A cached record is stale. |
| S-F05 | Failure | A tool response is partial. |
| S-F06 | Failure | A tool response has an unexpected schema. |
| S-F07 | Failure | Records are duplicated. |
| S-X01 | Adversarial | A note contains instruction-like text. |
| S-X02 | Adversarial | A retrieved document attempts prompt injection. |
| S-X03 | Adversarial | A source falsely claims to override policy. |
| S-X04 | Adversarial | Tool output requests credential disclosure. |
| S-X05 | Adversarial | Evidence is misleading but irrelevant. |
| S-D01 | Demonstration | The agent's conclusion is correct but it is not authorized to execute the action. |
| M-R01 | Multi-agent routine | A provider submits typed evidence and the payer verifies and accepts the transaction. |
| M-R02 | Multi-agent routine | Deterministic facts or authoritative sources resolve the disagreement. |
| M-A01 | Multi-agent ambiguous | A stale policy claim is detected and cannot govern the transaction. |
| M-A02 | Multi-agent ambiguous | A legitimate policy or clinical disagreement requires human adjudication. |
| M-X01 | Multi-agent adversarial | A counterparty message attempts prompt injection. |
| M-X02 | Multi-agent adversarial | A counterparty presents a forged commitment. |
| M-X03 | Multi-agent adversarial | A counterparty presents a forged authorization token. |
| M-X04 | Multi-agent adversarial | A previously accepted transaction is replayed. |
| M-X05 | Multi-agent adversarial | A counterparty requests irrelevant protected information. |
| M-X06 | Multi-agent adversarial | A transaction includes a malicious evidence pointer. |
| M-X07 | Multi-agent adversarial | A counterparty attempts schema smuggling, message tampering, or permission expansion. |
| M-F01 | Multi-agent failure | Clarification requests form an infinite or excessive loop. |
| M-F02 | Multi-agent failure | Institutional systems issue contradictory commitments. |
| M-F03 | Multi-agent failure | Human and agent decisions race or conflict. |
| M-D01 | Multi-agent demonstration | A complete provider-payer dispute ends in an attributable, separately authorized commitment. |

## Architecture constraints

| ID | Constraint |
|---|---|
| C01 | Use synthetic data only; never add real PHI. |
| C02 | The LLM may investigate and propose but may not authorize or execute consequential actions. |
| C03 | Authorization operates on typed structured inputs using deterministic rules and no LLM call. |
| C04 | Only the executor may perform consequential state changes, and it requires a valid authorization decision. |
| C05 | Workflow transitions are enforced outside the agent. |
| C06 | Every material claim links to versioned or timestamped source evidence. |
| C07 | Human approvals and rejections are attributable and audited. |
| C08 | Retrieved content and tool output are untrusted and cannot change policy or permissions. |
| C09 | Authority is deny-by-default and bounded by a versioned operating-envelope manifest. |
| C10 | Important fixes include a minimal regression scenario. |
| C11 | Prefer transparent, replaceable model integration and deterministic orchestration where appropriate. |
| C12 | Build the working system before UI polish, broad standards conformance, or proprietary integrations. |
| C13 | Complete and stabilize the single-agent core before beginning any `MA-*` goal. |
| C14 | Treat provider and payer institutions and all counterparty content as mutually untrusted. |
| C15 | Agents do not transact directly; authorized organizational endpoints send and receive transactions. |
| C16 | Cross-boundary workflow is driven by typed transactions; natural language is non-binding data. |
| C17 | Institutional commitments require a separate authority decision and authenticated transaction. |
| C18 | Disclosure authority is independent of argumentative usefulness and enforces purpose, scope, classification, retention, and minimum necessity. |
| C19 | Negotiation uses a predefined action/transition space with deterministic limits and escalation. |
| C20 | Do not use an LLM as a legally or institutionally authoritative arbitrator. |
| C21 | Distributed traces share correlation while preserving each institution's audit boundary. |
| C22 | Each multi-agent participant has distinct internal-authority and external-transaction envelopes. |
| C23 | The initial buyer is provider-side and the operator is a prior-authorization exception specialist unless discovery evidence records a justified change. |
| C24 | Record an adopt, adapt, interoperate, or reimplement decision before recreating an adjacent standard, repository, framework, or service. |
| C25 | The thin slice uses recognizable FHIR R4 and Da Vinci PAS/DTR concepts, validates its declared subset, and documents intentional deviations. |
| C26 | Keep hard safety, end-to-end success, component quality, workflow impact, reviewer behavior, latency, and cost measures distinct; never manufacture client ROI. |
| C27 | Label component, project-scenario, external-benchmark, and shadow-pilot evidence separately; publish no external benchmark score unless unchanged tasks and verifiers actually ran. |

## Non-goals

- Diagnosis, treatment recommendation, or claims of clinical validity.
- Real PHI or a dependency on proprietary EHR access.
- Model self-confidence as a primary safety mechanism.
- An LLM authorizing its own work.
- Optimizing primarily for autonomous-action rate.
- Simulating an entire hospital or polishing a UI before the core system works.
- Free-form agent negotiation, model identity as authority, or one institution
  minting authority for another.
- Building competing FHIR, Da Vinci, policy-engine, orchestration, or A2A
  standards when an adapter or established primitive is sufficient.
- Pitching the initial product simultaneously to providers, payers, regulators,
  and generic agent-platform buyers.
- Claiming production, clinical, HIPAA, legal, regulatory, client-ROI, or
  external-benchmark readiness from synthetic project evidence.

## Project-wide definitions

- **Consequential action:** an externally visible or state-changing action such
  as submitting an appeal, requesting information, updating status, or closing a
  case.
- **Material claim:** an assertion used to select policy, justify an action, or
  affect an authorization outcome.
- **Authorization correctness:** the deterministic decision matches the
  scenario expectation for the same structured request.
- **Complete trace:** correlates case, agent/config versions, tool activity,
  sources, claims, action request, authorization, any human decision, execution,
  timing, and errors.
- **Institutional transaction:** a typed, authenticated cross-boundary message
  sent by an authorized organizational endpoint; it is not made authoritative by
  agent authorship or counterparty acceptance.
- **Commitment:** a binding institutional transaction separately authorized by
  the sender's authority gate, distinct from explanatory or negotiating text.
- **Review-ready case:** an administrative case whose identifiers, relevant
  evidence, exact policy reference, contradictions, missing information, and
  proposed next action are assembled for an authorized reviewer without making
  a clinical or coverage determination.
- **Evidence tier:** one of component test, Caduceus project scenario, unchanged
  external benchmark/standards fixture, or separately governed shadow-pilot
  evidence. Claims from one tier do not imply another.
- **Shadow pilot:** a future client-controlled deployment that observes or
  prepares workflow outputs under client-approved governance without inheriting
  production authority from the synthetic portfolio system.

## Testing and vetting strategy

Development is test-first where behavior can be specified deterministically and
evaluation-first where behavior is probabilistic. Data-specific details refine
fixtures, distributions, and thresholds later; they do not postpone testing the
system's authority, workflow, provenance, and failure-containment boundaries.

| ID | Layer | Required approach | Primary proof |
|---|---|---|---|
| TV-01 | Deterministic units | Define expected behavior before implementing domain contracts, workflow transitions, policy rules, provenance validation, and executor guards. | Fast unit tests with exact assertions. |
| TV-02 | External contracts | Define the supported profile, schema, error behavior, and intentional deviations before implementing an adapter. | Versioned consumer/provider contract tests and reference fixtures. |
| TV-03 | Safety properties | Test invariants across valid, invalid, missing, duplicated, stale, and reordered inputs. | Negative, boundary, property-based, and state-transition tests. |
| TV-04 | Project scenarios | Add a versioned fixture with an expected action shape, evidence requirements, authorization outcome, and severity before fixing a material scenario failure. | Executable `S-*` or `M-*` scenario and retained regression test. |
| TV-05 | Probabilistic investigation | Specify eval cases and scoring rules before changing prompts, tools, retrieval, or models; avoid exact-string tests when semantic structure is the requirement. | Repeatable eval run with versioned model/configuration, fixtures, scorers, and variance where relevant. |
| TV-06 | End-to-end workflow | Exercise the complete path separately from component and subtask success. | Trace-linked case result covering intake, investigation, proposal, authorization, review, and permitted execution behavior. |
| TV-07 | Release vetting | Evaluate hard safety gates independently from quality, workflow, reviewer, latency, and cost targets. | Deterministic release decision and versioned evidence report. |
| TV-08 | Operational and customer validation | Validate data fit, operator behavior, workflow impact, and value only in the evidence tier that supports the claim. | D0 discovery evidence, reproducible synthetic baseline, or separately governed EV-04 shadow-pilot evidence. |

The following invariants are testable before representative client data exists:

- no consequential action executes without a valid independent authorization;
- the model cannot mint, expand, or override its permissions;
- invalid workflow transitions fail closed;
- every material claim has a valid evidence reference;
- missing, contradictory, or stale evidence produces the expected review or
  denial outcome;
- malformed, partial, timed-out, or adversarial tool output cannot change
  policy or authority;
- duplicate submissions and replay attempts are rejected or handled
  idempotently;
- a correct proposal may remain review-required and unexecuted, as in S-D01;
- every consequential decision can be reconstructed from its structured trace.

Representative data or operator evidence is required to determine realistic
missingness, coding and documentation variation, payer-policy variation, case
mix and base rates, production latency, cost thresholds, reviewer behavior,
workflow impact, and ROI. Until that evidence exists, synthetic fixtures should
cover known structural and failure classes, and operational targets should
remain provisional. Synthetic breadth is not evidence of representative client
performance.

For an implementation change, the preferred loop is:

1. Define or select the smallest failing unit, contract, property, scenario, or
   eval case that expresses the intended behavior.
2. Implement the minimum behavior needed to satisfy it without weakening an
   existing guardrail.
3. Run the affected layer and the relevant broader regression suite.
4. Retain material failure cases, record model/configuration and fixture
   versions, and route discoveries that do not belong to the active goal.

When a failing test cannot reasonably precede a documentation, exploration, or
infrastructure change, the goal must still state its binary verification
evidence. Manual inspection alone is insufficient when the resulting behavior
can be automated and asserted.

## Traceability and change control

The product contract and roadmap have distinct responsibilities:

- `ACT-*`, `VM-*`, `DH-*`, `BR-*`, `AS-*`, and `TV-*` identify actors, value
  measures, deployment hypotheses, build-versus-reuse subjects, assumptions,
  and testing/vetting layers.
- `O*` identifies the durable product outcomes that justify implementation.
- `S-*` and `M-*` identify whole-project acceptance scenarios.
- `C*` identifies constraints that every applicable goal must preserve.
- Roadmap goals define bounded increments and use goal-local `AC` checks as the
  binary proof required to complete that increment.
- Tests, demonstrations, decision records, and evidence reports provide the
  verification artifacts behind those checks.

A roadmap goal should reference—not duplicate—the outcomes, scenarios, and
constraints it advances. Goal-level acceptance checks remain distinct from
whole-project scenarios unless that goal must satisfy a scenario end to end.

Discovery may change a buyer, workflow, value, or deployment hypothesis. Such a
change requires evidence and a decision record plus synchronized updates to the
source specification, this charter, and any affected roadmap dependency. A
change to authority boundaries, safety constraints, evidence tiers, or the
project thesis is an explicit product-contract change rather than incidental
implementation work.

## Verification policy

Every goal must satisfy each of its own acceptance criteria and preserve the
applicable constraints above. Verification evidence must be recorded in the
cycle handoff. Every roadmap goal must declare its applicable `TV-*` layers,
and the handoff must map each declared layer to concrete evidence. The default
evidence is automated tests plus inspection of the produced artifact; a manual
statement is insufficient when behavior can be tested. A goal that changes
behavior must update the relevant documentation.
External standards and benchmark claims must identify exact fixture/task,
verifier, adapter, and version evidence. Workflow-value targets without operator
or client data must be labeled provisional.

Failures found outside the active goal must be routed once: to a named future
goal, to the backlog, or to an observation. Do not silently expand the active
goal.
