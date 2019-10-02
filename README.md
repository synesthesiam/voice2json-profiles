# voice2json profiles

Speech models and supporting files for [voice2json](https://github.com/synesthesiam/voice2json).

## Data

Files are contained in `<LANGUAGE>/<LOCALE>` directories. Each locale directory should contain a `SOURCE` file describing where it was sourced from. The `LICENSE` file in each locale directory covers the artifacts for that specific profile.

Directories with `pocketsphinx` contain [CMU Sphinx](https://cmusphinx.github.io/) acoustic models. Directories with `kaldi` contain [Kaldi](https://kaldi-asr.org) acoustic models (either `gmm` or `nnet3`).

## Supported Languages

The following languages are supported with at least one pre-trained speech model. Some languages have multiple locales (Spanish/Mexican Spanish), and some locales have multiple speech models (U.S. English).

A model is considered to be **Verified** if at least one member of the community has reported success with it. Models that are not verified are still fine to use, and testing them is a great way to contribute!

* Catalan
    * [ca-es_pocketsphinx-cmu](https://github.com/synesthesiam/ca-es_pocketsphinx-cmu)
* Dutch (Nederlands)
    * [nl_pocketsphinx-cmu](https://github.com/synesthesiam/nl_pocketsphinx-cmu)
        * Status: **Verified**
* English
    * U.S. English
        * [en-us_pocketsphinx-cmu](https://github.com/synesthesiam/en-us_pocketsphinx-cmu)
            * Status: **Verified**
        * [en-us_kaldi-zamia](https://github.com/synesthesiam/en-us_kaldi-zamia)
            * Status: **Verified**
        * [en-us_julius-github](https://github.com/synesthesiam/en-us_julius-github)
    * Indian English
        * [en-in_pocketsphinx-cmu](https://github.com/synesthesiam/en-in_pocketsphinx-cmu)
* French (Français)
    * [fr_pocketsphinx-cmu](https://github.com/synesthesiam/fr_pocketsphinx-cmu)
        * Status: **Verified**
* German (Deutsch)
    * [de_pocketsphinx-cmu](https://github.com/synesthesiam/de_pocketsphinx-cmu)
* Greek (Ελληνικά)
    * [el-gr_pocketsphinx-cmu](https://github.com/synesthesiam/el-gr_pocketsphinx-cmu)
* Hindi (Devanagari)
    * [hi_pocketsphinx-cmu](https://github.com/synesthesiam/hi_pocketsphinx-cmu)
* Italian (Italiano)
    * [it_pocketsphinx-cmu](https://github.com/synesthesiam/it_pocketsphinx-cmu)
        * Status: **Verified**
* Kazakh (қазақша)
    * [kz_pocketsphinx-cmu](https://github.com/synesthesiam/kz_pocketsphinx-cmu)
* Mandarin (中文)
    * [zh-cn_pocketsphinx-cmu](https://github.com/synesthesiam/zh-cn_pocketsphinx-cmu)
* Polish (polski)
    * [pl_julius-github](https://github.com/synesthesiam/pl_julius-github)
* Portugese (Português)
    * [pt-br_pocketsphinx-cmu](https://github.com/synesthesiam/pt-br_pocketsphinx-cmu)
        * Status: **Verified**
* Russian (Русский)
    * [ru_pocketsphinx-cmu](https://github.com/synesthesiam/ru_pocketsphinx-cmu)
* Spanish (Español)
    * [es_pocketsphinx-cmu](https://github.com/synesthesiam/es_pocketsphinx-cmu)
    * Mexian Spanish
        * [es-mexican_pocketsphinx-cmu](https://github.com/synesthesiam/es-mexican_pocketsphinx-cmu)
* Swedish (svenska)
    * [sv_kaldi-montreal](https://github.com/synesthesiam/sv_kaldi-montreal)
* Vietnamese (Tiếng Việt)
    * [vi_kaldi-montreal](https://github.com/synesthesiam/vi_kaldi-montreal)

## Acknowledgements

The acoustic models and pronunciation dictionaries come from one of:

* [CMU Sphinx Acoustic Models](https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/)
* [Zamia ASR Models](https://github.com/gooofy/zamia-speech)
* [Montreal Forced Aligner Pretrained Models](https://montreal-forced-aligner.readthedocs.io/en/latest/pretrained_models.html)
* [Julius Models](https://sourceforge.net/projects/juliusmodels/)

When language models or grapheme-to-phoneme models were unavailable, they were generated using:

* Data from [Universal Dependencies](https://github.com/UniversalDependencies)
* The [Phonetisaurus](https://github.com/AdolfVonKleist/Phonetisaurus) G2P tool
