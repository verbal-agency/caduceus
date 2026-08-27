# Cycle-ready roadmap

## Identifier key

`D0` is the discovery goal, `G##` identifies a core implementation goal, and
`MA-#` identifies a gated future multi-agent goal. `{goal}-AC#` is a binary
acceptance criterion owned by that goal. Goals trace to charter outcomes (`O##`),
constraints (`C##`), single-institution scenarios (`S-*`), multi-agent scenarios
(`M-*`), and testing/vetting layers (`TV-##`). `FP-#` identifies a future-phase
entry criterion, while `B##` identifies an unordered backlog item. The complete
namespace and scenario-category definitions are in the
[project charter](project-charter.md#identifier-key).

This roadmap converts the executable-goals section of
[`bounded_healthcare_agency_project.md`](../bounded_healthcare_agency_project.md)
into bounded handoffs for the `cycle` skill. It does not activate or implement a
goal. Goal ordering follows the source specification except where explicit
dependencies require a later prerequisite. The roadmap has two phases: the
single-agent core (`D0`, then `G00`–`G20`) and a gated future multi-agent phase
(`MA-0`–`MA-8`).

## How to consume this roadmap

1. Select exactly one goal: the first `proposed` goal whose dependencies are
   `complete`, unless the user explicitly chooses another eligible goal.
2. Mark it `active` only when the user asks to begin, cycle, or automatically
   advance.
3. Execute only its in-scope work and verify every `AC` row.
4. Record evidence and route findings according to the cycle skill.
5. Mark it `complete` only when all criteria pass, then propose the next eligible
   goal. Do not implement that next goal in the same cycle without explicit
   authorization.

Allowed statuses are `proposed`, `active`, `blocked`, and `complete`. There is no
active goal at roadmap creation time.

## Test-first execution and traceability

Every goal declares applicable `TV-*` verification layers from the
[project charter](project-charter.md#testing-and-vetting-strategy). Those layers
are requirements of the goal, not descriptive tags. A cycle handoff must name
each applicable layer and link it to the tests, evals, reports, decision records,
or discovery evidence that satisfy it.

For any goal that changes executable behavior:

1. Define the smallest failing deterministic test or versioned probabilistic
   eval that expresses the intended behavior before implementation when
   practicable.
2. Implement the minimum coherent behavior without weakening an existing
   authority, provenance, workflow, or evidence guardrail.
3. Run the targeted check and the relevant broader regression suite.
4. Retain every material failure as a regression fixture and record the fixture,
   policy, model/configuration, scorer, and adapter versions that affect it.
5. Record a reason when documentation, exploration, or infrastructure work
   cannot reasonably begin with a failing automated check; the goal's binary
   acceptance evidence still applies.

Probabilistic behavior follows TV-05: eval cases and scoring rules precede
prompt, retrieval, tool, or model changes; exact-string assertions are avoided
when semantic structure is the requirement; and sample count plus observed
variance are reported when nondeterminism could change the conclusion. TV-08
evidence remains provisional unless it comes from an EV-04 governed shadow
pilot. Neither synthetic breadth nor a strong component score establishes
representative client performance.

## Status and dependency index

| Goal | Status | Depends on | Capability unlocked |
|---|---|---|---|
| D0 | proposed | None | Customer-shaped deployment brief and baseline |
| G00 | proposed | D0 | Runnable project shell |
| G01 | proposed | G00 | Typed domain contracts |
| G02 | proposed | G01 | Enforced workflow state |
| G03 | proposed | G00, G01 | Standards-recognizable synthetic FHIR R4 records |
| G04 | proposed | G00, G01 | Da Vinci-aligned deterministic payer simulator |
| G05 | proposed | G01 | Versioned policy repository |
| G06 | proposed | G01, G03, G05 | Claim provenance validation |
| G07 | proposed | G01, G02, G05, G06 | Deterministic authorization |
| G08 | proposed | G02, G07 | Guarded consequential executor |
| G09 | proposed | G03, G04, G05, G06 | Investigation agent |
| G10 | proposed | G07, G08, G09 | First end-to-end case |
| G11 | proposed | G10 | Executable evaluation harness |
| G12 | proposed | G11 | Standards and external-evaluation alignment |
| G13 | proposed | G08, G10 | Attributable human review |
| G14 | proposed | G11 | Adversarial defenses and tests |
| G15 | proposed | G11 | Deterministic release gate |
| G16 | proposed | G07, G11, G15 | Versioned operating envelope |
| G17 | proposed | G10, G13 | Case reconstruction |
| G18 | proposed | G12, G13, G14, G15, G16, G17 | Incident/remediation proof |
| G19 | proposed | G18 | Reproducible deployment |
| G20 | proposed | G19 | Portfolio package |
| MA-0 | proposed | G20 and future-phase gate | Institutional identities and trust model |
| MA-1 | proposed | MA-0 | A2A-carried healthcare transaction profile |
| MA-2 | proposed | MA-1 | Outbound authority and disclosure gate |
| MA-3 | proposed | MA-1 | Inbound verification gate |
| MA-4 | proposed | MA-1, MA-3 | Claims and dispute graph |
| MA-5 | proposed | MA-2, MA-3, MA-4 | Bounded negotiation protocol |
| MA-6 | proposed | MA-5 | Cross-institution human escalation |
| MA-7 | proposed | MA-2, MA-3, MA-4, MA-5, MA-6 | Adversarial evals and multi-agent release gates |
| MA-8 | proposed | MA-7 | Provider-payer lifecycle demonstration |

## Goal D0 — Define the deployment brief and baseline

**Objective:** Convert the project thesis into a customer-shaped, measurable,
and bounded first deployment before implementation begins.

**Dependencies:** None. **Advances:** O13–O16. Scenarios: S-D01 as the planned
thin-slice outcome. Constraints: C23–C27.

**Verification layers:** TV-08.

**In scope:** target buyer/operator/stakeholder map, current-state workflow and
systems, definition of a review-ready case, administrative-versus-clinical
authority boundary, discovery evidence and assumptions, value hypothesis and
baseline, one-case demo contract, build-versus-reuse decisions, and adoption/
handoff hypothesis. **Excluded:** application scaffolding, product
implementation, client-data ingestion, production claims, and activating later
goals.

**Deliverables:** `docs/deployment-brief.md`, `docs/current-workflow.md`,
`docs/value-hypothesis.md`, `docs/build-vs-reuse.md`, discovery evidence/
assumptions log, stakeholder map, demo contract, and proposed handoff approach.

| Criterion | Binary acceptance check | Expected evidence |
|---|---|---|
| D0-AC1 | The first buyer is a provider-side prior-authorization or revenue-cycle organization and the daily operator is an exception specialist, unless discovery evidence records a justified alternative. | Deployment brief and decision record. |
| D0-AC2 | The operator workflow documents handoffs, systems, pain points, stakeholders, and the exact definition of a review-ready case. | Current-state workflow map and stakeholder review. |
| D0-AC3 | At least three domain-expert/prospective-user conversations inform discovery when accessible; otherwise the evidence review is complete and explicitly labeled an unvalidated substitute. | Interview notes or sourced evidence review plus assumptions log. |
| D0-AC4 | Administrative preparation is explicitly separated from clinical judgment, coverage decision, and institutional commitment authority. | Authority-boundary review checklist. |
| D0-AC5 | Baseline/target measures cover investigator time, time to review-ready draft, evidence completeness, reviewer acceptance/edit rate, escalation quality, cost per successful case, and unauthorized executions; unsupported targets are labeled provisional. | Value-hypothesis and baseline table. |
| D0-AC6 | The first demo is bounded to one lumbar MRI denial ending in the correct-but-not-authorized outcome. | Approved demo contract referencing S-D01. |
| D0-AC7 | Synthea, FHIR/Da Vinci, policy engines, orchestration, HealthAdminBench, and A2A each have an adopt/adapt/interoperate/reimplement decision with rationale. | Build-versus-reuse ADR set. |
| D0-AC8 | Every material deployment-brief ambiguity is resolved or recorded as a blocker before G00 can activate. | D0 completion checklist and routed findings. |
| D0-AC9 | The deployment brief separates tests specifiable without client data from data-dependent vetting and routes the latter to discovery, adapter validation, or the governed EV-04/B06 shadow pilot. | Testing/vetting matrix linked to the charter and backlog. |

**Risks/findings to carry:** A literature-based discovery substitute preserves
momentum but does not validate customer demand. No synthetic result may be
presented as client ROI or production readiness.

## Goal G00 — Initialize the project

**Objective:** Create a minimal runnable Python service and test foundation.

**Dependencies:** D0. **Advances:** O01, O16. Scenarios: none directly.
Constraints: C01, C12, C24.

**Verification layers:** TV-01.

**In scope:** dependency management, source/test layout, FastAPI health route,
pytest configuration, local setup instructions, integration-adapter boundaries,
architecture decisions, and a guard or documented check against real patient
data. **Excluded:** healthcare domain models, databases, agents, authorization,
deployment, and production UI.

**Deliverables:** `pyproject.toml`, application entry point, health endpoint,
tests, README setup commands, and initial adapter/ADR structure.

| Criterion | Binary acceptance check | Expected evidence |
|---|---|---|
| G00-AC1 | A documented local command starts the application without import/configuration failure. | Command transcript or automated startup test. |
| G00-AC2 | `GET /health` returns a 2xx response with a stable machine-readable healthy status. | API test. |
| G00-AC3 | The documented test command exits zero from a clean checkout with at least one collected test. | Test transcript. |
| G00-AC4 | Committed fixtures and examples contain synthetic data only and README states the prohibition on real PHI. | Repository scan plus documentation inspection. |
| G00-AC5 | The deterministic local path requires no proprietary EHR, paid cloud deployment, or production model credential. | Clean-environment setup test. |

**Risks/findings to carry:** Keep dependencies minimal; storage and model-provider
choices belong to later goals.

## Goal G01 — Define domain contracts

**Objective:** Define typed, serializable contracts for the bounded-agency flow.

**Dependencies:** G00. **Advances:** O01, O03, O04, O05, O07. Scenarios:
S-R01, S-S04. Constraints: C01–C06, C09.

**Verification layers:** TV-01, TV-03.

**In scope:** typed `Case`, `Evidence`, `Claim`, `ProposedAction`,
`AuthorizationRequest`, and `AuthorizationDecision`; enumerated action classes,
authorization outcomes, identifiers, and validation. **Excluded:** persistence,
rules, workflow transition behavior, and API endpoints beyond examples/tests.

**Deliverables:** domain models, enums, representative valid/invalid fixtures,
serialization and validation tests.

| Criterion | Binary acceptance check | Expected evidence |
|---|---|---|
| G01-AC1 | Every required model round-trips through the chosen wire format without data loss. | Parameterized tests. |
| G01-AC2 | Malformed requests, unknown actions/outcomes, and missing required identifiers fail validation. | Negative tests. |
| G01-AC3 | The action enum includes the eight source-specified classes and the outcome enum includes all four outcomes. | Enum contract test. |
| G01-AC4 | A proposed action and an authorization decision are distinct types, with no field allowing an agent to self-assert authorization. | Schema snapshot/inspection test. |

**Risks/findings to carry:** Avoid encoding authorization policy in validation;
G07 owns policy decisions.

## Goal G02 — Implement the workflow state machine

**Objective:** Make case-state transitions independently and deterministically
enforceable.

**Dependencies:** G01. **Advances:** O01, O04. Scenarios: S-R04, S-S04.
Constraints: C02, C05.

**Verification layers:** TV-01, TV-03.

**In scope:** state enum, explicit transition table, transition service, and a
write boundary that prevents direct agent mutation. **Excluded:** payer calls,
authorization policy, persistence hardening, and human review UI.

**Deliverables:** transition service and tests for every allowed/disallowed edge.

| Criterion | Binary acceptance check | Expected evidence |
|---|---|---|
| G02-AC1 | Each declared valid transition succeeds and returns/records the new state. | Table-driven tests. |
| G02-AC2 | Every undeclared transition fails with a deterministic typed error and leaves state unchanged. | Table-driven negative tests. |
| G02-AC3 | Application/agent-facing code cannot persist a state change except through the transition service. | Boundary test and code inspection. |
| G02-AC4 | Duplicate submission and premature closure paths are rejected in the relevant states. | Scenario-focused tests. |

**Risks/findings to carry:** Concurrency control may remain in-memory here; any
persistence race discovered later routes to the goal that introduces storage.

## Goal G03 — Integrate synthetic FHIR R4 records

**Objective:** Provide realistic, deterministic, standards-recognizable records
for agent investigation without building a novel patient generator.

**Dependencies:** G00, G01. **Advances:** O01, O02, O14. Scenarios: S-R01, S-R02,
S-A01, S-A02, S-F01, S-F02, S-F04, S-F05, S-F06, S-F07. Constraints: C01,
C06, C12, C24, C25.

**Verification layers:** TV-01, TV-02, TV-03.

**In scope:** Synthea or Synthea-derived deterministic fixtures; declared FHIR
R4 profile subset; stable IDs and useful subsets of Patient, Coverage,
Encounter, Procedure, Condition, ServiceRequest, Claim, and Task; adapter,
retrieval/search interfaces; conformance/deviation tests; deterministic failure
modes. **Excluded:** broad FHIR conformance, real EHR integration, a novel
patient generator, and agent reasoning.

**Deliverables:** fixture pipeline, FHIR adapter, supported-profile declaration,
linked fixtures for multiple patients, failure fixtures, deviation log, and
tests.

| Criterion | Binary acceptance check | Expected evidence |
|---|---|---|
| G03-AC1 | Each required resource type is retrievable by a stable ID. | API/service tests. |
| G03-AC2 | All references in the baseline fixture resolve to an existing resource of the declared type. | Referential-integrity test. |
| G03-AC3 | The fixture pipeline deterministically provides at least three distinct synthetic patients/cases without real PHI. | Fixture snapshot plus data scan. |
| G03-AC4 | Resources validate as FHIR R4 against the declared supported subset; every intentional deviation is documented and tested. | Conformance report and deviation tests. |
| G03-AC5 | Timeout, malformed, stale, partial, unexpected-schema, and duplicate modes can be invoked deterministically without changing baseline behavior. | Failure-mode tests. |
| G03-AC6 | The implementation reuses Synthea/Synthea-derived data or records why a custom fixture is materially better for the thin slice. | ADR and fixture provenance. |

**Risks/findings to carry:** Standards fidelity beyond the declared thin-slice
profiles remains B05; do not hide a custom contract behind “FHIR-like.”

## Goal G04 — Integrate a Da Vinci-aligned payer simulator

**Objective:** Simulate deterministic prior-authorization and appeal
interactions through recognizable FHIR R4 and Da Vinci PAS/DTR contracts.

**Dependencies:** G00, G01. **Advances:** O01, O02, O14. Scenarios: S-R03,
S-R04, S-A05, S-F03, S-F05, S-F06, S-X03, S-X04. Constraints: C01, C08,
C24, C25.

**Verification layers:** TV-01, TV-02, TV-03.

**In scope:** authorization lookup, policy lookup adapter, additional-information
request, appeal submission, structured denial reasons, idempotency/duplicate
behavior, declared FHIR/PAS request/response validation, adapter to selected Da
Vinci reference behavior, and deterministic error modes. **Excluded:** live
payer integration, a competing interoperability standard, policy authoring,
authorization of calls, and human review.

**Deliverables:** simulator interfaces/endpoints, Da Vinci adapter/fixtures,
contract/deviation documentation, and tests.

| Criterion | Binary acceptance check | Expected evidence |
|---|---|---|
| G04-AC1 | The four required operations return deterministic responses for identical fixture inputs. | Contract tests. |
| G04-AC2 | Denials expose a structured reason and referenced policy ID/version. | Response-schema tests. |
| G04-AC3 | Invalid and duplicate submissions are rejected or returned idempotently according to a documented contract. | Negative/idempotency tests. |
| G04-AC4 | Timeout, partial, malformed, and malicious-output fixtures are reproducible and explicitly marked untrusted. | Failure/adversarial tests. |
| G04-AC5 | The thin-slice request and response validate against the declared FHIR R4/Da Vinci contract. | Reference-fixture contract test. |
| G04-AC6 | Custom simulator behavior is limited to deterministic test needs and documented as such. | Adapter ADR and deviation inspection. |

**Risks/findings to carry:** Consequential submission remains unreachable to the
agent until G08 and G10.

## Goal G05 — Implement the policy repository

**Objective:** Make payer policies versioned, retrievable, and citable.

**Dependencies:** G01. **Advances:** O02, O05, O07. Scenarios: S-A03, S-A04,
S-A05, S-X03. Constraints: C03, C06, C08.

**Verification layers:** TV-01, TV-03.

**In scope:** structured metadata plus interpretable text, stable section IDs,
multiple versions, freshness/currentness, ambiguous clauses, and retrieval.
**Excluded:** authorization decisions and an external policy engine.

**Deliverables:** schema, repository interface, baseline/current/stale fixtures,
and tests.

| Criterion | Binary acceptance check | Expected evidence |
|---|---|---|
| G05-AC1 | A policy is retrievable by ID/version and exposes stable section identifiers. | Repository tests. |
| G05-AC2 | Current and stale versions are deterministically distinguishable from metadata. | Freshness tests. |
| G05-AC3 | Fixtures include an ambiguous clause and multiple potentially applicable policies without embedding executable instructions. | Fixture inspection/tests. |
| G05-AC4 | A claim/action can cite policy ID, exact version, and section using G01 contracts. | Integration contract test. |

**Risks/findings to carry:** Policy interpretation remains probabilistic in G09;
authority stays deterministic in G07.

## Goal G06 — Implement the evidence/provenance graph

**Objective:** Validate traceable links from every material claim to versioned
source evidence.

**Dependencies:** G01, G03, G05. **Advances:** O03, O07. Scenarios: S-R01,
S-A01, S-A05, S-S02, S-S03, S-F04, S-X05. Constraints: C06.

**Verification layers:** TV-01, TV-03.

**In scope:** claim-to-evidence links, source locator/type/version/timestamp,
materiality, freshness, and provenance validation. **Excluded:** deciding truth,
resolving contradictions, model prompting, and full trace storage.

**Deliverables:** provenance representation, validator, valid/invalid examples,
and tests.

| Criterion | Binary acceptance check | Expected evidence |
|---|---|---|
| G06-AC1 | A material claim can reference one or more resolvable source artifacts. | Positive integration tests. |
| G06-AC2 | Missing, nonexistent, or mismatched sources fail with typed validation reasons. | Negative tests. |
| G06-AC3 | Stale-source metadata is detected without relying on model judgment. | Freshness tests. |
| G06-AC4 | Conflicting evidence can be represented without the provenance layer silently resolving it. | Conflict fixture test. |

**Risks/findings to carry:** Semantic claim support grading belongs to G11.

## Goal G07 — Implement deterministic authorization engine v1

**Objective:** Decide independently whether a structured proposed action is
allowed, constrained, review-required, or denied.

**Dependencies:** G01, G02, G05, G06. **Advances:** O04, O05. Scenarios:
S-R01, S-R02, S-R04, S-A05, S-S01, S-S03, S-S04, S-D01. Constraints: C02,
C03, C05, C06, C09.

**Verification layers:** TV-01, TV-03.

**In scope:** agent/action permissions, state requirements, evidence/provenance,
mandatory-review, clinical-judgment prohibition, policy version/freshness,
contradictions, risk/reversibility, and deterministic reason codes. **Excluded:**
execution, human decisions, operating-envelope manifest loading, and LLM calls.

**Deliverables:** rules engine, decision service, rule fixtures/matrix, and tests.

| Criterion | Binary acceptance check | Expected evidence |
|---|---|---|
| G07-AC1 | Repeated evaluation of the same request and rule version yields an identical outcome and reason codes. | Determinism test. |
| G07-AC2 | Unpermitted actions and clinical-judgment requests return `DENY`; mandatory-review cases return `REQUIRE_HUMAN_REVIEW`. | Rule-matrix tests. |
| G07-AC3 | Missing/stale policy or insufficient provenance cannot produce an unconstrained `ALLOW`. | Negative rule tests. |
| G07-AC4 | The authorization runtime and dependency graph contain no LLM/model-provider call. | Architecture test/inspection. |
| G07-AC5 | Each decision records request ID, rules/version, outcome, and machine-readable reasons. | Schema/persistence test. |

**Risks/findings to carry:** Envelope-based deny-by-default is completed in G16;
v1 uses explicit configuration.

## Goal G08 — Implement the guarded executor

**Objective:** Create the sole boundary for consequential state-changing actions.

**Dependencies:** G02, G07. **Advances:** O04, O05, O08. Scenarios: S-R03,
S-R04, S-S04, S-D01. Constraints: C02, C04, C05.

**Verification layers:** TV-01, TV-03.

**In scope:** executor interface, decision authenticity/integrity checks,
request/decision binding, rejection behavior, idempotency, calls into payer/state
services, and audit events. **Excluded:** agent access, human approval creation,
and cloud security hardening.

**Deliverables:** executor, authorization proof/binding mechanism, audit event,
and tests.

| Criterion | Binary acceptance check | Expected evidence |
|---|---|---|
| G08-AC1 | Missing, invalid, expired/superseded, or request-mismatched authorization is rejected before side effects. | Negative tests with side-effect assertions. |
| G08-AC2 | `DENY` and `REQUIRE_HUMAN_REVIEW` decisions cannot execute. | Outcome matrix tests. |
| G08-AC3 | A valid allowed request executes at most once and records request and decision IDs. | Idempotency/integration test. |
| G08-AC4 | No other application component has a tested direct path to consequential adapters. | Boundary/architecture test. |

**Risks/findings to carry:** G13 adds a human decision that can satisfy the
review requirement; it must not mutate the original engine decision.

## Goal G09 — Build investigation agent v1

**Objective:** Let a replaceable LLM-backed agent investigate the provider-side
exception case and propose a typed, cited action through explicit read-only
tools without execution access.

**Dependencies:** G03, G04, G05, G06. **Advances:** O02, O03, O04, O07.
Scenarios: S-R01, S-R02, S-R03, S-A01, S-A02, S-A03, S-A04, S-A05, S-S02,
S-S03. Constraints: C02, C06, C08, C11, C23, C24.

**Verification layers:** TV-02, TV-03, TV-05.

**In scope:** explicit read-only tools, deterministic orchestration boundaries,
structured output, provider abstraction/fake provider, evidence linking, and
contradiction reporting. **Excluded:** authorization calls as a self-approval
mechanism, executor access, broad scenario optimization, and prompt-injection
hardening beyond trust-boundary basics.

**Deliverables:** agent runner, tool definitions, model adapter, fake-model test
path, and a simple denial-case test.

| Criterion | Binary acceptance check | Expected evidence |
|---|---|---|
| G09-AC1 | The agent completes the baseline synthetic denial investigation using only declared read-only tools. | Deterministic integration test. |
| G09-AC2 | Its output validates as an `AuthorizationRequest` and every material claim carries provenance references. | Contract/provenance test. |
| G09-AC3 | Contradictions and missing information remain explicit rather than being filled with inferred clinical facts. | Negative scenario tests. |
| G09-AC4 | The agent process has no import, credential, tool, or network path to the executor/consequential adapters. | Architecture/security test. |
| G09-AC5 | The same orchestration can run with a fake provider in tests and a documented configured provider locally. | Adapter tests and setup documentation. |
| G09-AC6 | Any orchestration framework has a build-versus-reuse decision and is not treated as the institutional authorization boundary. | ADR and architecture boundary test. |
| G09-AC7 | The baseline case, expected structured behavior, and scorer are versioned before prompt, retrieval, tool, or model tuning; every tuning attempt records its provider/model/configuration. | Versioned baseline eval case and tuning comparison record. |

**Risks/findings to carry:** Live-provider quality is measured later; G09 proves
the boundary and one baseline capability.

## Goal G10 — Implement the first end-to-end case

**Objective:** Run the deployment brief's lumbar MRI denial from intake through
a cited proposal, deterministic authorization, and guarded execution outcome.

**Dependencies:** G07, G08, G09. **Advances:** O01–O05, O07, O08, O13–O15.
Scenarios: S-R01, S-D01. Constraints: C01–C06, C11, C23–C26.

**Verification layers:** TV-02, TV-03, TV-06, TV-08.

**In scope:** composing existing services for one allow/review baseline,
correlation IDs, a minimal trace sink, and end-to-end tests. **Excluded:** full
eval harness, human review implementation, production observability UI, and
scenario breadth.

**Deliverables:** orchestration entry point/API, standards-recognizable baseline
fixture, trace record, provisional manual/synthetic workflow baseline, local
demo path, and end-to-end test.

| Criterion | Binary acceptance check | Expected evidence |
|---|---|---|
| G10-AC1 | The run retrieves the expected evidence and applicable exact policy version. | End-to-end assertions. |
| G10-AC2 | The proposed action is valid, evidenced, and evaluated by G07 before G08 sees it. | Correlated trace/order assertions. |
| G10-AC3 | The executor performs or refuses the action exactly as the authorization outcome requires. | Side-effect assertions. |
| G10-AC4 | One correlation ID reconstructs inputs, tool activity, claims, request, decision, and execution result. | Trace snapshot test. |
| G10-AC5 | A demonstration variant proves a correct proposal can still be review-required and unexecuted. | S-D01 end-to-end test. |
| G10-AC6 | The case uses the declared FHIR R4 and Da Vinci-aligned adapters and runs locally without a cloud account. | Contract assertions and clean local demo transcript. |
| G10-AC7 | Time to a review-ready case is measured against a reproducible baseline and labeled provisional when no operator baseline exists. | Versioned baseline/result report. |

**Risks/findings to carry:** Trace schema may be extended compatibly by G13 and
G17.

## Goal G11 — Build the evaluation harness

**Objective:** Make canonical scenarios machine-executable, repeatable, graded,
classified, and summarized.

**Dependencies:** G10. **Advances:** O09, O10, O11, O15. Scenarios: seeds across
all canonical categories. Constraints: C10, C26, C27.

**Verification layers:** TV-04, TV-05, TV-06, TV-08.

**In scope:** scenario schema, runner, deterministic graders, failure taxonomy,
metrics, evidence-tier labels, workflow/value-baseline measures, report, and at
least 20 representative scenarios. **Excluded:** arbitrary scenario-count
growth, release gating, and fixing every agent-quality miss.

**Deliverables:** scenario format/fixtures, runner, graders, taxonomy, report,
and methodology documentation.

| Criterion | Binary acceptance check | Expected evidence |
|---|---|---|
| G11-AC1 | At least 20 uniquely identified scenarios run unattended with fixed fixture/config versions. | Runner transcript and count assertion. |
| G11-AC2 | Each result reports pass/fail and the exact violated expectation(s). | Report snapshot tests. |
| G11-AC3 | Reports aggregate all source-specified minimum metrics, with cost marked unavailable only for providers that expose none. | Metrics schema/report test. |
| G11-AC4 | Every failed eval receives exactly one primary failure class from the documented taxonomy. | Grader invariant test. |
| G11-AC5 | Agent, authorization, execution, and environment failures are distinguishable. | Seeded-failure tests. |
| G11-AC6 | End-to-end success is separate from subtask success, and safety, quality, workflow, reviewer, latency, and cost metrics are not collapsed into one score. | Metrics invariant and report snapshot. |
| G11-AC7 | Every result identifies fixture, policy, agent/model/config, evaluator, and evidence-tier versions. | Result-schema validation. |
| G11-AC8 | Probabilistic cases support repeated trials and report sample count plus outcome distribution or variance whenever nondeterminism can affect the conclusion. | Repeated-run fixture and statistical report assertions. |
| G11-AC9 | A prompt, retrieval, tool, or model change records a pre-change result and a comparable post-change result, and every material failure or improvement case remains in the versioned corpus. | Eval-first workflow test and retained-regression inventory. |

**Risks/findings to carry:** Authorization correctness and unauthorized execution
must remain visible as hard-safety inputs, not blended into an average score.

## Goal G12 — Validate standards and external-evaluation alignment

**Objective:** Make project evidence comparable to healthcare standards and
external evaluation work without implying false conformance or benchmark
performance.

**Dependencies:** G11. **Advances:** O09, O10, O14. Scenarios: S-R01–S-R04,
S-A01–S-A05, S-S01–S-S04, S-F01–S-F07, S-X01–S-X05, S-D01. Constraints:
C01, C08, C10, C25, C27.

**Verification layers:** TV-02, TV-04, TV-05.

**In scope:** coverage inventory for at least 20 deep project scenarios,
Da Vinci/FHIR reference-fixture contract tests, HealthAdminBench semantic
crosswalk, external adapter only where task/verifier semantics remain unchanged,
and versioned evidence-tier report. **Excluded:** arbitrary scenario-count
targets, false benchmark equivalence, changing external tasks/verifiers, and
manual review beyond scenarios intentionally testing it.

**Deliverables:** coverage inventory, standards fixture tests, HealthAdminBench
crosswalk, any valid external adapter, and evidence-tier report.

| Criterion | Binary acceptance check | Expected evidence |
|---|---|---|
| G12-AC1 | At least 20 deep project scenarios cover every canonical single-agent scenario and all five required categories. | Coverage inventory validator. |
| G12-AC2 | Every scenario declares an expected authorization outcome; high-risk cases declare prohibited behavior and severity. | Corpus invariant test. |
| G12-AC3 | At least one official/reference Da Vinci request-response fixture passes through the declared adapter and contract tests. | Standards-fixture transcript. |
| G12-AC4 | The HealthAdminBench crosswalk identifies comparable and non-comparable GUI versus tool/API task and verifier semantics. | Reviewed crosswalk document. |
| G12-AC5 | No external score is published unless unchanged tasks and verifiers actually ran against a documented adapter. | Evidence report and claim audit. |
| G12-AC6 | Scenario growth is justified by distinct risk, branch, regression, or customer requirement; the suite runs unattended except intentional review cases. | Scenario rationale inventory and full-suite transcript. |

**Risks/findings to carry:** HealthAdminBench's GUI computer-use semantics may
not be directly comparable to Caduceus tools/APIs. A documented non-equivalence
is more credible than a fabricated benchmark score.

## Goal G13 — Add human-review workflow

**Objective:** Make attributable human approval or rejection an explicit part of
authorization and execution.

**Dependencies:** G08, G10. **Advances:** O06, O08, O15. Scenarios: S-A03, S-A04,
S-S01, S-S02, S-S04, S-D01. Constraints: C04, C07, C26.

**Verification layers:** TV-01, TV-03, TV-06, TV-08.

**In scope:** review queue, reviewer identity/role, approve/reject with rationale,
decision binding, audit events, and execution after valid approval. **Excluded:**
advanced UI, identity-provider integration, and allowing reviewers to rewrite the
agent request silently.

**Deliverables:** review service/API, decision contract, audit integration,
reviewer feedback/material-edit metrics, and tests.

| Criterion | Binary acceptance check | Expected evidence |
|---|---|---|
| G13-AC1 | A review-required action has no side effect before a valid human approval bound to the same request/decision. | Integration test. |
| G13-AC2 | Approval records reviewer identity, timestamp, rationale, and bound request/decision IDs. | Audit-schema test. |
| G13-AC3 | Rejection permanently prevents that request instance from executing. | Negative/idempotency test. |
| G13-AC4 | Approval cannot override a `DENY` decision or modify the proposed payload. | Security tests. |
| G13-AC5 | Human decisions appear in the correlated trace. | Trace assertion. |
| G13-AC6 | Reviewer acceptance, rejection, material-edit, and handling-time measures are captured without treating higher acceptance as inherently better. | Reviewer-metrics tests/report. |

**Risks/findings to carry:** Production-grade authentication belongs to G19;
this goal uses explicit synthetic reviewer identities and roles.

## Goal G14 — Add adversarial defenses

**Objective:** Ensure untrusted retrieved content and tool output cannot change
authority, permissions, policy, or disclose credentials.

**Dependencies:** G11. **Advances:** O04, O09, O10. Scenarios: S-X01–S-X05.
Constraints: C02, C08, C10.

**Verification layers:** TV-03, TV-04, TV-05.

**In scope:** trust labels/data-instruction separation, input handling, least
privilege, secret redaction/non-exposure, logging, adversarial scenarios, and
regressions. **Excluded:** a claim of complete prompt-injection prevention or
unrelated application-security work.

**Deliverables:** defense controls, adversarial fixtures, tests, and threat-model
update.

| Criterion | Binary acceptance check | Expected evidence |
|---|---|---|
| G14-AC1 | Note/document/tool instructions cannot modify authorization configuration or the operating permission set. | S-X01–S-X04 tests. |
| G14-AC2 | Retrieved content cannot add tools or produce direct executor access. | Capability-boundary tests. |
| G14-AC3 | Credential requests receive no secret material, including in traces/errors. | Canary-secret tests and log scan. |
| G14-AC4 | Privilege-escalation attempts are classified and logged without executing the requested side effect. | Eval and trace assertions. |
| G14-AC5 | Misleading irrelevant evidence does not satisfy declared evidence requirements. | S-X05 grader/rule test. |

**Risks/findings to carry:** Document residual model susceptibility honestly in
G20.

## Goal G15 — Build the release gate

**Objective:** Convert versioned evaluation results into a deterministic,
explainable release decision.

**Dependencies:** G11. **Advances:** O11, O15. Scenarios: all available evals.
Constraints: C03, C10, C26, C27.

**Verification layers:** TV-01, TV-07.

**In scope:** hard gates, quality targets, workflow-value and reviewer-adoption
targets, evidence tiers, candidate/suite identity, blocked/pass report, and
CLI/service evaluator. **Excluded:** deployment, envelope changes, automatic
threshold tuning, and fabricated ROI.

**Deliverables:** gate configuration, evaluator, tiered report,
launch-criteria/value-target documentation, and tests.

| Criterion | Binary acceptance check | Expected evidence |
|---|---|---|
| G15-AC1 | Any known unauthorized consequential execution blocks release. | Seeded report test. |
| G15-AC2 | Any unresolved critical authorization regression blocks release. | Seeded report test. |
| G15-AC3 | Less than 100% enforcement of mandatory human-review rules blocks release. | Threshold-boundary tests. |
| G15-AC4 | Hard gates are evaluated separately from quality targets and cannot be averaged away. | Evaluator unit tests. |
| G15-AC5 | The report names candidate, eval suite/config versions, status, metrics, and each blocking reason. | Report snapshot. |
| G15-AC6 | Workflow-value, reviewer, cost, and external-evidence targets are labeled and cannot offset a hard-safety failure. | Seeded mixed-score tests. |
| G15-AC7 | Each reported claim identifies its component, project-scenario, external, or future shadow-pilot evidence tier. | Evidence-tier validation. |

**Risks/findings to carry:** Initial non-safety quality thresholds must be
documented as provisional evidence-based choices, not invented guarantees.

## Goal G16 — Implement the operating-envelope manifest

**Objective:** Make deployed authority explicit, versioned, deny-by-default, and
dependent on relevant passing eval evidence plus approval.

**Dependencies:** G07, G11, G15. **Advances:** O05, O11, O12. Scenarios: S-S01,
S-S04, S-D01. Constraints: C03, C09.

**Verification layers:** TV-01, TV-03, TV-07.

**In scope:** manifest schema/versioning, validated workflows, autonomous,
conditional, and prohibited actions, required eval suite/version, approval
record, authorization integration, and expansion/contraction tests. **Excluded:**
actual production deployment and autonomous envelope updates.

**Deliverables:** manifest, loader/validator, authorization integration, change
workflow, documentation, and tests.

| Criterion | Binary acceptance check | Expected evidence |
|---|---|---|
| G16-AC1 | Authorization denies any workflow/action absent from the active envelope. | Deny-by-default tests. |
| G16-AC2 | Manifest changes create a new version and preserve the prior version/audit record. | Versioning tests. |
| G16-AC3 | Model or agent-version changes alone do not expand authority. | Upgrade regression test. |
| G16-AC4 | Expansion activation fails without the declared relevant passing eval suite and explicit approver record. | Change-workflow tests. |
| G16-AC5 | Envelope contraction takes effect without requiring broader authority or model cooperation. | Contraction integration test. |

**Risks/findings to carry:** Production approval identity and deployment binding
are hardened in G19.

## Goal G17 — Add observability and case reconstruction

**Objective:** Let a reviewer reconstruct every consequential case
chronologically without reading raw model logs.

**Dependencies:** G10, G13. **Advances:** O07, O08. Scenarios: S-D01 plus one
failure and one human-review case. Constraints: C06, C07.

**Verification layers:** TV-01, TV-03, TV-06.

**In scope:** structured trace schema/storage, correlation/causation IDs, safe
tool result references or hashes, timeline endpoint/report, timing/errors, and
redaction. **Excluded:** a polished dashboard, vendor observability platform,
and raw secret/prompt dumping.

**Deliverables:** trace sink, timeline projection/API or report, tests, and
observability documentation.

| Criterion | Binary acceptance check | Expected evidence |
|---|---|---|
| G17-AC1 | A reviewer view orders tool activity, sources, claims, proposal, authorization, human decision, execution, and errors for a case. | Timeline integration/snapshot test. |
| G17-AC2 | Events record case, agent/model/config, policy, and correlation identifiers sufficient to join the flow. | Schema invariant test. |
| G17-AC3 | Source/tool payloads are stored safely as redacted content or integrity-checkable references/hashes. | Redaction and reference tests. |
| G17-AC4 | The baseline, review-required, and failed-tool cases answer “why did the system take/refuse this action?” from the timeline alone. | Reviewer checklist/test fixtures. |

**Risks/findings to carry:** Portfolio presentation of traces belongs to G20.

## Goal G18 — Run the intentional incident exercise

**Objective:** Demonstrate detection, containment, remediation, regression, and
release recovery for a serious mandatory-review authorization bug.

**Dependencies:** G12, G13, G14, G15, G16, G17. **Advances:** O08–O12.
Scenarios: S-S04, S-D01. Constraints: C04, C07, C09, C10.

**Verification layers:** TV-03, TV-04, TV-07.

**In scope:** reproduce the vulnerable behavior in an isolated test fixture or
temporary change, capture a failing eval, show the gate blocking, fix root cause,
add minimal regression, run targeted/full suites, reassess envelope, and write
the postmortem. **Excluded:** leaving a known vulnerable implementation on the
main path or fabricating evidence after the fact.

**Deliverables:** incident fixture/evidence, remediation, regression, passing
reports, and `docs/incident-postmortem.md`.

| Criterion | Binary acceptance check | Expected evidence |
|---|---|---|
| G18-AC1 | A captured pre-fix eval proves a mandatory-review action could incorrectly reach execution. | Preserved failing report/fixture. |
| G18-AC2 | The release gate blocks that candidate and names the critical regression. | Preserved blocked report. |
| G18-AC3 | Root cause is fixed and a minimal regression fails on the vulnerable implementation and passes on the fix. | Targeted test evidence. |
| G18-AC4 | The full eval suite and release gate pass after remediation, or the goal remains incomplete with blockers reported. | Full-suite and gate reports. |
| G18-AC5 | The postmortem covers detection, impact, root cause, containment, remediation, regression, and envelope decision. | Document checklist. |

**Risks/findings to carry:** Preserve test artifacts without preserving an
exploitable runtime switch in production configuration.

## Goal G19 — Deploy the bounded synthetic pilot

**Objective:** Reproducibly deploy the thin slice in the selected cloud using
synthetic data, only intended interfaces, enforced safety gates, and a local
Docker path.

**Dependencies:** G18. **Advances:** O11, O12, O16. Scenarios: deployed smoke
subset of S-R01, S-S04, S-D01. Constraints: C01–C04, C07–C09, C23–C27.

**Verification layers:** TV-02, TV-06, TV-07, TV-08.

**Decision required before activation:** Use the deployment target selected or
left open by D0. If the deployment brief did not resolve it, the cycle must ask;
cloud breadth is not a substitute for one reproducible gated deployment.

**In scope:** containers, CI tests/evals/gate, chosen cloud infrastructure,
secret handling, basic service authentication/authorization, least-exposed
network surface, reproducible deployment, local Docker demo, operator/developer
handoff, and runbooks. **Excluded:** real PHI, production healthcare use,
proprietary EHR/payer access, client-data shadow pilot, and enterprise-grade
HA/compliance claims.

**Deliverables:** local/container config, CI workflow, infrastructure as code,
deployment config, secret/deployment/operator handoff runbooks, and smoke tests.

| Criterion | Binary acceptance check | Expected evidence |
|---|---|---|
| G19-AC1 | A documented command/workflow deploys a fresh environment reproducibly from versioned config. | CI/deployment transcript. |
| G19-AC2 | Unit/integration tests, required eval subset, and release gate run before deploy and block it on failure. | CI negative/positive evidence. |
| G19-AC3 | Repository and produced images/artifacts contain no committed secrets or real PHI. | Secret/data scan. |
| G19-AC4 | Only documented API/reviewer interfaces are externally reachable; internal data, authorization, and executor services are not directly public. | Network/IAM inspection or automated probe. |
| G19-AC5 | Deployed smoke scenarios preserve authorization, human-review, and no-unauthorized-execution invariants. | Post-deploy smoke report. |
| G19-AC6 | Deployed smoke tests reproduce the S-D01 correct-but-not-authorized case. | Post-deploy S-D01 trace. |
| G19-AC7 | A local deterministic Docker path remains runnable without cloud or production model credentials. | Clean local demo transcript. |
| G19-AC8 | Deployment documentation explicitly disclaims production healthcare, HIPAA, legal, clinical, and regulatory readiness. | Claim-boundary review. |

**Risks/findings to carry:** Cost, region, account/project, and DNS are external
prerequisites to record before activation; do not bypass core controls with
deployment stubs.

## Goal G20 — Package the portfolio narrative

**Objective:** Make the engineering, field-deployment, business-value, and
safety reasoning legible to an interviewer or prospective client without
overstating readiness.

**Dependencies:** G19. **Advances:** O01–O16. Scenarios: S-R01, S-S04, S-D01
and the G18 incident. Constraints: C01, C12, C23–C27.

**Verification layers:** TV-07, TV-08.

**In scope:** excellent README, architecture/authorization/eval/launch/envelope
docs, architecture diagram, 3–5 minute demo path, deployment brief/current-state
workflow, build-versus-reuse comparison, standards/external-evidence report,
value baseline, adoption/handoff playbook, separate interview/client-pilot
narratives, current eval/release reports, incident, deployment, and limitations.
**Excluded:** unsupported production/clinical/compliance/ROI claims, UI polish
unrelated to the demo, hiding limitations, and requiring the MA phase.

**Deliverables:** final technical and field-deployment documentation, diagram,
scripted demo, evidence bundle, client shadow-pilot framing, and link/check
validation.

| Criterion | Binary acceptance check | Expected evidence |
|---|---|---|
| G20-AC1 | README answers all fourteen questions enumerated in source specification §20. | Documentation checklist. |
| G20-AC2 | The 3–5 minute demo reproducibly shows the provider exception, FHIR/policy evidence, cited proposal, deterministic `REQUIRE_HUMAN_REVIEW`, refused pre-review execution, trace, and release evidence. | Timed dry-run transcript/recording plan. |
| G20-AC3 | Build/reuse, standards/deviations, eval tiers, workflow measures, architecture, authorization, envelope, incident, deployment, handoff, and limitations docs match current behavior. | Cross-document review and automated link checks. |
| G20-AC4 | Published artifacts identify their code, fixture, policy, model/config, evaluator, envelope, and evidence-tier versions. | Artifact metadata validation. |
| G20-AC5 | The deterministic setup/demo passes from a clean checkout without proprietary accounts; model-backed setup is separately documented and all links resolve. | Clean-room smoke test and link checker. |
| G20-AC6 | The client narrative proposes bounded discovery/shadow-pilot acceptance criteria, explicitly routes EV-04 validation to B06, and makes no production-readiness or manufactured-ROI claim. | Client narrative and backlog-link review checklist. |
| G20-AC7 | The core demo is independently valuable and does not require any `MA-*` implementation. | Demo dependency audit. |

**Risks/findings to carry:** State explicitly what would have to change before
real healthcare deployment; portfolio readiness is not clinical or regulatory
validation.

## Future phase gate

Goals `MA-0` through `MA-8` implement governed transactions between mutually
untrusted synthetic provider and payer institutions. They are not stretch
features of an active core goal and are unnecessary for the initial interview
demo or client-pilot narrative. `MA-0` is ineligible until D0 and all
`G00`–`G20` goals are complete and the user explicitly confirms that the
single-agent core is stable enough to extend. That confirmation must be
recorded in the cycle handoff; completing G20 alone does not silently activate
the future phase.

The future-phase gate passes only when all of the following have evidence:

| Gate | Binary entry check | Expected evidence |
|---|---|---|
| FP-1 | `D0` and every `G00`–`G20` goal are `complete`. | Roadmap status audit. |
| FP-2 | The latest required core evaluation suite and release gate pass with zero unresolved critical authorization regressions or unauthorized consequential executions. | Versioned eval and release reports. |
| FP-3 | The deployed core version, active operating envelope, and portfolio evidence identify the same validated candidate. | Version/candidate reconciliation. |
| FP-4 | The user explicitly authorizes the governed multi-agent phase after reviewing the stability evidence. | Recorded user decision in the MA-0 cycle handoff. |

## Goal MA-0 — Define institutional identities and trust model

**Objective:** Represent synthetic provider and payer organizations as distinct
security and authority domains with independently verifiable identities.

**Dependencies:** G20 plus explicit core-stability confirmation. **Advances:**
O17, O18. Scenarios: M-R01, M-X02, M-X03, M-X07. Constraints: C13–C15, C20,
C22.

**Verification layers:** TV-01, TV-03.

**In scope:** organization and organization-scoped agent identities, a testable
signing/verification mechanism, key/credential ownership boundaries, unknown or
disabled sender handling, A2A adopt/adapt/interoperate decision and security
responsibility map, and trust-boundary documentation. **Excluded:** production
PKI, real institutions, a competing generic agent transport, inter-agent domain
payload schemas, and one institution delegating authority for the other.

**Deliverables:** identity contracts/registry, signing and verification
interfaces, synthetic provider/payer fixtures, trust model, A2A ADR/security
map, and tests.

| Criterion | Binary acceptance check | Expected evidence |
|---|---|---|
| MA0-AC1 | Provider and payer have distinct stable organization identities, and every agent identity is scoped to exactly one organization. | Identity invariant tests. |
| MA0-AC2 | A receiver verifies the asserted sender against authenticated message metadata and rejects unknown, disabled, or organization-mismatched identities. | Positive/negative verification tests. |
| MA0-AC3 | Provider credentials cannot create a message that verifies as payer-originated, and vice versa. | Cross-domain forgery tests. |
| MA0-AC4 | The trust model names organizational endpoints, agents, credentials, policy gates, and counterparty content as separate trust boundaries. | Documentation checklist. |
| MA0-AC5 | The implementation and documentation make no production identity, PKI, or non-repudiation claim beyond the chosen synthetic mechanism. | Architecture review. |
| MA0-AC6 | A2A discovery/security concepts are reused where applicable and every healthcare-domain extension is documented. | A2A mapping/ADR review. |

**Risks/findings to carry:** Credential rotation, compromise, and production PKI
remain future hardening unless later goals need a synthetic lifecycle fixture.

## Goal MA-1 — Define the healthcare transaction profile

**Objective:** Replace free-form provider-payer chat with typed, versioned
institutional domain transactions carried through the selected A2A-compatible
transport and distinguishing non-binding messages from commitments.

**Dependencies:** MA-0. **Advances:** O18, O20, O22. Scenarios: M-R01, M-A01,
M-X02, M-X07. Constraints: C14–C17.

**Verification layers:** TV-01, TV-02, TV-03.

**In scope:** schemas for `CLAIM`, `EVIDENCE_SUBMISSION`, `REQUEST_EVIDENCE`,
`REQUEST_CLARIFICATION`, `PROPOSE_RESOLUTION`, `COUNTERPROPOSAL`,
`ACCEPT_RESOLUTION`, `REJECT_RESOLUTION`, `REQUEST_HUMAN_REVIEW`,
`ESCALATE_DISPUTE`, and `COMMIT_ACTION`; transaction identity/version, case and
correlation IDs, sender/recipient, timestamp/expiry, evidence/policy references,
authorization metadata, and A2A task/message/artifact mappings. **Excluded:**
forking/reimplementing generic A2A discovery, transport, streaming, or task
lifecycle without a recorded incompatibility; gate decisions; negotiation
orchestration; and free-form text driving workflow transitions.

**Deliverables:** transaction models/enums, examples, A2A mapping/adapter,
schema documentation, and validation tests.

| Criterion | Binary acceptance check | Expected evidence |
|---|---|---|
| MA1-AC1 | Every required transaction type round-trips through the wire format with a unique transaction ID, case ID, sender, recipient, type, timestamp, and schema version. | Parameterized serialization tests. |
| MA1-AC2 | Malformed, unknown-version, missing-identity, expired, or structurally smuggled transactions fail closed with typed errors. | Negative/schema-fuzz tests. |
| MA1-AC3 | Evidence and policy references are machine-readable and can identify exact source and policy versions. | Contract tests. |
| MA1-AC4 | `COMMIT_ACTION` is structurally distinct from claims, explanations, proposals, acceptance language, and all other non-binding messages. | Schema invariant tests. |
| MA1-AC5 | Natural-language fields are explicitly modeled as untrusted, non-authoritative data. | Schema metadata and documentation inspection. |
| MA1-AC6 | Domain payloads round-trip through the selected A2A representation without making natural language authoritative. | A2A adapter contract test. |
| MA1-AC7 | Generic A2A lifecycle/transport behavior is reused unless a tested incompatibility is recorded. | Dependency/ADR audit. |

**Risks/findings to carry:** Backward-compatible schema evolution is required
once a second version exists; do not add speculative compatibility machinery now.

## Goal MA-2 — Implement the outbound authority and disclosure gate

**Objective:** Prevent an institutional agent from sending messages,
disclosures, or commitments outside its external transaction envelope.

**Dependencies:** MA-1. **Advances:** O19, O22. Scenarios: M-R01, M-X02, M-X05,
M-X07. Constraints: C15, C17, C18, C22.

**Verification layers:** TV-01, TV-02, TV-03.

**Decision required before activation:** Choose and document whether a payload
with unauthorized fields is rejected in full or transformed to an explicitly
auditable minimum-necessary payload. This changes the protocol contract and must
not be selected silently.

**In scope:** external transaction envelope, allowed recipients/purposes/types,
commitment limits, patient/case scope, data classification, minimum-necessary
fields, retention/expiry metadata, human-review rules, authorization proof, and
signed send boundary. **Excluded:** inbound verification, negotiation, real PHI,
and permission changes based on agent output.

**Deliverables:** envelope schema/fixture, disclosure policy, outbound gate,
decision/audit event, tests, and documentation of the field-handling decision.

| Criterion | Binary acceptance check | Expected evidence |
|---|---|---|
| MA2-AC1 | A transaction type, recipient, purpose, or case scope absent from the sender's active external envelope is blocked before transmission. | Rule-matrix tests with transport spy. |
| MA2-AC2 | Unauthorized disclosure fields never cross the organizational boundary and the gate records the exact reason and disposition. | Data-canary and audit tests. |
| MA2-AC3 | `COMMIT_ACTION` requires explicit commitment authority and any mandated human approval independently of proposal or acceptance text. | Commitment boundary tests. |
| MA2-AC4 | Agent output, counterparty text, or a received authorization claim cannot modify the gate's rules or expand its envelope. | Privilege-escalation tests. |
| MA2-AC5 | Every sent transaction binds sender identity, gate decision, envelope version, payload integrity, timestamp/expiry, and transaction ID in verifiable metadata. | Send/verify integration test. |

**Risks/findings to carry:** Internal read authority remains distinct from
external disclosure authority even when the same evidence would strengthen a
case.

## Goal MA-3 — Implement the inbound verification gate

**Objective:** Treat every counterparty transaction as untrusted and admit it
only after independent identity, integrity, schema, authorization-metadata, and
replay checks.

**Dependencies:** MA-1. **Advances:** O20. Scenarios: M-R01, M-X01–M-X04,
M-X06, M-X07. Constraints: C14–C16, C20.

**Verification layers:** TV-01, TV-02, TV-03.

**In scope:** signature/sender/recipient verification, schema and expiry checks,
payload-integrity binding, transaction-ID replay protection, authorization
metadata checks, safe evidence-reference handling, and admission audit events.
**Excluded:** trusting remote policy decisions as local authority, dereferencing
arbitrary evidence, negotiation behavior, and local authorization changes.

**Deliverables:** inbound gate, replay store/interface, verification decision,
audit integration, and tests.

| Criterion | Binary acceptance check | Expected evidence |
|---|---|---|
| MA3-AC1 | Valid known-sender transactions pass verification without being treated as locally authorized actions. | Positive integration test. |
| MA3-AC2 | Invalid identity/signature, tampering, wrong recipient, invalid schema, expired authorization metadata, and schema smuggling are rejected before agent or workflow processing. | Verification matrix tests. |
| MA3-AC3 | A repeated transaction ID or authenticated replay is rejected deterministically without duplicating effects. | Replay/idempotency tests. |
| MA3-AC4 | Natural-language content cannot alter local policy, permissions, tool definitions, or verification behavior. | M-X01 security tests. |
| MA3-AC5 | Evidence pointers are retained as untrusted references and cannot trigger an unapproved fetch or credential disclosure. | M-X06 capability tests. |

**Risks/findings to carry:** Transport-level denial of service beyond bounded
synthetic request limits is not a claim of this phase.

## Goal MA-4 — Build the claims and dispute graph

**Objective:** Represent cross-institution facts, claims, evidence, policy
references, interpretations, agreement, and disagreement as a structured graph.

**Dependencies:** MA-1, MA-3. **Advances:** O21, O23. Scenarios: M-R02, M-A01,
M-A02, M-X06. Constraints: C06, C14, C20, C21.

**Verification layers:** TV-01, TV-03.

**In scope:** institution-attributed claim/evidence/policy nodes and typed edges,
explicit dispute nodes, agreed versus disputed facts, source/version/freshness,
and dispute categories for fact, missing evidence, authenticity, freshness,
policy applicability/interpretation, terminology mapping, workflow state,
authority, and clinical judgment. **Excluded:** deciding which institution is
right, negotiation transitions, and automated legal or clinical adjudication.

**Deliverables:** graph contracts/store interface, projection/query operations,
fixtures, and tests.

| Criterion | Binary acceptance check | Expected evidence |
|---|---|---|
| MA4-AC1 | Each claim retains its institution/agent author and links to machine-readable evidence and policy references with versions. | Graph invariant tests. |
| MA4-AC2 | Conflicting claims create an explicit categorized dispute node without overwriting either claim. | Conflict fixture tests. |
| MA4-AC3 | Agreed facts and disputed facts are independently queryable for a case. | Query tests. |
| MA4-AC4 | Stale, unverifiable, or malicious references retain their verification state and cannot count as verified support. | Provenance/security tests. |
| MA4-AC5 | No graph operation resolves policy interpretation or clinical judgment by model opinion alone. | Architecture tests/inspection. |

**Risks/findings to carry:** Graph scoring or semantic truth ranking is outside
scope unless later evaluation proves a bounded need.

## Goal MA-5 — Implement the bounded negotiation protocol

**Objective:** Allow machine-resolvable disputes to advance through a predefined
transaction/state space while loops, invalid transitions, and unresolved
high-consequence questions stop or escalate deterministically.

**Dependencies:** MA-2, MA-3, MA-4. **Advances:** O21. Scenarios: M-R02, M-A01,
M-A02, M-F01. Constraints: C15, C16, C19, C20.

**Verification layers:** TV-01, TV-03, TV-04.

**In scope:** transaction transition graph, deterministic Level 0 resolution,
bounded clarification, constrained proposal/counterproposal, permitted
resolution action set, turn/request/time limits, stop reasons, and escalation
signals. **Excluded:** open-ended chat, new transaction types invented at
runtime, clinical/legal arbitration, and human-review implementation.

**Deliverables:** protocol state machine, resolution rules, limit configuration,
orchestrator, trace events, and tests.

| Criterion | Binary acceptance check | Expected evidence |
|---|---|---|
| MA5-AC1 | Every undeclared transaction transition is rejected without changing dispute or institutional state. | Transition-table tests. |
| MA5-AC2 | Missing evidence, authoritative-source mismatch, invalid workflow state, stale policy, and declared deterministic calculations resolve or stop with explicit machine-readable reasons. | Level 0 rule tests. |
| MA5-AC3 | Clarifications and proposals are limited to configured transaction types, action choices, turns, requests, and deadlines. | Boundary tests. |
| MA5-AC4 | Loops and limit exhaustion terminate with escalation or a terminal failure state rather than continued messages. | M-F01 tests. |
| MA5-AC5 | Policy/clinical disputes and consequences outside delegated envelopes cannot be finalized by negotiation. | M-A02 and envelope tests. |

**Risks/findings to carry:** Optimize neither message count nor speed at the
expense of correctness or appropriate escalation.

## Goal MA-6 — Implement cross-institution human escalation

**Objective:** Pause machine negotiation and route unresolved or
high-consequence disputes to authorized institutional humans, then separately
authorize any resulting commitment.

**Dependencies:** MA-5. **Advances:** O22, O23. Scenarios: M-A02, M-F02, M-F03,
M-D01. Constraints: C07, C17, C19–C21.

**Verification layers:** TV-01, TV-03, TV-06.

**In scope:** either-party review request, negotiation pause/lock, institution-
scoped reviewer identity/role, attributable decision and rationale, conflict/race
handling, return-to-protocol outcome, and separate commitment authorization.
**Excluded:** external adjudication, real-world legal authority, and allowing a
human decision from one institution to mint authority for the other.

**Deliverables:** escalation/review contracts and service, protocol integration,
commitment handoff, distributed audit events, and tests.

| Criterion | Binary acceptance check | Expected evidence |
|---|---|---|
| MA6-AC1 | Either institution can require review, after which machine negotiation and commitment execution pause deterministically. | Bilateral integration tests. |
| MA6-AC2 | Each human decision records institution, reviewer identity/role, timestamp, rationale, case/dispute IDs, and decision version. | Audit-schema tests. |
| MA6-AC3 | Stale, racing, or contradictory human/agent decisions cannot silently overwrite a newer or locked decision. | Concurrency/version tests. |
| MA6-AC4 | A human resolution does not bind the counterparty until the responsible institution's gate separately authorizes and signs `COMMIT_ACTION`. | Commitment integration tests. |
| MA6-AC5 | Unresolved external-adjudication cases stop with an explicit escalated state rather than invoking an LLM arbitrator. | Terminal-state tests. |

**Risks/findings to carry:** Real external appeals, regulators, contractual
dispute mechanisms, and independent reviewers remain research-only.

## Goal MA-7 — Build adversarial multi-agent evals and release gates

**Objective:** Measure governed transaction behavior and block release on any
known critical commitment, disclosure, review-bypass, forgery, replay, or
cross-agent policy-control failure.

**Dependencies:** MA-2, MA-3, MA-4, MA-5, MA-6. **Advances:** O23. Scenarios:
M-A01, M-A02, M-X01–M-X07, M-F01–M-F03. Constraints: C08–C10, C14, C18–C22.

**Verification layers:** TV-03, TV-04, TV-05, TV-07.

**In scope:** executable adversarial scenarios from the source specification,
multi-agent metrics/taxonomy, institutional consistency checks, hard release
gates, blocked/pass report, and regression workflow. **Excluded:** optimizing for
shortest negotiation or claiming exhaustive distributed-system security.

**Deliverables:** scenario corpus/runner extensions, graders, metrics, release
rules/report, regressions, and methodology documentation.

| Criterion | Binary acceptance check | Expected evidence |
|---|---|---|
| MA7-AC1 | The suite covers cross-agent injection, forged commitment/token, replay, irrelevant-data request, malicious evidence pointer, infinite clarification, contradictory commitment, stale policy, and legitimate human adjudication. | Scenario inventory validator. |
| MA7-AC2 | No test permits an unauthorized commitment or disclosure, and mandatory escalations occur as expected. | Full-suite report and side-effect assertions. |
| MA7-AC3 | Attacks and failures are classified/logged, with metrics for source-specified resolution, escalation, message/turn, unsupported-claim, invalid-attempt, rejection, mismatch, loop/deadlock, overturn, and consistency measures. | Metrics/report schema tests. |
| MA7-AC4 | Any successful unauthorized commitment/disclosure, human-review bypass, accepted forged token, unresolved critical replay flaw, or natural-language policy mutation blocks release. | Seeded hard-gate tests. |
| MA7-AC5 | Each important remediation includes a minimal regression and the full multi-agent suite remains unattended and reproducible. | Regression invariant and rerun transcript. |

**Risks/findings to carry:** Quality targets must not average away hard-safety
failures or reward shorter negotiation when it reduces correctness.

## Goal MA-8 — Demonstrate the provider-payer case lifecycle

**Objective:** Run one complete synthetic provider-payer dispute through both
institutional systems, ending in an attributable separately authorized
commitment with an end-to-end reconstructable timeline.

**Dependencies:** MA-7. **Advances:** O17–O23. Scenarios: M-R01, M-R02, M-A02,
M-D01. Constraints: C13–C22.

**Verification layers:** TV-02, TV-03, TV-06, TV-07.

**In scope:** the source-specified eleven-step lifecycle, shared case/correlation
identity, institution-local traces, a combined authorized projection, provenance,
deterministic partial resolution, human escalation, commitment authorization,
final state synchronization, demo script, and release evidence. **Excluded:**
real institutional connectivity, real PHI, free-form negotiation, and production
federated observability.

**Deliverables:** two-institution fixture/configuration, lifecycle orchestration,
timeline projection, end-to-end tests, demo script, and release report.

| Criterion | Binary acceptance check | Expected evidence |
|---|---|---|
| MA8-AC1 | Every cross-boundary message in the lifecycle is typed, identity-verified, integrity-protected, independently admitted, and authorized by its sender. | End-to-end trace assertions. |
| MA8-AC2 | All material claims link to source/version provenance, and agreed versus disputed facts remain distinguishable. | Claims-graph assertions. |
| MA8-AC3 | Neither agent directly creates a binding commitment; the unresolved interpretation triggers attributable review and a separate payer commitment authorization. | Authority-boundary assertions. |
| MA8-AC4 | The combined timeline identifies each institution/agent, evidence, gate decision, negotiation transition, review, binding commitment, and point of non-machine resolution while preserving local audit boundaries. | Timeline snapshot and reviewer checklist. |
| MA8-AC5 | Both systems reach a consistent final case/transaction state, the multi-agent release gate passes, and the demo distinguishes model reasoning from institutional authority. | State consistency test, gate report, and timed demo dry run. |

**Risks/findings to carry:** The result is a prototype control plane for governed
autonomous transactions, not evidence of legal, clinical, or production
readiness.

## Completion arc

D0 establishes the buyer, operator, workflow, value baseline, thin slice, and
reuse decisions. G00–G06 establish the runnable shell, standards-recognizable
synthetic integrations, typed state, and provenance. G07–G10 add
the central authority boundary and prove it end to end. G11–G17 make behavior
measurable, reviewable, gated, and explicitly bounded. G18 proves the failure
response. G19–G20 deploy and communicate a bounded synthetic pilot for
interviewers and prospective clients. After an explicit stability gate,
MA-0–MA-8 extend those controls across mutually untrusted institutions using an
A2A-compatible transport, healthcare transaction profile, dual authority
envelopes, bounded negotiation, disclosure policy, human escalation,
adversarial release gates, and a provider-payer lifecycle.

The first eligible goal is **D0**. It remains proposed until the user explicitly
asks to begin or invokes `cycle`. No `MA-*` goal is eligible while D0 or any core
goal is incomplete or core stability is unconfirmed.
