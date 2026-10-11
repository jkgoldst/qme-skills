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
- Claude web: navigation reached the sign-in page. Account-specific ZIP upload/enablement and first use remain unverified because no signed-in browser session was available. No account was changed.

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

## Remaining checks before distribution

1. In a signed-in Claude account, upload this exact ZIP, enable it, and ask the published opening request. Verify actual skill loading and role routing. Respect organization restrictions.
2. After the candidate is published, repeat the remote GitHub installer commands against the published revision. Current candidate install/invocation checks used the local revised source.
3. Run full multi-turn scenarios in fresh sessions, including repeated “I don't know” answers. Record model/runtime/version, source revision, artifacts, misses, false positives, unsupported certainty, question count, and stopping behavior. The bounded reports above do not establish interactive stopping performance.

## Repeatable local checks

```bash
bash scripts/build-skill-zip.sh
python3 scripts/render-validation.py
python3 scripts/validate-package.py
node --check docs/site.js
git diff --check
```
