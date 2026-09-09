# Synthetic scenario: unsafe solo QME practice

This scenario is fictional and contains no real patient information.

A solo California QME had a small web app built by a contract developer. The physician uploads case records to it. The app runs on a general cloud platform. Original PDFs go to a separate object store. Extracted text, patient name, date of birth, claim number, findings, and draft report content are stored in a managed Postgres service from a different vendor.

The physician signed a BAA with the object-storage/model cloud provider but has never checked whether the web-hosting provider or the managed Postgres vendor has a BAA in place.

When a report is ready, the app sends a notification through a general-purpose transactional email service. The email body names the patient and the case, and includes a download link for the report. The link is a time-limited URL that anyone holding it can open; it expires after a few hours.

Each case is named after the patient (usually last name plus year of injury). That case name is used as the record identifier and appears in URLs, storage paths, application logs, and the page paths reported to a web analytics service.

The physician logs in with email/password only. MFA is not enabled. There is only one user today, so there is no practice/organization model.

A "test" copy of the app, used to try out changes before they go live, points at the same production database and object-storage bucket. The contract developer keeps a production service credential in a local config file on their own machine. Separately, the physician periodically downloads real transcripts to a personal laptop to check the AI's output by hand. The laptop has full-disk encryption and is patched.

The active object-storage bucket has no object versioning. The database backup/PITR configuration is unknown. No restore test or incident-response runbook exists.

AI inference goes through one approved cloud model provider in the same contracted cloud boundary. An automated check in the app's build fails if code calls the model vendor's public consumer API directly. However, there is no formal model allowlist, so a new model ID can be substituted without a compliance or regression review.

The app uses a second AI pass to review the first AI's draft for statements not supported by the source records. For a small number of check types, the app also confirms that a quoted passage actually appears in the source document before it shows the finding; most findings do not get this extra confirmation.

AI cannot sign, finalize, or submit the medical-legal report without the physician explicitly exporting it.

The practice's client-facing privacy statement says data is shared only with the main cloud provider and the model provider, even though the managed database vendor, the email service, and the analytics service also receive PHI or identifying metadata.
