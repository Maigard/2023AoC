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
        max_cubes = collections.defaultdict(lambda: 0)
        for reveal in game[1]:
            for (cube, count) in reveal.items():
                max_cubes[cube] = max(max_cubes[cube], count)
        total += max_cubes["red"] * max_cubes["green"] * max_cubes["blue"]
    print(total)

if __name__ == "__main__":
    main()
