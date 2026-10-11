# QME AI Setup Review

Assemble a concise report around a single evidence register. Extract the supplied factual clauses there, retaining their conditions, control scope, and evidence level. Use the register's IDs elsewhere instead of creating fresh factual paraphrases; when repeating a factual clause is necessary, copy that clause with its condition and level intact. Scope lists the reviewed domains and intended activity, not a reconstructed end-to-end sequence. Matrix facts are evidence IDs; write the risk interpretation and recommended action separately. Strong controls reference the same IDs and explain their value and limits. Draft requests retain placeholders for unresolved account, purpose, and ownership. Finalize the scoped statement after the matrix using SKILL.md, and check it against every gap, unknown, and priority rationale.

## Scope and assessment

- Reviewed workflow/intended activity:
- Operating situation and established control owners (evidence IDs or UNKNOWN):
- Account/environment and deployed revision, if established:
- Review date and audit conversation/report storage:
- Evidence inspected:
- Exclusions and areas not reviewed:

Use the scoped statement defined in SKILL.md. Explain established gaps and material unknowns separately. This review does not authorize patient-data use.

## Executive findings

State the most urgent action and cite its evidence IDs. Summarize the established gaps and material unknowns by their finding IDs. Keep factual wording in the register; state risk interpretations conditionally where they depend on unknowns.

## Current-state data flow and trust boundaries

Use data-flow.md. Only include actual or reported paths, labeled accordingly.

## Evidence register

| ID | Exact factual claim | Level | Locator or attributed report | Account/environment/revision | Observed date | Limits |
|---|---|---|---|---|---|---|

## Control/findings matrix

| ID / domain | Evidence IDs for the factual basis | Risk interpretation | Control status: gap / unknown / no gap identified | Priority and reason | Owner / next action | Evidence needed to close |
|---|---|---|---|---|---|---|

## Strong controls worth preserving

Reference evidence IDs, then describe each control's value and limits. Carry the register's evidence level into this section; a reported agreement remains REPORTED, with terms and coverage uninspected.

## Subprocessors

List evidence-established external providers here. If component-to-provider mappings are unresolved, state that in prose and keep those components in the component inventory. An approved subprocessor list matching a route establishes alignment, not that every route component is itself an external provider.

| Vendor | Purpose | Data categories | PHI possible? | Contract evidence/status | Region evidence/status | Established account/control owner (evidence or UNKNOWN) |
|---|---|---|---|---|---|---|

## Action plan

Group applicable actions by P0 / P1 / P2 using SKILL.md. Include recommended action owner, affected activity, and observable closure evidence. Label proposed assignments as recommended throughout the matrix, action plan, and evidence requests; current control ownership needs separate evidence. If a group has no actions, say so. Drafting a plan does not execute it.

## Unknowns and reassessment

List material blockers and who can supply evidence. Describe what additional review is needed. Avoid treating unreviewed areas as passes.

## Vendor evidence request

For managed services or inaccessible controls, draft a short request with the exact scoped artifacts needed. Describe established current use using its evidence ID. Where the data purpose or intended use is unstated, frame the request as an evaluation for possible use and ask the owner to supply the missing scope; retain placeholders for unknown product, account, and purpose. Never send it automatically.

## Questions for counsel

Include only unresolved questions requiring legal interpretation. Do not determine entity status or invent contractual duties.

## Scope limitation

This is a technical and operational evidence review based on the controls reviewed and evidence available. It is not legal advice, a compliance certification, a formal security assessment, or permission to use patient data.
