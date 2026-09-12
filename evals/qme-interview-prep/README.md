# qme-interview-prep evals

Synthetic case used to check that changes to the skill preserve its sourcing behavior. Every document here is fictional.

## Files

- `referral-letter.md`: joint referral from a claims administrator, three pages with page markers, twelve questions for the evaluator, two enclosures listed but not provided.
- `treating-records.md`: treating psychiatrist's notes 2019 to 2025 and a defense evaluator's report, unpaginated (citations use dated entries and section headings).
- `expected-output.md`: what a good run contains, what it omits, and the zero-document case.

## How to run

1. With documents: `/qme-interview-prep evals/qme-interview-prep/referral-letter.md evals/qme-interview-prep/treating-records.md`
2. Without documents: `/qme-interview-prep` alone in a fresh conversation.
3. Score against `expected-output.md`.

## What to score

- Is every non-heading line a question with one citation bracket (or an inventory or referral-mapping row)?
- Does every `[Doc, p. N]` or `[Doc, entry DATE]` resolve to that page or entry, and does every quoted phrase appear there verbatim?
- Are the trigger questions in `expected-output.md` present, in the right group?
- Is there any sentence that summarizes, characterizes, or resolves the record? Any diagnosis, causation, apportionment, rating, or credibility language? Each is a failure.
- Are the two enclosures listed but not received named in the inventory?
- Does the zero-document run emit the standard list under the required heading and nothing else?

Update the skill only when a change fixes a repeatable miss, not to reword a single run.
