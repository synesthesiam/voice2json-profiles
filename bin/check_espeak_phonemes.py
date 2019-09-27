#!/usr/bin/env python3
import re
import subprocess
import argparse


def main():
    parser = argparse.ArgumentParser(
        "check_espeak_phonemes.py",
        description="Pronounces and confirms each example in phoneme_examples.txt",
    )
    parser.add_argument("examples", help="Path to phoneme examples text file")
    parser.add_argument("map", help="Path to espeak phoneme map file")
    parser.add_argument("--voice", help="espeak voice")
    args = parser.parse_args()

    # Load examples
    with open(args.examples, "r") as examples_file:
        for example_line in examples_file:
            example_line = example_line.strip()
            if (len(example_line) == 0) or example_line.startswith("#"):
                continue

            dict_phoneme, word, espeak_phoneme_str = re.split(r"\s+", example_line, maxsplit=2)
            espeak_phonemes = re.split(r"\s+", espeak_phoneme_str)

            # Repeat until stopped by user
            while True:
                # Load map
                phoneme_map = {}
                with open(args.map, "r") as map_file:
                    for map_line in map_file:
                        map_line = map_line.strip()
                        if (len(map_line) == 0) or map_line.startswith("#"):
                            continue

                        map_dict_phoneme, map_espeak_phoneme = re.split(r"\s+", map_line)
                        phoneme_map[map_dict_phoneme] = map_espeak_phoneme

                # Speak expected
                print(dict_phoneme, word, "expected")
                espeak_cmd = ["espeak", "-x", "-s", "80"]
                if args.voice is not None:
                    espeak_cmd.extend(["-v", args.voice])

                espeak_cmd.append(word)
                subprocess.check_call(espeak_cmd)

                # Speak actual
                actual_espeak = [phoneme_map.get(p, p) for p in espeak_phonemes]
                actual_espeak_str = "".join(actual_espeak)

                print(dict_phoneme, word, "actual")
                espeak_cmd = ["espeak", "-x", "-s", "80"]
                if args.voice is not None:
                    espeak_cmd.extend(["-v", args.voice])

                espeak_cmd.append(f"[[{actual_espeak_str}]]")
                subprocess.check_call(espeak_cmd)

                # User input
                print("[r]epeat/[n]ext: ", end="")
                command = input()
                if not command.startswith("r"):
                    break

# -----------------------------------------------------------------------------

if __name__ == "__main__":
    main()
