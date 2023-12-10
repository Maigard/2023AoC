#!/bin/env python3
import sys
import re

def parse_input(filename):
    symbols = []
    parts = []
    with open(filename, "r") as f:
        for (num,line) in enumerate(f):
            for match in re.finditer(r"(\d)+|([^\.])", line[:-1]):
                try:
                    span = match.span()
                    parts.append({"partnum": int(match.group(0)), "row": num, "span": (span[0], span[1]-1)})
                except ValueError:
                    symbols.append({"symbol": match.group(0), "row": num, "col": match.span()[0]})
    return symbols, parts

def near(part, symbol):
    return part["row"] - 1 <= symbol["row"] <= part["row"] + 1 and part["span"][0] - 1 <= symbol["col"] <= part["span"][1] + 1

def main():
    symbols, parts = parse_input(sys.argv[1])
    totalparts = sum([part["partnum"] for part in parts])
    for symbol in symbols:
        parts = [part for part in parts if not near(part, symbol)]
    print(totalparts - sum([part["partnum"] for part in parts]))

if __name__ == "__main__":
    main()
