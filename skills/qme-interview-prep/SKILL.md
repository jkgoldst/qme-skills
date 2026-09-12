---
name: qme-interview-prep
description: Turn what a California psychiatric QME has before the exam (referral letter, records, prior QME/AME reports, deposition transcripts) into the questions to ask the injured worker. Every question cites a document and page or is labeled a standard question. Produces questions only, never a summary of the record. Runs with zero documents.
argument-hint: "[folder or files: referral letter, records, prior reports, depositions]"
compatibility: Claude (web/desktop upload; Pro, Max, Team, Enterprise with code execution), Claude Code, Codex. Other skill-aware agents untested.
---

# QME Interview Prep

Produce the list of questions a psychiatric QME should ask the injured worker at the evaluation, built from the documents the physician has in hand. The physician takes the history and forms every opinion. This skill points at what to ask and where each question came from.

## What comes in

Accept these and nothing else:

- referral or cover letter (from the claims administrator, an attorney, or the Medical Unit)
- medical records (PDF or text)
- prior QME, AME, or treating physician medical-legal reports
- deposition transcripts

Anything else offered (a draft report, an exam transcript, a personnel file with no cover letter, a spreadsheet) is set aside with one line saying why. It is not read.

With no documents at all, the output is the heading `Standard questions only. No case documents were provided.` followed by groups 1 through 7 with their standard questions from `references/question-frame.md`. No inventory, no group 8, no referral-mapping table.

## Sourcing rule

Every line of output is a question with a citation, a heading, or a row in the document inventory or the referral-mapping table. The citation is either

- `[Document, p. N]` where the document is short-named from its own title page and N is the page as it appears in the file. When the file carries no page numbers, a records set is cited by dated entry (`[Raman records, entry 04/22/2019]`) and a report by section heading (`[Whitfield report, IDENTIFYING DATA]`), or
- `[standard question]` for a question every psychiatric QME asks regardless of the record.

One citation bracket per question. A bracket names two sources only when the question puts one document against another (`[Referral letter, p. 1; Raman records, entry 06/03/2023]`).

A sourced question opens with the record's own words or a bare fact (a date, a dose, a document's name), then asks. Quote verbatim, at most 25 words, and cite the quote. Diagnoses, scores, ratings, apportionment figures, and a party's label for an event (an employer calling a counseling "good-faith", counsel calling it "retaliatory") stay out of the memo; the worker is asked about the event, the symptom, the medication, or the statement underneath them, in plain words. State nothing about the record outside a question. A reader who deletes every question from the output is left with headings and nothing else.

The "Establish:" lines in `references/question-frame.md` are for the writer. They do not appear in the memo.

## Process

1. **Inventory the documents.** One row per document, short-named from its own title page, with page count (or "unpaginated") and type. Type is one of the four kinds under "What comes in", in those words; who obtained a report or who objects to it is a question trigger, not an inventory entry. A file that holds two documents (a records set followed by a prior evaluator's report) gets two rows sharing the file name, so each can be cited by its own short name. Documents the referral letter lists as enclosed but that were not provided get their own row, marked `listed in referral, not received`. This inventory and the referral-mapping table are the only non-question content in the memo.
2. **Read every document in full.** Deposition transcripts and prior reports are read to the last page, including the identifying-data and history sections where a prior evaluator records what the worker told them; a records set is read entry by entry. Skimming produces standard questions dressed as sourced ones.
3. **Extract question triggers.** While reading, note each fact that the injured worker should confirm, dispute, date, or expand on: a date, a diagnosis, a medication, a statement attributed to the worker, a personnel action, a prior claim, a stressor, a conflict between two documents. Each trigger becomes a question in step 4; one fact may feed questions in more than one group. Then take every date the referral asserts (date or period of injury, hire, last day worked, claim filing, each personnel action) and find where the records agree or differ; each difference is a trigger. Conflicts are asked about, never resolved.

   Write the triggers down as a list, one line each with its citation, before writing any question. The list is complete when it holds, from every document:
   - every statement the document attributes to the worker (what the worker "reports", "denies", "states", "elects");
   - every finding a prior evaluator makes about the worker's history (continuity of treatment or medication, symptom-free periods, what the worker told that evaluator);
   - every event the referral's statement of the claim names (hire, each complaint or grievance, each personnel action and any written response to it, last day worked), and each question the referral poses that names an event;
   - every evaluation or document the referral or a report says exists, received or not: did it happen, what does the worker recall of it;
   - every difference between two documents.
4. **Write the questions by group.** Use the eight groups in `references/question-frame.md`, in that order. Groups 1 through 7 hold questions about their topic, whether the record or the standard list prompted them. Group 8 holds only the questions that put a record statement to the worker: a statement attributed to the worker, a prior evaluator's finding, or a conflict between two documents. Every trigger of those three kinds on the step 3 list becomes a group 8 question; a trigger that also opens a topic gets a second, plainer question in that topic's group. Under each group, sourced questions first, then the group's standard questions. A standard question that the record already answers is still asked; the exam is where the worker answers it in the physician's presence. Where the referral letter poses questions to the physician, each one maps to the interview questions that gather what the physician needs to answer it; cite the letter's page.
5. **Check the memo against `templates/question-list.md`.** Every question carries one citation bracket. Every quote appears in the cited document word for word. No sentence characterizes the record, the worker, or the claim.

Completion: the memo lists every accepted document in the inventory, groups 1 through 7 each carry at least their standard questions, every line of the step 3 trigger list is a question somewhere in the memo, every date the referral asserts has been checked against the records, and every sourced question resolves to a page or entry that exists.

## Output

Fill `templates/question-list.md`. "Prepared" is the date the skill runs, from the system clock. In an agent with a filesystem, also write it beside the inputs as `interview-prep-YYYY-MM-DD.md`. Otherwise return it in the conversation.

## Boundaries

The output contains no diagnosis, no opinion on causation, apportionment, disability, or impairment, no rating, and no assessment of the worker's credibility. Those belong to the physician after the exam. If a document asks the physician for one of these, the memo carries the interview questions that bear on it and nothing more. A physical condition the referral names (headaches, a back injury) gets its current-treatment and history questions like any other complaint; whether it is within specialty is the physician's call.

Records review, chronology, and case summary are separate jobs. This skill neither indexes nor summarizes the record.

Run this in the account that `/qme-env-audit` has cleared for case data. Read only the files the physician provided.
