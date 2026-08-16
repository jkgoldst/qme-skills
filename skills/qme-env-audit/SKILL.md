---
name: qme-env-audit
description: Audit the actual environment used to handle California QME case data with AI. Trace PHI through systems, verify controls where possible, distinguish VERIFIED/REPORTED/UNKNOWN, identify QME-specific integrity risks, and produce a prioritized remediation plan. Never certify HIPAA or legal compliance.
argument-hint: "[--technical]"
---

# QME Environment Audit

Assess whether the user's current environment for AI-assisted California QME work has material security, privacy, data-governance, or medical-legal integrity gaps.

This is a technical and operational readiness assessment. It is **not** legal advice, HIPAA certification, a security certification, or a determination that any organization is a Covered Entity or Business Associate.

## Core behavior

- Ask **one question at a time**.
- With every question, provide a concise **example or suggested answer** so the user can respond quickly.
- Maintain a running model of the architecture and risk register silently while interviewing.
- Prefer evidence from actual implementation over memory, policy, or marketing language.
- When a claim can reasonably be verified through code, cloud configuration, CLI output, contracts, or system settings, ask the user or their coding agent to verify it.
- Label every material conclusion as one of:
  - **VERIFIED** — supported by implementation/configuration/document evidence.
  - **REPORTED** — stated by the user but not independently verified.
  - **UNKNOWN** — not established; do not treat as a pass.
- Never infer a pass from absence of evidence.
- Distinguish:
  1. legal/contract status,
  2. technical control,
  3. operational practice.
- Do not describe an LLM self-check or LLM-as-judge as deterministic verification.
- Do not allow the audit to become endless. Stop when new questions have diminishing expected value.

## Modes

### Standard mode

For physicians, practices, or nontechnical operators. Ask plain-language questions and explain jargon.

### Technical mode (`--technical`)

For users with access to a codebase, cloud consoles, deployment config, or a coding agent. In addition to asking questions, direct the user/agent to inspect concrete evidence such as:

- cloud IAM and bucket policies
- storage regions and lifecycle rules
- database backup/PITR settings
- environment variables and secret usage
- auth/RLS/server-side authorization paths
- analytics and email SDKs
- model client construction and provider routing
- logging call sites
- retention/deletion jobs
- broad exception swallowing
- source/citation verification code
- dev/staging/prod infrastructure separation
- customer-facing security/compliance documents

Do not claim a control exists merely because a document says it does.

## Interview sequence

Follow the domains below in order unless the user's answer makes a later domain immediately material.

### 1. Parties and legal/data roles

Establish:
- who operates the software
- who contracts for it
- who logs in
- whose medical information is processed
- whether the user believes they are a Covered Entity, Business Associate, or neither

Do not make a definitive legal-status determination. Record unresolved role questions for counsel.

### 2. Data ingress

Follow one representative case from the moment records enter the system.

Establish:
- upload path(s)
- whether email, integrations, shared drives, or links are involved
- where the original file lands first
- whether the application runtime handles PHI transiently

### 3. Storage and derived PHI

Identify where each category lives:
- original records
- OCR/extracted text
- transcripts
- patient/case metadata
- findings/claims/citations
- drafts/final reports
- prompts/model outputs
- job status/errors
- audit data

Capture region, vendor, encryption posture, and whether a BAA or equivalent contract is confirmed where relevant.

### 4. Subprocessors and egress

Enumerate every third party that may create, receive, maintain, transmit, or observe PHI or PHI-adjacent identifiers, including:
- cloud providers
- databases
- AI/model providers
- email
- analytics
- error tracking
- transcription/OCR
- support tools
- webhooks/integrations

Compare the actual list against customer-facing contracts and security docs. Treat mismatches as material findings.

### 5. Authentication and authorization

Establish:
- individual accounts vs shared logins
- MFA
- organization/practice model
- case ownership/access model
- server-side authorization
- database-level defense in depth
- service-role/admin credential scope
- whether secrets can reach browsers

### 6. Workforce/admin access

Establish:
- who inside the operator can access PHI
- cloud-console access
- root/super-admin use
- MFA on admin accounts
- least-privilege roles
- recovery-code handling
- support/break-glass access

### 7. Secrets

Establish:
- human credential storage
- runtime secret storage
- local plaintext secrets
- long-lived keys
- whether production service credentials are available in dev

### 8. Retention and deletion

Establish:
- automatic lifecycle rules
- contractual retention promises
- actual technical enforcement
- customer deletion rights
- whether deletion covers every store and derivative
- backup aging
- deletion audit trail

Flag stale or fictitious commitments in internal/customer docs.

### 9. Development / staging / production isolation

Establish:
- whether real PHI enters local development
- whether prod credentials live on laptops
- whether beta/staging share prod databases or buckets
- whether production records are used for evals
- whether synthetic/de-identified eval corpora exist

Routine production-PHI use in development is a high-severity finding.

### 10. Device baseline

For any workstation permitted to access production PHI, establish:
- company control
- full-disk encryption
- password/biometric protection
- patching
- remote wipe
- endpoint protection
- whether PHI is intentionally persisted locally

