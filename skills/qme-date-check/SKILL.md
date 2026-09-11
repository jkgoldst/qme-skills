---
name: qme-date-check
description: Run the date arithmetic checks on a QME draft before signing. Finds years that collide, ages that do not add up against the date of birth, a date of injury or last day worked stated two ways, disability that starts before the last day worked, the date of injury restated in a section it does not belong in, and dates in the future. Deterministic; every finding quotes the two places that disagree. The draft against its own anchor dates only.
argument-hint: "<draft.docx or draft.txt> [--today YYYY-MM-DD]"
compatibility: Claude (web/desktop upload; Pro, Max, Team, Enterprise with code execution), Claude Code, Codex. Other skill-aware agents untested.
---

# QME Date Check

Ten deterministic checks over one draft report. Each finding names the check, states the arithmetic, and quotes the sentence or sentences involved. The physician decides which value is right; the check only shows that two values disagree.

## Input

One draft: `.docx`, `.txt`, or `.md`. The draft supplies its own anchors: the date of injury and last day worked from IDENTIFYING DATA, the date of birth from a `DOB:` line, the evaluation date from a `Date of Evaluation:` line. A check whose anchor is absent stays silent; silence from a missing anchor is reported as such, never as a pass.

## Run

With code execution: `python3 scripts/date_check.py <draft> [--today YYYY-MM-DD]`. Standard library only; `.docx` is read with python-docx when present, otherwise from the document XML. `--today` defaults to the machine date; pass the signing date when checking an older draft.

Without code execution: split the draft at its ALL-CAPS section headings, list every full date (month, day, year), every age, and the anchors above, then apply the ten checks in `references/checks.md` by hand in that order. Write down each check you could not apply and why.

## Output

Fill `templates/findings-table.md`: one row per finding with the check id, the arithmetic, location A with its quote, and location B with its quote when two places disagree. Close with the anchors used (or `absent`) and the checks that stayed silent for lack of an anchor. Report the count of findings and stop; the table carries no advice on which value to keep.

## The ten checks

| id | fires when |
|---|---|
| `f1_doi` | The date of injury in IDENTIFYING DATA differs from a date of injury stated in any other section. |
| `f1_last_day_worked` | Same, for the last day worked. |
| `f6_month_year_collision` | The same month and day appear in adjacent years in two different sections. |
| `f6_age_year_math` | The evaluee's stated age is more than one year off the date of birth as of the evaluation date; two sections give ages more than a year apart; or "N years since YYYY" fails against the evaluation year. |
| `f6_anchor_year_offset` | A date shares month and day with the date of injury or last day worked but carries a different year. |
| `f6_doi_section_routing` | The full date of injury appears in a section with no business restating it (family history, medications, mental status) and is not a relative reference ("two weeks after"). |
| `f6_ttd_predates_ldw` | A temporary disability period begins before the last day worked. |
| `f6_termination_date_spread` | Termination or last-worked dates in narrative sections are more than seven days apart. |
| `f6_future_year` | A date or year falls after today. |
| `f6_recent_year_plausibility` | Withdrawal candidate in the source registry; listed here so the count matches, not run by the script. |

`references/checks.md` has the full definition of each, including the anchors, the sections each check reads, and what it deliberately ignores.

## Boundaries

The draft against itself. This check reads no transcript, no records, and no prior report; a date that is wrong everywhere in the draft is invisible to it. Use it as the last pass before signing, after content review.
