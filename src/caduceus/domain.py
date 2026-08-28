"""Typed wire contracts for Caduceus's bounded-agency flow.

These models describe data shape only. Workflow transitions, authorization
rules, persistence, and execution are owned by later goals.
"""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field


NonEmptyString = Annotated[str, Field(min_length=1)]
NonEmptyStrings = Annotated[tuple[NonEmptyString, ...], Field(min_length=1)]


class DomainModel(BaseModel):
    """Shared fail-closed wire-format behavior for domain contracts."""

    model_config = ConfigDict(extra="forbid", frozen=True)


class ActionClass(StrEnum):
    """The source-defined administrative action vocabulary."""

    READ_RECORD = "READ_RECORD"
    SEARCH_POLICY = "SEARCH_POLICY"
    REQUEST_INFORMATION = "REQUEST_INFORMATION"
    DRAFT_APPEAL = "DRAFT_APPEAL"
    SUBMIT_APPEAL = "SUBMIT_APPEAL"
    UPDATE_CASE_STATUS = "UPDATE_CASE_STATUS"
    CLOSE_CASE = "CLOSE_CASE"
    ESCALATE_TO_HUMAN = "ESCALATE_TO_HUMAN"


class AuthorizationOutcome(StrEnum):
    """The source-defined result vocabulary for a later authority service."""

    ALLOW = "ALLOW"
    ALLOW_WITH_CONSTRAINTS = "ALLOW_WITH_CONSTRAINTS"
    REQUIRE_HUMAN_REVIEW = "REQUIRE_HUMAN_REVIEW"
    DENY = "DENY"


class Case(DomainModel):
    """An administrative exception case, before workflow state is introduced."""

    case_id: NonEmptyString
    workflow: NonEmptyString
    patient_id: NonEmptyString
    payer_id: NonEmptyString


class Evidence(DomainModel):
    """A versioned or timestamped source reference associated with a case."""

    evidence_id: NonEmptyString
    case_id: NonEmptyString
    source_type: NonEmptyString
    source_locator: NonEmptyString
    source_version: NonEmptyString
    source_observed_at: datetime


class Claim(DomainModel):
    """A material administrative assertion with explicit evidence references."""

    claim_id: NonEmptyString
    case_id: NonEmptyString
    statement: NonEmptyString
    evidence_ids: NonEmptyStrings


class ProposedAction(DomainModel):
    """An agent- or operator-authored action proposal, not an authorization."""

    action_id: NonEmptyString
    case_id: NonEmptyString
    action_class: ActionClass
    rationale: NonEmptyString
    claim_ids: NonEmptyStrings
    evidence_ids: NonEmptyStrings


class AuthorizationRequest(DomainModel):
    """A request for a later independent authorization decision."""

    request_id: NonEmptyString
    case_id: NonEmptyString
    agent_id: NonEmptyString
    agent_version: NonEmptyString
    proposed_action: ProposedAction


class AuthorizationDecision(DomainModel):
    """The authority-service output associated with one authorization request."""

    decision_id: NonEmptyString
    authorization_request_id: NonEmptyString
    outcome: AuthorizationOutcome
    reason_codes: NonEmptyStrings
