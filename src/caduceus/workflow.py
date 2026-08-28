"""Deterministic case-workflow state enforcement."""

from __future__ import annotations

from enum import StrEnum
from types import MappingProxyType
from typing import Final

from pydantic import Field

from caduceus.domain import DomainModel, NonEmptyString


class CaseState(StrEnum):
    """Source-defined administrative case states."""

    NEW = "NEW"
    INVESTIGATING = "INVESTIGATING"
    MISSING_INFORMATION = "MISSING_INFORMATION"
    READY_FOR_REVIEW = "READY_FOR_REVIEW"
    READY_FOR_SUBMISSION = "READY_FOR_SUBMISSION"
    SUBMITTED = "SUBMITTED"
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    DENIED = "DENIED"
    ESCALATED = "ESCALATED"
    CLOSED = "CLOSED"


ALLOWED_TRANSITIONS: Final = MappingProxyType(
    {
        CaseState.NEW: (CaseState.INVESTIGATING,),
        CaseState.INVESTIGATING: (
            CaseState.MISSING_INFORMATION,
            CaseState.READY_FOR_REVIEW,
            CaseState.ESCALATED,
        ),
        CaseState.MISSING_INFORMATION: (
            CaseState.INVESTIGATING,
            CaseState.ESCALATED,
        ),
        CaseState.READY_FOR_REVIEW: (
            CaseState.MISSING_INFORMATION,
            CaseState.READY_FOR_SUBMISSION,
            CaseState.ESCALATED,
        ),
        CaseState.READY_FOR_SUBMISSION: (
            CaseState.SUBMITTED,
            CaseState.ESCALATED,
        ),
        CaseState.SUBMITTED: (
            CaseState.PENDING,
            CaseState.APPROVED,
            CaseState.DENIED,
            CaseState.ESCALATED,
        ),
        CaseState.PENDING: (
            CaseState.MISSING_INFORMATION,
            CaseState.APPROVED,
            CaseState.DENIED,
            CaseState.ESCALATED,
        ),
        CaseState.APPROVED: (CaseState.CLOSED,),
        CaseState.DENIED: (
            CaseState.READY_FOR_REVIEW,
            CaseState.ESCALATED,
            CaseState.CLOSED,
        ),
        CaseState.ESCALATED: (CaseState.CLOSED,),
        CaseState.CLOSED: (),
    }
)


class WorkflowStateRecord(DomainModel):
    """Persistable workflow state snapshot for one case."""

    case_id: NonEmptyString
    state: CaseState
    version: int = Field(ge=0)


class WorkflowTransitionError(ValueError):
    """Raised when a requested workflow transition is not declared."""

    def __init__(
        self, case_id: str, from_state: CaseState, to_state: CaseState
    ) -> None:
        self.case_id = case_id
        self.from_state = from_state
        self.to_state = to_state
        super().__init__(
            f"invalid workflow transition for {case_id}: "
            f"{from_state.value} -> {to_state.value}"
        )


class WorkflowStateNotFoundError(KeyError):
    """Raised when a transition targets an unknown case."""


def transition_case_state(
    current: WorkflowStateRecord, to_state: CaseState
) -> WorkflowStateRecord:
    """Return the next state snapshot if the transition is explicitly allowed."""

    if to_state not in ALLOWED_TRANSITIONS[current.state]:
        raise WorkflowTransitionError(current.case_id, current.state, to_state)
    return WorkflowStateRecord(
        case_id=current.case_id,
        state=to_state,
        version=current.version + 1,
    )


class WorkflowStateService:
    """Agent-facing boundary for recording case-state transitions."""

    def __init__(self) -> None:
        self._records: dict[str, WorkflowStateRecord] = {}

    def create_case(self, case_id: str) -> WorkflowStateRecord:
        record = WorkflowStateRecord(case_id=case_id, state=CaseState.NEW, version=0)
        self._records[case_id] = record
        return record

    def get_state(self, case_id: str) -> WorkflowStateRecord:
        try:
            return self._records[case_id]
        except KeyError as exc:
            raise WorkflowStateNotFoundError(case_id) from exc

    def transition(self, case_id: str, to_state: CaseState) -> WorkflowStateRecord:
        updated = transition_case_state(self.get_state(case_id), to_state)
        self._records[case_id] = updated
        return updated
