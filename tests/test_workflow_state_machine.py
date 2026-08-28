"""Tests for deterministic case-workflow state enforcement."""

from __future__ import annotations

import inspect

import pytest
from pydantic import ValidationError

from caduceus.workflow import (
    ALLOWED_TRANSITIONS,
    CaseState,
    WorkflowStateRecord,
    WorkflowStateService,
    WorkflowTransitionError,
    transition_case_state,
)


EXPECTED_STATE_VALUES = (
    "NEW",
    "INVESTIGATING",
    "MISSING_INFORMATION",
    "READY_FOR_REVIEW",
    "READY_FOR_SUBMISSION",
    "SUBMITTED",
    "PENDING",
    "APPROVED",
    "DENIED",
    "ESCALATED",
    "CLOSED",
)


@pytest.mark.parametrize("from_state", tuple(ALLOWED_TRANSITIONS))
def test_declared_transitions_succeed(from_state: CaseState) -> None:
    current = WorkflowStateRecord(case_id="CASE-SYN-001", state=from_state, version=0)

    for to_state in ALLOWED_TRANSITIONS[from_state]:
        updated = transition_case_state(current, to_state)

        assert updated.case_id == current.case_id
        assert updated.state is to_state
        assert updated.version == current.version + 1


@pytest.mark.parametrize(
    ("from_state", "to_state"),
    [
        (from_state, to_state)
        for from_state in CaseState
        for to_state in CaseState
        if to_state not in ALLOWED_TRANSITIONS[from_state]
    ],
)
def test_undeclared_transitions_fail_without_changing_state(
    from_state: CaseState, to_state: CaseState
) -> None:
    current = WorkflowStateRecord(case_id="CASE-SYN-001", state=from_state, version=4)

    with pytest.raises(WorkflowTransitionError) as exc_info:
        transition_case_state(current, to_state)

    assert exc_info.value.case_id == current.case_id
    assert exc_info.value.from_state is from_state
    assert exc_info.value.to_state is to_state
    assert current.state is from_state
    assert current.version == 4


def test_state_enum_matches_the_source_contract() -> None:
    assert tuple(state.value for state in CaseState) == EXPECTED_STATE_VALUES


def test_service_records_state_changes_only_through_transition_boundary() -> None:
    service = WorkflowStateService()
    created = service.create_case("CASE-SYN-001")

    with pytest.raises(ValidationError):
        created.state = CaseState.SUBMITTED

    copied = created.model_copy(update={"state": CaseState.SUBMITTED})
    assert copied.state is CaseState.SUBMITTED
    assert service.get_state("CASE-SYN-001").state is CaseState.NEW

    updated = service.transition("CASE-SYN-001", CaseState.INVESTIGATING)

    assert updated.state is CaseState.INVESTIGATING
    assert service.get_state("CASE-SYN-001") == updated


def test_agent_facing_service_has_no_direct_state_mutator() -> None:
    public_methods = {
        name
        for name, member in inspect.getmembers(WorkflowStateService, inspect.isfunction)
        if not name.startswith("_")
    }

    assert public_methods == {"create_case", "get_state", "transition"}


@pytest.mark.parametrize(
    ("from_state", "to_state"),
    [
        (CaseState.SUBMITTED, CaseState.SUBMITTED),
        (CaseState.PENDING, CaseState.SUBMITTED),
        (CaseState.READY_FOR_SUBMISSION, CaseState.CLOSED),
        (CaseState.NEW, CaseState.CLOSED),
    ],
)
def test_duplicate_submission_and_premature_closure_are_rejected(
    from_state: CaseState, to_state: CaseState
) -> None:
    current = WorkflowStateRecord(case_id="CASE-SYN-001", state=from_state, version=2)

    with pytest.raises(WorkflowTransitionError):
        transition_case_state(current, to_state)
