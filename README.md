# QME Skills

Open, reusable AI skills for safer and better California QME workflows.

This repository starts with one public-good skill: **`/qme-env-audit`** — a structured review of the environment used to handle QME case data with AI.

The goal is not to certify HIPAA compliance or give legal advice. The goal is to help physicians, practices, and technical operators understand how case data actually moves through their systems, verify controls where possible, distinguish facts from assumptions, and leave with a concrete remediation plan.

## First skill

### `/qme-env-audit`

Use this skill to review:

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

The skill asks one question at a time, gives an example answer with each question, and labels findings as **VERIFIED**, **REPORTED**, or **UNKNOWN**.

## Install

Once this repository is public, install the skill with the standard skills installer:

```bash
npx skills add jkgoldst/qme-skills --skill=qme-env-audit
```

Then invoke:

```text
/qme-env-audit
```

For a codebase/infrastructure-backed review, ask for technical mode:

```text
/qme-env-audit --technical
```

## Repository structure

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

## Design principles

1. **Follow the data.** Trace one real case through the system instead of asking generic compliance questions.
2. **Prefer implementation over policy.** If code, configuration, CLI output, contracts, or cloud settings can verify a claim, inspect them.
3. **Never turn uncertainty into a pass.** Unknown means unknown.
4. **Separate legal status from technical control.** A BAA is not a security architecture; encryption is not a legal determination.
5. **Fail safe.** Do not describe an LLM self-check as deterministic verification.
6. **Preserve physician responsibility.** AI may assist, but the physician owns the medical-legal opinion and final report.
7. **Be useful, not exhaustive.** Stop when additional questioning has diminishing value and produce a prioritized action plan.

## What this does not do

This project does **not**:

- certify that an environment is HIPAA compliant
- determine that a physician, practice, or vendor is a Covered Entity or Business Associate
- provide legal advice
- replace California workers' compensation counsel, privacy counsel, or a formal security assessment

## Status

`qme-env-audit` is an early public-good skill. The intended development loop is:

**build → test on synthetic environments → dogfood on real architectures → revise → publish**

Future candidate skills include `/orient-case`, `/build-chronology`, `/find-conflicts`, and `/prep-evaluation`.
