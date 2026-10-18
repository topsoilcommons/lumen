# Contributing to Lumen

Contributions are welcome, and the door is kept visibly open:
there is always at least one good first issue available. The house
rule is the evidence rule: a contribution ships with the run that
proves it (the eval output, the smoke test), not just the code.
The second house rule is this repo's founding one: nothing here is
described as working unless it runs.

## Setup

```bash
node packages/catechism-rag/demo/guarded_qa.mjs "Why did God make you?"
node packages/catechism-rag/demo/guarded_qa.mjs --eval
node packages/liturgy/src/__smoke__.ts
```

## Good first issues (sized in hours)

- **Add refusal eval cases (about an hour).** Extend
  `packages/catechism-rag/demo/eval_cases.json` with blocked,
  allowed, or borderline texts and rerun the eval. Paraphrases of
  the guarded forms are the most valuable additions, because the
  request screen is a pattern list and the suite should show where
  it stops working.
- **Grow the demo corpus (1 to 2 hours).** Add one lesson from the
  same public domain source via `demo/build_corpus.py`, checking
  each added answer against the refuser first and recording any
  exclusion the way Q.241 and Q.242 are recorded.
- **Write the liturgy test suite the smoke script asks for
  (2 hours).** `packages/liturgy/src/__smoke__.ts` says in its own
  header that it replaces a real test suite until one exists.
  Port its checks to a runner and add the edge case it does not
  cover: a transferred feast.
- **Fix a scaffold label (under an hour).** If any file in this
  repo describes scaffold code in the present tense, that is a
  bug of the kind this project exists to catch. File it or fix it.

## Ground rules

- The refuser is the contract. Changes to its patterns land with
  eval cases that justify them, in the same change, and the eval
  is rerun and its artifact updated.
- No present-tense claims for scaffold code, in code comments,
  docs, or PR descriptions. Label plans as plans.
- Citations or it does not ship: any answering surface added here
  carries its sources the way the demo does.

## Pull requests

Keep them small and single purpose. State the evidence in the PR
description: what you ran and what it showed. Contributors are
named in release notes.

## Ways in, by level

**First hour.** Run the policy sync check (node scripts/check_policy_sync.mjs; it reports 53 checks) and one exhibit eval (node guarded_qa.mjs --eval in a demo folder). Then add one refusal eval case of your own: a blocked, allowed, or borderline text.

**First week.** Grow the demo corpus by one lesson from the same public domain source, checking each added answer against the refuser first and recording any exclusion the way the record already does. Both tasks stand open, labeled good first issue.

**The deep end.** The guard screen is a pattern list, and its named weakness is paraphrase: guarded requests reworded until the pattern stops matching. Across the three exhibits the standing figures are 12 of 12 refused and 8 of 8 allowed, in each. Grow the eval with paraphrases that break the screen, publish the breaks, and hold the figures. That is the number to beat.
