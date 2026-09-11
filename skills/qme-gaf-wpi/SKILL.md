---
name: qme-gaf-wpi
description: Check every GAF and Whole Person Impairment pair in a California psychiatric QME draft against the 2005 PDRS conversion table before signing. Flags a GAF/WPI pair the table disagrees with, a GAF within two points of the 69 to 70 rating cliff, and a GAF or WPI stated without its partner. Lookup only; the score stays the physician's.
argument-hint: "[draft file: .docx, .txt, or .md]"
compatibility: Claude (web/desktop upload; Pro, Max, Team, Enterprise with code execution), Claude Code, Codex. Other skill-aware agents untested.
---

# QME GAF to WPI check

Before the physician signs, confirm that every Global Assessment of Functioning score in the draft converts to the Whole Person Impairment the draft states, per the 2005 Schedule for Rating Permanent Disabilities. The table is a point lookup with no interpolation; a mismatch is a transcription or arithmetic error, never a judgment call. This check reports the table's value and the sentence it disagrees with. Which score is right is the physician's decision.

## Input

One draft report: `.docx`, `.txt`, or `.md`. Nothing else is read. A draft with no GAF and no WPI anywhere yields the one-line result `No GAF or WPI stated; nothing to check.`

## Run the script first

`scripts/gaf_wpi_check.py` is stdlib-only Python 3 and does the whole job deterministically:

```bash
python3 scripts/gaf_wpi_check.py path/to/draft.docx
```

It prints every finding in the format below. When Python is unavailable, do the same work by hand from `references/pdrs-2005-gaf-wpi.md`, applying the rules in the next section exactly; state at the top of the memo that the lookup was manual.

## Rules the script applies

Section scope. Only sections the physician rates count: any heading containing IMPAIRMENT, DIAGNOSIS, DISCUSSION, DISABILITY, CONCLUSION, or SUMMARY, and any draft with no headings at all. A GAF inside a records-review or prior-report section is another evaluator's score; the memo lists it under "Not checked" with its sentence and moves on.

A stated GAF is a sentence containing exactly one match of `GAF score of N`, `GAF of N`, `GAF score N`, `GAF rating of N`, or `Global Assessment of Functioning (GAF) score of N`, with N from 1 to 100. `GAF range of 55-65` is a range, never a score. A sentence with two GAF scores is ambiguous and is listed under "Not checked" rather than paired.

A stated WPI is `Whole Person Impairment` or `WPI` followed within 60 characters by a percentage, single (`18%`) or range (`12-13%`).

Pairing. A GAF and a WPI in the same sentence are a pair. Otherwise the nearest unpaired GAF and WPI in the same section, within three sentences of each other, are a pair. A lone GAF or WPI that restates a value already paired somewhere in the draft is a restatement, listed with the consistent pairs; a lone value paired nowhere is an orphan.

Sentences end at `.`, `!`, or `?` followed by space, except after Mr., Ms., Mrs., Dr., and M.D.

Three checks, in this order:

1. **Mismatch.** The pair's WPI (or range) fails to include the table's value for that GAF. Finding: `MISMATCH`, quote the sentence, state the table's value with citation.
2. **Boundary.** The GAF is 68, 69, 70, 71, or 72. The table's only discontinuity is 69 to 70 (2% to 0%); one point of dictation slip changes the rating. Finding: `BOUNDARY`, quote the sentence, state this score's WPI and both neighbors' so the physician confirms the score deliberately. Fires whether or not the pair matches.
3. **Orphan.** A GAF with no WPI within reach, or a WPI with no GAF, and no pair elsewhere stating the same value. Finding: `ORPHAN`, quote the sentence, state what is missing and, for a lone GAF, the table's value.

Every finding cites `2005 Schedule for Rating Permanent Disabilities, Section 1, GAF-to-WPI conversion table, p. 1-16`.

## Output

Fill `templates/findings.md`: the findings in draft order, then "Not checked" (out-of-scope and ambiguous mentions, each quoted), then a one-line count. With a filesystem, also write it beside the draft as `gaf-wpi-check-YYYY-MM-DD.md`.

A clean draft reports `0 findings` and still lists every pair checked with its table value, so the physician sees what was verified.

## Boundaries

The memo states table values and quotes the draft. It never proposes a GAF, picks between two stated scores, applies a future earning capacity adjustment or any other step after WPI, or comments on whether the impairment is reasonable. A `[PHYSICIAN: ...]` placeholder in the draft is a prompt, not a statement; its contents are skipped.

Run this in the account that `/qme-env-audit` has cleared for case data.
