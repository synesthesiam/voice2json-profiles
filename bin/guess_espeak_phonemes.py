#!/usr/bin/env python3
import re
import argparse
import subprocess
import concurrent.futures
from collections import defaultdict, Counter
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(
        "guess_espeak_phonemes.py",
        description="Uses espeak-ng to guess the mapping between dictionary phonemes and espeak's phonemes",
    )
    parser.add_argument("frequent_words", help="Path to text file with frequent words")
    parser.add_argument("dictionary", help="Path to pronunciation dictionary")
    parser.add_argument("--voice", help="espeak voice")
    args = parser.parse_args()

    # Load frequent words
    with open(args.frequent_words, "r") as word_file:
        words = set([w.strip().upper() for w in word_file.read().splitlines()])

    # Generate espeak phonemes in parallel
    espeak_args = []
    if args.voice is not None:
        espeak_args.extend(["-v", args.voice])

    def to_espeak(word):
        return (
            word,
            re.split(
                r"\s+",
                subprocess.check_output(
                    ["espeak-ng", "-q", "-x", "--sep= "] + espeak_args + [word]
                )
                .decode()
                .strip(),
            ),
        )

    with concurrent.futures.ThreadPoolExecutor() as executor:
        word_to_espeak = dict(executor.map(to_espeak, words))

    # phoneme -> espeak
    candidates = Counter()
    all_phonemes = set()

    # Find pronunciations for each frequently used word
    with open(args.dictionary, "r") as dict_file:
        for line in dict_file:
            line = line.strip()
            if len(line) == 0:
                continue

            # Use explicit whitespace (avoid 0xA0)
            parts = re.split(r"[ \t]+", line)
            word = parts[0]

            if "(" in word:
                word = word[: word.index("(")]

            pronunciation = parts[1:]
            all_phonemes.update(pronunciation)

            # Skip short words
            if len(word) < 3:
                continue

            upper_word = word.upper()
            if (upper_word in words) and (upper_word in word_to_espeak):
                espeak_phonemes = word_to_espeak[upper_word]

                scale = len(espeak_phonemes) / len(pronunciation)
                for i, dict_phoneme in enumerate(pronunciation):
                    j = int(scale * i)
                    candidates[(dict_phoneme, espeak_phonemes[j])] += 1

    # -------------------------------------------------------------------------

    # Assign naively by highest count
    assignments = {}
    for candidate, count in candidates.most_common():
        dict_phoneme, espeak_phoneme = candidate
        if dict_phoneme not in assignments:
            assignments[dict_phoneme] = espeak_phoneme

    # Print candidates and ? for phonemes with no candidates
    for dict_phoneme in sorted(all_phonemes):
        print(dict_phoneme, assignments.get(dict_phoneme, "?"))


# -----------------------------------------------------------------------------

if __name__ == "__main__":
    main()
