# Caduceus

A provider-side prior-authorization exception workbench exploring bounded
agency in consequential healthcare operations, using synthetic administrative
data only.

## Identifier key

`D0` is the discovery goal, `G##` identifies core implementation goals, and
`MA-#` identifies the gated future multi-agent phase. Goal acceptance criteria
use `{goal}-AC#`; other project requirements and evidence use the namespaces
defined in the [project-charter identifier key](docs/project-charter.md#identifier-key).

## Planning sources

- [`bounded_healthcare_agency_project.md`](bounded_healthcare_agency_project.md)
  is the original project specification.
- [`docs/project-charter.md`](docs/project-charter.md) defines the canonical
  outcomes, scenarios, constraints, and project-wide verification rules.
- [`docs/roadmap.md`](docs/roadmap.md) contains the ordered, cycle-ready goals.
- [`docs/backlog.md`](docs/backlog.md) contains optional work that is outside the
  core roadmap.

Goals `D0`, `G00`, and `G01` are complete. `G01` establishes typed,
JSON-serializable bounded-agency contracts; `G02` is the first proposed,
eligible goal and is not yet active.
The governed multi-agent `MA-*` phase remains ineligible until the complete
single-agent core is explicitly confirmed stable.

## Local development

Prerequisites: Python 3.12 or newer and [uv](https://docs.astral.sh/uv/).

```bash
uv sync --group dev
uv run pytest
uv run uvicorn caduceus.app:app --host 127.0.0.1 --port 8765
```

In a separate terminal, verify the local service:

```bash
curl http://127.0.0.1:8765/health
```

The endpoint returns `{"status":"healthy"}`. The documented test command is
`uv run pytest`; run `uv run python scripts/check_synthetic_data.py` to check
the fixture/example data policy separately.

## Synthetic-data-only policy

Never add real protected health information (PHI), client data, proprietary EHR
exports, or production credentials to this repository. Committed fixtures and
examples must be synthetic. Before adding a fixture or example directory at
`fixtures/`, `examples/`, or `tests/fixtures/`, add a `SYNTHETIC_DATA.md` file
at its root stating its source and confirming that all contents are synthetic.
The automated check enforces that marker requirement; it does not make an
unverified claim that arbitrary data is safe to commit.

## Initial architecture

The service currently exposes only a health route. The `caduceus.domain` module
defines frozen, extra-field-forbidden Pydantic contracts for cases, evidence,
claims, action proposals, authorization requests, and authorization decisions.
It contains no workflow rules, authorization policy, persistence, or execution
behavior. Adapter implementations remain intentionally absent: FHIR records,
payer behavior, policy retrieval, model integration, and consequential
execution are introduced by their owning goals. See
[ADR 0001](docs/adr/0001-local-service-and-adapter-boundaries.md).
