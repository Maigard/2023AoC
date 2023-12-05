#!/bin/env python3
import sys
import collections

def parse_input(filename):
    games = []
    with open(filename, "r") as f:
        for line in f:
            line = line.split(":")
            game = int(line[0].split(" ")[-1])
            reveals = []
            for i in line[1].strip().split(";"):
                reveal = collections.defaultdict(lambda: 0)
                for j in i.strip().split(","):
                    j = j.split()
                    reveal[j[1]] = int(j[0])
                reveals.append(reveal)
            games.append((game, tuple(reveals)))
    return tuple(games)

def main():
    total = 0
    games = parse_input(sys.argv[1])
    for game in games:
        for reveal in game[1]:
            if reveal["red"] > 12 or reveal["green"] > 13 or reveal["blue"] > 14:
                break
        else:
            total += game[0]
    print(total)

if __name__ == "__main__":
    main()
