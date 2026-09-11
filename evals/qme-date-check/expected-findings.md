# Expected findings: seeded-draft.txt, today = 2025-03-20

Anchors: DOI 2024-02-28 and LDW 2024-02-28 (IDENTIFYING DATA), DOB 1985-03-04, evaluation date 2025-03-15.

## Must fire

| Check | Seeded defect | A | B |
|---|---|---|---|
| `f1_doi` | DOI 2024-02-28 vs 2023-02-28 | IDENTIFYING DATA | OCCUPATIONAL HISTORY |
| `f6_month_year_collision` | 11/14/2022 vs 11/14/2023 (counseling) | CURRENT COMPLAINTS | HISTORY OF INJURY |
| `f6_month_year_collision` | 1/9/2024 vs 1/9/2025 (defense evaluation) | DISCUSSION | HISTORY ... MEDICAL RECORDS |
| `f6_month_year_collision` | 2/28/2023 vs 2/28/2024 | OCCUPATIONAL HISTORY | IDENTIFYING DATA |
| `f6_age_year_math` | 43-year-old vs DOB (40 as of evaluation) | DISCUSSION | DOB line |
| `f6_age_year_math` | ages 40 and 43 in different places | FRONT MATTER or IDENTIFYING DATA | DISCUSSION |
| `f6_age_year_math` | "four years, from 2014" is 11 years by 2025 | OCCUPATIONAL HISTORY | |
| `f6_anchor_year_offset` | 2023-02-28 vs DOI 2024-02-28 | IDENTIFYING DATA | OCCUPATIONAL HISTORY |
| `f6_anchor_year_offset` | 2023-02-28 vs LDW 2024-02-28 | IDENTIFYING DATA | OCCUPATIONAL HISTORY |
| `f6_doi_section_routing` | 2024-02-28 in FAMILY HISTORY (father's death) | FAMILY HISTORY | |
| `f6_ttd_predates_ldw` | TTD from 2024-01-15, LDW 2024-02-28 | DISABILITY STATUS | IDENTIFYING DATA |
| `f6_termination_date_spread` | stopped working 2024-02-12 vs terminated 2024-03-20 (37 days) | HISTORY OF INJURY | SOCIAL HISTORY |
| `f6_future_year` | re-evaluation 2027-03-15 | FUTURE MEDICAL TREATMENT | |

Thirteen findings. `f1_last_day_worked` has no seeded defect and stays silent.

## Must stay silent

- "one child, age 12" (SOCIAL HISTORY): not the evaluee's age.
- "Weekly psychotherapy since June 2023" (CURRENT TREATMENT): month-and-year only.
- "41-year-old" in IDENTIFYING DATA against DOB (40): within one year.
- "in treatment with Dr. Raman for six years, since 2019": 2025 minus 2019 is 6.
- 2025-03-15 (evaluation date, P&S date) is not in the future as of 2025-03-20.

## Must not appear

- Any statement of which of two values is correct.
- Any finding drawn from outside the draft.
