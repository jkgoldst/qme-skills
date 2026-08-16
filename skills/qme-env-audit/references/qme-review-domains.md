# QME environment review domains

This reference is a compact checklist for the domains `/qme-env-audit` should cover. It is not a legal checklist and should not be treated as exhaustive.

1. Parties and legal/data roles
2. Data ingress
3. Original and derived PHI storage
4. Subprocessors and egress
5. Authentication and authorization
6. Workforce/admin access
7. Secrets and credentials
8. Retention and deletion
9. Dev/staging/prod isolation
10. Endpoint/device baseline
11. Export, sharing, and collaboration
12. Backup and recovery
13. Incident response
14. Customer-facing security/compliance claims
15. Change governance
16. Identifiers, URLs, logs, analytics, and notifications
17. Data minimization
18. Source immutability and version lineage
19. Grounding and citation verification
20. Fail-safe behavior
21. Physician control over final medical-legal output
22. Model/provider governance
23. Security/privacy ownership

## QME-specific lens

Generic healthcare security is necessary but not sufficient. The review should also ask whether the environment preserves:

- physician responsibility for the medical-legal opinion
- clear separation between source evidence, AI-derived findings, and physician conclusions
- provenance back to the source record
- explicit physician action before finalization/export
- controlled information flow into the evaluator's working environment

When legal questions arise, record them for counsel rather than turning the skill into a legal-opinion engine.
