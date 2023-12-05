#!/bin/env python3
import sys

def main():
    numbers = []
    with open(sys.argv[1], "r") as f:
        for line in f:
            line = "".join(i for i in line if i in "0123456789")
            numbers.append(int(line[0] + line[-1]))
    print(sum(numbers))

if __name__ == "__main__":
    main()
