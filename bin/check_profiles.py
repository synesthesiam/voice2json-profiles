#!/usr/bin/env python3
import os
import sys
from pathlib import Path

import pydash
import yaml

from utils import load_profile

def main():
    for yml_path_str in sys.stdin:
        yml_path = Path(yml_path_str.strip())
        profile_dir = yml_path.parent
        profile_name = profile_dir.name

        # Check common files
        common_files = [
            profile_dir / "acoustic_model",
            profile_dir / "base_dictionary.txt",
            profile_dir / "base_language_model.txt",
            profile_dir / "g2p.fst",
            profile_dir / "phoneme_examples.txt",
            profile_dir / "espeak_phonemes.txt",
            profile_dir / "sentences.ini",
            profile_dir / "stop_words.txt",
            profile_dir / "custom_words.txt",
            profile_dir / "frequent_words.txt",
            profile_dir / "SOURCE",
            profile_dir / "LICENSE",
            profile_dir / "clean.sh",
        ]

        for p in common_files:
            if not p.exists():
                print(profile_name, "missing", p.name)

        # ---------------------------------------------------------------------

        with open(yml_path, "r") as yml_file:
            profile = load_profile(yml_file)

        kaldi_model_type = pydash.get(profile, "speech-to-text.kaldi.model-type", "")

        if len(kaldi_model_type) > 0:
            # Check Kaldi specific files
            model_dir = profile_dir / "acoustic_model"
            kaldi_files = [
                model_dir / "model" / "final.mdl",
                model_dir / "model" / "graph" / "HCLG.fst",
                model_dir / "phones" / "nonsilence_phones.txt",
                model_dir / "phones" / "silence_phones.txt",
            ]

            if kaldi_model_type == "gmm":
                kaldi_files.extend([model_dir / "conf" / "mfcc.conf"])
            elif kaldi_model_type == "nnet3":
                kaldi_files.extend(
                    [
                        model_dir / "conf" / "online_cmvn.conf",
                        model_dir / "conf" / "mfcc_hires.conf",
                    ]
                )

            for p in kaldi_files:
                if not p.exists():
                    print(profile_name, "missing", p.name)


# -----------------------------------------------------------------------------

if __name__ == "__main__":
    main()
