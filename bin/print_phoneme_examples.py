#!/usr/bin/env python3
import sys
import re
import argparse
from collections import defaultdict

# This script loads frequently used words in a language, looks up their
# pronunciations in a pronunciation dictionary, then prints an example word +
# pronunciation for each phoneme.


def main():
    parser = argparse.ArgumentParser(
        "print_phoneme_examples.py",
        description="Prints phoneme examples by selecting from a list of frequent words",
    )
    parser.add_argument("frequent_words", help="Path to text file with frequent words")
    parser.add_argument("dictionary", help="Path to pronunciation dictionary")
    parser.add_argument(
        "--exclude_chars", nargs="*", default=["'"], help="Phoneme characters to exclude"
    )
    args = parser.parse_args()

    args.exclude_chars = set(args.exclude_chars)
    phoneme_transform = lambda p: "".join(c for c in p if c not in args.exclude_chars)

    # Download frequently used words in the given language
    with open(args.frequent_words, "r") as word_file:
        words = set([w.strip().upper() for w in word_file.read().splitlines()])

    # phoneme -> [(word, pronunciation), ...]
    examples = defaultdict(list)
    example_words = set()

    # Words with more than one pronunciation
    multi_pron_words = set()

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

            # Exclude meta words from Julius dictionaries
            if parts[1].startswith("["):
                parts = parts[1:]

            # Record example words for each phoneme
            upper_word = word.upper()
            if upper_word in words:

                # Check if word has already been part of an example
                if word in example_words:
                    multi_pron_words.add(word)

                pronunciation = [phoneme_transform(p) for p in parts[1:]]

                for phoneme in pronunciation:
                    examples[phoneme].append((word, pronunciation))
                    example_words.add(word)

    # 1st pass: pick unique example words for every phoneme.
    # Prefer words without multiple pronunciations.
    used_words = set()
    assigned_words = {}
    for phoneme in examples:
        # Choose the shortest, unused example word for this phoneme.
        # Exclude words with 3 or fewer letters.
        # Exclude words with multiple pronunciations.
        for word, pron in sorted(examples[phoneme], key=lambda kv: len(kv[0])):
            if (
                (len(word) > 3)
                and (word not in multi_pron_words)
                and (word not in used_words)
            ):
                assigned_words[phoneme] = (word, pron)
                used_words.add(word)
                break

    # 2nd pass: fill in remaining phonemes.
    # Prefer words > 3 characters long.
    for phoneme in sorted(examples.keys()):
        if phoneme not in assigned_words:
            # Choose the shortest, unused example word for this phoneme.
            # Exclude words with 3 or fewer letters.
            for word, pron in sorted(examples[phoneme], key=lambda kv: len(kv[0])):
                if (len(word) > 3) and (word not in used_words):
                    assigned_words[phoneme] = (word, pron)
                    used_words.add(word)
                    break

    # 3rd pass: fill in remaining phonemes.
    # Print assigned words.
    for phoneme in sorted(examples.keys()):
        if phoneme not in assigned_words:
            # Choose the shortest, unused example word for this phoneme.
            # Exclude words with 3 or fewer letters.
            for word, pron in sorted(examples[phoneme], key=lambda kv: len(kv[0])):
                if word not in used_words:
                    assigned_words[phoneme] = (word, pron)
                    used_words.add(word)
                    break

        # Output format is:
        # phoneme word pronunciation
        example_word, example_pron = assigned_words[phoneme]
        print(phoneme, example_word, " ".join(example_pron))


# -----------------------------------------------------------------------------

if __name__ == "__main__":
    main()
