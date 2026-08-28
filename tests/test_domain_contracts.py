"""Tests for the typed, serializable bounded-agency contracts."""

from __future__ import annotations

from copy import deepcopy

import pytest
from pydantic import ValidationError

from caduceus.domain import (
    ActionClass,
    AuthorizationDecision,
    AuthorizationOutcome,
    AuthorizationRequest,
    Case,
    Claim,
    Evidence,
    ProposedAction,
)
from domain_fixtures import (
    AUTHORIZATION_DECISION_PAYLOAD,
    AUTHORIZATION_REQUEST_PAYLOAD,
    CASE_PAYLOAD,
    CLAIM_PAYLOAD,
    EVIDENCE_PAYLOAD,
    INVALID_AUTHORIZATION_DECISION_PAYLOAD,
    INVALID_AUTHORIZATION_REQUEST_PAYLOAD,
    PROPOSED_ACTION_PAYLOAD,
)


@pytest.mark.parametrize(
    ("model_type", "payload"),
    [
        (Case, CASE_PAYLOAD),
        (Evidence, EVIDENCE_PAYLOAD),
        (Claim, CLAIM_PAYLOAD),
        (ProposedAction, PROPOSED_ACTION_PAYLOAD),
        (AuthorizationRequest, AUTHORIZATION_REQUEST_PAYLOAD),
        (AuthorizationDecision, AUTHORIZATION_DECISION_PAYLOAD),
    ],
)
def test_required_domain_models_round_trip_without_data_loss(
    model_type: type[Case]
    | type[Evidence]
    | type[Claim]
    | type[ProposedAction]
    | type[AuthorizationRequest]
    | type[AuthorizationDecision],
    payload: dict[str, object],
) -> None:
    model = model_type.model_validate(payload)

    assert model_type.model_validate_json(model.model_dump_json()) == model


@pytest.mark.parametrize(
    ("model_type", "payload"),
    [
        (AuthorizationRequest, INVALID_AUTHORIZATION_REQUEST_PAYLOAD),
        (AuthorizationDecision, INVALID_AUTHORIZATION_DECISION_PAYLOAD),
        (Case, {key: value for key, value in CASE_PAYLOAD.items() if key != "case_id"}),
        (
            AuthorizationRequest,
            {
                key: deepcopy(value)
                for key, value in AUTHORIZATION_REQUEST_PAYLOAD.items()
                if key != "request_id"
            },
        ),
    ],
)
def test_malformed_or_incomplete_contracts_fail_validation(
    model_type: type[Case] | type[AuthorizationRequest] | type[AuthorizationDecision],
    payload: dict[str, object],
) -> None:
    with pytest.raises(ValidationError):
        model_type.model_validate(payload)


def test_action_and_outcome_enums_match_the_source_contract() -> None:
    assert tuple(action.value for action in ActionClass) == (
        "READ_RECORD",
        "SEARCH_POLICY",
        "REQUEST_INFORMATION",
        "DRAFT_APPEAL",
        "SUBMIT_APPEAL",
        "UPDATE_CASE_STATUS",
        "CLOSE_CASE",
        "ESCALATE_TO_HUMAN",
    )
    assert tuple(outcome.value for outcome in AuthorizationOutcome) == (
        "ALLOW",
        "ALLOW_WITH_CONSTRAINTS",
        "REQUIRE_HUMAN_REVIEW",
        "DENY",
    )


def test_proposed_actions_cannot_self_assert_an_authorization_outcome() -> None:
    proposed_action_fields = set(ProposedAction.model_fields)

    assert ProposedAction is not AuthorizationDecision
    assert "outcome" not in proposed_action_fields
    assert "authorization" not in proposed_action_fields
    assert "decision" not in proposed_action_fields

    with pytest.raises(ValidationError):
        ProposedAction.model_validate(
            {**PROPOSED_ACTION_PAYLOAD, "outcome": "ALLOW"}
        )
