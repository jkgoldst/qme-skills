---
name: qme-env-audit
description: Review an AI setup for California QME case data. Map data flows, assess evidence, and prioritize gaps when a physician, practice, or software operator requests an environment review.
---

# QME AI Setup Review

Review the stated workflow for material privacy, security, data-governance, and QME integrity gaps. Produce a scoped evidence review and actionable next steps. This is not legal advice, a compliance certification, or permission to use patient data.

## Start safely

Explain before the first question:

> No patient records are needed. Describe the workflow using fictional examples. Do not paste passwords, API keys, patient identifiers, or unredacted configuration files. This review identifies gaps and unresolved questions; it does not certify an account for patient data. Making changes is a separate task.

Ask one question at a time, with a concise fictional example or suggested answer. Accept “I don't know” without making the user investigate controls they cannot access.

Use facts already supplied. If the user has stated their operating situation or workflow, acknowledge it and ask the next material unknown instead of repeating the role question. Otherwise, first identify the operating situation:

> Are you using an AI service directly, buying a managed QME application, or operating software yourself? Example: “I use an AI chat account directly, and my assistant uploads files.”

Then establish the tools, workflow being reviewed, intended use of real case data, and where this audit conversation and report are stored. Account tier alone does not establish contractual coverage, retention, training terms, or permitted data use. When the audit host's handling is unknown, continue with fictional descriptions and redacted evidence only. Inspect supplied artifacts only to the extent needed; do not reproduce sensitive contents in the report. If sensitive material appears, stop requesting it, avoid echoing it, and explain how to provide a redacted equivalent.

## Route by responsibility

Use the user's operating situation, not their technical vocabulary, to select the path. `--technical` requests deeper evidence inspection; it does not grant access or authorize changes.

### Physician using an AI service

Review the exact service/account, who can access it, how files enter and leave, connected tools, training/retention terms, deletion, local downloads, and review before using output. Establish whether originals and physician edits can be recovered and whether generated facts are source-linked. Treat a shared login as a reported individual-attribution and revocation gap, even when record sensitivity or vendor terms are unknown. Keep inaccessible infrastructure controls as vendor questions. Do not interrogate the physician about database policies or deployment configuration.

### Practice buying a managed application

Map practice-side uploads, access, exports, devices, and physician review. Ask for redacted agreement sections, relevant account settings, or a vendor's scoped evidence summary. Produce a short vendor evidence request for unresolved processing, access isolation, retention/deletion, recovery, subprocessors, model routing, and QME integrity safeguards. Draft requests for the user; do not send them to a vendor.

### Software operator

Read [technical review domains](references/qme-review-domains.md) and review the applicable architecture. Use available read-only evidence rather than asking the user to restate it. Establish the deployed revision/environment before treating repository code as runtime evidence. Do not print secrets or broad environment dumps, expand permissions, change settings, or test a production case. If access is unavailable, list the specific redacted evidence needed from the operator.

Mixed workflows may need more than one path. Name the boundaries and who owns each control.

## Evidence and interpretation

Read [evidence levels](references/evidence-levels.md) before assigning findings. Label each material factual claim VERIFIED, REPORTED, or UNKNOWN. Every VERIFIED claim needs an evidence locator, environment/account scope, observation date, and limits. A repository file proves what that file contains, not what production runs. A signed agreement proves the quoted commitment, not implementation. A quote match proves text presence, not clinical truth or the validity of an opinion.

Across the scope, summary, diagrams, tables, and action rationales, tie current-state claims to supplied facts or directly inspected evidence. Keep physician review and its purpose UNKNOWN unless stated or evidenced; the user’s profession and request for this setup review establish neither. A local download does not establish authorization or development use. Keep unstated senders, recipients, review, export, access, and onward-sharing steps UNKNOWN in the scope and summary as well as the detailed inventory. Keep recommendations separate from current-state facts.

Separate observed fact, risk interpretation, and action. Never infer a pass from silence, a missing search result, or marketing language. Preserve conflicting evidence instead of averaging it into confidence. Unknown is not a failed control or a pass.

