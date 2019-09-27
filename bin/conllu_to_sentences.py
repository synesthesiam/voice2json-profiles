#!/usr/bin/env python3
import argparse

from conllu import parse_incr


def main():
    parser = argparse.ArgumentParser(
        "conllu_to_sentences.py",
        description="Extracts sentences from a CONLLU formatted file",
    )
    parser.add_argument("conllu", help="Path to CONLLU file")
    args = parser.parse_args()

    with open(args.conllu, "r") as in_file:
        for tokens in parse_incr(in_file):
            s = " ".join(t["form"] for t in tokens if t["upostag"] != "PUNCT")
            print(s)


# -----------------------------------------------------------------------------

if __name__ == "__main__":
    main()
