# 2005 PDRS: GAF to Whole Person Impairment

Source: California Division of Workers' Compensation, *Schedule for Rating Permanent Disabilities* (effective January 1, 2005), Section 1, "Psychiatric Impairment," GAF-to-WPI conversion table, page 1-16. The schedule is a public document published by the DWC.

The table is a point lookup: one GAF, one WPI, no interpolation. Every row below was checked against the published page programmatically (all 100 rows) before this file was written. Re-derive from the source if any row is ever questioned; do not hand-edit a single value.

The only discontinuity is GAF 69 (2%) to GAF 70 (0%). GAF 70 and above rate 0% WPI. GAF 1 rates 90%.

Future earning capacity (FEC), occupational and age adjustments (Sections 2 through 5 of the schedule) are separate steps applied after WPI. They are outside this table and outside `/qme-gaf-wpi`.

| GAF | WPI | GAF | WPI | GAF | WPI | GAF | WPI |
|---|---|---|---|---|---|---|---|
| 1 | 90 | 26 | 73 | 51 | 29 | 76 | 0 |
| 2 | 89 | 27 | 72 | 52 | 27 | 77 | 0 |
| 3 | 89 | 28 | 71 | 53 | 26 | 78 | 0 |
| 4 | 88 | 29 | 71 | 54 | 24 | 79 | 0 |
| 5 | 87 | 30 | 70 | 55 | 23 | 80 | 0 |
| 6 | 87 | 31 | 69 | 56 | 21 | 81 | 0 |
| 7 | 86 | 32 | 67 | 57 | 20 | 82 | 0 |
| 8 | 85 | 33 | 65 | 58 | 18 | 83 | 0 |
| 9 | 84 | 34 | 63 | 59 | 17 | 84 | 0 |
| 10 | 84 | 35 | 61 | 60 | 15 | 85 | 0 |
| 11 | 83 | 36 | 59 | 61 | 14 | 86 | 0 |
| 12 | 82 | 37 | 57 | 62 | 12 | 87 | 0 |
| 13 | 82 | 38 | 55 | 63 | 11 | 88 | 0 |
| 14 | 81 | 39 | 53 | 64 | 9 | 89 | 0 |
| 15 | 80 | 40 | 51 | 65 | 8 | 90 | 0 |
| 16 | 80 | 41 | 48 | 66 | 6 | 91 | 0 |
| 17 | 79 | 42 | 46 | 67 | 5 | 92 | 0 |
| 18 | 78 | 43 | 44 | 68 | 3 | 93 | 0 |
| 19 | 78 | 44 | 42 | 69 | 2 | 94 | 0 |
| 20 | 77 | 45 | 40 | 70 | 0 | 95 | 0 |
| 21 | 76 | 46 | 38 | 71 | 0 | 96 | 0 |
| 22 | 76 | 47 | 36 | 72 | 0 | 97 | 0 |
| 23 | 75 | 48 | 34 | 73 | 0 | 98 | 0 |
| 24 | 74 | 49 | 32 | 74 | 0 | 99 | 0 |
| 25 | 73 | 50 | 30 | 75 | 0 | 100 | 0 |

The same values, in the form `scripts/gaf_wpi_check.py` carries them, are the authoritative copy for the script; this page is the human-readable one. Both were generated from the same parse of the source page.
