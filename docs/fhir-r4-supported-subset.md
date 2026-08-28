# FHIR R4 supported subset for G03

This document defines the versioned synthetic FHIR R4 contract used by G03. It
is a thin-slice adapter contract, not a claim of broad FHIR server conformance.

## Supported resource types

The G03 fixture and adapter support these FHIR R4 resource types:

| Resource | Required fields in this subset | Required references |
|---|---|---|
| Patient | `resourceType`, `id`, `identifier`, `name`, `gender`, `birthDate` | None |
| Coverage | `resourceType`, `id`, `status`, `beneficiary`, `payor` | `beneficiary.reference` to `Patient` |
| Encounter | `resourceType`, `id`, `status`, `class`, `subject`, `period` | `subject.reference` to `Patient` |
| Procedure | `resourceType`, `id`, `status`, `code`, `subject`, `encounter`, `performedPeriod` | `subject.reference` to `Patient`; `encounter.reference` to `Encounter` |
| Condition | `resourceType`, `id`, `clinicalStatus`, `code`, `subject`, `encounter`, `recordedDate` | `subject.reference` to `Patient`; `encounter.reference` to `Encounter` |
| ServiceRequest | `resourceType`, `id`, `status`, `intent`, `code`, `subject`, `encounter`, `reasonReference` | `subject.reference` to `Patient`; `encounter.reference` to `Encounter`; `reasonReference.reference` to `Condition` |
| Claim | `resourceType`, `id`, `status`, `type`, `use`, `patient`, `created`, `provider`, `priority`, `insurance`, `item` | `patient.reference` to `Patient`; `insurance.coverage.reference` to `Coverage`; `item.encounter.reference` to `Encounter` |
| Task | `resourceType`, `id`, `status`, `intent`, `focus`, `for`, `input` | `focus.reference` to `ServiceRequest`; `for.reference` to `Patient`; `input.valueReference.reference` to `Claim` |

## Adapter behavior

- Resources are loaded from `fixtures/fhir_r4/baseline_bundle.json`.
- Resources are retrieved by exact resource type and stable `id`.
- Cross-resource references use the standard `ResourceType/id` reference shape.
- Baseline validation rejects missing required fields, unsupported resource
  types, duplicate resource identities, unresolved references, stale records,
  and fields outside the declared top-level subset.
- Deterministic failure modes are available for timeout, malformed, stale,
  partial, unexpected-schema, and duplicate scenarios.

## Intentional deviations

- The fixture is a small custom deterministic fixture rather than raw generated
  Synthea output. Provenance and rationale are recorded in
  `fixtures/fhir_r4/PROVENANCE.md`.
- The adapter validates only the declared top-level fields and references above.
  It does not claim full FHIRPath, terminology binding, package validation, or
  server capability conformance.
- Search is limited to listing resources by type and exact-ID retrieval. General
  FHIR REST search parameters are outside G03.
- Payer-specific Da Vinci PAS/DTR behavior is outside this subset and belongs to
  G04.
