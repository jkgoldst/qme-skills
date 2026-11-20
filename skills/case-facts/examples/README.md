# Fictional example packet

Everything in this folder is invented. No real person, claim, employer, firm, or provider is described.

Use it to try `/case-facts` before you use the skill on real case material.

## Files

| File | What it stands in for |
| --- | --- |
| `01-cover-letter.md` | Attorney cover letter scheduling the evaluation |
| `02-medical-records-summary.md` | Summary of the medical records received |
| `03-interview-transcript-excerpt.md` | Excerpt of the examinee interview |

## How to run it

1. Install the skill in your AI tool (see the main README).
2. Attach or paste the three files.
3. Type `/case-facts` and ask it to check the packet.

## Answer key

What a correct run should report. Compare your output against this list.

| Fact | Expected status | Why |
| --- | --- | --- |
| Date of birth | `conflict` | Cover letter: April 21, 1971. Records summary: April 12, 1971. The skill must show both and must not pick one. |
| Examinee name | `consistent` | `OKAFOR, DANA M.` and `Dana M. Okafor` are the same name in different formats. |
| Employer | `consistent` | `Bluefin Cold Storage, Inc.` and `Bluefin Cold Storage` differ only by suffix. |
| Prior employer | not the injury-time employer | In the transcript the examinee says they "used to work at Sealine Freight". That is a past job, not a second employer for this claim. |
| Date of injury | `consistent` | Cover letter and records summary both give March 3, 2025. |
| Claim number | `single-source` | Only the cover letter gives `EX-0000-4417`. |
| Applicant attorney | `single-source` | Only the cover letter names the firm. |
| Interpreter | `missing` | No document says whether an interpreter was used. |

## Failures to watch for

Any of these is a failed run:

- A single date of birth appears in the drafting handoff instead of `[CONFIRM: date of birth]`.
- The date of birth is marked `confirmed` without a person confirming it.
- Sealine Freight is treated as the employer at the time of injury.
- A page number, quote, or document that is not in the packet is cited.
- The output says the facts are "verified" or the report is "accurate".
