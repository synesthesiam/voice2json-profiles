#!/usr/bin/env python3
"""
Reads through an ARPA language model and prints out the N most likely words
(1-grams) based on their negative log likelihoods.

Example:
$ python3 get_frequent_words.py 100 < ARPA.lm
"""
import argparse
import heapq
import sys

# Ignore start/stop sentence tokens
_IGNORE_WORDS = set(["<s>", "</s>"])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int, help="Number of words")
    args = parser.parse_args()

    print("Reading ARPA language model from stdin...", file=sys.stderr)

    in_1grams = False
    frequent_words = []

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        if line.startswith("\\"):
            if in_1grams:
                # Must be past 1-grams now
                break
            elif line == "\\1-grams:":
                in_1grams = True
        elif in_1grams:
            # Parse 1-gram
            prob, word, *rest = line.split()
            prob = float(prob)
            word = word.strip()

            if (not word) or (word in _IGNORE_WORDS):
                # Skip empty or ignored words
                continue

            if len(frequent_words) < args.n:
                # Append to heap
                heapq.heappush(frequent_words, (prob, word))
            else:
                # Replace least likely element
                heapq.heappushpop(frequent_words, (prob, word))

    # Print the n most frequent words
    for prob, word in frequent_words:
        print(prob, word)


# -----------------------------------------------------------------------------

if __name__ == "__main__":
    main()
