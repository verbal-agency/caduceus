"""Synthetic FHIR R4 fixture adapter for the G03 thin slice."""

from __future__ import annotations

import copy
import json
from collections.abc import Iterator, Mapping
from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path
from types import MappingProxyType
from typing import Any, Final


SUPPORTED_RESOURCE_TYPES: Final = (
    "Patient",
    "Coverage",
    "Encounter",
    "Procedure",
    "Condition",
    "ServiceRequest",
    "Claim",
    "Task",
)

REQUIRED_FIELDS: Final = MappingProxyType(
    {
        "Patient": (
            "resourceType",
            "id",
            "identifier",
            "name",
            "gender",
            "birthDate",
        ),
        "Coverage": ("resourceType", "id", "status", "beneficiary", "payor"),
        "Encounter": (
            "resourceType",
            "id",
            "status",
            "class",
            "subject",
            "period",
        ),
        "Procedure": (
            "resourceType",
            "id",
            "status",
            "code",
            "subject",
            "encounter",
            "performedPeriod",
        ),
        "Condition": (
            "resourceType",
            "id",
            "clinicalStatus",
            "code",
            "subject",
            "encounter",
            "recordedDate",
        ),
        "ServiceRequest": (
            "resourceType",
            "id",
            "status",
            "intent",
            "code",
            "subject",
            "encounter",
            "reasonReference",
        ),
        "Claim": (
            "resourceType",
            "id",
            "status",
            "type",
            "use",
            "patient",
            "created",
            "provider",
            "priority",
            "insurance",
            "item",
        ),
        "Task": (
            "resourceType",
            "id",
            "status",
            "intent",
            "focus",
            "for",
            "input",
        ),
    }
)

TOP_LEVEL_FIELDS: Final = MappingProxyType(
    {
        "Patient": REQUIRED_FIELDS["Patient"] + ("meta",),
        "Coverage": REQUIRED_FIELDS["Coverage"] + ("meta",),
        "Encounter": REQUIRED_FIELDS["Encounter"] + ("meta",),
        "Procedure": REQUIRED_FIELDS["Procedure"] + ("meta", "reasonReference"),
        "Condition": REQUIRED_FIELDS["Condition"] + ("meta",),
        "ServiceRequest": REQUIRED_FIELDS["ServiceRequest"] + ("meta",),
        "Claim": REQUIRED_FIELDS["Claim"] + ("meta", "diagnosis",),
        "Task": REQUIRED_FIELDS["Task"] + ("meta", "description", "businessStatus"),
    }
)


class FhirFailureMode(StrEnum):
    """Deterministic adapter failure modes required by G03."""

    TIMEOUT = "timeout"
    MALFORMED = "malformed"
    STALE = "stale"
    PARTIAL = "partial"
    UNEXPECTED_SCHEMA = "unexpected_schema"
    DUPLICATE = "duplicate"


class FhirAdapterError(Exception):
    """Base error for synthetic FHIR adapter failures."""


class FhirAdapterTimeoutError(FhirAdapterError):
    """Raised when the deterministic timeout mode is active."""


class FhirResourceNotFoundError(FhirAdapterError, KeyError):
    """Raised when a requested resource does not exist in the fixture."""


@dataclass(frozen=True)
class FhirValidationIssue:
    """Validation issue for the declared supported subset."""

    code: str
    location: str
    message: str


