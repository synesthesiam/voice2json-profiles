#!/usr/bin/env python3
"""
Reads words from standard in and prints their phonetic pronunciations on standard out.

Requires a pre-built phonetic dictionary.
"""
import argparse
import sys
import re
from collections import defaultdict


def main():
    parser = argparse.ArgumentParser(prog="words2phonemes.py")
    parser.add_argument("dictionary", help="Phonetic dictionary (CMU format)")
    parser.add_argument(
        "--print-word", action="store_true", help="Print word before phonemes"
    )
    parser.add_argument(
        "--sep", default=" ", help="Separator between phonemes (default: space)"
    )
    parser.add_argument(
        "--case", choices=["upper", "lower"], help="Case transformation (default: none)"
    )
    args = parser.parse_args()

    transform = lambda s: s
    if args.case == "upper":
        transform = str.upper
    elif args.case == "lower":
        transform = str.lower

    pron_dict = read_dict(args.dictionary, transform=transform)

    print("Reading words from stdin...", file=sys.stderr)
    for word in sys.stdin:
        word = word.strip()
        if word:
            if args.print_word:
                print(word, end=" ")

            prons = pron_dict.get(transform(word))
            if prons:
                print(args.sep.join(prons[0]))
            else:
                print("")


def read_dict(dict_path, transform=None):
    """Load a CMU pronunciation dictionary."""
    word_pronunciations = defaultdict(list)

    with open(dict_path, "r") as dict_file:
        for line in dict_file:
            line = line.strip()
            if len(line) == 0:
                continue

            # Use explicit whitespace (avoid 0xA0)
            parts = re.split(r"[ \t]+", line)
            word = parts[0]

            if "(" in word:
                word = word[: word.index("(")]

            if transform:
                word = transform(word)

            # Exclude meta words from Julius dictionaries
            if parts[1].startswith("["):
                parts = parts[1:]

            pronunciation = [p for p in parts[1:]]
            word_pronunciations[word].append(pronunciation)

    return word_pronunciations


# -----------------------------------------------------------------------------

if __name__ == "__main__":
    main()
