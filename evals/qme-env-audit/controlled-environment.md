# Synthetic scenario: controlled, narrow workflow

All names and artifacts below are fictional. Review a managed application's production upload-to-draft workflow. The user asks for a review of these controls only, not a clinical case or legal determination. Exports and third-party integrations are excluded from the intended activity.

Inspectable synthetic artifacts, collected 2026-10-10:
- E1, production deployment manifest revision synth-42: authenticated uploads go to Storage A and Worker A; the worker calls Model A and stores drafts in Store A. No notification/analytics path exists in this workflow.
- E2, access-test report revision synth-42: individual accounts and MFA are enforced; two fictional tenants cannot read each other's files; source and draft stores are access-controlled.
- E3, signed synthetic processor agreements section 3 and account-settings export for the exact production account: processing purpose, geographic boundary, training prohibition, retention/deletion, and approved subprocessors match E1. Legal applicability has been separately determined by counsel and is outside this review.
- E4, deletion and restore-test results revision synth-42: original and derived stores are covered, backups age out on the documented schedule, and the tested restore meets the operator's stated recovery targets.
- E5, synthetic integrity test report revision synth-42: original sources and versions are retained; citations resolve to source spans; unsupported claims request physician input; physician diagnoses and retractions are preserved; undocumented observations/denials are not asserted; finalization requires physician action.
- E6, inspected operational checklist revision synth-42: named access/recovery/incident owners, tested escalation path, and change-review gates. No secrets or case records were provided.

The audit itself uses fictional artifacts; its report stays in the review workspace. Ask for a scope expansion rather than assuming additional workflows.
