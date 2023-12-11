#!/bin/env python3
import sys
import collections

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

def main():
    numcards = 0
    cards = parse_input(sys.argv[1])
    totalcards = [1] * len(cards)
    for (i,card) in enumerate(cards):
        winnums = len(card["winning"] & card["nums"])
        for j in range(i+1,i+1+winnums):
            totalcards[j] += totalcards[i]
    print(sum(totalcards))

if __name__ == "__main__":
    main()
