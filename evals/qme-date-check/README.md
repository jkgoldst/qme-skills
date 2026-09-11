# qme-date-check evals

Synthetic seeded-defect draft used to check that changes to the skill preserve every check. All names, dates, and providers are fictional.

## Files

- `seeded-draft.txt`: a short draft with one seeded defect per check, plus controls that must stay silent (a child's age, a relative reference to the date of injury, a month-and-year-only mention).
- `expected-findings.md`: the findings a good run produces, the controls, and the anchors.

## How to run

1. `python3 skills/qme-date-check/scripts/date_check.py evals/qme-date-check/seeded-draft.txt --today 2025-03-20`
2. Or, in an agent without code execution: `/qme-date-check evals/qme-date-check/seeded-draft.txt` and ask for today = 2025-03-20.
3. Score against `expected-findings.md`.

## What to score

- Is every seeded defect found, under the right check id, with both locations quoted?
- Do the controls stay silent?
- Does the output name the anchors it used and say which checks stayed silent?
- Is there any sentence saying which value is correct? That is a failure; the check shows disagreement, the physician resolves it.
