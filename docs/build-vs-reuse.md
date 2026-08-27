# D0 build-versus-reuse decisions

These architecture decision records apply the charter's C24 decision rule:
choose **adopt**, **adapt**, **interoperate**, or **reimplement** before building
an adjacent capability. A choice does not imply broad conformance, production
readiness, or that a later goal has already verified the integration.

## Decision index

| ID | Capability | Decision | First verification or revisit |
|---|---|---|---|
| BR-01 | Synthea | Adapt | G03 |
| BR-02 | FHIR R4 | Interoperate | G03 and G12 |
| BR-03 | Da Vinci PAS/DTR/CRD | Adapt and interoperate | G04 and G12 |
| BR-04 | Policy and authorization engines | Reimplement the narrow thesis-specific rules behind an adapter | G07; compare OPA in B01 |
| BR-05 | Orchestration runtime | Reimplement minimal deterministic control flow | G02/G09; revisit before G13/G19 |
| BR-06 | HealthAdminBench | Interoperate only where semantics remain unchanged | G12 |
| BR-07 | A2A | Interoperate, deferred | MA-1 after the future-phase gate |
| BR-08 | Existing healthcare-agent demonstrations | Adapt comparison patterns only | G09/G20 |

## BR-01 — Synthea synthetic records

**Decision: adapt.** Use [Synthea](https://github.com/synthetichealth/synthea)
to generate synthetic patient histories and adapt selected output into small,
committed, deterministic fixtures. Do not build a patient generator or depend
on a full regenerated population for ordinary tests. Pin the generator version,
seed, transformation, and resulting fixture provenance. G03 verifies that no
real PHI enters the repository and that the fixture supports the declared FHIR
surface.

## BR-02 — FHIR R4

**Decision: interoperate.** Use FHIR R4 resource shapes, identifiers, references,
and validation for a declared subset rather than a bespoke “FHIR-like” schema.
Keep internal domain contracts distinct behind a FHIR adapter and document every
intentional deviation. G03 selects the exact resources/profiles and validator;
G12 tests the claim against pinned external fixtures. Recognizable subset
behavior is not broad FHIR conformance.

## BR-03 — Da Vinci PAS, DTR, and CRD

**Decision: adapt and interoperate.** Model the deterministic payer simulator
and provider interaction on the published
[Da Vinci PAS implementation guide](https://hl7.org/fhir/us/davinci-pas/)
and use the [Da Vinci payer reference implementation](https://github.com/HL7-DaVinci/br-payer)
as a contract/reference source. The local simulator remains deterministic and
small, but its declared operations and fixtures must be recognizable at the
adapter boundary. G04 pins the package/version and deviations; G12 determines
whether any external conformance statement is supportable.

## BR-04 — Policy and authorization engines

**Decision: reimplement the narrow rule set behind a stable adapter.** Begin
with typed Python rules because the project thesis requires payload-bound
institutional authority, evidence/provenance checks, workflow state, and
human-review requirements that must remain transparent in the first thin slice.
[Open Policy Agent](https://github.com/open-policy-agent/opa) is a credible
general-purpose policy engine, but adding it now would not remove those domain
contracts. G07 verifies the decision interface and fail-closed behavior. B01
retains an OPA/Cedar comparison; OpenLeash and AgentGate remain conceptual
comparators rather than required dependencies.

## BR-05 — Orchestration runtime

**Decision: reimplement minimal deterministic control flow.** Build explicit
workflow state and a small, inspectable investigation loop before adopting a
framework. [LangGraph](https://github.com/langchain-ai/langgraph) is a later
candidate if durable execution, pause/resume, or human-in-the-loop recovery
requirements exceed the local design. G02 and G09 must keep the model outside
workflow authority; revisit before G13 or G19 if durable runtime evidence
justifies adoption.

## BR-06 — HealthAdminBench

**Decision: interoperate conditionally.** In G12, crosswalk suitable tasks from
[HealthAdminBench](https://github.com/som-shahlab/health-admin-bench) to project
capabilities. Publish a benchmark result only if the task, verifier, environment,
adapter, and version run unchanged. Changed tasks become Caduceus EV-02 cases,
not a HealthAdminBench score.

## BR-07 — A2A

**Decision: interoperate, deferred.** If the gated multi-agent phase begins,
carry typed healthcare transactions over the
[A2A protocol](https://github.com/a2aproject/A2A) rather than recreating generic
agent discovery or messaging. The institutional identity, authority,
disclosure, integrity, and replay profile remains Caduceus-specific. A2A is not
a dependency of D0 or G00–G20 and is revisited in MA-1 only after the future-
phase gate passes.

## BR-08 — Existing healthcare-agent demonstrations

**Decision: adapt comparison patterns only.** The
[AWS healthcare-agent sample](https://github.com/aws-samples/sample-healthcare-agents)
and [Microsoft prior-authorization multi-agent accelerator](https://github.com/microsoft/Prior-Authorization-Multi-Agent-Solution-Accelerator)
show relevant data gathering, policy, review, and prior-authorization flows.
Treat them as implementation comparators, not foundations: they carry cloud
dependencies and different agent/authority boundaries. Caduceus must
differentiate on independent authorization, provenance, and correct-but-not-
authorized execution rather than reproduce generic multi-agent orchestration.

## Cross-cutting acceptance effect

Every later adapter or dependency change must record its exact version,
supported contract, deviations, failure behavior, and reason for revisiting the
D0 decision. A library may implement mechanics; it cannot grant the model
authority, erase provenance requirements, or upgrade evidence from EV-01/EV-02
to a customer claim.
