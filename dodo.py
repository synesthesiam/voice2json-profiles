#!/usr/bin/env python3
"""doit file"""
from pathlib import Path

from doit import create_after

DOIT_CONFIG = {"action_string_formatting": "new"}

# -----------------------------------------------------------------------------

_DIR = Path(__file__).parent
_BIN = _DIR / "bin"

_EXCLUDE_PROFILES = set(["hindi/hi_pocketsphinx-cmu"])

_PROFILE_DIRS = []
with open(_DIR / "PROFILES", "r") as profiles_file:
    for line in profiles_file:
        line = line.strip()
        if line and (line not in _EXCLUDE_PROFILES):
            _PROFILE_DIRS.append(_DIR / line)

# -----------------------------------------------------------------------------


def task_frequent_words():
    """Generate list of 10,000 most frequent words."""
    for profile_dir in _PROFILE_DIRS:
        base_lm = profile_dir / "base_language_model.txt.gz"
        if not base_lm.is_file():
            continue

        frequent_words = profile_dir / "frequent_words.txt"
        get_frequent_words = _BIN / "get_frequent_words.py"
        yield {
            "name": profile_dir.name,
            "file_dep": [base_lm],
            "targets": [frequent_words],
            "actions": [
                f"zcat {{dependencies}} | '{get_frequent_words}' 10000 | cut -d' ' -f2 > {{targets}} "
            ],
        }


# -----------------------------------------------------------------------------

# epitran language codes
_LANG_CODE = {
    "ca": "cat-Latn",
    "ca-es": "cat-Latn",
    "nl": "nld-Latn",
    "en": "eng-Latn",
    "en-in": "eng-Latn",
    "fr": "fra-Latn",
    "de": "deu-Latn",
    "hi": "hin-Deva",
    "it": "ita-Latn",
    "kz": "kaz-Cyrl",
    "pl": "pol-Latn",
    "pt": "por-Latn",
    "pt-br": "por-Latn",
    "ru": "rus-Cyrl",
    "es": "spa-Latn",
    "es-mexican": "spa-Latn",
    "sv": "swe-Latn",
    "vi": "vie-Latn",
}


@create_after(executed="frequent_words")
def task_frequent_ipa():
    """Generate IPA for frequent words."""
    for profile_dir in _PROFILE_DIRS:
        lang = profile_dir.name.split("_")[0]
        if lang not in _LANG_CODE:
            continue

        lang_code = _LANG_CODE[lang]
        frequent_words = profile_dir / "frequent_words.txt"

        if not frequent_words.is_file():
            continue

        frequent_ipa = profile_dir / "frequent_words.ipa"

        words2ipa = _BIN / "words2ipa.py"

        yield {
            "name": profile_dir.name,
            "file_dep": [frequent_words],
            "targets": [frequent_ipa],
            "actions": [
                f"'{words2ipa}' --print-word --sep ' ' '{lang_code}' < {{dependencies}} > {{targets}}"
            ],
        }


# -----------------------------------------------------------------------------

_VOICES = {"ca-es": "ca", "es-mexican": "es", "zh-cn": "zh"}


@create_after(executed="frequent_words")
def task_frequent_espeak():
    """Generate eSpeak phonemes for frequent words."""
    for profile_dir in _PROFILE_DIRS:
        lang = profile_dir.name.split("_")[0]
        voice = _VOICES.get(lang, lang)
        frequent_words = profile_dir / "frequent_words.txt"

        if not frequent_words.is_file():
            continue

        frequent_espeak = profile_dir / "frequent_words.espeak"

        words2espeak = _BIN / "words2espeak.sh"

        yield {
            "name": profile_dir.name,
            "file_dep": [frequent_words],
            "targets": [frequent_espeak],
            "actions": [
                f"'{words2espeak}' --print-word -v {voice} < {{dependencies}} > {{targets}}"
            ],
        }


# -----------------------------------------------------------------------------


@create_after(executed="frequent_words")
def task_frequent_phonemes():
    """Generate speech system phonetic pronunciations for frequent words."""
    for profile_dir in _PROFILE_DIRS:
        base_dict = profile_dir / "base_dictionary.txt.gz"
        if not base_dict.is_file():
            continue

        frequent_words = profile_dir / "frequent_words.txt"

        if not frequent_words.is_file():
            continue

        frequent_phonemes = profile_dir / "frequent_words.phonemes"

        words2phonemes = _BIN / "words2phonemes.py"

        yield {
            "name": profile_dir.name,
            "file_dep": [frequent_words, base_dict],
            "targets": [frequent_phonemes],
            "actions": [
                f"bash -c '{words2phonemes} --case upper --print-word <(zcat {base_dict}) < {frequent_words} > {{targets}}'"
            ],
        }


# -----------------------------------------------------------------------------


@create_after(executed="frequent_ipa")
@create_after(executed="frequent_phonemes")
def task_align_ipa():
    """Align IPA phonemes with speech system phonemes."""
    for profile_dir in _PROFILE_DIRS:
        frequent_ipa = profile_dir / "frequent_words.ipa"
        frequent_phonemes = profile_dir / "frequent_words.phonemes"

        if (not frequent_ipa.is_file()) or (not frequent_phonemes.is_file()):
            continue

        ipa_phonemes = profile_dir / "ipa_phonemes.txt"

        align_phonemes = _BIN / "align_phonemes.py"

        yield {
            "name": profile_dir.name,
            "file_dep": [frequent_phonemes, frequent_ipa],
            "targets": [ipa_phonemes],
            "actions": [f"'{align_phonemes}' '{frequent_phonemes}' '{frequent_ipa}' > {{targets}}"],
        }


# -----------------------------------------------------------------------------


@create_after(executed="frequent_espeak")
@create_after(executed="frequent_phonemes")
def task_align_espeak():
    """Align eSpeak phonemes with speech system phonemes."""
    for profile_dir in _PROFILE_DIRS:
        frequent_espeak = profile_dir / "frequent_words.espeak"
        frequent_phonemes = profile_dir / "frequent_words.phonemes"

        if (not frequent_espeak.is_file()) or (not frequent_phonemes.is_file()):
            continue

        espeak_phonemes = profile_dir / "espeak_phonemes.txt"

        align_phonemes = _BIN / "align_phonemes.py"

        yield {
            "name": profile_dir.name,
            "file_dep": [frequent_phonemes, frequent_espeak],
            "targets": [espeak_phonemes],
            "actions": [f"'{align_phonemes}' '{frequent_phonemes}' '{frequent_espeak}' > {{targets}}"],
        }
