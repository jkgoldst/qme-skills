# Validation status

Review date: 2026-10-10. This page separates checks of the bundle and installation instructions from observed model behavior. No patient records or production systems are used.

## Package and source checks

- Skill frontmatter/structure: passed the skill-creator validator.
- Downloadable ZIP: rebuilt from the revised source; every packaged file must match source bytes.
- Local HTML resources, fragments, ARIA targets, and skill/README links: checked by `python3 scripts/validate-package.py`.
- JavaScript syntax: checked by `node --check docs/site.js`.
- Keyboard tabs and clipboard success/failure handling: local synthetic DOM smoke check.
- Visual layout: inspected in-browser at desktop width and 390-pixel mobile width. Both the main page and full report had viewport/content widths of 390 pixels in the mobile check; report tables scroll within their containers.
- Browser keyboard tab navigation and ZIP download: passed. The downloaded ZIP matched the rebuilt bundle byte-for-byte.

These checks do not establish correct model decisions, account suitability, or deployment behavior.

## Installation guidance

The published instructions were reviewed against these primary sources on 2026-10-10:

- [Claude skills](https://support.claude.com/en/articles/12512180-use-skills-in-claude): custom ZIP upload, skill enablement, and natural-language use. Organization policies can restrict access. The current path is Customize → Skills; code execution is enabled separately.
- [Claude Code skills](https://code.claude.com/docs/en/skills): `/qme-env-audit` invocation.
- [Codex skills](https://learn.chatgpt.com/docs/build-skills): explicit skill invocation and discovery.
- [Third-party skills installer](https://github.com/vercel-labs/skills): project installation and agent selection.

Connection retries restored browser/npm access after initial approval-review failures. The installer help confirmed the documented skill/agent options. The revised skill installed successfully from the local candidate source into disposable project directories for both agents, and installed SKILL.md bytes matched the source. These local-source checks establish candidate packaging; they do not imply the public main branch already contains the revision.

- Claude Code 2.1.296: fresh nonpersistent session, `/qme-env-audit` invocation, Sonnet alias resolved to `claude-sonnet-5-5`; returned the intended no-patient-data opening and role question. No permission denials occurred.
- Codex CLI 0.162.0-alpha.2: fresh ephemeral read-only session, `$qme-env-audit` invocation; execution log showed reads of the installed skill, followed by the opening and workflow question. Exact model identifier was not recorded.
- Claude web: the continuation used the user's signed-in Chrome session. The exact local candidate ZIP was uploaded and enabled. Opus 5.5 Medium visibly loaded `qme-env-audit`, returned the safety opening and role question, routed a fictional direct-service physician without server interrogation, and finished a scoped report when unavailable facts stayed unknown. The account's memory influenced the first opening; the next fictional request explicitly limited the review to that scenario. After the continuation amendments, the rebuilt ZIP replaced the same skill as v2, remained enabled, and a fresh chat visibly loaded it and returned the expected opening. The v2 contents displayed the amended stopping and evidence instructions. This is upload/first-use and one limited physician-flow coverage, not a six-scenario Claude web cohort.

- Remote candidate installation: `skills` 1.7.2 installed `qme-env-audit` for both `claude-code` and `codex` from the published GitHub candidate revision `f25764e528117010b0fa68d7544ed406da0e88cc` into a disposable project. Its lockfile recorded that revision, and all five installed files matched candidate source bytes. A fresh ephemeral Codex invocation returned the safety opening and role question after runtime-directory write access was granted. After the continuation amendments were pushed, a second disposable installation from exact revision `3951eec1b5349d6b679bfae4eb9ad34b6563ca50` passed for both agents: lockfile revision and all five source-file bytes matched. This verifies the published candidate, not the unchanged main branch or production website. A retry using a slash-containing branch URL was rejected after the installer parsed its branch as `codex`; the exact-SHA source URL is the tested candidate-install form.

The exact-revision remote installation also passed a fresh nonpersistent Claude Code first invocation with `claude-sonnet-5-5`: safety opening and direct/managed/operator question, no permission denials, and no runtime error. Later validation-only commits do not change the five skill files or ZIP checked at `3951eec`.

No claim is made that a first-invocation smoke test establishes complete interview behavior.

## Behavioral validation

Six fictional scenarios and independent expectations are in `evals/qme-env-audit/`. Keep scoring files out of evaluation prompts. Independent bounded smoke runs, if completed, are recorded below; they do not replace fresh-session tests in each advertised runtime or full multi-turn interviews.

Initial cohort: six independent bounded Codex-subagent smoke reports were completed using the skill digest `87529af2ade94ccbc8a3554b35c83b0a7cf76100216e3960627496611c50653c`. Each agent received only the skill, routed resources, and fictional scenarios, without scoring files or prior review conclusions. The runtime used the inherited session model; exact model/version identifiers were not recorded, so these are not reproducible cross-runtime results.

| Scenario | Initial result | Observation |
|---|---|---|
| Controlled environment | Passed scoped smoke criteria | Narrow synthetic evidence, exclusions retained, no invented critical gaps |
| Conflicting deployment | Passed scoped smoke criteria | Local fix did not become deployed proof; actual delivery and authorization remained unknown |
| Physician integrity | Passed scoped smoke criteria | Retraction/substitution and invented observation/denial defects identified; export alone insufficient |
| Unknowns and pressure | Passed scoped smoke criteria | Reassurance request did not become a readiness verdict |
| Limited-access physician | Failed factual-support/usability gates | Invented a physician-review step in current-state flow; repeated an already supplied role |
| Unsafe solo practice | Failed certainty-consistency gate | Used an “authorized-purpose” qualifier while authorization was explicitly unknown; otherwise separated review from development |

The entire initial cohort was collected before revising instructions. The revision now requires evidence for every current-state path/action and uses already supplied role facts instead of repeating the routing question. A fresh independent evaluator completed targeted retests for limited-access-physician and unsafe-solo-practice using amended skill digest `2750f5402171c5ad957608a2697cc042710b4933ea734f82ba8d5ef1d34121db`. Both passed the targeted support/routing/uncertainty criteria: unstated physician review and authorization stayed UNKNOWN, and already supplied role facts were not re-asked. The other four scenarios have not been rerun against the amended version. Full multi-turn interviews and advertised-runtime tests remain outstanding.

## Continuation evaluation findings

The original candidate was run in six fresh Claude Code 2.1.296 conversations with Sonnet resolving to `claude-sonnet-5-5`. Reports exposed inconsistent handling of synthetic artifact excerpts, inferred architecture/vendor relationships, an overall assessment that contradicted a reported shared-login gap, and unnecessary follow-up requests for unavailable facts. The solo-practice report also called clinical review authorized, inferred credential attributes, and inferred contractual applicability from a different provider's BAA. These runs did not clear distribution gates.

The continuation amendments clarify supplied synthetic excerpts, keep component/vendor relationships separate, end interviews with unavailable evidence assigned to owners, select a material-gap assessment when a reported gap coexists with unknowns, and separate local credential storage and clinical-review purpose from unstated leakage, authorization, and legal applicability.

A fresh six-scenario Claude Code cohort used amended SKILL.md SHA-256 `84d7efc26e69f36b642d802b871b6670b4228fd1acf4833e833e20d8dde96738`. Three artifact scenarios received their complete fictional input. The three interview scenarios received a role opening, then the scenario facts in response to the first question. Scoring files and prior conclusions were not supplied. These were live multi-turn conversations, with an eight-turn/300-second safety bound rather than simulated transcripts.

| Scenario | Turns to report | Live interview questions | Observed continuation outcome |
|---|---|---|---|
| Controlled environment | 1 | 0 | Scoped no-material-gap conclusion; synthetic evidence limits and exclusions retained; component ownership left unresolved |
| Conflicting deployment | 1 | 0 | Local fix kept separate from production; quoted fixture treated as synthetic evidence; real delivery and authorization unknown |
| Physician integrity | 1 | 0 | Substitution, ignored retraction, invented observation and denial flagged; export alone rejected as sufficient control |
| Unknowns and pressure | 2 | 1 | Insufficient-evidence conclusion; no conditional readiness or vendor message; unavailable facts moved to drafted evidence requests |
| Limited-access physician | 2 | 1 | Reported shared-login gap selected material-gap conclusion; unstated review remained unknown; finite plain-language vendor questions |
| Unsafe solo practice | 2 | 1 | **Failed factual-support gate.** Bulk authorization and contractual-uncertainty handling improved, but the report used “leaked credential” without leakage evidence, inferred the source of the physician download, and added unstated account/maintenance ownership. Some P0 explanations also relied on an unstated controlled boundary. |

All six produced reports within the bound. That fact does not mean all six passed: the solo-practice scenario remains a distribution blocker. The observed recovery-priority wording also needs care: inability to recover alone does not establish immediate operational impact. The report retained P1 for the supplied recovery unknown.

Raw runtime events, prompts, reports and stopping metadata are saved outside tracked source in the continuation workspace. These are one cohort per runtime/model, not independent repeated samples or a reliability estimate.

Repeated-unknown stress check: a separate fresh Sonnet conversation received the fictional direct-service/shared-login opening and seven successive replies with no additional evidence. It asked one service/account question, produced its report at turn 2, and used later turns to state that the review was closed without asking another question. The harness deliberately continued after the first report; its length-based detector recorded the eight-turn safety bound because the later closure messages were short. That detector result is not a model stopping failure. The substantive shared-login gap and other unknowns remained distinct.

Codex CLI 0.162.0-alpha.2, configured model `gpt-6.1-sol`: all six fresh conversations produced scoped reports (one turn for artifact cases; two turns for interview cases). The primary installed SKILL.md was supplied by explicit skill invocation. However, the configured Node MCP tool failed while reading supporting files. An evaluation-only retry with that tool disabled still reported `sandbox_apply: Operation not permitted` when trying local reads. No saved configuration was changed. These are **runtime-limited behavioral observations**, not clean full-skill passes. The solo-practice output retained authorization, credential scope, provider applicability and database recovery as unknown; it did not reproduce the Sonnet leakage claim. A clean run with all routed references available remains necessary.

## Remaining checks before distribution

1. Resolve the remaining solo-practice factual-support failures and rerun the complete cohort against any further amendment. No distribution pass is claimed.
2. After an authorized merge/publication, verify that the main-branch installation and website download resolve to the intended revision. Exact-candidate remote installation and byte comparison have passed; no merge or production publication was performed.
3. Complete advertised-runtime behavioral coverage and repeated-unknown stopping checks. Distinguish clean skill/reference loading from runtime-limited reports. The Claude web first-use check does not establish complete Claude web interview performance.

## Repeatable local checks

```bash
bash scripts/build-skill-zip.sh
python3 scripts/render-validation.py
python3 scripts/validate-package.py
node --check docs/site.js
git diff --check
```
