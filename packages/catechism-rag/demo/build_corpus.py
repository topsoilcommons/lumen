#!/usr/bin/env python3
"""
Build demo/corpus.json from the Baltimore Catechism No. 2.

Source: "A Catechism of Christian Doctrine, No. 2" (the Baltimore
Catechism), public domain, Project Gutenberg ebook 14552:
https://www.gutenberg.org/cache/epub/14552/pg14552.txt

The corpus is a deliberately small selection of lessons (the end of
man, the sacraments in general, Baptism, Confirmation, the gifts and
fruits of the Holy Ghost, Penance, Contrition, Indulgences, the
Holy Eucharist, the ends for which the Holy Eucharist was
instituted, prayer), 121 questions in total.

Three questions are excluded on purpose, and the exclusion is part
of the design record: Q. 241, Q. 242, and Q. 250 quote the words of
consecration verbatim ("This is My body; this is My blood"). The
package's output refuser (src/refuser.ts) hard rejects that shape
before rendering, by design, so a verbatim answer to those three
questions could never be served. Rather than weaken the refuser,
the demo corpus omits them. See demo/README.md, "Known tensions".

Lesson Fifteenth, On Confirmation (Q. 166 to Q. 175), was added on
2026-10-17. Every one of its ten answers was checked against the
output refuser before it was added, in the same way as the rest of
the corpus: none tripped it, so this lesson has no exclusions. In
particular Q. 170, which quotes the words the bishop says in
anointing, was checked and returned no refusal; its answer quotes
the Confirmation form, not the words of absolution, consecration,
or ordination that the refuser rejects by shape.

Lesson Sixteenth, On the Gifts and Fruits of the Holy Ghost
(Q. 176 to Q. 186), was added on 2026-10-18. Every one of its eleven
answers was checked against the output refuser before it was added,
in the same way as the rest of the corpus: none tripped it, so this
lesson has no exclusions.

Lesson Seventeenth, On the Sacrament of Penance (Q. 187 to Q. 194),
was completed on 2026-10-18. Q. 187 to Q. 190 were already in the
corpus as a partial selection from this lesson; Q. 191 to Q. 194
were added in this pass, completing the lesson. Every one of the
four new answers was checked against the output refuser before it
was added, in the same way as the rest of the corpus: none tripped
it, so this lesson has no exclusions.

Lesson Eighteenth, On Contrition (Q. 195 to Q. 207), was added on
2026-10-19. Every one of its thirteen answers was checked against
the output refuser before it was added, in the same way as the rest
of the corpus: none tripped it, so this lesson has no exclusions.

Lesson Nineteenth, On Confession (Q. 208 to Q. 223), was added on
2026-10-19 (evening). Every one of its sixteen answers was checked
against the output refuser before it was added, in the same way as
the rest of the corpus: none tripped it, so this lesson has no
exclusions.

Lesson Twentieth, On the Manner of Making a Good Confession
(Q. 224 to Q. 230), was added on 2026-10-20. Every one of its seven
answers was checked against the output refuser before it was added,
in the same way as the rest of the corpus: none tripped it, so this
lesson has no exclusions.

Lesson Twenty-First, On Indulgences (Q. 231 to Q. 237), was added
on 2026-10-20. Every one of its seven answers was checked against
the output refuser before it was added, in the same way as the rest
of the corpus: none tripped it, so this lesson has no exclusions.

Lesson Twenty-Second, On the Holy Eucharist (Q. 238 to Q. 250),
was completed on 2026-10-21. Q. 238 to Q. 240 and Q. 243 to Q. 248
were already in the corpus as a partial selection from this
lesson, and Q. 241 and Q. 242 were already excluded (see above).
The two remaining answers were checked against the output refuser
before adding, in the same way as the rest of the corpus: Q. 249
did not trip it and was added; Q. 250 tripped it
(sacrament_substitution, because its answer quotes the words of
consecration verbatim), so Q. 250 is excluded and the exclusion is
recorded in the corpus below, in the same way as Q. 241 and
Q. 242. All thirteen lesson answers, Q. 238 to Q. 250, were
checked: ten did not trip the refuser and three (Q. 241, Q. 242,
Q. 250) did, all three excluded.

Lesson Twenty-Third, On the Ends for Which the Holy Eucharist
Was Instituted (Q. 251 to Q. 261), was added on 2026-10-21.
Every one of its eleven answers was checked against the output
refuser before it was added, in the same way as the rest of the
corpus: none tripped it, so this lesson has no exclusions.

Usage: python build_corpus.py <path-to-pg14552.txt> [out.json]
"""

