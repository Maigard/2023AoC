#!/bin/env python3
import sys

def parse_input(filename):
    cards = []
    with open(filename, "r") as f:
        for line in f:
            line = line.split("|")
            winning = line[0].strip().split()
            cards.append({
                "card": int(winning[1][:-1]),
                "winning": {int(i) for i in winning[2:]},
                "nums": {int(i) for i in line[1].strip().split()}
            })
    return cards

def score_card(card):
    wins = len(card["winning"] & card["nums"])
    return (2 ** (wins - 1)) if wins > 0 else 0

def main():
    cards = parse_input(sys.argv[1])
    print(sum([score_card(card) for card in cards]))

if __name__ == "__main__":
    main()
