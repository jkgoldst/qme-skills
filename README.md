# AI Skills for California QMEs

Open, reusable AI workflows for safer, more rigorous California Qualified Medical Evaluator work.

These skills are designed to help physicians and practices use AI for repetitive, high-volume work while keeping evidence traceable, uncertainty visible, and medical-legal judgment with the physician.

> **Maintained by the team behind Tresa.** The open skills are independently usable under the MIT license. Using Tresa is optional.

## Try QME AI Setup Review

Site: **[qmeaihero.com](https://qmeaihero.com)**. A skill is reusable instructions installed in an AI assistant. This review adapts to whether you use an AI service, buy a managed application, or operate software.

Describe your tools and workflow, then supply selected redacted evidence where available. You receive a data-flow map, scoped findings, priority actions, and questions for your vendor or technical support. **No patient files are needed.** Keep patient identifiers, passwords, and API keys out of the audit. Installing the skill does not change your account's terms or implement controls. The review does not certify an account for patient data.

[Read a complete fictional report](https://qmeaihero.com/sample-report.html) ([HTML source](./docs/sample-report.html)). This is an authored illustration, not a behavioral test result.

### Claude, without a terminal

1. Download [`qme-env-audit.zip`](./docs/qme-env-audit.zip).
2. Enable code execution in Settings → Capabilities. Open Customize → Skills → + → Create skill → Upload a skill, and upload the ZIP.
3. Enable the skill and start a new chat. Ask:

```text
Use qme-env-audit to review my QME AI setup. Start with my tools and workflow. No patient files.
```

Your organization may restrict custom skills. See [Claude's current installation guidance](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

### Claude Code

Run in the project where you want the skill available:

```bash
npx skills@latest add jkgoldst/qme-skills --skill qme-env-audit --agent claude-code
```

Start a new session and type `/qme-env-audit`. Add `--technical` to request deeper code/configuration inspection. See [Claude Code skills](https://code.claude.com/docs/en/skills).

### Codex

Run in the project where you want the skill available:

```bash
npx skills@latest add jkgoldst/qme-skills --skill qme-env-audit --agent codex
```

Start a new session and ask:

```text
$qme-env-audit Review my QME AI setup.
```

Add `--technical` for deeper code/configuration inspection. See [Codex skills](https://learn.chatgpt.com/docs/build-skills).

The installer is the third-party [skills CLI](https://github.com/vercel-labs/skills). [Validation status](./docs/validation.md) separates package/installation checks from model behavior and account-specific checks.

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

The collection is organized into five **Stages**: the order a physician meets them, not the order they were built:

**01 Safe Environment → 02 Master the Record → 03 Find What Matters → 04 Prepare the Physician → 05 Defend the Report**

### 01 · Safe Environment

- **[`/qme-env-audit`](./skills/qme-env-audit/SKILL.md)**: Audit the environment used to handle QME case data with AI. **Available**
- **`/qme-env-setup`**: Build a safe environment step by step, walking the physician through the parts only they can do (accounts, agreements, storage). The audit checks a setup; this one creates it. *Planned*

### 02 · Master the Record

- **`/orient-case`**: Create a compact case map from the packet and cover letters. *Planned*
- **`/build-chronology`**: Build a source-backed medical/legal timeline. *Planned*
- **`/summarize-records`**: Summarize records into a consistent QME-oriented structure. *Planned*

### 03 · Find What Matters

- **`/find-conflicts`**: Find contradictions across records, history, exam, and draft. *Planned*
- **`/find-evidence`**: Surface the strongest supporting and conflicting evidence for a question or conclusion. *Planned*
- **`/reason-about-causation`**: Assemble an evidence map for industrial causation; the physician decides. *Planned*
- **`/reason-about-apportionment`**: Assemble candidate contributing factors and evidence; the physician decides. *Planned*

### 04 · Prepare the Physician

- **`/prep-evaluation`**: Identify patient-specific issues and questions to clarify during the evaluation. *Planned*
- **`/draft-from-findings`**: Turn physician-approved findings into source-linked prose. *Planned*

### 05 · Defend the Report

- **`/completeness-review`**: Check whether required questions and report elements are addressed. *Planned*
- **`/substantial-evidence-review`**: Challenge whether opinions are adequately supported by the record and reasoning. *Planned*
- **`/contradiction-review`**: Check for unresolved contradictions within the report or between report and record. *Planned*

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

The skill routes by responsibility and asks one question at a time with a fictional example answer. A physician can say “I don't know”; inaccessible controls become scoped vendor/operator evidence requests.

Where technical access is available, it should verify claims instead of relying solely on self-report.

Findings are labeled:

- **VERIFIED**: directly inspected evidence for the exact claim, with locator, scope, date, and limits
- **REPORTED**: attributed to the user or operator, without independently inspected evidence
- **UNKNOWN**: a material fact not established, with the evidence needed to resolve it

The final output prioritizes work as:

**Contain → Consolidate → Harden → Verify → Scale**

with specific **P0 / P1 / P2** actions, owners, and closure evidence. Material unknowns remain visible. Final assessments name gaps, insufficient evidence, or no material gaps in the controls reviewed; they do not give blanket readiness verdicts.

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
    ├── expected-findings.md
    ├── behavior-expectations.md
    ├── controlled-environment.md
    ├── limited-access-physician.md
    ├── conflicting-deployment.md
    ├── unknown-and-pressure.md
    └── physician-integrity.md
```

The goal is to catch regressions such as:

- missing a known high-risk control gap
- incorrectly turning an unknown into a pass
- describing an LLM self-check as deterministic verification
- overclaiming legal or compliance status
- losing physician-control safeguards

## Repository Structure

- `skills/`: reusable instructions, routed references, and output templates.
- `docs/`: the GitHub Pages site, fictional report, validation record, and downloadable ZIP.
- `evals/`: fictional scenarios and separate scoring criteria.
- `scripts/`: ZIP packaging, validation-page rendering, and package/link checks.

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