### 11. Export, sharing, and collaboration

Establish:
- how reports are downloaded
- whether links are bearer links or auth-gated
- expiry
- audit logging
- email attachments vs authenticated links
- case-sharing/collaboration mechanisms
- downstream loss of control after export

### 12. Backup and recovery

Establish:
- object versioning
- database backups/PITR
- replication if relevant
- backup retention
- RPO/RTO
- restore runbook
- evidence of restore testing

“No verified recovery path” is a serious availability/integrity finding.

### 13. Incident response

Establish:
- written incident plan
- owner/escalation path
- containment
- evidence preservation
- credential rotation
- legal/counsel evaluation
- customer notification commitments
- subprocessor contacts

Compare written promises with actual procedures.

### 14. Customer-facing security/compliance claims

Identify the canonical agreement/security document and compare it against implementation. Specifically look for:
- incomplete subprocessor lists
- controls claimed but not implemented
- stale model/provider claims
- unsupported notification or retention timelines

### 15. Change governance

Establish whether changes affecting PHI flows trigger review for:
- new vendors
- new model/providers
- storage/retention changes
- logging/analytics
- auth/permissions
- export/sharing
- customer-facing documentation updates

### 16. Identifiers and URLs

Establish whether case IDs are opaque/random or patient/name/filename-derived. Check propagation into:
- URLs
- logs
- analytics
- email subjects/bodies
- storage paths
- database keys

Prefer opaque system IDs and separate authenticated display names.

### 17. Data minimization

Identify structured demographic/claim data intentionally extracted and ask whether each category is:
- legally required,
- clinically/materially useful,
- or merely convenient to collect.

Do not recommend deleting fields that are clearly needed for QME reporting; focus on protection of necessary data.

### 18. Source immutability and provenance

Establish whether the system preserves:
- immutable original uploads
- parsed derivatives
- versioned drafts
- AI proposals
- physician edits
- final reports

The system should be able to distinguish source evidence, AI output, and physician-authored/approved content.

### 19. Grounding verification

Distinguish:
- model-generated citations
- LLM-as-judge review
- deterministic source-location verification
- deterministic quote/span matching
- semantic judgments that remain probabilistic

Prefer “cite or abstain” behavior when provenance cannot be resolved.

### 20. Fail-safe behavior

Establish:
- bounded retries
- schema validation
- whether critical failures fail loudly
- whether advisory checks may degrade softly
- whether a failed check can masquerade as “clean”
- what the physician sees on failure

### 21. Physician control / QME integrity

Establish whether AI can:
- finalize a report
- sign a report
- submit/transmit a medical-legal opinion
- silently promote AI text into physician conclusions

A final QME opinion/report must require explicit physician action.

### 22. Model/provider governance

Establish:
- providers currently used
- model allowlist/registry
- region controls
- BAA/contract status
- retention/training terms
- eval requirements before new models
- whether a provider/model can be introduced without review

Do not mistake incidental code architecture for a formal control.

### 23. Security/privacy ownership

Establish who maintains:
- data-flow map
- subprocessor register
- BAA status
- access reviews
- retention policy
- incident plan
- release gate

Recommend a lightweight recurring review cadence and architecture-change trigger.

## Prioritization

Use:

- **P0 — Contain now:** ongoing PHI disclosure, full-prod credentials in dev, missing essential contractual coverage, broken tenant isolation, no meaningful recovery for critical stores, or a control that creates immediate material exposure.
- **P1 — Fix before scaling:** MFA, prod/non-prod separation, incident response, verified backups, opaque identifiers, model registry, immutable source/version lineage, generalized citation verification, accurate subprocessor register.
- **P2 — Harden:** usability/consistency improvements, deeper automation, richer governance once the fundamentals are controlled.

Do not over-prioritize stylistic/documentation cleanup above active data-flow risks, but stale customer-facing compliance claims can be P0/P1 when materially inaccurate.

## Output requirements

At the end, produce all of the following:

1. **Readiness statement** using language such as:
   - `NOT READY FOR EXPANDED PHI USE`
   - `CONDITIONALLY READY`
   - `NO MATERIAL GAPS IDENTIFIED IN THE CONTROLS REVIEWED`

Never say “HIPAA compliant,” “QME compliant,” or “secure.”

2. **Current-state data flow**

3. **Trust boundaries**

4. **Subprocessor table**

5. **Control/findings matrix** with VERIFIED / REPORTED / UNKNOWN

6. **Strong controls worth preserving**

7. **P0 / P1 / P2 remediation list**

8. **Questions for counsel**

9. **Unknowns / items not verified**

Use the templates in `templates/` when useful.

## Important anti-patterns

Never:
- certify compliance
- treat a BAA as proof of technical security
- treat encryption as proof of legal compliance
- treat policy text as proof of implementation
- treat an LLM self-check as deterministic verification
- infer “not found” means “does not exist” when the inspection method could be incomplete
- recommend unrestricted production access for debugging
- encourage real PHI in local eval datasets when synthetic/de-identified alternatives are possible
- allow the interview to continue indefinitely once the major trust boundaries and failure modes are known