import json
import re
import sys
from pathlib import Path

SELECTED = (
    list(range(1, 12))          # Lesson First: the end of man
    + list(range(136, 142))     # the sacraments in general
    + list(range(152, 158))     # Baptism
    + list(range(166, 176))     # Confirmation
    + list(range(176, 187))     # the gifts and fruits of the Holy Ghost
    + list(range(187, 195))     # Penance
    + list(range(195, 208))     # Contrition
    + list(range(208, 224))     # Confession
    + list(range(224, 231))     # the manner of making a good Confession
    + list(range(231, 238))     # Indulgences
    + [238, 239, 240]           # the Holy Eucharist (241, 242 excluded, see above)
    + list(range(243, 250))     # (250 excluded, see above)
    + list(range(251, 262))     # the ends for which the Holy Eucharist was instituted
    + list(range(303, 308))     # prayer
)

LESSONS = [
    (1, 11, "On the End of Man"),
    (136, 141, "On the Sacraments in General"),
    (152, 157, "On Baptism"),
    (166, 175, "On Confirmation"),
    (176, 186, "On the Gifts and Fruits of the Holy Ghost"),
    (187, 194, "On the Sacrament of Penance"),
    (195, 207, "On Contrition"),
    (208, 223, "On Confession"),
    (224, 230, "On the Manner of Making a Good Confession"),
    (231, 237, "On Indulgences"),
    (238, 250, "On the Holy Eucharist"),
    (251, 261, "On the Ends for Which the Holy Eucharist Was Instituted"),
    (303, 307, "On Prayer"),
]


def lesson_for(number):
    for lo, hi, name in LESSONS:
        if lo <= number <= hi:
            return name
    return ""


def main():
    raw = Path(sys.argv[1]).read_text(encoding="utf-8")
    start = raw.index("LESSON FIRST")
    body = raw[start:]
    # The lookahead also stops at a LESSON heading, so the last
    # question of a complete lesson (Q. 175 here) does not swallow
    # the next lesson's heading into its answer.
    pattern = re.compile(r"(\d+)\.\s+Q\.\s+(.*?)\nA\.\s+(.*?)(?=\n\d+\.\s+Q\.|\nLESSON\s|\Z)",
                         re.DOTALL)
    passages = []
    for match in pattern.finditer(body):
        number = int(match.group(1))
        if number not in SELECTED:
            continue
        question = " ".join(match.group(2).split())
        answer = " ".join(match.group(3).split())
        # Stop the last answer of the book from swallowing trailing matter
        answer = answer.split("*** END OF THE PROJECT GUTENBERG")[0].strip()
        passages.append({
            "id": f"BC2 Q.{number}",
            "question_number": number,
            "lesson": lesson_for(number),
            "question": question,
            "answer": answer,
            "source": "Baltimore Catechism No. 2 (Project Gutenberg 14552)",
        })
    passages.sort(key=lambda p: p["question_number"])
    out = {
        "corpus": "Baltimore Catechism No. 2, selected lessons (public domain)",
        "source_url": "https://www.gutenberg.org/cache/epub/14552/pg14552.txt",
        "passage_count": len(passages),
        "excluded": [
            {"id": "BC2 Q.241", "reason": "Answer quotes the words of consecration verbatim; the output refuser rejects that shape by design."},
            {"id": "BC2 Q.242", "reason": "Question and answer quote the words of consecration verbatim; same design conflict as Q.241."},
            {"id": "BC2 Q.250", "reason": "Answer quotes the words of consecration verbatim; same design conflict as Q.241."},
        ],
        "passages": passages,
    }
    out_path = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(__file__).with_name("corpus.json")
    out_path.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(f"wrote {out_path} with {len(passages)} passages")


if __name__ == "__main__":
    main()
