"""Tests for the declared synthetic FHIR R4 fixture adapter."""

from __future__ import annotations

from pathlib import Path

import pytest

from caduceus.adapters.fhir_r4 import (
    FhirAdapterTimeoutError,
    FhirFailureMode,
    SyntheticFhirR4Adapter,
    SUPPORTED_RESOURCE_TYPES,
)


REPOSITORY_ROOT = Path(__file__).parents[1]
FIXTURE_PATH = REPOSITORY_ROOT / "fixtures" / "fhir_r4" / "baseline_bundle.json"
SUPPORTED_SUBSET_DOC = REPOSITORY_ROOT / "docs" / "fhir-r4-supported-subset.md"
PROVENANCE_DOC = REPOSITORY_ROOT / "fixtures" / "fhir_r4" / "PROVENANCE.md"


def test_each_required_resource_type_is_retrievable_by_stable_id() -> None:
    adapter = SyntheticFhirR4Adapter.from_bundle(FIXTURE_PATH)

    for resource_type in SUPPORTED_RESOURCE_TYPES:
        expected_id = f"{resource_type.lower()}-syn-001"
        resource = adapter.get_resource(resource_type, expected_id)

        assert resource["resourceType"] == resource_type
        assert resource["id"] == expected_id


def test_all_baseline_references_resolve_to_existing_resources() -> None:
    adapter = SyntheticFhirR4Adapter.from_bundle(FIXTURE_PATH)

    assert adapter.validate_references() == ()


def test_fixture_provides_three_distinct_synthetic_patients_and_cases() -> None:
    adapter = SyntheticFhirR4Adapter.from_bundle(FIXTURE_PATH)

    patients = adapter.list_resources("Patient")
    tasks = adapter.list_resources("Task")

    assert tuple(patient["id"] for patient in patients) == (
        "patient-syn-001",
        "patient-syn-002",
        "patient-syn-003",
    )
    assert tuple(task["id"] for task in tasks) == (
        "task-syn-001",
        "task-syn-002",
        "task-syn-003",
    )
    assert {task["for"]["reference"] for task in tasks} == {
        "Patient/patient-syn-001",
        "Patient/patient-syn-002",
        "Patient/patient-syn-003",
    }


def test_resources_validate_against_declared_supported_subset() -> None:
    adapter = SyntheticFhirR4Adapter.from_bundle(FIXTURE_PATH)

    assert adapter.validate_supported_subset() == ()


def test_retrieved_resources_do_not_mutate_adapter_state() -> None:
    adapter = SyntheticFhirR4Adapter.from_bundle(FIXTURE_PATH)
    resource = adapter.get_resource("Patient", "patient-syn-001")

    resource["id"] = "tampered"

    assert adapter.get_resource("Patient", "patient-syn-001")["id"] == "patient-syn-001"


def test_supported_subset_and_provenance_are_documented() -> None:
    subset_text = SUPPORTED_SUBSET_DOC.read_text(encoding="utf-8")
    provenance_text = PROVENANCE_DOC.read_text(encoding="utf-8")

    for resource_type in SUPPORTED_RESOURCE_TYPES:
        assert resource_type in subset_text

    assert "Intentional deviations" in subset_text
    assert "custom deterministic fixture" in provenance_text
    assert "Synthea" in provenance_text
    assert "materially better for the thin slice" in provenance_text


@pytest.mark.parametrize(
    ("failure_mode", "expected_code"),
    (
        (FhirFailureMode.MALFORMED, "missing_resource_type"),
        (FhirFailureMode.STALE, "stale_resource"),
        (FhirFailureMode.PARTIAL, "unresolved_reference"),
        (FhirFailureMode.UNEXPECTED_SCHEMA, "unexpected_schema"),
        (FhirFailureMode.DUPLICATE, "duplicate_resource"),
    ),
)
def test_failure_modes_are_deterministic_and_do_not_change_baseline(
    failure_mode: FhirFailureMode, expected_code: str
) -> None:
    baseline = SyntheticFhirR4Adapter.from_bundle(FIXTURE_PATH)
    failing = SyntheticFhirR4Adapter.from_bundle(FIXTURE_PATH, failure_mode=failure_mode)

    assert expected_code in {issue.code for issue in failing.validate_supported_subset()}
    assert baseline.validate_supported_subset() == ()
    assert len(tuple(baseline.iter_resources())) == 24


def test_timeout_failure_mode_is_deterministic_and_preserves_baseline() -> None:
    baseline = SyntheticFhirR4Adapter.from_bundle(FIXTURE_PATH)
    failing = SyntheticFhirR4Adapter.from_bundle(
        FIXTURE_PATH, failure_mode=FhirFailureMode.TIMEOUT
    )

    with pytest.raises(FhirAdapterTimeoutError):
        failing.get_resource("Patient", "patient-syn-001")

    assert baseline.get_resource("Patient", "patient-syn-001")["id"] == "patient-syn-001"
