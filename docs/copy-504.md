# Copy deck for #504

Every string on the three pages, in page order. `[FIXED]` lines come from #504 or ADR 0029 and are not up for review. `[REVIEW]` lines are drafts. Edit in place or answer by section; the build copies from this file.

Rules applied throughout: physician's moment first, second person, no AI vendor in the hero, no "Skill" or command above the fold, no named roadmap, no "coming soon", no em dashes, every claim true today.

## Open questions before build

1. **Where the environment check lives.** Drafted as the first tick on the strip, labeled "Before any of it". Alternative: a one-line precondition above the strip ("First, check your setup") and six ticks only. First tick keeps one visual system; the precondition line keeps the strip to real case moments.
2. **F15 and F16 classification.** Both are single-physician and deterministic, but were built from cohort patterns. Drafted as managed. Say if either should be open.
3. **Whether the home page carries a sample finding.** Drafted without one; the env-audit page keeps it. The hero page stays short.

---

## Page 1: index.html

### Top bar
- Brand: `QME AI Hero` [FIXED, existing]
- Theme button: `Dark` / `Light` [existing]

### Hero
- Eyebrow: `For California QMEs` [REVIEW]
- Headline: `Before the exam. Before you sign.` [FIXED]
- Subhead: `Free tools for California QMEs that prepare your questions and check your draft, run privately in the AI account you already have.` [FIXED]
- CTA (one button): `Check your setup first` [REVIEW]. Scrolls to "Start here". Alternatives: `Start with the setup check`, `See where your case data goes`.

### Lifecycle strip
Ticks, left to right [REVIEW]:
`Before any of it` · `Referral` · `Records` · `Exam` · `Draft` · `Signing` · `Deposition`

Card at "Before any of it" [REVIEW]:
- Name: `Environment check`
- Under the name: `/qme-env-audit`
- One line: `Where case data goes in your AI account, and what to fix, before any real case goes in.`
- Link: `What happens when you run it` (to the env-audit page)

Card at "Draft" [FIXED label, REVIEW body]:
- Name: `Draft review`
- Under the name: `Full draft review, by invitation` [FIXED]
- One line: `Your draft checked against the transcript, the records, and itself, on a managed case.`
- Link: `Request an invitation` (to the managed-reviewer page)

Under the strip: `More moments as we go.` [FIXED]

### Tresa peer section (first scroll)
- Line: `The Skills check what's in front of you. Tresa checks it against everything else in the case.` [FIXED]
- Drafting sentence (exactly one): `Tresa also drafts the report from your interview and records, for your review and signature.` [REVIEW]
- Link: `See Tresa` → https://app.tresagroup.com [REVIEW]

### Start here
- Heading: `Start with the environment check` [REVIEW]
- Lede: `It asks about your setup one question at a time, tells you what it could verify and what it could not, and gives you a fix list in priority order. Run it before any real case goes into that account.` [REVIEW]
- Steps [REVIEW; the no-terminal path is the only one on this screen]:
  1. `Download the environment check` (link to qme-env-audit.zip) `(zip)`
  2. `In Claude, open Settings, then Capabilities, then Skills, and upload it.`
  3. `Start a new chat and type /qme-env-audit.`
- Note: `Needs a Claude Pro, Max, Team, or Enterprise plan with code execution turned on.` [REVIEW]

### Trust
- Heading: `Runs in your account. Nothing leaves it.` [REVIEW]
- Body: `Each tool runs inside the AI account you already pay for. Nothing is uploaded to us, there is no login, and no case data reaches our side. Whether that account is fit for case data is exactly what the environment check tells you.` [REVIEW]

### Technical toggle (below the fold, collapsed)
- Summary: `For technical users` [REVIEW]
- Body [REVIEW]:
  - `These are Agent Skills: a folder with a SKILL.md and reference files, MIT licensed, source on GitHub.` (GitHub links to the repo)
  - Terminal: `npx skills@latest add jkgoldst/qme-skills` with Copy
  - `Works in Claude Code, Codex, and other skill-aware agents. Then run /qme-env-audit, or /qme-env-audit --technical for a codebase- or infrastructure-backed review.`

### Footer
- `QME AI Hero is an open project from Tresa. MIT licensed.` [REVIEW]

---

## Page 2: qme-env-audit.html (per-Skill page)

- Eyebrow: `Before any of it` [REVIEW]
- Title: `Environment check` with `/qme-env-audit` underneath [REVIEW]
- Lede: `See where case data goes in your AI account, what can be verified right now, and what to fix before you rely on it for real evaluations.` [REVIEW; adapted from the current hero]

### What happens when you run it [FIXED heading]
[REVIEW body]
1. `It asks one question at a time about how you and your staff use the account: who logs in, where files go, what is kept, what gets emailed.`
2. `Each answer is marked verified, reported, or unknown. An assumption is never quietly turned into a pass.`
3. `You get a short list of findings in priority order, each with the evidence, why it matters for a QME, and the fix.`
4. `Fix the top items, run it again, and confirm the gap closed.`

