# Expected findings

Both fixtures are fictional. Score a run by whether it produces exactly these findings, quotes the sentence, and cites the 2005 PDRS table page 1-16.

## draft-mismatch.md

Findings (1):

- MISMATCH, IMPAIRMENT. Quote: "A GAF of 55 corresponds to a Whole Person Impairment (WPI) rating of 24%." Stated GAF 55, WPI 24%. Table: 23%.

Not checked (2):

- HISTORY OF INJURY AS DESCRIBED IN MEDICAL RECORDS: Dr. Raman's GAF 58 (another evaluator's score).
- HISTORY OF INJURY AS DESCRIBED IN MEDICAL RECORDS: Dr. Whitfield's GAF 58 / 18% (another evaluator's score; the pair happens to match, and it is still not checked).

Must not appear:

- An ORPHAN on the DISCUSSION GAF 55 or on the first IMPAIRMENT GAF 55 sentence: both restate the score paired in IMPAIRMENT and belong under "Pairs checked and consistent" as restatements.
- Any reading of "GAF range of 51-60" as a score.
- Any finding drawn from text inside a `[PHYSICIAN: ...]` placeholder.
- Any statement of which score the physician should use.

## draft-boundary-orphan.md

Findings (2):

- BOUNDARY, IMPAIRMENT. Quote: "Based on the clinical interview, Mr. Delacroix-Ibarra is assessed a GAF score of 69." GAF 69 converts to 2%; GAF 68 to 3% and GAF 70 to 0%. Confirm 69 is intended.
- ORPHAN, SUMMARY OF CONCLUSIONS. Quote: "3. Whole Person Impairment: 8%." WPI 8% with no GAF within reach.

Pairs consistent (2):

- IMPAIRMENT: GAF 69, WPI 2%; table 2%.
- IMPAIRMENT: GAF 69 restated in the first sentence, no WPI; table 2%.

Must not appear:

- A MISMATCH on the GAF 69 / 2% pair.
- Any pairing of the SUMMARY OF CONCLUSIONS 8% with the IMPAIRMENT GAF 69; they are in different sections.
- Any remark that 8% and 2% disagree with each other beyond the ORPHAN finding; reconciling them is the physician's job.

## Empty input

A draft with no GAF and no WPI returns the single line "No GAF or WPI stated; nothing to check."
