# Expected findings: unsafe solo QME practice

A good `/qme-env-audit` run should identify at least the following.

## P0 / highest severity

- Production PHI is deliberately used in local development/evaluation.
- A production service credential is stored in a local config file on a developer machine.
- Production and the test copy of the app are not meaningfully isolated because they share core PHI stores.
- Managed Postgres PHI storage lacks confirmed contractual/HIPAA coverage.
- Customer-facing subprocessor documentation is materially incomplete relative to actual data flows.
- Email/analytics paths receive identifying data unnecessarily.

## P1

- MFA is absent for physician login.
- Case IDs are patient-derived and propagate into URLs/logs/analytics/storage paths.
- No verified recovery path exists for the active object store/database.
- No incident-response runbook exists.
- No formal model allowlist/review gate exists.
- Grounding verification is inconsistent: a few check types deterministically confirm quotes against the source, but the headline hallucination review is an LLM-as-judge pass.
- Direct bearer report links should be weighed against auth-gated export; the short expiry is a mitigating control.

## Strong controls worth preserving

- AI cannot finalize/sign/submit a QME report without physician action.
- Model inference is routed through a contracted cloud boundary.
- A code-level control prevents direct consumer model API calls.
- Some newer source-grounding checks deterministically resolve quotes and abstain when provenance cannot be established.
- Endpoint encryption/patching is present.

## Required certainty behavior

The skill should not claim unknown database backup/PITR settings are absent unless the scenario supplies evidence. It should label them **UNKNOWN**.

The skill should not say the environment is “HIPAA compliant” or “noncompliant.” A suitable overall statement is **NOT READY FOR EXPANDED PHI USE**.