### What good looks like [existing, keep; wording lightly touched, REVIEW]
1. `Each person has their own login. No shared accounts.`
2. `Case data stays inside a known, bounded environment.`
3. `Model and vendor access is explicit, not assumed.`
4. `PHI does not leak through convenience tools like email or chat.`
5. `Retention and deletion are decisions, not accidents.`
6. `Backups and recovery are understood before they are needed.`

### Example finding [existing block; keep verbatim per #432 rules: labeled, generic, true]
- Label: `Example output` (already present as "Example output." in the footnote; keep)

### What it is not [REVIEW]
`This is a readiness check, not legal advice, a HIPAA certification, or a determination that your practice is a Covered Entity or Business Associate.`

### Install [REVIEW]
Same three steps as the home page, then the technical toggle with the terminal command.

### Compatibility [REVIEW; also the new `compatibility` field in SKILL.md]
`Claude web and desktop by upload (Pro, Max, Team, Enterprise, with code execution on); Claude Code and Codex by command. Other skill-aware agents untested.`

Proposed SKILL.md frontmatter line:
`compatibility: Claude (web/desktop upload; Pro, Max, Team, Enterprise with code execution), Claude Code, Codex. Other skill-aware agents untested.`

---

## Page 3: draft-review.html (managed reviewer, one neutral page)

- Eyebrow: `At the draft` [REVIEW]
- Title: `Full draft review` [REVIEW; names the capability, never a command]
- Lede: `Your draft, checked against the interview transcript, the records, and itself. Every finding points at the sentence and the source it conflicts with. You decide what to do with it.` [REVIEW]
- Where it runs: `The review runs on a managed case. Today an invitation is a Tresa Trial Physician account; the review runs on the case you bring to it.` [REVIEW; decision 5 requires the "managed case" statement]

### How it is different from the Skills [REVIEW]
`The Skills check what is in front of you: one document, one table, one date. The review holds the whole case at once, and it is calibrated on the errors physicians actually made in signed reports.`

### What it checks [REVIEW; one line per family, evidence standard, open or managed; no check names, thresholds, prompts, or numbers]

| Family | What is checked | Evidence standard | Open or managed |
|---|---|---|---|
| Same fact, same value | The patient's name, date of injury, last day worked, pronouns, and causation percentages agree everywhere they appear. | The draft against itself. | Open |
| Document self-consistency | A fact left as an open question in one section is not asserted as settled in another; a denial is not affirmed elsewhere; no paragraph is repeated. | The draft against itself. | Managed |
| Draft against interview | Any fact the draft states differently from what was said in the room. | The draft against the transcript, adjudicated. | Managed |
| Empty sections and placeholders | Nothing left blank or bracketed reaches a signed report. | The draft. | Open |
| Date arithmetic | Years that collide, ages that do not add up, disability that starts before the last day worked, dates in the future. | The draft against its own anchor dates. | Open |
| Denials the transcript contradicts | The draft says a topic was denied when the interview addressed it. | The draft against the transcript, adjudicated. | Managed |
| Diagnosis carried through | The diagnosis you stated, with the specifiers you gave, and not one you ruled out. | The draft against what you said in the interview. | Managed |
| Judgment stays with you | P&S status, causation percentages, GAF, WPI, and statutory terms are not asserted where you did not state them. | The draft against the interview. | Managed |
| GAF near a boundary | A stated GAF close enough to a rating boundary to be worth confirming. | The 2005 PDRS table. | Open |
| Credibility left unreconciled | Credibility language, exaggeration notes, and an invalid testing profile all present with no reconciliation. | The draft. | Managed (see open question 2) |
| More than one disability period | Several disability periods under one diagnosis without the framing that supports it. | The draft. | Managed (see open question 2) |
| GAF and WPI agree | The stated GAF and WPI match the table. | The 2005 PDRS table. | Open |
| Records fidelity | What the draft says a record says, against the record. | The draft against the records. | Managed |
| Duplicate scans | The same document scanned twice in one side's production. | The records. | Managed |
| The interview against itself | Facts stated two ways in the same interview, and whether two different people could explain it. | The transcript, adjudicated and verified. | Managed |

Below the table: `Open families are the ones you can reproduce from public material; they become Skills as we go. Managed families were built and calibrated on signed reports and stay with the review.` [REVIEW]

### Request an invitation [REVIEW]
- Heading: `Request an invitation`
- Fields: `Name` · `Email` · `Practice`
- Button: `Request an invitation`
- Under the form: `Submissions go to Formspree, then to us. Name, email, practice only. No case material.` [agreed in grilling Q5]
- After submit (in page): `Thank you. We will be in touch.`

---

## Strings retired from the current site
- `open skills for California QMEs` (rail foot and eyebrow)
- `STAGE 01 · SAFE ENVIRONMENT` and all Stage numbers
- `Install /qme-env-audit`, `View on GitHub` (hero)
- `Choose your operating model` section (self-operated vs managed cards)
- `Next → Master the Record · coming`
- `AI can organize and challenge the evidence. The physician owns the medicine.` (epigraph; say if you want it kept somewhere)
- `not tied to any commercial QME application` (README, per ADR 0029 decision 8)
