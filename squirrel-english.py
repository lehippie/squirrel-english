"""Little Squirrel personnal english trainer.

Hedgehog editions, 2022.
"""

import re
import traceback
from pathlib import Path
from random import randint, shuffle


DATABASE = next(Path(__file__).parent.glob("*.txt"))
PATTERN = re.compile(r"")


def read_database(dbpath=DATABASE):
    db = []
    print(f"Reading database '{dbpath.stem}'...")
    with open(dbpath, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.count(";") != 1:
                print(f"[W] Line '{line}' incorrectly formatted.")
                continue
            db.append([])
            for lang in line.split(";"):
                ctx = ""
                if "(" in lang:
                    ctx = lang[lang.index("(") + 1 : lang.index(")")]
                    lang = lang[: lang.index("(")]
                words = [word.strip() for word in lang.split(",")]
                db[-1].append([words, ctx])
    return db


def main(db):
    k = 0
    shuffle(db)
    while db:
        k += 1
        entry = db.pop()
        shuffle(entry)
        (questions, qctx), (answers, _) = entry
        shuffle(questions)
        if qctx:
            answer = input(f"{k}) {questions[0]} ({qctx})? ")
        else:
            answer = input(f"{k}) {questions[0]} ? ")
        if answer.lower() in [a.lower() for a in answers]:
            print("-> Congratulations Little Squirrel \o/")
            if len(answers) > 1:
                others = ", ".join(a for a in answers if a != answer)
                print(f"  other answers: {others}")
        else:
            print("-> Oh Nooooo Little Squirrel :/")
            print(f"  answers: {', '.join(answers)}")
            db.insert(randint(-15, -9), entry)
        print()


if __name__ == "__main__":
    print("--- Welcome to Squirrel-English v2 ! ---\n")
    try:
        db = read_database()
        print()
        main(db)
    except:
        print()
        traceback.print_exc()
        input("Press Enter to quit.")
        exit()
    input("No more words! Press Enter to exit.")
