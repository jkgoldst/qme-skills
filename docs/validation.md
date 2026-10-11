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

## Ordered follow-up, October 10, 2026

The next requested sequence was to fix unsupported facts, rerun all six scenarios, evaluate Codex with full reference access, and then review merge readiness and published installation. Work stopped at a complete evaluation boundary when the user requested a handoff. No merge or production deployment occurred.

The amendments extend evidence support to every report section, separate established owners from recommended action owners, remove the sample architecture diagram, require complete evidence-backed path rows, preserve shared-login assessment consistency, distinguish broken test/production isolation from unknown credential controls, and make unknown-dependent risk explanations conditional. The technical checklist now requests credential storage and lifetime evidence rather than priming particular credential attributes. No additional skill was created.

Several complete intermediate Claude cohorts and two API/DNS-error retries informed these changes. Their reports are retained in the follow-up transcript archive. A completed report is not a passed evaluation. The final unchanged source set used SKILL.md SHA-256 `a13126d0292a9bdad8af8161c93298fd0c021fc7d8c242d1c7a712bc8bfe1d8c`; all five source-file hashes are in the follow-up results JSON.

Final Claude Code 2.1.296 cohort, Sonnet resolving to `claude-sonnet-5-5`: artifact inputs produced reports in one turn with no live questions; role-first interview inputs produced reports in two turns with one live question. Scoring expectations and prior conclusions were withheld.

| Scenario | Final Claude observation |
|---|---|
| Controlled environment | Scoped positive assessment with evidence limits and exclusions retained |
| Conflicting deployment | Source fix kept separate from deployed evidence; real delivery and unauthorized disclosure unknown |
| Physician integrity | Required failures identified, but the opening assumes the export gate would carry flawed content through unchanged; that downstream behavior is unstated |
| Unknowns and pressure | No readiness verdict or sent request; current ownership assertions nevertheless conflict with its UNKNOWN ownership statement |
| Limited-access physician | Shared-login gap and overall assessment agree; unstated physician review and purpose remain unknown; no infrastructure interrogation |
| Unsafe solo practice | Original leakage, credential-lifetime, download-source, and account-ownership errors did not recur. **Factual-support gate still failed:** it asserts three distinct vendor relationships and actual read/write behavior beyond the supplied facts |

These residual factual-support issues prevent a distribution pass. Narrow corrections improved behavior but did not demonstrate reliable factual restraint across all scenarios. The final reports and their failure locations should guide the next amendment; do not select an earlier successful sample as proof that the final candidate passes.

Codex CLI 0.162.0-alpha.2, configured `gpt-6.1-sol` with low reasoning: six fresh sessions produced scoped reports. The previous local-read sandbox failure was avoided through an evaluation-only stdio MCP tool restricted to existing files within each disposable installed skill. Its read logs and byte comparisons confirm the same five-file source set. The helper rejects paths outside the skill and exposes no mutation operation. This was a reference-access mechanism for evaluations, not a shipped tool or a change to saved Codex configuration.

The initial attempt could not initialize Codex state databases until filesystem access to its runtime directory was granted. In the next cohort, five cases read all applicable references; the solo case's resumed command did not expose its technical reference tool. A fresh solo retry passed the tool overrides directly at the resume subcommand, read all five files, and produced a report after two questions and a final unknown answer. The earlier limited run is retained, not treated as clean coverage.

| Scenario | Codex turns to report | Live questions | Applicable files read | Manual scoped result |
|---|---|---|---|---|
| Controlled environment | 1 | 0 | 5 | Passed scoped criteria |
| Conflicting deployment | 1 | 0 | 5 | Passed scoped criteria |
| Physician integrity | 1 | 0 | 5 | Passed scoped criteria |
| Unknowns and pressure | 2 | 1 | 4 | Passed scoped criteria |
| Limited-access physician | 2 | 1 | 4 | Passed scoped criteria |
| Unsafe solo practice, fresh retry | 3 | 2 | 5 | Passed scoped criteria |

No material factual-support or readiness error was found in those six Codex reports on manual review. This is one sample per scenario using scoped MCP access, not a reliability estimate or proof that the ordinary configured native file reader works. Unrelated plugin-icon warnings and a model-list refresh timeout appeared in stderr; the actual reports and required reference reads completed.

The latest ZIP matches the local source and passes structural validation. The signed-in Claude web account still has the earlier v2 upload described above, not this follow-up's latest source. Final-source web replacement and exact-revision remote installation remain unperformed. Earlier exact-revision installation results apply only to the earlier source sets explicitly named above.

## Resumed correction cohorts, October 10, 2026

The handoff was resumed in the existing candidate worktree. Three narrow amendments addressed component/vendor comparisons, configured connections versus completed operations, export requirements versus downstream behavior, established ownership versus proposed action owners, and permission-dependent risk statements. Each amendment was followed by all six fresh Claude scenarios and scoped Codex reference coverage. No scoring files or prior outcomes were supplied to either evaluator. Fictional inputs only were used.

Initial runtime attempts failed before evaluation: Claude reported not logged in and Codex could not initialize state databases. After runtime filesystem/network access was granted, fresh separate cohorts completed. Startup failures are retained as runtime errors, not behavioral scores. Claude remained authenticated according to its local auth status; saved configuration was not changed.

The completed cohorts use Claude Code Sonnet (`claude-sonnet-5-5`) and Codex CLI configured `gpt-6.1-sol`. Artifact cases received their complete scenario. Interview cases received a role opening, the scenario, and unknown answers as needed. The live bounds remain eight turns/300 seconds for Claude and six turns with 180-second command limits for Codex. Installed five-file snapshots and actual scoped MCP reference reads are recorded separately for each source set.

