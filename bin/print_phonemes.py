#!/usr/bin/env python3
import sys
import re
import argparse


def main():
    parser = argparse.ArgumentParser(
        "print_phonemes.py",
        description="Prints the unique set of phonemes from a pronunciation dictionary",
    )
    parser.add_argument("dictionary", help="Path to pronunciation dictionary")
    args = parser.parse_args()

    phonemes = set()
    with open(args.dictionary, "r") as dict_file:
        for line in dict_file:
            line = line.strip()
            if len(line) == 0:
                continue

            # Use explicit whitespace (avoid 0xA0)
            parts = re.split(r"[ \t]+", line)
            phonemes.update(parts[1:])

        for phoneme in sorted(phonemes):
            print(phoneme)


# -----------------------------------------------------------------------------

if __name__ == "__main__":
    main()
