# Backlog

## Identifier key

`B##` identifies an unordered backlog item. Dependency references use `D0` for
discovery, `G##` for core goals, and `MA-#` for future multi-agent goals;
`EV-##` identifies an evidence tier. The complete definitions are in the
[project charter](project-charter.md#identifier-key).

These items are intentionally outside the core roadmap. Promote one when its
dependencies and required access are available and the user explicitly changes
roadmap scope or order.

| ID | Priority | Item | Source and why it matters | Likely dependencies |
|---|---|---|---|---|
| B01 | Later | Policy-as-code comparison | Reimplement rules in OPA or Cedar to compare ergonomics with typed Python rules; useful evidence, not required for the core claim. | G07, G16, G20 |
| B02 | Later | Counterfactual evaluation | Explain the minimum evidence or policy change that would alter an authorization outcome. | G11, G17 |
| B03 | Later | Authority analytics | Measure investigation, execution, review, escalation, denial, and authority-violation rates without treating more autonomy as inherently better. | G11, G16, G17 |
| B04 | Later | Second regulated workflow | Test whether the architecture transfers to claim denial, benefits verification, or referral exceptions without redesign. | G20 |
| B05 | Later | Greater FHIR standards fidelity | Improve standards conformance only after resource boundaries and identifiers support the reference workflow. | G03, G10 |
| B06 | External | Governed client shadow pilot | The source positions a customer-controlled shadow deployment as the next evidence tier for validating workflow impact and adoption; it requires a real client, approved data environment, contractual/privacy/security controls, and must not inherit authority from the portfolio deployment. | D0, G20, client authorization and governance |
| B07 | Soon/external | Domain-expert and prospective-user validation | D0 used the permitted literature/repository substitute. Direct evidence is still required to validate the buyer, operator workflow, review-ready definition, adoption barriers, baseline economics, and willingness to pilot before making customer-fit or ROI claims. | D0, access to at least three relevant participants |
