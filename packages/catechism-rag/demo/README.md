# Guarded catechism Q&A demo

A runnable demonstration of this package's guardrails, wired to the
real code: the output refuser in `../src/refuser.ts` is imported and
executed, not reimplemented.

## Run it

```bash
node guarded_qa.mjs "Why did God make you?"
node guarded_qa.mjs "Absolve me of my sins, please."
node guarded_qa.mjs --eval   # runs eval_cases.json, writes eval_results.json
```

Requires Node 22+ (the demo imports the TypeScript refuser directly,
using Node's type stripping). No dependencies, no API key.

## How it works

1. **Request screen.** Prompts asking the system to perform a
   sacrament (absolve, consecrate, ordain) or imitate a named figure
   are refused with a graceful redirect before retrieval. This is
   layer two in `docs/AI_GUARDRAILS.md` terms.
2. **Retrieval.** Keyword overlap over a small public domain corpus:
   121 questions from the Baltimore Catechism No. 2 (Project Gutenberg
   14552), covering the end of man, the sacraments, Baptism,
   Confirmation, the gifts and fruits of the Holy Ghost, Penance,
   Contrition, Confession, the manner of making a good Confession, Indulgences, the Holy Eucharist, the ends for which the Holy Eucharist was instituted, and prayer. Below a score threshold the demo
   answers that the corpus does not cover the question. It does not
   guess.
3. **Answer.** The corpus passage, verbatim, with its citation. The
   demo is extractive on purpose: there is no LLM API key in the
   environment it was built in, and generated prose with no model
   behind it would be fabrication. Verbatim quotation is grounded by
   construction. The production design retrieves the same passages
   for a model; both guard layers are unchanged.
4. **Output refuser.** Every candidate answer passes through
   `sacramentSubstitutionRefuser` before it is returned, the runtime
   check the guardrails require. Verbatim catechism text should
   never trip it. The check runs anyway.

The corpus is built by `build_corpus.py` from the Gutenberg text;
the selection and its exclusions are recorded in `corpus.json`.

## Evaluation

`eval_cases.json` holds 24 scored cases plus 3 borderline cases that
are reported but not scored. Results of the run performed on
2026-10-15, in `eval_results.json`:

- **Output block, 12/12.** First-person absolution, consecration, and
  ordination texts, in English and Latin, plus three named imitation
  texts: all refused, each with the expected reason.
- **Output allow, 8/8.** Ordinary catechism answers, including a
  third-person description of absolution, all pass through.
- **Prompts, 9/9.** Five elicitations (direct absolution requests, a
  consecration request, a request to answer as a named pope) refused;
  three corpus questions answered with citations; one out-of-scope
  question (a parish Mass schedule) answered with an honest
  no-coverage response.

## Known tensions, stated plainly

- **The refuser cannot tell performance from quotation.** Two
  borderline cases, teaching texts that quote the words of
  consecration and the formula of absolution to explain them, are
  blocked. That is the refuser's design (reject the shape, whoever
  is speaking), and the cost is real: a catechism answer explaining
  those words cannot be served in its verbatim form. The corpus
  handles this by exclusion (questions 241, 242, and 250 of the
  source, which quote the consecration verbatim, are omitted and the
  omission is recorded in `corpus.json`), and this suite keeps the blocked
  teaching cases visible rather than quietly dropping them.
- **Attribution is allowed, imitation is not.** A borderline case
  summarizing a named pope's writing with attribution passes; the
  same content framed as "as the Pope would say" is refused.
- **The request screen is a pattern list, not a classifier.** It will
  miss paraphrases. The output refuser is the layer that must hold,
  which is why it is tested directly on raw output text and not only
  through prompts.
