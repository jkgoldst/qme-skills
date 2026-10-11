# Expected findings: unsafe solo QME practice

The scenario is a fictional operator narrative, not inspected implementation evidence. Its factual claims are REPORTED; unspecified settings remain UNKNOWN. Score the claim, supporting facts, urgency, and closure action separately.

## P0 containment

- Test deployment shares production PHI stores. Recommend isolating testing and pausing testing against those stores.
- Email/analytics receive patient-identifying content. Recommend minimizing identifying fields and reviewing recipient/access and contractual boundaries. Do not assert an unauthorized disclosure or confirmed breach without evidence.
- Assess the production service credential's scope and local protection promptly. It is a risk requiring containment review, not proof the credential was leaked.

## P1 gaps and material unknowns

- Hosting/database contractual coverage is UNKNOWN, not definitively absent. Request agreements and applicability review. Pause affected use if an essential requirement is established but coverage cannot be confirmed.
- Customer subprocessor documentation is incomplete according to the narrative.
- Physician MFA is absent according to the narrative.
- Patient-derived identifiers propagate through URLs/logs/analytics/storage. Assess the paths and remove unnecessary identifying metadata.
- No verified recovery path exists: object versioning is reported disabled, database backup/PITR is UNKNOWN, and restore testing has not occurred. Unknown recovery configuration is a P1 evidence/recovery task, not proof no backup exists.
- Incident-response procedures and model review controls are missing according to the narrative.
- An LLM-as-judge review is probabilistic; quote checks establish source text presence for their covered checks, not clinical truth.
- Weigh bearer report links against recipient/access requirements. Their expiry is a mitigating control.
- Physician export is reported required, but protection of diagnoses, retractions, invented observations, and undocumented denials remains UNKNOWN.

## Preserve and qualify controls

- Reported physician finalization boundary, contracted model route, build check against direct provider calls, partial quote verification, and endpoint encryption/patching.
- Do not upgrade these to VERIFIED without inspectable artifacts.

## Required restraint

- Physician review of downloaded transcripts on an encrypted, patched laptop is not stated to be software development or evaluation-fixture use. Do not invent that finding. Ask about authorization, purpose, local retention, and sharing only as needed. Do not label the review authorized when authorization remains unknown.
- A single-user practice does not establish broken tenant isolation.
- No legal certification, noncompliance determination, or blanket readiness verdict.
- Overall: MATERIAL GAPS IDENTIFIED, with material unknowns and a scoped action plan.
