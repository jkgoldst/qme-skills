# Synthetic scenario: unsafe solo QME practice

This scenario is fictional and contains no real patient information.

A solo California QME uses a web app to upload case records. The app is hosted on a general cloud platform. Original PDFs go to a separate object store. Extracted text, patient name, date of birth, claim number, findings, and draft report content are stored in a managed Postgres service.

The physician has a BAA with the object-storage/model cloud provider but has never checked whether the web-hosting provider or managed Postgres provider has a BAA in place.

The app emails the patient surname and case identifier through a general email delivery service when the report is ready. The completion email includes a one-hour bearer download URL for the report.

Case identifiers are typed manually by the physician and are usually the patient's surname. Those IDs also appear in URLs, storage paths, application logs, and analytics page paths.

The physician logs in with email/password only. MFA is not enabled. There is only one user today, so there is no practice/organization model.

The same production database and object-storage bucket are used by production and beta. Local development has a production service credential in `.env.local`, and the physician/developer routinely downloads real transcripts to a laptop for evaluation work. The laptop has full-disk encryption and is patched.

The active object-storage bucket has no object versioning. The database backup/PITR configuration is unknown. No restore test or incident-response runbook exists.

AI inference goes through one approved cloud model provider in the same contracted cloud boundary. A code test prevents direct calls to the model vendor's consumer API. However, there is no formal model allowlist, so a new model ID can be substituted without a compliance or regression review.

The system uses an LLM-as-judge hallucination critic. Newer checks deterministically resolve exact quotes against source text before displaying some findings, but this verification is not universal.

AI cannot sign, finalize, or submit the medical-legal report without the physician explicitly exporting it.

The customer agreement says subprocessors are limited to the main cloud provider and model provider, even though the managed database, email service, and analytics SDK also receive PHI or identifying metadata.
