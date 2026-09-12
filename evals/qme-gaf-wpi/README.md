# qme-gaf-wpi evals

Two fictional draft excerpts and the findings a correct run produces.

- `draft-mismatch.md`: one seeded GAF/WPI mismatch in the rated sections, two out-of-scope prior-evaluator scores, a GAF range, and placeholders that must be skipped.
- `draft-boundary-orphan.md`: a correct pair at GAF 69 (the boundary), plus a WPI in a conclusions section with no GAF near it.
- `expected-findings.md`: the answer key.

## How to run

```bash
python3 skills/qme-gaf-wpi/scripts/gaf_wpi_check.py evals/qme-gaf-wpi/draft-mismatch.md
python3 skills/qme-gaf-wpi/scripts/gaf_wpi_check.py evals/qme-gaf-wpi/draft-boundary-orphan.md
```

Or invoke `/qme-gaf-wpi` on each file in an agent and compare the memo to the key. The script's output is the reference behavior; a manual run by the agent must match it finding for finding.

## What to score

- Exactly the expected findings, with the right kind (MISMATCH / BOUNDARY / ORPHAN) and section.
- Every finding quotes the draft sentence verbatim and states the table value with the page citation.
- Out-of-scope scores appear under "Not checked," never as findings.
- No score is proposed and no rating step beyond the table lookup is performed.
