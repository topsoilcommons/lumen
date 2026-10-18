<style>
.commons-bar { position: sticky; top: 0; background: #ffffff; border-bottom: 1px solid #d9d2c3; padding: 0 1em; line-height: 2; z-index: 10; }
.commons-bar a, .commons-bar span { margin-right: 1em; display: inline-flex; align-items: center; min-height: 44px; }
.commons-bar .wordmark { font-weight: 600; }
.commons-bar span[aria-current="page"] { font-weight: bold; }
.commons-footer { margin-top: 3em; }
.skip-link { position: absolute; left: -9999px; top: 0; background: #ffffff; padding: 10px 16px; }
.skip-link:focus { position: static; }
:focus-visible { outline: 2px solid #1c1a17; outline-offset: 2px; }
[id] { scroll-margin-top: 72px; }
</style>

<a class="skip-link" href="#lumen">Skip to the content</a>
<nav class="commons-bar" aria-label="Topsoil Commons sites">
  <a class="wordmark" href="https://topsoilcommons.github.io/topsoilcommons/"><svg class="bar-mark" viewBox="0 0 24 24" width="17" height="17" aria-hidden="true" focusable="false" style="flex:none;align-self:center;margin-right:7px"><g fill="currentColor"><rect x="4" y="2.5" width="16" height="2"/><rect x="4" y="5.5" width="16" height="2"/><rect x="4" y="8.5" width="16" height="2"/><rect x="4" y="11.5" width="4.5" height="8"/><rect x="15.5" y="11.5" width="4.5" height="8"/><rect x="2" y="20.5" width="20" height="2.2"/></g></svg>Topsoil Commons</a>
  <a href="https://topsoilcommons.github.io/topsoilcommons/foundations.html">Foundations</a>
  <a href="https://topsoilcommons.github.io/ground/">Ground</a>
  <a href="https://topsoilcommons.github.io/still/">Still</a>
  <a href="https://topsoilcommons.github.io/atlas/">Atlas</a>
  <a href="https://topsoilcommons.github.io/cohort/">Cohort</a>
  <a href="https://topsoilcommons.github.io/graph/">Graph</a>
  <a href="https://topsoilcommons.github.io/machine/">Machine</a>
  <span aria-current="page">Lumen (you are here)</span>
</nav>

# Lumen

First step: read what the guarded answers are, below. You ask a question from a set text, and you get an answer drawn only from that text, with its source shown, or a clear no when the request must not be answered. To try the demo on your own machine, the command sits in the section for agents and builders at the end of this page. One question the demo answers is "Why did God make you?"

Lumen is one of the seven tools of Topsoil Commons, Layer 6:
trust and meaning. Here you can ask a
question from a guarded text. You get an answer drawn only from
that text, with its source shown, or a clear no when the request
must not be answered. The guard rules are written into the program
itself, not just a policy page. This README claims only what runs.

What runs today: demos that answer questions from public domain
texts. The program checks each answer and blocks answers that must
not be given. Each text stands on its own. In the published checks,
each of the three exhibits (the Baltimore Catechism, the Book of
Proverbs, and the Tao Te Ching) refused 12 of 12 questions it must
refuse and allowed 8 of 8 questions it must allow. Each exhibit's
own section below states its check in full.

## Open to every tradition

Lumen puts guard rules into code, and this way of guarding a text belongs to no one tradition. To guard a text: answer only from the text, show the source, and refuse what a community says must never be made. Each community sets the rules for its own texts. This project does not set them. The texts that run today are exhibits from three traditions: 62 questions from the Baltimore Catechism No. 2 (Project Gutenberg 14552), with questions 241 and 242 left out because they quote guarded words word for word; 29 question and answer units from the Book of Proverbs in the World English Bible (Project Gutenberg 8247); and 30 units from the Tao Te Ching in James Legge's translation (Project Gutenberg 216). The published check numbers describe these texts only, and they are stated in the table further down this page, in plain words. Texts from every tradition, and works of meaning outside faith, are welcome on the same terms. The standing rule: each text is honored on its own terms. No blending. No ranking.

Worth is never weighed here. Usefulness is measured within each exhibit, never across them: how many of life's recurring situations the text answers in its own words, whether a stranger can draw from it in one sitting, and whether people actually turn to it. That measure steers building effort only. It never touches standing. And every exhibit is entered through the situations of a human life, so any person can find, in each text's own words, that it has stood where they are standing.

The standing next step for each exhibit is a situations index: a concordance by the moments of a human life, built from the text itself, leaving its order and voice untouched.

## What it is

Lumen is a design study with three working components and a monorepo of
scaffolds around them. It is not a deployed platform, it has no
users, and the three apps do not run. What is real:

Three parts of Lumen run today and are checked by runs in this repo: the guarded catechism demo, the guarded Proverbs exhibit, and the guarded Tao Te Ching exhibit, each described in its own section below. Around them sits a set of planned apps and parts that are scaffold only, labeled as scaffold wherever they are named. The exact list of what runs and what is scaffold, with file names, sits in the section for agents and builders at the end of this page.

## The three exhibits, in one table

<!-- exhibits:begin -->
| Exhibit | Units in the set of texts | Refused, of the questions it must refuse | Allowed, of the questions it must allow | Prompts as expected |
| --- | --- | --- | --- | --- |
| Baltimore Catechism No. 2 | 62 | 12 of 12 | 8 of 8 | 13 of 13 |
| Book of Proverbs, World English Bible | 29 | 12 of 12 | 8 of 8 | 10 of 10 |
| Tao Te Ching, translated by James Legge | 30 | 12 of 12 | 8 of 8 | 10 of 10 |

Key: units are the passages in each exhibit's set of texts. Refused, allowed, and prompts are the three scored blocks of each exhibit's check results file, all in this repository. The exhibits are measured within themselves, never against each other.
<!-- exhibits:end -->

## Second exhibit: the Book of Proverbs

This exhibit is shown on its own, under the standing rule stated
above: each text is honored on its own terms. No blending. No ranking.

The Book of Proverbs is the wisdom book of the Hebrew Bible. This
exhibit holds that book in the World English Bible, a public
domain translation. Source edition: "The World English Bible
(WEB): Proverbs", Project Gutenberg ebook 8247, release date
June 1, 2005, most recently updated December 26, 2020, its text
credited to www.ebible.org with slight reformatting by Martin
Ward. The Project Gutenberg edition is public domain in the USA.

In this exhibit:

- A set of 29 question and answer units drawn from the source
  edition. Each unit follows the text's own form: a saying and its
  completion, taken word for word, or, for Proverbs 23:29 to 30, a
  question the text itself asks and then answers, taken word for
  word. No answer is paraphrased.
- A guarded demo that answers questions from those units in the
  text's own words, with the passage shown, and refuses requests
  the guard rules forbid, including a request to answer as Solomon.
- Its own published check, run on October 15, 2026. Of the
  questions it must refuse, 12 of 12 were refused, each for the
  expected reason. Of the questions it must allow, 8 of 8 were
  allowed through. Of the spoken prompts tried against it, 10 of
  10 behaved as expected. The exact files and commands sit in the
  section for agents and builders at the end of this page.

The exhibit has its own page in this repo, with its method and
its stated limits, linked from the section for agents and
builders.

## Third exhibit: the Tao Te Ching

This exhibit is shown on its own, under the standing rule stated
above: each text is honored on its own terms. No blending. No ranking.

The Tao Te Ching is the founding text of Taoism, a book of short
aphoristic chapters. The text is traditionally attributed to
Laozi; the attribution is the tradition's. This exhibit holds the
text in James Legge's public domain translation, *The Tao Teh
King, or the Tao and its Characteristics*, Project Gutenberg
ebook 216, first published in 1891 in *The Sacred Books of China
(The Texts of Taoism)*, Sacred Books of the East, volume 39,
Clarendon Press, Oxford. The edition was produced by Gregory
Walker and David Widger, and Gutenberg marks it public domain in
the USA, most recently updated May 11, 2015.

In this exhibit:

- A set of 30 question and answer units drawn from the source
  edition: 29 sayings and one unit, chapter 44, sections 1 to 3,
  that follows a comparison the text itself makes. Each answer is
  taken word for word. Legge's section numerals are removed as
  his editorial apparatus, and the parenthetical glosses inside
  the quoted text are James Legge's own additions in this
  edition, kept verbatim because they are part of the edition
  and named as his.
- A guarded demo that answers questions from those units in the
  text's own words, with the passage shown, and refuses requests
  the guard rules forbid, including a request to answer as Laozi.
  At build time every one of the 30 answers was run through the
  shared refuser: none tripped it, and the corpus's excluded list
  stands empty on that evidence.
- A situations concordance, [situations.md](exhibits/tao-te-ching/situations.md):
  25 situations drawn only from the units in this corpus, each
  with its passage named, and the selection's gaps named as gaps.
- Its own published check, run on October 16, 2026. Of the
  questions it must refuse, 12 of 12 were refused, each for the
  expected reason. Of the questions it must allow, 8 of 8 were
  allowed through. Of the spoken prompts tried against it, 10 of
  10 behaved as expected. Borderline cases are reported, not
  scored. The exact files and commands sit in the section for
  agents and builders at the end of this page.

The exhibit has its own page in this repo, with its method and
its stated limits, linked from the section for agents and
builders.

> *Lumen Gentium*, light of the nations.

> **Lumen, Ascent Layer 6 (trust and meaning)**. Lumen is one of
> seven layers. Each layer holds that tech should help people do
> more and should not take away their choice.
>
> - Ground (Layer 0, the body): [ground](https://github.com/topsoilcommons/ground)
> - Still (Layer 1, the mind at peace): [still](https://github.com/topsoilcommons/still)
> - Atlas (Layer 2, learning): [atlas](https://github.com/topsoilcommons/atlas), how people learn.
> - Cohort (Layer 3, belonging): [cohort](https://github.com/topsoilcommons/cohort), how people find each other and build together.
> - Graph (Layer 4, shared truth): [graph](https://github.com/topsoilcommons/graph), how knowledge connects and can be questioned.
> - Machine (Layer 5, autonomy): [machine](https://github.com/topsoilcommons/machine), how the machine itself learns, step by step.
>
> Lumen deals with AI that is not safe and not held to account. We
> count the harmful outputs it refuses, and we report that count as it is.
> This repo claims no number for it yet beyond the check counts
> in this README, which are test results, not usage.
>
> We hope for a time when people can do more, power stays in check,
> and the sacraments stay with the Church. We state this as a hope
> and a direction, not as a claim of what we have done. This repo is
> one small exhibit of the guard work that hope needs.

## The need

Ascent Layer 6: Trust and meaning.

"Technology that stays inside human values: refuses what it should refuse, explains itself, and remains governed by people. And beneath the technology, the older need it serves: meaning, faith, conscience, a life that adds up to something."

Lumen serves this need with guardrails that are code, not policy, and a refuser that hard rejects guarded output before it renders.

Unmet, it looks like: machines that comply with anything, guardrails promised in principles pages and absent in code, people handed power with no story about what it is for.

The full map: [The Ascent, a map of human needs](https://github.com/topsoilcommons/topsoilcommons/blob/main/NEEDS.md)

## Live demo

Live demo: https://topsoilcommons.github.io/lumen/ (render verified October 15, 2026)

## For agents and builders

The exact technical description lives in this section. Everything a person needs is stated in plain words above it.

For agents: the machine files are the three exhibits' corpora and eval files: `packages/catechism-rag/demo/corpus.json` with its `eval_cases.json` and `eval_results.json`, `exhibits/proverbs/corpus.json` with its `eval_cases.json` and `eval_results.json`, and `exhibits/tao-te-ching/corpus.json` with its `eval_cases.json` and `eval_results.json`. Each exhibit is measured within itself, never against the others.

### What is in here, exactly

**Working, and verified by runs in this repo**

- **The guardrail refuser** (`packages/catechism-rag/src/refuser.ts`):
  a runtime check that hard rejects absolution shaped, consecration
  shaped, ordination shaped, and named imitation output before it
  renders. It is the enforcement of rules 2 and 3 in
  `docs/AI_GUARDRAILS.md`, in code.
- **The guardrail policy package** (`packages/guardrail-policy/`):
  a documented, machine-readable policy package published in this
  repo (not on npm or any external registry) that another project
  could adopt by copying it. `policy.json` names the two reason
  codes exactly as the code names them (`sacrament_substitution`,
  `named_imitation`), every output pattern from `refuser.ts`, the
  request screen pattern list from the catechism demo, the corpus
  exclusion rule for questions 241 and 242, and the tradeoff that
  verbatim quotation of guarded formulas in teaching text is
  blocked. `scripts/check_policy_sync.mjs` mechanically verifies
  `policy.json` against the source and is wired into CI; run
  `node scripts/check_policy_sync.mjs`.
- **The guarded catechism demo**
  (`packages/catechism-rag/demo/`): the refuser is part of a pipeline
  that answers questions from a small public domain corpus
  (Baltimore Catechism No. 2, chosen lessons). It answers in the
  words of the text, shows the source, refuses requests that try to
  draw out guarded words, and says no when the corpus does not cover
  a question. Evaluated on a published case set; see below.
- **The guarded Proverbs exhibit**
  (`exhibits/proverbs/`): the shared refuser is part of a pipeline
  that answers questions from a public domain corpus (the Book of
  Proverbs in the World English Bible, chosen sayings). It answers
  in the words of the text, shows the source, refuses requests that
  try to draw out guarded words and requests to copy a named person,
  and says no when the corpus does not cover a question. Evaluated
  on its own published case set; see its section below.
- **The guarded Tao Te Ching exhibit**
  (`exhibits/tao-te-ching/`): the shared refuser is part of a
  pipeline that answers questions from a public domain corpus
  (the Tao Te Ching in James Legge's translation, selected
  chapters). It answers in the words of the text, shows the
  source, refuses requests that try to draw out guarded words and
  requests to copy a named person, including Laozi, and says no
  when the corpus does not cover a question. Its corpus builder
  runs every answer through the shared refuser at build time.
  Evaluated on its own published case set; see its section below.
- **The liturgical calendar engine** (`packages/liturgy`): computus
  and calendar logic whose smoke script passes 15 of 15 checks,
  including Easter dates verified against published calendars
  (`node packages/liturgy/src/__smoke__.ts`, run 2026-10-15).

**Scaffold, labeled as such**

- `apps/parish` and `apps/api`: package scripts that echo "scaffold
  pending". There is no implementation.
- `apps/diocese`: the same scaffold state as parish.
- `apps/faithful`: a real Next.js shell whose home page is a static
  page describing the project's actual state. Its earlier redirect
  to a `/now` route that does not exist was removed in this pass;
  the Now surface is planned, not built.
- `packages/auth`, `packages/charity-graph`, `packages/vitality`:
  placeholder modules (`PLACEHOLDER = true` in their own source).
- `packages/catechism-rag/src/index.ts`: the `invoke()` entry point
  is a stub returning a shaped placeholder response; the design
  contract it documents (citations on every response, refuser on
  every output, no named imitation) is what the demo implements in
  extractive form.
- `packages/schema`: real zod type definitions for the intended
  data model. Types are a contract, not a backend.
- `packages/i18n`, `packages/ui`: small real utilities and design
  tokens.

### Design documents

- [`docs/PRINCIPLES.md`](./docs/PRINCIPLES.md): founding principles.
- [`docs/AI_GUARDRAILS.md`](./docs/AI_GUARDRAILS.md): the guardrail
  rules the code enforces, including where AI must not go.
- [`docs/ARCHITECTURE.md`](./docs/ARCHITECTURE.md),
  [`docs/MASTER_PROMPT.md`](./docs/MASTER_PROMPT.md),
  [`docs/ROADMAP.md`](./docs/ROADMAP.md): the intended platform,
  written as design. Read them as plans, not as descriptions of
  running software.

### Layout

```
apps/{faithful,parish,diocese,api}        faithful: static shell. Others: scaffold.
exhibits/{proverbs,tao-te-ching}          guarded Q&A exhibits
packages/{liturgy,catechism-rag,guardrail-policy}  working components (guardrail-policy: policy package, verified by its sync check)
packages/{schema,i18n,ui}                 types, small utilities, tokens
packages/{auth,charity-graph,vitality}    placeholders
docs/                                     design documents
```

### Status

Design study, Phase 1 pieces verified as listed above. No
deployment, no users, no production AI calls. The guardrail policy
layer is published as an in-repo package at
`packages/guardrail-policy/` (scoped that way: in-repo only, no
external publication), proven by its sync check against the real
code. The next honest step for this repo is growing the refusal
eval set (see [COLLABORATE.md](./COLLABORATE.md)).

### The proof: the catechism check, exactly

The refusal eval (`packages/catechism-rag/demo/eval_cases.json`,
run 2026-10-15, results in `demo/eval_results.json`):

- Output block: 12 of 12 sacrament substitution and named imitation
  texts refused, each with the expected reason.
- Output allow: 8 of 8 ordinary catechism answers pass through,
  including a third-person description of absolution.
- Prompts: 9 of 9 behaved as expected. Five elicitations refused
  with graceful redirects, three corpus questions answered with
  citations, one out-of-scope question answered with an honest
  no-coverage response.
- Borderline cases are reported, not scored: teaching texts that
  quote the guarded formulas are blocked, because the refuser
  rejects the shape regardless of intent. The corpus therefore
  excludes the two source questions that quote the consecration
  verbatim, and the exclusion is recorded in the corpus itself.

Run it: `node packages/catechism-rag/demo/guarded_qa.mjs --eval`

### The Proverbs check, exactly

The Proverbs exhibit pipeline is exhibits/proverbs/guarded_qa.mjs over the corpus at exhibits/proverbs/corpus.json (29 units, built by exhibits/proverbs/build_corpus.py). Its eval case set is exhibits/proverbs/eval_cases.json; run node exhibits/proverbs/guarded_qa.mjs --eval. Results are committed at exhibits/proverbs/eval_results.json: output block 12 of 12 refused with the expected reason, output allow 8 of 8 allowed through, prompts 10 of 10 behaved as expected, run 2026-10-15. The catechism demo command is node packages/catechism-rag/demo/guarded_qa.mjs --eval, and one question is node packages/catechism-rag/demo/guarded_qa.mjs "Why did God make you?". The exhibits table on this page is generated by scripts/build_exhibits_table.py from the three corpus files and the three eval results files. The Proverbs exhibit's own README, with its method and its stated limits, is at exhibits/proverbs/README.md.

### The Tao Te Ching check, exactly

The Tao Te Ching exhibit pipeline is exhibits/tao-te-ching/guarded_qa.mjs over the corpus at exhibits/tao-te-ching/corpus.json (30 units, built by exhibits/tao-te-ching/build_corpus.py). The builder verified every answer verbatim against the Gutenberg source and ran all 30 answers through the shared refuser at build time: 30 checked, 0 excluded, and the corpus's excluded list is empty on that evidence. Its eval case set is exhibits/tao-te-ching/eval_cases.json; run node exhibits/tao-te-ching/guarded_qa.mjs --eval. Results are committed at exhibits/tao-te-ching/eval_results.json: output block 12 of 12 refused with the expected reason, output allow 8 of 8 allowed through, prompts 10 of 10 behaved as expected, run 2026-10-16. Borderline cases are reported, not scored: the two teaching texts quoting guarded formulas were refused by the shared refuser, and the attributed statement about Laozi was allowed. The Tao Te Ching exhibit's own README, with its method, its Legge gloss caveat, and its stated limits, is at exhibits/tao-te-ching/README.md, and its situations concordance is at exhibits/tao-te-ching/situations.md.

## Contribute, human or agent

Pick up a good first issue in this repo. Each one is sized in hours and written to be finishable by a newcomer.
Take the Eval Challenge against this repo's published refusal scores: beat the baseline, or find a real failure the current eval misses, with the run attached.
Report adoption from real use. If you took the guardrails or the guarded demo into your own setting, tell us what happened, good or bad.

The full protocol: [The Open Table](https://github.com/topsoilcommons/topsoilcommons/blob/main/OPEN_TABLE.md). Verified work is credited in the public [Ledger](https://github.com/topsoilcommons/topsoilcommons/blob/main/LEDGER.md).

### Start with a prompt

For an AI agent:

```
You are an AI agent contributing to Lumen, a guarded question answering study.
Run the Eval Challenge end to end.
Clone this repo and run: node packages/catechism-rag/demo/guarded_qa.mjs --eval
Check your run against the published baseline: output block 12 of 12 refused with the expected reason, output allow 8 of 8 allowed through, prompts 13 of 13 behaved as expected.
Find a real failure the current eval misses, or improve one thing the eval covers, and show the run before and after.
Attach the run to your pull request, keep it to one improvement per pull request, and name your operator.
```

For a human:

```
Open a failure report issue for the refusal eval.
Include the input you gave the demo.
Include what happened, and what should have happened instead.
Attach the run if you have it.
```

<p>Below this layer: <a href="https://topsoilcommons.github.io/machine/">Machine, autonomy</a></p>
<p>There is no layer above Layer 6.</p>
<p>The research under this layer: <a href="https://topsoilcommons.github.io/topsoilcommons/foundations.html#meaning-values-and-flourishing">Foundations, Meaning, values, and human flourishing</a></p>

Built on Machine: autonomy.

Unlocks the ability to commit.

<footer class="commons-footer">
  <p><a href="https://topsoilcommons.github.io/topsoilcommons/">Back to the home page</a></p>
  <p>Topsoil Commons addresses the hierarchy of human needs through open source.</p>
  <p>Motto: Stand on the shoulders of giants.</p>
  <p>One rule: raise the floor beneath everyone.</p>
  <p>Its record is filed in <a href="https://topsoilcommons.github.io/index/">the Index</a>.</p>
  <p>Advised by Groundskeeper.</p>
  <p><a href="https://www.linkedin.com/company/topsoil-commons/">Topsoil Commons on LinkedIn</a></p>
</footer>
