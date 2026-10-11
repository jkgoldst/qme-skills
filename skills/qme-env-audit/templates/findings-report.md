# QME AI Setup Review

Keep the report proportionate to the scope. Write the evidence register before synthesizing the summary, and state each fact there once. Elsewhere, refer to its ID rather than retelling the workflow. Use the same evidence-backed claims in the register and every other section, including the opening. Before finishing, check relationship comparisons, completed actions, and ownership against their cited evidence; narrow any paraphrase that adds a fact. An evidence label applies to the supported claim only: attribution as REPORTED still requires a supplied statement. For example, an operator requesting the review establishes their role, while ownership of a renderer or account stays UNKNOWN without an ownership statement. The scope names the reviewed controls and intended activity; distinguish reported completed actions from requirements such as an export gate. It does not complete an assumed sequence or recipient. Finalize the scoped statement after the matrix, using SKILL.md; check that it agrees with every gap/unknown status and priority rationale.

## Scope and assessment

- Reviewed workflow/intended activity:
- Operating situation and established control owners (evidence IDs or UNKNOWN):
- Account/environment and deployed revision, if established:
- Review date and audit conversation/report storage:
- Evidence inspected:
- Exclusions and areas not reviewed:

Use the scoped statement defined in SKILL.md. Explain established gaps and material unknowns separately. This review does not authorize patient-data use.

## Executive findings

State the most urgent action and its basis. Separate observed facts, risk interpretations, and unresolved assumptions.

## Current-state data flow and trust boundaries

Use data-flow.md. Only include actual or reported paths, labeled accordingly.

## Evidence register

| ID | Exact factual claim | Level | Locator or attributed report | Account/environment/revision | Observed date | Limits |
|---|---|---|---|---|---|---|

## Control/findings matrix

| ID / domain | Observed fact and evidence IDs | Risk interpretation | Control status: gap / unknown / no gap identified | Priority and reason | Owner / next action | Evidence needed to close |
|---|---|---|---|---|---|---|

## Strong controls worth preserving

Include evidence IDs and limits. A reported control remains REPORTED.

## Subprocessors

List evidence-established external providers here. If component-to-provider mappings are unresolved, state that in prose and keep those components in the component inventory. An approved subprocessor list matching a route establishes alignment, not that every route component is itself an external provider.

| Vendor | Purpose | Data categories | PHI possible? | Contract evidence/status | Region evidence/status | Established account/control owner (evidence or UNKNOWN) |
|---|---|---|---|---|---|---|

## Action plan

Group applicable actions by P0 / P1 / P2 using SKILL.md. Include recommended action owner, affected activity, and observable closure evidence. Label proposed assignments as recommended throughout the matrix, action plan, and evidence requests; current control ownership needs separate evidence. If a group has no actions, say so. Drafting a plan does not execute it.

## Unknowns and reassessment

List material blockers and who can supply evidence. Describe what additional review is needed. Avoid treating unreviewed areas as passes.

## Vendor evidence request

For managed services or inaccessible controls, draft a short request with the exact scoped artifacts needed. Never send it automatically.

## Questions for counsel

Include only unresolved questions requiring legal interpretation. Do not determine entity status or invent contractual duties.

## Scope limitation

This is a technical and operational evidence review based on the controls reviewed and evidence available. It is not legal advice, a compliance certification, a formal security assessment, or permission to use patient data.
