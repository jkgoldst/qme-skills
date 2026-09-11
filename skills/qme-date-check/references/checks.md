# Check definitions

Fresh MIT copy of the F6 date family (plus the two F1 date checks) from a managed QME critic. Same check definitions; results may differ from the managed reviewer as the two drift.

## Anchors

All anchors come from the draft itself.

- **Date of injury (DOI)**: the first "date of injury" sentence in IDENTIFYING DATA (fallback: the first "injured ... on <date>" sentence there).
- **Last day worked (LDW)**: the first "last worked on <date>" sentence in IDENTIFYING DATA. Fallback for the TTD check only: the first termination sentence anywhere.
- **Date of birth**: the first `DOB:` or "date of birth" line.
- **Evaluation date**: the first "Date of Evaluation:" or "Date of Re-evaluation:" line. Falls back to today for age math.

A check with no anchor emits nothing and the output says so.

## Sections

A section starts at a line that is entirely upper case (optionally wrapped in `=====` or ending in a colon). Text before the first heading is FRONT MATTER.

## Checks

### f1_doi
DOI anchor against every other "date of injury <date>" sentence in every other section. Fires on any difference. Quotes both.

### f1_last_day_worked
LDW anchor against every other "last worked <date>" sentence. Fires on any difference.

### f6_month_year_collision
Every full date in the draft, keyed by month and day. Fires when the same month and day appear with years one apart in two different sections. Month-and-year-only mentions ("March 2024") are ignored; that tier was withdrawn in the source for false positives.

### f6_age_year_math
Three sub-checks.
1. Each evaluee age ("Ms. X is a 41-year-old", "41-year-old woman", the `DOB: ... (41)` parenthetical) against the date of birth as of the evaluation date. Fires when off by more than one year. Ages of other people ("one child, age 12") are not evaluee ages and are ignored.
2. Two evaluee ages more than a year apart anywhere in the draft.
3. "for N years ... since YYYY" (either order, digits or words up to twenty) against the evaluation year. Fires when off by more than one year.

### f6_anchor_year_offset
Every full date against the DOI and LDW anchors. Fires when month and day match and the year differs.

### f6_doi_section_routing
The full DOI appearing in a section outside the set where it belongs (identifying data, history of injury, review of records, current complaints, occupational history, diagnosis, discussion, causation, disability, impairment, apportionment, prior industrial injuries, declaration, billing). A mention preceded in the same sentence by a relative word (after, before, since, following, until, from, through, between, prior to) is a relative reference and is ignored.

### f6_ttd_predates_ldw
Each "temporarily totally/partially disabled from <date>" (also TTD/TPD) against the LDW anchor. Fires when the disability start is earlier.

### f6_termination_date_spread
Termination and last-worked dates (terminated, separated, resigned, laid off, stopped working, went off work, has not worked since, last worked) pooled from identifying data, history of injury, occupational history, current complaints, social history, disability, discussion. Fires when the earliest and latest are more than seven days apart and sit in different sections.

### f6_future_year
Any full date after today, or any bare year greater than today's year. A planned future re-evaluation date will fire; the physician confirms it is intended.

### f6_recent_year_plausibility
Source definition: an uncorroborated single date two years before the evaluation date that would be plausible one year later. Marked a withdrawal candidate in the source registry for false positives. Listed, not run.