class SyntheticFhirR4Adapter:
    """Read-only adapter over a deterministic synthetic FHIR R4 fixture bundle."""

    def __init__(
        self,
        resources: tuple[Mapping[str, Any], ...],
        *,
        failure_mode: FhirFailureMode | None = None,
    ) -> None:
        self._failure_mode = failure_mode
        self._resources = _apply_failure_mode(resources, failure_mode)
        self._index = _index_resources(self._resources)

    @classmethod
    def from_bundle(
        cls, path: Path, *, failure_mode: FhirFailureMode | None = None
    ) -> SyntheticFhirR4Adapter:
        bundle = json.loads(path.read_text(encoding="utf-8"))
        entries = bundle.get("entry", [])
        resources = tuple(entry.get("resource", {}) for entry in entries)
        return cls(resources, failure_mode=failure_mode)

    def iter_resources(self) -> Iterator[Mapping[str, Any]]:
        return iter(tuple(_copy_resource(resource) for resource in self._resources))

    def list_resources(self, resource_type: str) -> tuple[Mapping[str, Any], ...]:
        return tuple(
            _copy_resource(resource)
            for resource in self._resources
            if resource.get("resourceType") == resource_type
        )

    def get_resource(self, resource_type: str, resource_id: str) -> Mapping[str, Any]:
        if self._failure_mode is FhirFailureMode.TIMEOUT:
            raise FhirAdapterTimeoutError("deterministic FHIR adapter timeout")
        try:
            return _copy_resource(self._index[(resource_type, resource_id)])
        except KeyError as exc:
            raise FhirResourceNotFoundError(f"{resource_type}/{resource_id}") from exc

    def validate_supported_subset(self) -> tuple[FhirValidationIssue, ...]:
        issues: list[FhirValidationIssue] = []
        seen: set[tuple[str, str]] = set()

        for position, resource in enumerate(self._resources):
            location = f"entry[{position}]"
            resource_type = resource.get("resourceType")
            resource_id = resource.get("id")

            if not isinstance(resource_type, str):
                issues.append(
                    FhirValidationIssue(
                        "missing_resource_type",
                        location,
                        "resourceType is required",
                    )
                )
                continue
            if resource_type not in SUPPORTED_RESOURCE_TYPES:
                issues.append(
                    FhirValidationIssue(
                        "unsupported_resource_type",
                        location,
                        f"{resource_type} is outside the declared subset",
                    )
                )
                continue

            for field_name in REQUIRED_FIELDS[resource_type]:
                if field_name not in resource:
                    issues.append(
                        FhirValidationIssue(
                            "missing_required_field",
                            f"{location}.{field_name}",
                            f"{resource_type}.{field_name} is required",
                        )
                    )

            unexpected = set(resource) - set(TOP_LEVEL_FIELDS[resource_type])
            for field_name in sorted(unexpected):
                issues.append(
                    FhirValidationIssue(
                        "unexpected_schema",
                        f"{location}.{field_name}",
                        f"{resource_type}.{field_name} is outside the declared subset",
                    )
                )

            if isinstance(resource_id, str):
                identity = (resource_type, resource_id)
                if identity in seen:
                    issues.append(
                        FhirValidationIssue(
                            "duplicate_resource",
                            location,
                            f"{resource_type}/{resource_id} appears more than once",
                        )
                    )
                seen.add(identity)

            if _is_stale(resource):
                issues.append(
                    FhirValidationIssue(
                        "stale_resource",
                        location,
                        f"{resource_type}/{resource_id} is older than the fixture floor",
                    )
                )

        issues.extend(self.validate_references())
        return tuple(issues)

    def validate_references(self) -> tuple[FhirValidationIssue, ...]:
        issues: list[FhirValidationIssue] = []
        identities = set(self._index)

        for resource in self._resources:
            source_type = str(resource.get("resourceType", "<unknown>"))
            source_id = str(resource.get("id", "<unknown>"))
            for reference in _iter_references(resource):
                target = _parse_reference(reference)
                if target is None:
                    continue
                if target not in identities:
                    issues.append(
                        FhirValidationIssue(
                            "unresolved_reference",
                            f"{source_type}/{source_id}",
                            f"{source_type}/{source_id} references {reference}",
                        )
                    )

        return tuple(issues)


def _index_resources(
    resources: tuple[Mapping[str, Any], ...]
) -> dict[tuple[str, str], Mapping[str, Any]]:
    index: dict[tuple[str, str], Mapping[str, Any]] = {}
    for resource in resources:
        resource_type = resource.get("resourceType")
        resource_id = resource.get("id")
        if isinstance(resource_type, str) and isinstance(resource_id, str):
            index.setdefault((resource_type, resource_id), resource)
    return index


def _copy_resource(resource: Mapping[str, Any]) -> Mapping[str, Any]:
    return copy.deepcopy(resource)


def _iter_references(value: Any) -> Iterator[str]:
    if isinstance(value, Mapping):
        reference = value.get("reference")
        if isinstance(reference, str):
            yield reference
        for child in value.values():
            yield from _iter_references(child)
    elif isinstance(value, list):
        for child in value:
            yield from _iter_references(child)


def _parse_reference(reference: str) -> tuple[str, str] | None:
    if "/" not in reference:
        return None
    resource_type, resource_id = reference.split("/", 1)
    if not resource_type or not resource_id:
        return None
    return resource_type, resource_id


def _is_stale(resource: Mapping[str, Any]) -> bool:
    meta = resource.get("meta")
    if not isinstance(meta, Mapping):
        return False
    last_updated = meta.get("lastUpdated")
    return isinstance(last_updated, str) and last_updated < "2026-01-01T00:00:00Z"


def _apply_failure_mode(
    resources: tuple[Mapping[str, Any], ...], failure_mode: FhirFailureMode | None
) -> tuple[Mapping[str, Any], ...]:
    mutated = list(copy.deepcopy(resources))

    if failure_mode is None or failure_mode is FhirFailureMode.TIMEOUT:
        return tuple(mutated)
    if failure_mode is FhirFailureMode.MALFORMED:
        mutated[0].pop("resourceType", None)
    elif failure_mode is FhirFailureMode.STALE:
        mutated[0].setdefault("meta", {})["lastUpdated"] = "2020-01-01T00:00:00Z"
    elif failure_mode is FhirFailureMode.PARTIAL:
        mutated = [resource for resource in mutated if resource.get("id") != "claim-syn-001"]
    elif failure_mode is FhirFailureMode.UNEXPECTED_SCHEMA:
        mutated[0]["undeclaredExtension"] = {"valueString": "schema drift"}
    elif failure_mode is FhirFailureMode.DUPLICATE:
        mutated.append(copy.deepcopy(mutated[0]))

    return tuple(mutated)
