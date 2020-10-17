#!/usr/bin/env python3
import sys
import re
import argparse
from collections import Counter


def main():
    parser = argparse.ArgumentParser(
        "print_phonemes.py",
        description="Prints the unique set of phonemes from a pronunciation dictionary",
    )
    parser.add_argument("dictionary", help="Path to pronunciation dictionary")
    parser.add_argument(
        "--min-count",
        type=int,
        help="Minimum use count before printing phoneme in list",
    )
    parser.add_argument(
        "--counts", action="store_true", help="Print counts with list"
    )
    args = parser.parse_args()

    if args.dictionary == "-":
        dict_file = sys.stdin
    else:
        dict_file = open(args.dictionary, "r")

    phonemes = Counter()
    with dict_file:
        for line in dict_file:
            line = line.strip()
            if len(line) == 0:
                continue

            # Use explicit whitespace (avoid 0xA0)
            parts = re.split(r"[ \t]+", line)

            for phoneme in parts[1:]:
                phonemes[phoneme] += 1

    for phoneme in sorted(phonemes):
        count = phonemes[phoneme]
        if args.min_count is None or (count >= args.min_count):
            if args.counts:
                print(phoneme, count)
            else:
                print(phoneme)


# -----------------------------------------------------------------------------

if __name__ == "__main__":
    main()
