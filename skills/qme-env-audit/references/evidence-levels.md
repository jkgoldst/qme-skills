# Evidence levels

Use these labels consistently in `/qme-env-audit`.

## VERIFIED

A claim supported by direct evidence such as:

- code inspection
- cloud/IAM configuration
- CLI output
- database schema or policy
- signed contract or BAA
- deployment configuration
- runtime environment setting
- directly observed UI/account setting

Example:

> **VERIFIED:** S3 bucket versioning is disabled; `get-bucket-versioning` returned no configuration.

## REPORTED

A claim stated by the user or operator but not independently checked.

Example:

> **REPORTED:** Only the practice owner has administrative access.

Do not silently promote REPORTED to VERIFIED.

## UNKNOWN

A material fact the audit could not establish.

Example:

> **UNKNOWN:** Database point-in-time recovery configuration could not be inspected with the available credential.

UNKNOWN is not a pass.

## Conflicting evidence

When implementation and documentation disagree, show both and prefer implementation for the current-state technical finding.

Example:

> **VERIFIED:** Physician MFA is not implemented in the application.
>
> **CONFLICT:** Security documentation states MFA is a current control.

This should normally create a remediation item to correct either the implementation or the documentation.
