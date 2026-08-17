# AI Skills for California QMEs

Open, reusable AI workflows for safer, more rigorous California Qualified Medical Evaluator work.

These skills are designed to help physicians and practices use AI for repetitive, high-volume work while keeping evidence traceable, uncertainty visible, and medical-legal judgment with the physician.

> **Public-good project:** the open skills in this repository are intended to be useful on their own and are not tied to any commercial QME application.

## Try the first skill

Install from this repository with the standard skills installer:

```bash
npx skills@latest add jkgoldst/qme-skills
```

Then run:

```text
/qme-env-audit
```

For a codebase- or infrastructure-backed review:

```text
/qme-env-audit --technical
```

> The repository is currently in early development. Installation is intended to be tested across supported agent environments before the first public release.

## Why QME Skills Exist

AI can read thousands of pages, summarize records, draft prose, and find inconsistencies. But generic AI workflows are not designed around California med-legal practice, PHI handling, source provenance, or physician responsibility.

QME Skills encode repeatable workflows so the agent does the same disciplined thing each time instead of improvising from a generic prompt.

### "I don't know whether my AI setup is appropriate for QME case data."

Use **[`/qme-env-audit`](./skills/qme-env-audit/SKILL.md)**.

It walks through the actual environment, follows PHI through the system, distinguishes verified facts from reported assumptions, and produces a prioritized remediation plan.

### "I need to understand a massive case quickly."

**`/orient-case`** is planned to turn a packet and cover letters into a compact case map: dates of injury, body parts, parties, allegations, prior opinions, and questions the QME must answer.

### "I need a reliable chronology, not another generic summary."

**`/build-chronology`** is planned to produce a source-backed medical/legal timeline with provenance and explicit uncertainty.

## Skills

The collection is organized around the QME lifecycle:

**Orient → Master the record → Examine → Reason → Write → Defend**

### Security & setup

- **[`/qme-env-audit`](./skills/qme-env-audit/SKILL.md)** — Audit the environment used to handle QME case data with AI. **Available**

### Understand the case

- **`/orient-case`** — Create a compact case map from the packet and cover letters. *Planned*
- **`/build-chronology`** — Build a source-backed medical/legal timeline. *Planned*
- **`/summarize-records`** — Summarize records into a consistent QME-oriented structure. *Planned*

### Investigate

- **`/find-conflicts`** — Find contradictions across records, history, exam, and draft. *Planned*
- **`/prep-evaluation`** — Identify patient-specific issues and questions to clarify during the evaluation. *Planned*
- **`/find-evidence`** — Surface the strongest supporting and conflicting evidence for a question or conclusion. *Planned*

### Reason

- **`/reason-about-causation`** — Assemble an evidence map for industrial causation; the physician decides. *Planned*
- **`/reason-about-apportionment`** — Assemble candidate contributing factors and evidence; the physician decides. *Planned*

### Write

- **`/draft-from-findings`** — Turn physician-approved findings into source-linked prose. *Planned*

### Review & defend

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
└── qme-env-audit/
    ├── README.md
    ├── unsafe-solo-practice.md
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
├── skills/
│   └── qme-env-audit/
│       ├── SKILL.md
│       ├── references/
│       │   ├── evidence-levels.md
│       │   └── qme-review-domains.md
│       └── templates/
│           ├── data-flow.md
│           └── findings-report.md
└── evals/
    └── qme-env-audit/
        ├── README.md
        ├── unsafe-solo-practice.md
        └── expected-findings.md
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
