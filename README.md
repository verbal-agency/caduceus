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

No goal is active yet. An explicit request to begin or `cycle` should select
the first `proposed` roadmap goal whose dependencies are complete; initially
that is `D0`, which defines the buyer, operator workflow, value baseline, thin
slice, and build-versus-reuse decisions before implementation. The governed
multi-agent `MA-*` phase remains ineligible until D0 and the complete
single-agent core are explicitly confirmed stable.
