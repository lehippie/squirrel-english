#!/usr/bin/env python

"""Little Squirrel personnal english trainer.

Hedgehog editions, 2022.
"""

from pathlib import Path
from random import choice, randint, shuffle


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
            db.append([])
            for entry in line.split(";"):
                words = tuple(map(str.strip, entry.split(",")))
                db[-1].append(words)
    return db


def main():
    db = read_database()
    shuffle(db)
    while db:
        entry = db.pop()
        print(entry)
        shuffle(entry)
        print(entry)
        questions, answers = entry
        shuffle(questions)
        answer = input(questions[0] + "? ")
        if answer in answers:
            print("-> Congratulations Little Squirrel \o/")
            if len(answers) > 1:
                others = ", ".join(a for a in answers if a != answer)
                print(f"  other answers: {others}")
        else:
            db.insert(randint(-15, -9), entry)
            print("-> Nooooo :/")
            print(f"  answers: {', '.join(answers)}")
        print()


if __name__ == "__main__":
    main()
