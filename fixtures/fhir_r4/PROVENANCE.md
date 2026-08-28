# G03 FHIR R4 fixture provenance

The `baseline_bundle.json` fixture is a custom deterministic fixture authored
for the Caduceus prior-authorization thin slice. It is synthetic and contains no
real PHI, client data, proprietary EHR export, or production credential.

The D0 build-versus-reuse decision for Synthea remains **adapt**: later fixture
work should adapt selected Synthea output rather than build a patient generator.
For G03, a custom deterministic fixture is materially better for the thin slice
because it keeps all identifiers, references, denial-relevant documentation,
missing-identifier cases, and failure-mode mutations small enough to inspect in
tests while avoiding a generator dependency before the adapter contract is
stable.

This is not a claim that Caduceus has broad FHIR conformance. The supported
subset and intentional deviations are declared in
`docs/fhir-r4-supported-subset.md`; broader standards fidelity remains routed to
B05 and G12.
