# D0 discovery evidence and assumptions log

## Method and limitation

D0 used an external document and repository review completed August 26, 2026.
No domain expert or prospective user was accessible for interview in this
cycle. This satisfies the roadmap's explicitly permitted D0-AC3 substitute but
does **not** validate demand, buyer identity, operator workflow, adoption,
willingness to pay, or return on investment.

## Evidence log

| Source | What it supports | What it does not support |
|---|---|---|
| [CMS Interoperability and Prior Authorization final-rule fact sheet](https://www.cms.gov/newsroom/fact-sheets/cms-interoperability-prior-authorization-final-rule-cms-0057-f) | Current regulatory/API direction, denial-reason and additional-information responses, and affected-payer operational context. | A provider buyer, this product design, or client value. |
| [CMS Prior Authorization API FAQ](https://www.cms.gov/initiatives/burden-reduction/overview/interoperability/frequently-asked-questions/prior-authorization-api) | Request-level API expectations and current CMS timing/response explanations. | One provider's implementation reality or exception workflow. |
| [AMA 2024 prior-authorization physician survey](https://www.ama-assn.org/system/files/prior-authorization-survey.pdf) | Material physician/practice burden and administrative capacity pressure. | An exception-specialist persona, software demand, or a Caduceus ROI estimate. |
| [HL7 Da Vinci PAS workflow](https://hl7.org/fhir/us/davinci-pas/2022May/usecases.html) and [current PAS guide](https://hl7.org/fhir/us/davinci-pas/) | Recognizable prior-authorization stages and a standards-shaped provider/payer boundary. | Full conformance, actual client screens, staffing, or handoffs. |
| [Synthea](https://github.com/synthetichealth/synthea) and [Da Vinci payer reference implementation](https://github.com/HL7-DaVinci/br-payer) | Reusable synthetic records and reference implementation material. | Representative client data or production interoperability. |
| [AWS healthcare-agent sample](https://github.com/aws-samples/sample-healthcare-agents) and [Microsoft accelerator](https://github.com/microsoft/Prior-Authorization-Multi-Agent-Solution-Accelerator) | Existing agentic prior-authorization patterns and comparison baselines. | The Caduceus authority thesis or proof of product differentiation. |
| [OPA](https://github.com/open-policy-agent/opa) and [LangGraph](https://github.com/langchain-ai/langgraph) | Reusable policy and orchestration options that should be evaluated before bespoke breadth. | Healthcare institutional authority or provenance controls by themselves. |
| [HealthAdminBench](https://github.com/som-shahlab/health-admin-bench) and [A2A](https://github.com/a2aproject/A2A) | Potential external task comparison and future protocol interoperability. | Permission to change benchmark semantics or evidence that multi-agent scope belongs in the core. |

## Synthesis

The problem is credible and current, and reusable standards, fixtures, and
reference implementations already cover substantial plumbing. Therefore the
project should not present a generic prior-authorization agent, custom FHIR
format, or agent protocol as novel. Its interview-relevant differentiator is
the control plane: evidence-bound proposals, deterministic institutional
authorization, attributable review, and a correct action that still cannot
execute.

Selecting the provider side and an exception specialist is a deliberate,
portfolio-bounding hypothesis. It is not a conclusion from customer discovery.
The design is good enough to begin a synthetic engineering demonstration, while
the commercial and workflow claims remain open.

## Assumptions after D0

| ID | D0 disposition | Confidence and next evidence |
|---|---|---|
| AS-01 | Retained: provider prior-authorization/revenue-cycle leadership is the buyer hypothesis. | Unvalidated. Test through B07 interviews before a buyer or demand claim. |
| AS-02 | Retained: an exception specialist is the daily-operator hypothesis. | Unvalidated. Observe interviews/workflow in B07; adapt the workflow if evidence differs. |
| AS-03 | Retained: less effort/time to review-ready is valuable if risk and review burden do not increase. | Directionally plausible, not quantified. Establish synthetic baseline in G10 and client value only in EV-04/B06. |
| AS-04 | D0 supplied a testable review-ready definition. | Design-complete but user-unvalidated. Seek operator/reviewer agreement in B07. |
| AS-05 | Retained: a narrow recognizable FHIR R4/Da Vinci boundary can support the thin slice. | Design hypothesis. Verify through G03/G04 contracts and G12 external alignment. |
| AS-06 | Unchanged: external-task semantic comparability is unknown. | Resolve with the G12 crosswalk before reporting EV-03. |
| AS-07 | Unchanged: deployment footprint, adoption, and handoff fit are unknown. | G19 proves reproducibility; B07 and a future client environment test fit. |
| AS-08 | Unchanged: client interest sufficient for a shadow pilot is unknown. | G20 feedback and B06/client authorization decide. |

## Routed discovery finding

B07 owns direct domain-expert and prospective-user validation. Its questions
include buyer/budget ownership, the operator's real start/end events and
systems, the review-ready definition, exception distribution, handoffs,
adoption barriers, baseline effort/cost, and pilot governance. Until that work
or EV-04 occurs, all corresponding client and market claims remain explicitly
unvalidated.
