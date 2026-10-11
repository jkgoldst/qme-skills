# Evidence levels and claim records

Use one label per factual claim, keeping risk interpretation separate.

## VERIFIED

Directly inspected evidence supports the exact claim within its stated scope. Record:

| Field | Required content |
|---|---|
| Claim | The narrow fact established |
| Locator | File and line, setting path, redacted CLI result reference, or agreement section |
| Scope | Account/environment, deployed revision where relevant, and data path |
| Observed | Actual inspection date; source/version date where available |
| Limits | What this evidence does not establish |

Use stable evidence IDs in the findings matrix. When a required field is unavailable, narrow the claim to what can actually be established or retain REPORTED/UNKNOWN. Never invent dates, locators, or deployment matches. Record collection dates separately from dates claimed in documents.

Examples:

- A source file routes a model call through provider X. It does not establish the deployed route without deployment evidence.
- A signed agreement contains a retention commitment. It does not prove deletion jobs enforce it.
- A directly observed account setting disables training. It does not prove all connected tools share that policy.
- An inspected notification fixture contains patient-identifying fields. It does not prove real notifications were sent or that recipients were unauthorized.

For a synthetic evaluation, inspect supplied artifact excerpts as synthetic evidence. A quoted fixture can verify its displayed text, and an explicitly supplied manifest or test-result excerpt can verify what that excerpt states, with the supplied locator, scope, date, and limits. File access is not required to inspect an excerpt. A description that merely says an artifact exists remains REPORTED. Neither form establishes live access or real-world behavior beyond its contents.

## REPORTED

The user or operator stated the fact, but no supporting artifact was inspected. Attribute the statement and record the interview date. A quoted claim about a setting is not observation of that setting.

## UNKNOWN

A material fact is not established. Record why and the specific evidence needed. Unknown is neither a pass nor proof of absence. A failed check must remain visible.

## Conflicts and conclusions

Show both the implementation and documentation evidence. Prefer deployed observations for current runtime facts while retaining the contractual claim separately. If the deployed revision cannot be established, report the disagreement and runtime unknown.

A risk interpretation must cite its supporting claims and any unresolved assumptions. Example: “Notification text contains identifying fields [E1]; recipient access and contractual coverage are UNKNOWN [U1]. This is an egress path to review, not evidence by itself of an unauthorized disclosure.”
