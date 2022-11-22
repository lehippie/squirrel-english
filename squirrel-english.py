"""Little Squirrel personnal english trainer.

Hedgehog editions, 2022.
"""

import traceback
from pathlib import Path
from random import randint, shuffle


DATABASE = Path(__file__).parent / "english vocabulary.txt"

def read_database(filepath=DATABASE):
    db = []
    with open(filepath, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.count(";") != 1:
                print(f'[W] Line "{line}" ignored: there should be only one ";"')
                continue
            if "(" in line:
                line = line[:line.index("(")]
            db.append([])
            for lang in line.split(";"):
                words = [word.strip() for word in lang.split(",")]
                db[-1].append(words)
    return db


def main(db):
    k = 0
    shuffle(db)
    while db:
        k += 1
        entry = db.pop()
        shuffle(entry)
        questions, answers = entry
        shuffle(questions)
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
    print("Welcome to Squirrel-English v2 !\n")
    print("Reading database...")
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
