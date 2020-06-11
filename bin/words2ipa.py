#!/usr/bin/env python3
"""
Reads words from standard in and print their IPA representation to standard out.

Uses the epitran library.
https://github.com/dmort27/epitran
"""
import argparse
import sys

from epitran import Epitran

# aar-Latn 	Afar
# amh-Ethi 	Amharic
# ara-Arab 	Literary Arabic
# aze-Cyrl 	Azerbaijani (Cyrillic)
# aze-Latn 	Azerbaijani (Latin)
# ben-Beng 	Bengali
# ben-Beng-red 	Bengali (reduced)
# cat-Latn 	Catalan
# ceb-Latn 	Cebuano
# cmn-Hans 	Mandarin (Simplified)*
# cmn-Hant 	Mandarin (Traditional)*
# ckb-Arab 	Sorani
# deu-Latn 	German
# deu-Latn-np 	German†
# deu-Latn-nar 	German (more phonetic)
# eng-Latn 	English‡
# fas-Arab 	Farsi (Perso-Arabic)
# fra-Latn 	French
# fra-Latn-np 	French†
# hau-Latn 	Hausa
# hin-Deva 	Hindi
# hun-Latn 	Hungarian
# ilo-Latn 	Ilocano
# ind-Latn 	Indonesian
# ita-Latn 	Italian
# jav-Latn 	Javanese
# kaz-Cyrl 	Kazakh (Cyrillic)
# kaz-Latn 	Kazakh (Latin)
# kin-Latn 	Kinyarwanda
# kir-Arab 	Kyrgyz (Perso-Arabic)
# kir-Cyrl 	Kyrgyz (Cyrillic)
# kir-Latn 	Kyrgyz (Latin)
# kmr-Latn 	Kurmanji
# lao-Laoo 	Lao
# mar-Deva 	Marathi
# mlt-Latn 	Maltese
# mya-Mymr 	Burmese
# msa-Latn 	Malay
# nld-Latn 	Dutch
# nya-Latn 	Chichewa
# orm-Latn 	Oromo
# pan-Guru 	Punjabi (Eastern)
# pol-Latn 	Polish
# por-Latn 	Portuguese
# ron-Latn 	Romanian
# rus-Cyrl 	Russian
# sna-Latn 	Shona
# som-Latn 	Somali
# spa-Latn 	Spanish
# swa-Latn 	Swahili
# swe-Latn 	Swedish
# tam-Taml 	Tamil
# tel-Telu 	Telugu
# tgk-Cyrl 	Tajik
# tgl-Latn 	Tagalog
# tha-Thai 	Thai
# tir-Ethi 	Tigrinya
# tpi-Latn 	Tok Pisin
# tuk-Cyrl 	Turkmen (Cyrillic)
# tuk-Latn 	Turkmen (Latin)
# tur-Latn 	Turkish (Latin)
# ukr-Cyrl 	Ukranian
# uig-Arab 	Uyghur (Perso-Arabic)
# uzb-Cyrl 	Uzbek (Cyrillic)
# uzb-Latn 	Uzbek (Latin)
# vie-Latn 	Vietnamese
# xho-Latn 	Xhosa
# yor-Latn 	Yoruba
# zul-Latn 	Zulu


def main():
    parser = argparse.ArgumentParser(prog="words2ipa.py")
    parser.add_argument("language", help="epitran language code (e.g., eng-Latn)")
    parser.add_argument(
        "--print-word", action="store_true", help="Print word before IPA"
    )
    parser.add_argument("--sep", help="Separator between IPA symbols (default: none)")
    args = parser.parse_args()

    e = Epitran(args.language)

    print("Reading words from stdin...", file=sys.stderr)
    for word in sys.stdin:
        word = word.strip()
        if word:
            if args.print_word:
                print(word, end=" ")

            ipa = e.trans_list(word)
            if args.sep:
                print(args.sep.join(ipa))
            else:
                print("".join(ipa))


if __name__ == "__main__":
    main()
