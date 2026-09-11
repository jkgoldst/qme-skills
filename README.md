# AI Skills for California QMEs

Open, reusable AI workflows for safer, more rigorous California Qualified Medical Evaluator work.

These skills are designed to help physicians and practices use AI for repetitive, high-volume work while keeping evidence traceable, uncertainty visible, and medical-legal judgment with the physician.

> **Public-good project:** the open skills in this repository are intended to be useful on their own and are not tied to any commercial QME application.

## Try the first skill

Site: **[qmeaihero.com](https://qmeaihero.com)** (Stage 01 · Safe Environment).

**In Claude (no terminal).** Download [`qme-env-audit.zip`](./docs/qme-env-audit.zip), then in Claude open *Settings → Capabilities → Skills* and upload it. Needs a Pro, Max, Team, or Enterprise plan with code execution enabled. Start a new chat and type:

```text
/qme-env-audit
```

**In Claude Code, Codex, or another skill-aware agent.** Install from this repository with the standard skills installer:

```bash
npx skills@latest add jkgoldst/qme-skills
```

Then run `/qme-env-audit`, or for a codebase- or infrastructure-backed review:

```text
/qme-env-audit --technical
```

Run the audit *before* you put real case data into whichever account you install it in — the audit will tell you whether that account is fit for it.

## Why QME Skills Exist

AI can read thousands of pages, summarize records, draft prose, and find inconsistencies. But generic AI workflows are not designed around California med-legal practice, PHI handling, source provenance, or physician responsibility.

QME Skills encode repeatable workflows so the agent does the same disciplined thing each time instead of improvising from a generic prompt.

### "I don't know whether my AI setup is appropriate for QME case data."

Use **[`/qme-env-audit`](./skills/qme-env-audit/SKILL.md)**.

It walks through the actual environment, follows PHI through the system, distinguishes verified facts from reported assumptions, and produces a prioritized remediation plan.

### "Does the WPI in my draft match the GAF I gave?"

Use **[`/qme-gaf-wpi`](./skills/qme-gaf-wpi/SKILL.md)**.

It finds every GAF and Whole Person Impairment pair in the draft and checks it against the 2005 PDRS table, quoting the sentence and citing the table page. It proposes no score.

### "I need to understand a massive case quickly."

**`/orient-case`** is planned to turn a packet and cover letters into a compact case map: dates of injury, body parts, parties, allegations, prior opinions, and questions the QME must answer.

### "I need a reliable chronology, not another generic summary."

**`/build-chronology`** is planned to produce a source-backed medical/legal timeline with provenance and explicit uncertainty.

## Skills

The collection is organized into five **Stages** — the order a physician meets them, not the order they were built:

**01 Safe Environment → 02 Master the Record → 03 Find What Matters → 04 Prepare the Physician → 05 Defend the Report**

### 01 · Safe Environment

- **[`/qme-env-audit`](./skills/qme-env-audit/SKILL.md)** — Audit the environment used to handle QME case data with AI. **Available**
- **`/qme-env-setup`** — Build a safe environment step by step, walking the physician through the parts only they can do (accounts, agreements, storage). The audit checks a setup; this one creates it. *Planned*

### 02 · Master the Record

- **`/orient-case`** — Create a compact case map from the packet and cover letters. *Planned*
- **`/build-chronology`** — Build a source-backed medical/legal timeline. *Planned*
- **`/summarize-records`** — Summarize records into a consistent QME-oriented structure. *Planned*

### 03 · Find What Matters

- **`/find-conflicts`** — Find contradictions across records, history, exam, and draft. *Planned*
- **`/find-evidence`** — Surface the strongest supporting and conflicting evidence for a question or conclusion. *Planned*
- **`/reason-about-causation`** — Assemble an evidence map for industrial causation; the physician decides. *Planned*
- **`/reason-about-apportionment`** — Assemble candidate contributing factors and evidence; the physician decides. *Planned*

### 04 · Prepare the Physician

- **`/prep-evaluation`** — Identify patient-specific issues and questions to clarify during the evaluation. *Planned*
- **`/draft-from-findings`** — Turn physician-approved findings into source-linked prose. *Planned*

### 05 · Defend the Report

- **[`/qme-gaf-wpi`](./skills/qme-gaf-wpi/SKILL.md)** — Check every GAF and WPI pair in a draft against the 2005 PDRS conversion table before signing; flags a mismatch, a score within two points of the 69 to 70 cliff, and a GAF or WPI stated without its partner. Lookup only; the score stays the physician's. **Available**
- **`/completeness-review`** — Check whether required questions and report elements are addressed. *Planned*
- **`/substantial-evidence-review`** — Challenge whether opinions are adequately supported by the record and reasoning. *Planned*
- **`/contradiction-review`** — Check for unresolved contradictions within the report or between report and record. *Planned*

## How These Skills Work

**Small and composable.** Each skill should do one QME job well rather than own the entire workflow.

**Evidence first.** Important claims should trace back to source material whenever the task allows it.

**Verify when possible.** Code, configuration, cloud settings, and contract language outrank memory or user assumption when they can be inspected directly.

**Uncertainty stays visible.** Unknown does not become "probably fine." Skills should distinguish what is verified, what is reported, and what remains unknown.

**Physician controlled.** AI can read, organize, challenge, and draft. The physician owns interpretation, medical judgment, and the final report.

**Portable.** Skills should work across models and agent environments wherever the workflow does not depend on a proprietary runtime.

**Open.** Inspect them, fork them, adapt them, and improve them.

## `/qme-env-audit`

The first skill is a structured technical and operational review of the environment used to handle QME case data with AI.

It reviews areas including:

- legal/data boundaries
- PHI ingress, storage, processing, and egress
- subprocessors and BAA status
- authentication and authorization
- production vs. development isolation
- retention, deletion, backup, and recovery
- logging, analytics, and notifications
- AI model/provider controls
- source grounding and provenance
- physician control over final QME output
- incident response and change governance

The skill asks one question at a time and provides an example answer so a nontechnical physician can participate without needing to know cloud or security vocabulary in advance.

Where technical access is available, it should verify claims instead of relying solely on self-report.

Findings are labeled:

- **VERIFIED** — supported by code, configuration, CLI output, contracts, or another inspectable source
- **REPORTED** — stated by the user but not independently verified
- **UNKNOWN** — material fact not yet established

The final output prioritizes work as:

**Contain → Consolidate → Harden → Verify → Scale**

with specific **P0 / P1 / P2** remediation items.

## What This Project Does Not Do

This project does **not**:

- certify that an environment is HIPAA compliant
- certify that an environment is "QME compliant" or secure
- determine that a physician, practice, or vendor is a Covered Entity or Business Associate
- provide legal advice
- replace California workers' compensation counsel, privacy counsel, or a formal security assessment
- make medical-legal conclusions on behalf of a physician

## Development & Testing

The intended development loop is:

**build → test on synthetic environments → dogfood on real architectures → revise → publish**

Skills should not be judged only by whether their output "looks good." Where practical, each skill should have repeatable evaluation cases with expected findings or behaviors.

Current eval structure:

```text
evals/
├── qme-env-audit/
│   ├── README.md
│   ├── unsafe-solo-practice.md
│   └── expected-findings.md
└── qme-gaf-wpi/
    ├── README.md
    ├── draft-mismatch.md
    ├── draft-boundary-orphan.md
    └── expected-findings.md
```

The goal is to catch regressions such as:

- missing a known high-risk control gap
- incorrectly turning an unknown into a pass
- describing an LLM self-check as deterministic verification
- overclaiming legal or compliance status
- losing physician-control safeguards

## Repository Structure

```text
qme-skills/
├── README.md
├── docs/                      # the site (GitHub Pages) + downloadable skill zips
│   ├── index.html
│   ├── qme-env-audit.zip      # built by scripts/build-skill-zip.sh
│   └── qme-gaf-wpi.zip
├── scripts/
│   └── build-skill-zip.sh
├── skills/
│   ├── qme-env-audit/
│   │   ├── SKILL.md
│   │   ├── references/
│   │   └── templates/
│   └── qme-gaf-wpi/
│       ├── SKILL.md
│       ├── references/pdrs-2005-gaf-wpi.md
│       ├── scripts/gaf_wpi_check.py
│       └── templates/findings.md
└── evals/
    ├── qme-env-audit/
    └── qme-gaf-wpi/
```

## Contributing

This project is early. The most useful contributions are likely to be:

- real-world feedback from QMEs and QME practices
- synthetic test environments that expose failure modes
- improvements to skill instructions and evidence handling
- corrections where a workflow overstates what an AI system can verify
- proposals for small, reusable QME skills

When proposing a new skill, prefer a narrow workflow with a clear input, output, physician decision boundary, and evaluation method.

## License

MIT. See [`LICENSE`](./LICENSE).
