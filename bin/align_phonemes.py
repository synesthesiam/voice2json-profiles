#!/usr/bin/env python3
"""
Attempts to guess the correspondence between a speech system's phonemes and some
other phoneme set (e.g., IPA or eSpeak).

Requires 2 text files:
* phonemes - <word> <phoneme1> <phoneme2> ...
* other - <word> <phoneme1> <phoneme2> ...

Alignment is done in 2 passes:

1. Count all cases where speech/other phoneme lists are the same length for a
given word. Assign phonemes based on highest count first.

2. Go back and assume unaligned phonemes are composed of two "others" instead of
one. Assign remaining phonemes based on highest count first.
"""
import argparse
import re
import typing
from collections import Counter
from dataclasses import dataclass, field


@dataclass
class Word:
    """Word with speech system and other phonemes."""

    word: str
    phonemes: typing.List[str] = field(default_factory=list)
    other: typing.List[str] = field(default_factory=list)


def clean(s: str) -> str:
    """Remove accents."""
    return s.strip().replace("'", "")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "phonemes", help="Path to file with words and speech system phonemes"
    )
    parser.add_argument("other", help="Path to file with words and other phonemes")
    parser.add_argument(
        "--examples", help="Path to file with speech system phoneme examples"
    )
    parser.add_argument(
        "--missing", default="?", help="String to print for missing phonemes"
    )
    args = parser.parse_args()

    all_phonemes: typing.Set[str] = set()
    words: typing.Dict[str, Word] = {}

    # Load speech system phonemes
    with open(args.phonemes, "r") as phoneme_file:
        for line in phoneme_file:
            line = line.strip()
            if line:
                word_str, *phonemes = line.split()
                if not phonemes:
                    continue

                word = words.get(word_str)
                if not word:
                    word = Word(word_str)
                    words[word_str] = word

                word.phonemes = [clean(p) for p in phonemes]
                all_phonemes.update(word.phonemes)

    # Load other phonemes
    with open(args.other, "r") as other_file:
        for line in other_file:
            line = line.strip()
            if line:
                word_str, *others = line.split()
                if not others:
                    continue

                word = words.get(word_str)
                if not word:
                    word = Word(word_str)
                    words[word_str] = word

                word.other = [clean(o) for o in others]

    # Load phoneme examples
    phoneme_example: typing.Dict[str, str] = {}

    if args.examples:
        with open(args.examples, "r") as examples_file:
            for line in examples_file:
                line = line.strip()
                if line:
                    phoneme, example, *phonemes = line.split()
                    all_phonemes.add(phoneme)
                    phoneme_example[phoneme] = example

    # -------------------------------------------------------------------------

    # phoneme -> other
    assignments: typing.Dict[str, str] = {}

    # ------
    # Pass 1
    # ------
    # Find candidates with identical lengths.
    phoneme_other = Counter()
    for word in words.values():
        if len(word.phonemes) == len(word.other):
            for phoneme, other in zip(word.phonemes, word.other):
                phoneme_other[(phoneme, other)] += 1

    # Assign naively based purely on count
    for candidate, count in phoneme_other.most_common():
        phoneme, other = candidate
        if (phoneme not in assignments) and (other not in assignments.values()):
            assignments[phoneme] = other

    # ------
    # Pass 2
    # ------
    # Assume unassigned phonemes map to two "others".
    assigned_others = set(assignments.values())
    unassigned = all_phonemes - set(assignments)

    if unassigned:
        for word in words.values():
            if len(word.other) > len(word.phonemes):
                others = list(word.other)
                for phoneme in word.phonemes:
                    if not others:
                        # No more others left
                        break

                    if (phoneme in unassigned) and (len(others) >= 2):
                        # Grab two "others" for this unassigned phoneme
                        phoneme_other[(phoneme, "".join(others[:2]))] += 1
                    else:
                        # Skip over "other" for already assigned phoneme
                        others = others[1:]

    # Do assignent again with (hopefully) new candidates
    for candidate, count in phoneme_other.most_common():
        phoneme, other = candidate
        if (phoneme not in assignments) and (other not in assignments.values()):
            assignments[phoneme] = other

    # -------------------------------------------------------------------------

    # Print candidates and ? for phonemes with no candidates
    for phoneme in sorted(all_phonemes):
        print(phoneme, assignments.get(phoneme, args.missing), end="")

        if args.examples:
            print(" ", phoneme_example.get(phoneme, ""))
        else:
            # End line
            print("")


# -----------------------------------------------------------------------------

if __name__ == "__main__":
    main()