Distinguish legal/contract status, technical control, and operational practice. Record legal-role and contractual-interpretation questions for counsel. A signed BAA for one provider does not establish that an agreement is legally required for another provider; applicability remains a counsel question until established. A BAA is not proof of technical security, and encryption is not proof of legal compliance. An LLM self-check remains probabilistic.

## QME integrity boundary

For workflows that generate or review clinical content, establish whether the system preserves physician-stated diagnoses, scores, conclusions, and retractions; separates evidence from AI proposals and physician-approved content; and requests physician input where provenance is absent. Ask about invented observations, undocumented denials, and claims that the physician performed an action. Explicit export alone does not establish these safeguards. Assess architecture or fictional examples, not a real case's medical merits. The physician owns the final opinion.

## Prioritize actions

Priority describes urgency of an action. Evidence level describes what is known. Explain both.

- **P0, contain now:** confirmed or credibly reported active exposure, unauthorized access, broken isolation, or a critical integrity/availability failure requiring immediate containment. Name the affected workflow and supporting facts. Use P1 to establish unknown credential access, device controls, authorization, or destination coverage; elevate to P0 only when supporting facts meet the containment criteria. A reported data path alone does not establish unauthorized disclosure or an uncontrolled boundary. Testing changes against production case stores is credibly reported broken isolation: recommend stopping that test activity at P0, without requiring evidence that harm already occurred. Where applicability of an essential contractual requirement is established but coverage is unconfirmed, recommend pausing the affected use pending confirmation, without declaring a breach or noncompliance.
- **P1, resolve before the affected use expands:** material unknowns about processing terms, authorization, recovery, retention, or physician safeguards; control gaps without demonstrated immediate exposure; materially inaccurate customer claims. Assign an owner and the evidence or change needed.
- **P2, harden:** lower-impact improvements once material gaps and unknowns are addressed.

No verified recovery path usually means a P1 evidence/recovery task. A confirmed inability to recover critical data with immediate operational impact may warrant P0; both conditions are required for that escalation. Patient-derived identifiers or production credentials require assessment of access, scope, purpose, propagation, and controls, not automatic claims of disclosure. A local config file alone does not establish credential lifetime, plaintext storage, device protection, or what data the credential can reach. For physician downloads, record the stated clinical-review purpose separately from authorization, retention, and sharing; keep those UNKNOWN when unstated, and reserve development/testing findings for evidenced development use.

## Finish the review

Track coverage silently. Treat an answered unknown as a recorded evidence task, not another interview question. End the interview once the applicable data paths and responsible parties are mapped, material gaps/unknowns have actions, and remaining questions would require unavailable evidence. Finish with the report and evidence requests for its owners; resume questions only when the user supplies new evidence or expands scope. If the user requests an early stop, produce a partial report with explicit unreviewed areas.

Read and use [findings report](templates/findings-report.md) and [data-flow guidance](templates/data-flow.md). Include the reviewed scope, evidence register, data flow/trust boundaries, subprocessors, control matrix, strong controls, priorities/owners, unknowns, and counsel/vendor questions as applicable.

Choose a scoped statement:

- **MATERIAL GAPS IDENTIFIED:** name the gaps, affected activity, and containment/remediation steps.
- **INSUFFICIENT EVIDENCE TO ASSESS:** use when material facts remain unknown and no established gap resolves the overall assessment. Name blockers, owners, and required evidence.
- **NO MATERIAL GAPS IDENTIFIED IN THE CONTROLS REVIEWED:** use only when applicable material controls have direct evidence and no unresolved material gaps or unknowns remain in the stated scope. List scope exclusions and evidence dates. This is not a guarantee or authorization.

If an established material gap and unknowns coexist, use MATERIAL GAPS IDENTIFIED and report both. A credibly reported gap can establish that assessment without becoming VERIFIED. Never use an unqualified “ready,” “secure,” “HIPAA compliant,” or “QME compliant” verdict. Reassessment must identify new evidence and which specific findings it resolves; a claimed fix alone stays REPORTED.
