"""Validate the committed synthetic FHIR R4 fixture subset."""

from __future__ import annotations

from pathlib import Path

from caduceus.adapters.fhir_r4 import SyntheticFhirR4Adapter


def main() -> int:
    repository_root = Path(__file__).parents[1]
    fixture_path = repository_root / "fixtures" / "fhir_r4" / "baseline_bundle.json"
    adapter = SyntheticFhirR4Adapter.from_bundle(fixture_path)
    issues = adapter.validate_supported_subset()

    if issues:
        print("Synthetic FHIR R4 fixture check failed:")
        for issue in issues:
            print(f"{issue.code}: {issue.location}: {issue.message}")
        return 1

    patient_count = len(adapter.list_resources("Patient"))
    case_count = len(adapter.list_resources("Task"))
    resource_count = len(tuple(adapter.iter_resources()))

    if patient_count < 3 or case_count < 3:
        print("Synthetic FHIR R4 fixture check failed:")
        print(f"expected at least 3 patients and cases, got {patient_count}/{case_count}")
        return 1

    print(
        "Synthetic FHIR R4 fixture check passed: "
        f"{resource_count} resources, {patient_count} patients, {case_count} cases."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
