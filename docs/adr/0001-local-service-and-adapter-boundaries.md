# ADR 0001: Local service foundation and adapter boundaries

**Status:** accepted in G00.

## Context

G00 must supply a runnable, deterministic local shell without beginning the
healthcare workflow or adding proprietary dependencies. D0 requires all future
FHIR record, payer behavior, policy retrieval, model, and consequential-action
integrations to be replaceable.

## Decision

Use FastAPI for the local HTTP boundary, Uvicorn for the development server,
and pytest for deterministic tests. The initial service exposes only `GET
/health`; it receives no case data, accepts no credentials, and performs no
external I/O.

Reserve `src/caduceus/adapters/` for future adapter implementations. G00 creates
no FHIR, payer, policy, model, or executor contract and makes no network call.
Those boundaries are introduced and tested by their owning goals: G03/G04,
G05, G09, and G08 respectively.

## Consequences

The local path requires only Python and open-source dependencies. This is a
deliberate reimplementation of the minimal service shell, not a replacement for
FHIR, Da Vinci, a policy engine, orchestration framework, or A2A. The D0
build-versus-reuse decisions remain controlling for those later capabilities.

