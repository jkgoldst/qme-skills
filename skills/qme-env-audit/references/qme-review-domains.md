# Technical review domains

Read for the software-operator path or a technical evidence request. Use applicable domains, not a mandatory 23-question interview. Keep questions plain-language and skip controls outside the reviewed workflow, recording why.

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

Distinguish development/testing from physician review of a draft. A local download alone does not establish development use. Assess purpose, authorization, device controls, and onward sharing separately.

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

A final QME opinion/report must require explicit physician action. Also establish whether safeguards:
- preserve physician-stated diagnoses, scores, and conclusions without silent substitution
- honor explicit retractions
- separate source facts, AI proposals, and physician-approved content
- abstain or request physician input when a finding has no source
- prevent invented examination observations, review actions, and patient denials without documented elicitation

Assess these safeguards using fictional examples or system evidence. Do not request a real clinical case or independently adjudicate a physician's opinion.

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
