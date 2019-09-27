#!/usr/bin/env python3
import sys
import os
import argparse
from pathlib import Path
from collections import defaultdict

from bs4 import BeautifulSoup
import requests


def main():
    """This script downloads frequently used words in the supported languages."""
    parser = argparse.ArgumentParser(
        "download_frequent_words.py",
        description="Downloads frequent words for all profile languages from https://www.ezglot.com",
    )
    parser.add_argument(
        "--directory",
        help="Directory to search for profile directories (default: current directory)",
    )
    args = parser.parse_args()

    if args.directory:
        profiles_dir = Path(args.directory)
    else:
        profiles_dir = Path.cwd()

    # Language code -> profile language
    languages = {
        "eng": "english",
        "deu": "german",
        "fra": "french",
        "spa": "spanish",
        "ita": "italian",
        "nld": "dutch",
        "rus": "russian",
        "vie": "vietnamese",
        "cmn": "mandarin",
        "hin": "hindi",
        "ell": "greek",
        "por": "portuguese",
        "swe": "swedish",
        "cat": "catalan",
    }

    for language_code, language_name in languages.items():
        language_dir = profiles_dir / language_name
        html_path = language_dir / "frequent_words.html"

        if not html_path.exists():
            # Download
            url = "https://www.ezglot.com/most-frequently-used-words.php?l={}&submit=Select".format(
                language_code
            )
            print(f"Downloading from {url}")

            with open(html_path, "w") as html_file:
                # Download frequently used words in the given language
                page = requests.get(url).text
                html_file.write(page)
        else:
            # Load cached file
            page = html_path.read_text()

        # Process HTML
        soup = BeautifulSoup(page, "html5lib")

        for locale_dir in language_dir.glob("*"):
            if not locale_dir.is_dir():
                continue

            freq_path = locale_dir / "frequent_words.txt"
            with open(freq_path, "w") as freq_file:
                for word_ul in soup.find_all(attrs={"class": "topwords"}):
                    for word_li in word_ul.findAll("li"):
                        word = word_li.text.strip().upper()

                        # Skip small words
                        if len(word) < 3:
                            continue

                        print(word, file=freq_file)

        print(language_name)


# -----------------------------------------------------------------------------

if __name__ == "__main__":
    main()
