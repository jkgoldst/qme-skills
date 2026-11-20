# MedLegal AI Hero: AI Skills for Medical-Legal Work

Free, practical AI skills for physicians doing medical-legal work. Use them with the AI tools you already have, or build your own workflows.

Site: **[qmeaihero.com](https://qmeaihero.com)**

Each skill is a set of reusable instructions that teaches an AI tool one medical-legal task. The skills keep evidence traceable, uncertainty visible, and medical judgment with the physician.

> **Public-good project:** the skills in this repository are meant to be useful on their own. They are not tied to any commercial application.

## New to AI in medical-legal work?

Read **[Start Here: Set Up AI for Medical-Legal Work](https://qmeaihero.com/start-here.html)** first. It covers choosing an AI environment, what to check before using real records, and trying your first skill on a fictional case.

## Skill #1: `/case-facts`

**Catch conflicting facts before they make it into the report.**

[`/case-facts`](./skills/case-facts/SKILL.md) checks identifying and administrative facts across your case documents: examinee name, date of birth, injury dates, claim and case numbers, employer, attorneys, and other parties. It shows what agrees, what conflicts, and what's missing, with the source for every value.

It never picks between conflicting values for you. Unresolved facts stay as visible placeholders, such as `[CONFIRM: date of birth]`, rather than being guessed.

It does not review diagnoses, causation, impairment, or legal conclusions.

Page: [qmeaihero.com/case-facts.html](https://qmeaihero.com/case-facts.html)

### Try it on a fictional case first

[`skills/case-facts/examples/`](./skills/case-facts/examples/) holds a fictional three-document packet (cover letter, records summary, interview excerpt) and an answer key listing what a correct run should report and what counts as a failure. No real patient information.

### Install

- **Claude Code and other agents that read skill folders:** copy [`skills/case-facts`](./skills/case-facts/) into your skills folder (for Claude Code, `~/.claude/skills/`), then type `/case-facts`.
- **Claude (claude.ai):** download [`case-facts.zip`](./docs/case-facts.zip) and upload it under *Settings → Capabilities → Skills*.
- **Chat products without skill support:** attach `SKILL.md` with your documents and ask the AI to follow it.

We are still testing installation across AI tools. Please open an issue with what worked and what didn't.

**Only use real patient records in an AI environment authorized for protected health information.** The skill provides no HIPAA compliance or security controls. If you can't establish that your setup is authorized, use fictional case files.

## More skills coming

Records review, report critique, deposition preparation, and other reusable workflows.

## How these skills work

**Small and composable.** Each skill does one medical-legal job well rather than owning the whole workflow.

**Evidence first.** Important claims trace back to source material.

**Uncertainty stays visible.** Unknown does not become "probably fine." An unresolved fact is better than a plausible invention.

**Physician controlled.** AI can read, organize, compare, and flag. The physician owns interpretation, medical judgment, and the final report.

**Tested, not just polished.** A skill is judged by whether it catches what it should and never invents what it shouldn't, not by whether its output looks good.

**Open.** Inspect them, fork them, adapt them, and improve them.

## What this project does not do

This project does **not**:

- certify that an environment is HIPAA compliant or secure
- provide legal or compliance advice
- guarantee an accurate report
- make medical-legal conclusions on behalf of a physician

## Repository structure

```text
qme-skills/
├── README.md
├── docs/                    # the site (GitHub Pages) and downloadable skill zips
├── scripts/
│   └── build-skill-zip.sh   # builds docs/<skill>.zip
├── skills/
│   ├── case-facts/
│   │   ├── SKILL.md
│   │   └── examples/        # fictional packet and answer key
│   └── qme-env-audit/       # earlier skill, not currently featured
└── evals/
```

## Contributing

This project is early. The most useful contributions:

- feedback from physicians doing medical-legal work
- fictional test cases that expose failure modes
- corrections where a skill overstates what an AI system can verify
- proposals for small, reusable skills with a clear input, output, physician decision boundary, and evaluation method

## License

MIT. See [`LICENSE`](./LICENSE).