| Final Claude scenario | Manual scoped result |
|---|---|
| Controlled environment | Passed scoped criteria; components kept separate from unidentified vendors, narrow positive assessment and exclusions retained |
| Conflicting deployment | Failed factual support: F2 labels the finding “Identifiers in email bodies” despite unstated notification transport. Real delivery and disclosure remain unknown |
| Physician integrity | Passed scoped criteria; all four generation defects identified and intervening export handling remains unknown |
| Unknowns and pressure | Failed completion/usability: report declares the interview ended but repeats unavailable workflow question 1 as unanswered rather than leaving only an evidence task |
| Limited-access physician | Core routing/shared-login/uncertainty criteria satisfied; vendor-request wording still assumes a records-review purpose that was not established |
| Unsafe solo practice | Failed factual support: register R15 and the strong-controls section omit the supplied without-export condition and state an absolute restriction on AI signing/submission. Permission and maintenance corrections held |

The intermediate cohorts also completed all six Claude reports. Their observed residual errors informed subsequent amendments: unsupported component-to-provider mappings and renderer ownership in the first, and an unsupported full-PHI-access consequence plus contractor maintenance role in the second. These reports remain historical evidence, not selected as a passing final cohort.

Final Codex coverage completed all six cases. Manual review found no material factual-support or readiness error. Artifact cases finished in one turn, limited-access and pressure cases in two turns, and the solo case in three turns after a final unknown answer. Actual read logs show five applicable files for operator/artifact cases and four for the two nontechnical cases. All six disposable installations byte-match the final frozen five-file snapshot. The two intermediate Codex cohorts also completed all six cases with applicable reads and matching snapshots. These are scoped observations through the read-only MCP helper, not proof of the ordinary native file reader or a reliability estimate.

The final Claude source still fails distribution gates. Further instruction amendments produced improvement but did not establish consistent factual restraint. No web skill replacement, latest-head remote installation, merge-readiness approval, merge, main-branch installation, or production-site parity is claimed from these runs.

Final source-file hashes are recorded in the results JSON; SKILL.md SHA-256 is `4686491faf06c9c94263c00a940962edb0efd0eb497909d2d6f4758924c5f073`. Reference/template hashes distinguish the three cohorts even where SKILL.md did not change. The first Codex harness computed its status digest at completion from the repository; the separately recorded installed five-file hashes and frozen-snapshot parity are the source identity authority.

The evidence package is saved outside tracked source at `/Users/jkgoldst/Documents/Codex/2026-10-10/wh/outputs/qme-resume-results.json` and `qme-resume-transcripts.zip`. It includes text reports, statuses, actual reference-read logs, harnesses, fictional scenarios/expectations, and three frozen five-file snapshots. Raw runtime events, authentication files, and saved configuration files are excluded from the archive. Scope remains one sample per scenario per cohort, not a reliability estimate or native-reader verification.

## Additional continuation: cohorts 4 through 7

Four additional five-file source snapshots were evaluated using the same fictional scenarios, live-turn bounds, and separate runtime sessions. Changes preserve notification categories and export prerequisites, close unavailable interviews as evidence tasks, keep bucket versioning separate from draft history, preserve unknown request purposes, and centralize factual claims in an evidence register. The final amendment explicitly separates absent restore testing from absent recovery documentation and model routing from unknown payload content.

Claude cohorts 4 through 6 each completed all six reports but did not pass distribution gates. Cohort 4 generalized absent bucket versioning into absent original/draft versioning and invented a processing purpose. Cohort 5 expanded no restore test/incident-response runbook into no recovery runbook and upgraded a reported agreement to confirmed contract status. Cohort 6 retained the recovery-summary expansion despite an accurate evidence register. Complete Codex cohorts 4 through 6 passed manual scoped criteria; this remains scoped-reader evidence, not ordinary native-reader verification.

The seventh Claude cohort additionally upgrades described deployment/documentation artifacts to VERIFIED and states that a physician decided to ask before real-data use without that fact being supplied. The physician-integrity opening says the physician must catch defects unaided even though intervening safeguards remain UNKNOWN. These regressions independently prevent distribution. No successful earlier sample is substituted for a failing final-source result.

The instruction-only approach has not established sufficiently consistent factual restraint. The next implementation should validate claims before report assembly: extract supplied factual clauses and evidence levels into a structured register, use IDs for all factual report cells, and check summary claims against their exact source clauses. Unknown conditions and unsupported provider/owner mappings must remain explicit. This design remains to be implemented and validated; no executable claim validator is included in this candidate.

Full per-cohort completion, source hashes, installed parity, scoped-reference reads, and manual findings are retained in the local follow-up evidence bundle. Every cohort is a single sample per scenario, not a reliability estimate. The existing Claude web v2 has not been replaced, the latest candidate has not been installed from a published exact SHA, and PR #5 remains a draft with distribution and merge-readiness gates open.

## Remaining checks before distribution

1. Resolve the final Claude factual-support failures, then rerun the complete cohort against any further amendment. Repeat the scoped Codex checks if its source files change. No distribution pass is claimed.
2. Replace the earlier Claude web v2 with the stable candidate, verify first use, and verify exact-revision installation from the updated published PR candidate.
3. Review merge readiness only after validation gates clear. Merge/publication requires user direction. Then verify main-branch installation and the production website download resolve to the intended source. Nothing was merged or published during this follow-up.

## Repeatable local checks

```bash
bash scripts/build-skill-zip.sh
python3 scripts/render-validation.py
python3 scripts/validate-package.py
node --check docs/site.js
git diff --check
```
