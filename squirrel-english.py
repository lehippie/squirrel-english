"""Little Squirrel personnal english trainer.

Little Hedgehog edition, 2022.
"""

from pathlib import Path
from random import randint, shuffle


DATABASE = Path(__file__).parent / "english vocabulary.txt"


def read_database(filepath=DATABASE):
    db = []
    with open(filepath, encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            db.append([])
            groups = line.split(";")
            for group in groups:
                words = [word.strip() for word in group.split(",")]
                db[-1].append(words)
    return db


def main():
    db = read_database()
    shuffle(db)
    while db:
        group = db.pop()
        shuffle(group)
        questions, answers = group
        shuffle(questions)
        answer = input(questions[0] + "? ")
        if answer in answers:
            print("-> Congratulations Little Squirrel \o/")
            if len(answers) > 1:
                others = ", ".join(a for a in answers if a != answer)
                print(f"  other answers: {others}")
        else:
            db.insert(randint(-15, -9), group)
            print("-> Nooooo :/")
            print(f"  answers: {', '.join(answers)}")
        print()


if __name__ == "__main__":
    main()
