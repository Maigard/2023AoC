#!/bin/env python3
import sys
import re

def main():
    lines = []
    keys = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
            "six": 6, "seven": 7, "eight": 8, "nine": 9,
            "0": 0, "1": 1, "2": 2, "3": 3, "4": 4,
            "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}

    with open(sys.argv[1], "r") as f:
        for line in f:
            line = re.findall(f"(?=({'|'.join(keys.keys())}))", line)
            line = [keys[i] for i in line]
            lines.append(line[0] * 10  + line[-1])
    print(sum(lines))

if __name__ == "__main__":
    main()
