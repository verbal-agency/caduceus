"""Synthetic representative payloads for domain-contract tests."""

from __future__ import annotations


CASE_PAYLOAD = {
    "case_id": "CASE-SYN-001",
    "workflow": "lumbar_mri_prior_auth",
    "patient_id": "PATIENT-SYN-001",
    "payer_id": "PAYER-SYN-001",
}

EVIDENCE_PAYLOAD = {
    "evidence_id": "EVIDENCE-SYN-001",
    "case_id": "CASE-SYN-001",
    "source_type": "synthetic_fhir_procedure",
    "source_locator": "Procedure/PT-SYN-001",
    "source_version": "1",
    "source_observed_at": "2026-08-26T12:00:00Z",
}

CLAIM_PAYLOAD = {
    "claim_id": "CLAIM-SYN-001",
    "case_id": "CASE-SYN-001",
    "statement": "Qualifying physical therapy is documented in the synthetic record.",
    "evidence_ids": ["EVIDENCE-SYN-001"],
}

PROPOSED_ACTION_PAYLOAD = {
    "action_id": "ACTION-SYN-001",
    "case_id": "CASE-SYN-001",
    "action_class": "DRAFT_APPEAL",
    "rationale": "Prepare an administrative appeal draft for review.",
    "claim_ids": ["CLAIM-SYN-001"],
    "evidence_ids": ["EVIDENCE-SYN-001"],
}

AUTHORIZATION_REQUEST_PAYLOAD = {
    "request_id": "AUTH-REQUEST-SYN-001",
    "case_id": "CASE-SYN-001",
    "agent_id": "caseworker-test",
    "agent_version": "test-v1",
    "proposed_action": PROPOSED_ACTION_PAYLOAD,
}

AUTHORIZATION_DECISION_PAYLOAD = {
    "decision_id": "AUTH-DECISION-SYN-001",
    "authorization_request_id": "AUTH-REQUEST-SYN-001",
    "outcome": "REQUIRE_HUMAN_REVIEW",
    "reason_codes": ["REVIEW_REQUIRED"],
}

INVALID_AUTHORIZATION_REQUEST_PAYLOAD = {
    **AUTHORIZATION_REQUEST_PAYLOAD,
    "proposed_action": {
        **PROPOSED_ACTION_PAYLOAD,
        "action_class": "REWRITE_PAYER_POLICY",
    },
}

INVALID_AUTHORIZATION_DECISION_PAYLOAD = {
    **AUTHORIZATION_DECISION_PAYLOAD,
    "outcome": "MAYBE",
}
