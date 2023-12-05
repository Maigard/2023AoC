#!/bin/env python3
import sys
import re

def main():
    lines = []
    keys = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
            "six": 6, "seven": 7, "eight": 8, "nine": 9}
    with open(sys.argv[1], "r") as f:
        for line in f:
            line = re.findall(r"(?=(0|1|2|3|4|5|6|7|8|9|zero|one|two|three|four|five|six|seven|eight|nine))", line)
            line = [keys[i] if i in keys else int(i) for i in line]
            lines.append(line[0] * 10  + line[-1])
    print(sum(lines))

if __name__ == "__main__":
    main()
