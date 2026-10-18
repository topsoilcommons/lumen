# The 110 percent checklist: Lumen

Ascent alignment: Ascent Layer 6, Trust and meaning. Aligned October 15, 2026 (see "The need" in the README and NEEDS.md in the profile repo).
State as of October 18, 2026. Every line carries its evidence; a line without evidence does not count as done. This file is maintained by the evolution pass.

## 100 percent: completeness
- [x] Every file of the verified local publish tree present on GitHub, proven by tree diff at launch (October 14 to 15, 2026)
- [x] README accurate against the code, including the honesty pass: the demo is extractive question answering over a public domain corpus (Baltimore Catechism No. 2, Gutenberg 14552) executing the real refuser, and it is labeled as such
- [x] LICENSE present
- [x] COLLABORATE.md present
- [x] CONTRIBUTING.md present
- [x] CI workflow present (the refusal eval plus an assertion on the result counts, on every push)

## The extra 10 percent
- [x] CI green on GitHub runners (verified October 15, 2026)
- [x] Repo description and topics set (description states the verified refusal results)
- [x] Good first issues open: #1 add refusal eval cases, #2 grow the demo corpus by one lesson (both labeled good first issue, sized in hours)
- [x] Tagged release: v0.1.0, first verified baseline (published, marked Latest)
- [x] Live demo: https://topsoilcommons.github.io/lumen/ (render verified October 15, 2026)
- [x] Fresh baseline rerun October 15, 2026: node packages/catechism-rag/demo/guarded_qa.mjs --eval, 12 of 12 blocked, 8 of 8 allowed, 9 of 9 prompts as expected, exit 0

## Working agreements
- AGENTS.md in this repo governs how changes are made and proven here.
- Documented tradeoff: verbatim quotation of guarded formulas inside teaching text is blocked by the refuser; corpus questions 241 to 242 are excluded and the exclusion is recorded in the project.
- [x] Guardrail policy layer published in-repo (October 16, 2026, scoped as in-repo only, no external publication): `packages/guardrail-policy/policy.json` (v1.0.0) and its README, extracted from `packages/catechism-rag/src/refuser.ts` and the catechism demo request screen, referencing (not duplicating) `packages/catechism-rag/demo/eval_cases.json`. Evidence: `node scripts/check_policy_sync.mjs` exits 0 (53 checks) and is wired into CI; refusal evals rerun the same day match baseline (catechism 12 of 12, 8 of 8, 13 of 13; Proverbs 12 of 12, 8 of 8, 10 of 10; Tao Te Ching 12 of 12, 8 of 8, 10 of 10).
