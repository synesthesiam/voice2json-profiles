# voice2json profiles

Speech models and supporting files for [voice2json](https://github.com/synesthesiam/voice2json).

## Data

Files are contained in `<LANGUAGE>/<LOCALE>` directories. Each locale directory should contain a `SOURCE` file describing where it was sourced from. The `LICENSE` file in each locale directory covers the artifacts for that specific profile.

* Directories with `pocketsphinx` contain [CMU Sphinx](https://cmusphinx.github.io/) acoustic models
* Directories with `kaldi` contain [Kaldi](https://kaldi-asr.org) acoustic models (either `gmm` or `nnet3`).
* Directories with `deepspeech` contain [Mozilla DeepSpeech](https://github.com/mozilla/DeepSpeech) acoustic models (version 0.6).
* Directories with `julius` contain [Julius](https://github.com/julius-speech/julius) acoustic models (DNN, version 4.5).

Some files are split into multiple parts so that they can be uploaded to GitHub. This is done with the `split` command:

```bash
split -d -b 25M FILE FILE.part-
```

They can be recombined simply with:

```bash
cat FILE.part-* > FILE
```

## Supported Languages

`voice2json` supports the following languages/locales. I don't speak or write any language besides U.S. English very well, so **please** let me know if any profile is broken or could be improved!

Untested profiles (highlighted below) *may* work, but I don't have the necessary data or enough understanding of the language to test them.

<table>
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th>Language</th>
      <th>Locale</th>
      <th>System</th>
      <th>Closed</th>
      <th>Open</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <a href="https://github.com/synesthesiam/ca-es_pocketsphinx-cmu">View</a>
      </td>
      <td>
        <a href="https://github.com/synesthesiam/ca-es_pocketsphinx-cmu/archive/v1.1.tar.gz">Download</a>
      </td>
      <td>Catalan</td>
      <td>ca-es</td>
      <td>pocketsphinx</td>
      <td>
        <strong>UNTESTED</strong>
      </td>
      <td>
        <strong>UNTESTED</strong>
      </td>
    </tr>
    <tr>
      <td>
        <a href="https://github.com/rhasspy/cs_kaldi-rhasspy">View</a>
      </td>
      <td>
        <a href="https://github.com/rhasspy/cs_kaldi-rhasspy/archive/v1.0.tar.gz">Download</a>
      </td>
      <td>Czech</td>
      <td>cs-cz</td>
      <td>Kaldi</td>
      <td>
        <strong>UNTESTED</strong>
      </td>
      <td>
        <strong>UNTESTED</strong>
      </td>
    </tr>
    <tr>
      <td>
        <a href="https://github.com/synesthesiam/nl_kaldi-cgn">View</a>
      </td>
      <td>
        <a href="https://github.com/synesthesiam/nl_kaldi-cgn/archive/v1.1.tar.gz">Download</a>
      </td>
      <td>Dutch (Nederlands)</td>
      <td>nl</td>
      <td>kaldi</td>
      <td>&#9733; &#9733; &#9733; &#9733; &#9733; (2x)</td>
      <td>&#9785; (1x)</td>
    </tr>
    <tr>
      <td>
        <a href="https://github.com/synesthesiam/nl_pocketsphinx-cmu">View</a>
      </td>
      <td>
        <a href="https://github.com/synesthesiam/nl_pocketsphinx-cmu/archive/v1.1.tar.gz">Download</a>
      </td>
      <td>Dutch (Nederlands)</td>
      <td>nl</td>
      <td>pocketsphinx</td>
      <td>&#9733; &#9733; &#9733; &#9733; (18x)</td>
      <td>&#9785; (3x)</td>
    </tr>
    <tr>
      <td>
        <a href="https://github.com/synesthesiam/en-in_pocketsphinx-cmu">View</a>
      </td>
      <td>
        <a href="https://github.com/synesthesiam/en-in_pocketsphinx-cmu/archive/v1.1.tar.gz">Download</a>
      </td>
      <td>English</td>
      <td>en-in</td>
      <td>pocketsphinx</td>
      <td>&#9785; (4x)</td>
      <td>&#9785; (4x)</td>
    </tr>
    <tr>
      <td>
        <a href="https://github.com/synesthesiam/en-us_deepspeech-mozilla">View</a>
      </td>
      <td>
        <a href="https://github.com/synesthesiam/en-us_deepspeech-mozilla/archive/v1.0.tar.gz">Download</a>
      </td>
      <td>English</td>
      <td>en-us</td>
      <td>deepspeech</td>
      <td>&#9733; &#9733; &#9733; &#9733; &#9733; (1x)</td>
      <td>&#9733; &#9733; &#9733; &#9733; (1x)</td>
    </tr>
    <tr>
      <td>
        <a href="https://github.com/synesthesiam/en-us_julius-github">View</a>
      </td>
      <td>
        <a href="https://github.com/synesthesiam/en-us_julius-github/archive/v1.1.tar.gz">Download</a>
      </td>
      <td>English</td>
      <td>en-us</td>
      <td>julius</td>
      <td>&#9733; &#9733; &#9733; &#9733; (1x)</td>
      <td>
        <strong>UNTESTED</strong>
      </td>
    </tr>
    <tr>
      <td>
        <a href="https://github.com/synesthesiam/en-us_kaldi-zamia">View</a>
      </td>
      <td>
        <a href="https://github.com/synesthesiam/en-us_kaldi-zamia/archive/v2.0.tar.gz">Download</a>
      </td>
      <td>English</td>
      <td>en-us</td>
      <td>kaldi</td>
      <td>&#9733; &#9733; &#9733; &#9733; &#9733; (3x)</td>
      <td>&#9733; &#9733; &#9733; &#9733; (1x)</td>
    </tr>
    <tr>
      <td>
        <a href="https://github.com/synesthesiam/en-us_pocketsphinx-cmu">View</a>
      </td>
      <td>
        <a href="https://github.com/synesthesiam/en-us_pocketsphinx-cmu/archive/v1.1.tar.gz">Download</a>
      </td>
      <td>English</td>
      <td>en-us</td>
      <td>pocketsphinx</td>
      <td>&#9733; &#9733; &#9733; &#9733; &#9733; (9x)</td>
      <td>&#9733; &#9733; &#9733; &#9733; (2x)</td>
    </tr>
    <tr>
      <td>
        <a href="https://github.com/synesthesiam/fr_kaldi-guyot">View</a>
      </td>
      <td>
        <a href="https://github.com/synesthesiam/fr_kaldi-guyot/archive/v1.0.tar.gz">Download</a>
      </td>
      <td>French (Français)</td>
      <td>fr</td>
      <td>kaldi</td>
      <td>&#9733; &#9733; &#9733; &#9733; (4x)</td>
      <td>&#9733; &#9733; &#9733; &#9733; (1x)</td>
    </tr>
    <tr>
      <td>
        <a href="https://github.com/rhasspy/fr_kaldi-rhasspy">View</a>
      </td>
      <td>
        <a href="https://github.com/rhasspy/fr_rhasspy-kaldi/archive/v1.0.tar.gz">Download</a>
      </td>
      <td>French (Français)</td>
      <td>fr</td>
      <td>kaldi</td>
      <td>&#9733; &#9733; &#9733; &#9733; &#9733; (3x)</td>
      <td>&#9785; &#9785; &#9785; &#9785; &#9785; (0.5x)</td>
    </tr>
    <tr>
      <td>
        <a href="https://github.com/synesthesiam/fr_pocketsphinx-cmu">View</a>
      </td>
      <td>
        <a href="https://github.com/synesthesiam/fr_pocketsphinx-cmu/archive/v1.1.tar.gz">Download</a>
      </td>
      <td>French (Français)</td>
      <td>fr</td>
      <td>pocketsphinx</td>
      <td>&#9733; &#9733; &#9733; &#9733; (23x)</td>
      <td>&#9785; (3x)</td>
    </tr>
    <tr>
      <td>
        <a href="https://github.com/synesthesiam/de_pocketsphinx-cmu">View</a>
      </td>
      <td>
        <a href="https://github.com/synesthesiam/de_pocketsphinx-cmu/archive/v1.1.tar.gz">Download</a>
      </td>
      <td>German (Deutsch)</td>
      <td>de</td>
      <td>pocketsphinx</td>
      <td>&#9733; &#9733; &#9733; &#9733; &#9733; (17x)</td>
      <td>&#9733; &#9733; &#9733; &#9733; &#9733; (3x)</td>
    </tr>
    <tr>
      <td>
        <a href="https://github.com/synesthesiam/de_deepspeech-aashishag">View</a>
      </td>
      <td>
        <a href="https://github.com/synesthesiam/de_deepspeech-aashishag/archive/v1.0.tar.gz">Download</a>
      </td>
      <td>German (Deutsch)</td>
      <td>de-DE</td>
      <td>deepspeech</td>
      <td>&#9733; &#9733; &#9733; &#9733; &#9733; (1x)</td>
      <td>&#9733; &#9733; &#9733; &#9733; (1x)</td>
    </tr>
    <tr>
      <td>
        <a href="https://github.com/synesthesiam/de_kaldi-zamia">View</a>
      </td>
      <td>
        <a href="https://github.com/synesthesiam/de_kaldi-zamia/archive/v2.0.tar.gz">Download</a>
      </td>
      <td>German (Deutsch)</td>
      <td>de-DE</td>
      <td>kaldi</td>
      <td>&#9733; &#9733; &#9733; &#9733; &#9733; (4x)</td>
      <td>&#9733; &#9733; &#9733; &#9733; (1x)</td>
    </tr>
    <tr>
      <td>
        <a href="https://github.com/synesthesiam/el-gr_pocketsphinx-cmu">View</a>
      </td>
      <td>
        <a href="https://github.com/synesthesiam/el-gr_pocketsphinx-cmu/archive/v1.1.tar.gz">Download</a>
      </td>
      <td>Greek (Ελληνικά)</td>
      <td>el-gr</td>
      <td>pocketsphinx</td>
      <td>&#9733; &#9733; &#9733; &#9733; &#9733; (15x)</td>
      <td>&#9785; (1x)</td>
    </tr>
    <tr>
      <td>
        <a href="https://github.com/synesthesiam/hi_pocketsphinx-cmu">View</a>
      </td>
      <td>
        <a href="https://github.com/synesthesiam/hi_pocketsphinx-cmu/archive/v1.0.tar.gz">Download</a>
      </td>
      <td>Hindi (Devanagari)</td>
      <td>hi</td>
      <td>pocketsphinx</td>
      <td>
        <strong>UNTESTED</strong>
      </td>
      <td>
        <strong>UNTESTED</strong>
      </td>
    </tr>
    <tr>
      <td>
        <a href="https://github.com/synesthesiam/it_pocketsphinx-cmu">View</a>
      </td>
      <td>
        <a href="https://github.com/synesthesiam/it_pocketsphinx-cmu/archive/v1.1.tar.gz">Download</a>
      </td>
      <td>Italian (Italiano)</td>
      <td>it</td>
      <td>pocketsphinx</td>
      <td>&#9733; &#9733; &#9733; &#9733; &#9733; (21x)</td>
      <td>&#9733; &#9733; &#9733; &#9733; &#9733; (7x)</td>
    </tr>
    <tr>
      <td>
        <a href="https://github.com/rhasspy/it_kaldi-rhasspy">View</a>
      </td>
      <td>
        <a href="https://github.com/rhasspy/it_kaldi-rhasspy/archive/v1.0.tar.gz">Download</a>
      </td>
      <td>Italian (Italiano)</td>
      <td>it</td>
      <td>kaldi</td>
      <td>&#9733; &#9733; &#9733; &#9733; &#9733; (1x)</td>
      <td>&#9733; &#9733; &#9733; &#9733; &#9733; (1x)</td>
    </tr>
    <tr>
      <td>
        <a href="https://github.com/synesthesiam/kz_pocketsphinx-cmu">View</a>
      </td>
      <td>
        <a href="https://github.com/synesthesiam/kz_pocketsphinx-cmu/archive/v1.1.tar.gz">Download</a>
      </td>
      <td>Kazakh (қазақша)</td>
      <td>kz</td>
      <td>pocketsphinx</td>
      <td>
        <strong>UNTESTED</strong>
      </td>
      <td>
        <strong>UNTESTED</strong>
      </td>
    </tr>
    <tr>
      <td>
        <a href="https://github.com/synesthesiam/ko-kr_kaldi-montreal">View</a>
      </td>
      <td>
        <a href="https://github.com/synesthesiam/ko-kr_kaldi-montreal/archive/v1.0.tar.gz">Download</a>
      </td>
      <td>Korean</td>
      <td>ko-kr</td>
      <td>kaldi</td>
      <td>&#9785; (4x)</td>
      <td>&#9785; (4x)</td>
    </tr>
    <tr>
      <td>
        <a href="https://github.com/synesthesiam/zh-cn_pocketsphinx-cmu">View</a>
      </td>
      <td>
        <a href="https://github.com/synesthesiam/zh-cn_pocketsphinx-cmu/archive/v1.1.tar.gz">Download</a>
      </td>
      <td>Mandarin</td>
      <td>zh-cn</td>
      <td>pocketsphinx</td>
      <td>
        <strong>UNTESTED</strong>
      </td>
      <td>
        <strong>UNTESTED</strong>
      </td>
    </tr>
    <tr>
      <td>
        <a href="https://github.com/synesthesiam/pl_julius-github">View</a>
      </td>
      <td>
        <a href="https://github.com/synesthesiam/pl_julius-github/archive/v1.1.tar.gz">Download</a>
      </td>
      <td>Polish (polski)</td>
      <td>pl</td>
      <td>julius</td>
      <td>
        <strong>UNTESTED</strong>
      </td>
      <td>
        <strong>UNTESTED</strong>
      </td>
    </tr>
    <tr>
      <td>
        <a href="https://github.com/synesthesiam/pt-br_pocketsphinx-cmu">View</a>
      </td>
      <td>
        <a href="https://github.com/synesthesiam/pt-br_pocketsphinx-cmu/archive/v1.1.tar.gz">Download</a>
      </td>
      <td>Portuguese (Português)</td>
      <td>pt-br</td>
      <td>pocketsphinx</td>
      <td>&#9733; &#9733; &#9733; &#9733; (51x)</td>
      <td>&#9785; (11x)</td>
    </tr>
    <tr>
      <td>
        <a href="https://github.com/synesthesiam/ru_pocketsphinx-cmu">View</a>
      </td>
      <td>
        <a href="https://github.com/synesthesiam/ru_pocketsphinx-cmu/archive/v1.1.tar.gz">Download</a>
      </td>
      <td>Russian (Русский)</td>
      <td>ru</td>
      <td>pocketsphinx</td>
      <td>&#9733; &#9733; &#9733; &#9733; &#9733; (17x)</td>
      <td>&#9785; (1x)</td>
    </tr>
    <tr>
      <td>
        <a href="https://github.com/synesthesiam/es_pocketsphinx-cmu">View</a>
      </td>
      <td>
        <a href="https://github.com/synesthesiam/es_pocketsphinx-cmu/archive/v1.1.tar.gz">Download</a>
      </td>
      <td>Spanish (Español)</td>
      <td>es</td>
      <td>pocketsphinx</td>
      <td>&#9733; &#9733; &#9733; &#9733; (25x)</td>
      <td>&#9733; &#9733; &#9733; &#9733; (15x)</td>
    </tr>
    <tr>
      <td>
        <a href="https://github.com/synesthesiam/es-mexican_pocketsphinx-cmu">View</a>
      </td>
      <td>
        <a href="https://github.com/synesthesiam/es-mexican_pocketsphinx-cmu/archive/v1.1.tar.gz">Download</a>
      </td>
      <td>Spanish</td>
      <td>es-mexican</td>
      <td>pocketsphinx</td>
      <td>&#9733; &#9733; &#9733; &#9733; &#9733; (9x)</td>
      <td>&#9733; &#9733; &#9733; &#9733; (2x)</td>
    </tr>
    <tr>
      <td>
        <a href="https://github.com/synesthesiam/sv_kaldi-montreal">View</a>
      </td>
      <td>
        <a href="https://github.com/synesthesiam/sv_kaldi-montreal/archive/v1.1.tar.gz">Download</a>
      </td>
      <td>Swedish (svenska)</td>
      <td>sv</td>
      <td>kaldi</td>
      <td>&#9733; &#9733; &#9733; &#9733; (3x)</td>
      <td>&#9785; (1x)</td>
    </tr>
    <tr>
      <td>
        <a href="https://github.com/synesthesiam/vi_kaldi-montreal">View</a>
      </td>
      <td>
        <a href="https://github.com/synesthesiam/vi_kaldi-montreal/archive/v1.1.tar.gz">Download</a>
      </td>
      <td>Vietnamese (Tiếng Việt)</td>
      <td>vi</td>
      <td>kaldi</td>
      <td>&#9733; &#9733; &#9733; &#9733; &#9733; (4x)</td>
      <td>&#9785; (1x)</td>
    </tr>
  </tbody>
</table>

### Legend

Each profile is given a &#9733; rating, indicating how accurate it was at transcribing a set of test WAV files. I'm considering anything below 75% accuracy to be effectively unusable (&#9785;).

 | Transcription Accuracy                   |              |
 | ---------------------------------------- | ------------ |
 | &#9733; &#9733; &#9733; &#9733; &#9733;  | [95%, 100%]  |
 | &#9733; &#9733; &#9733; &#9733;          | [90%, 95%)   |
 | &#9733; &#9733; &#9733;                  | [85%, 90%)   |
 | &#9733; &#9733;                          | [80%, 85%)   |
 | &#9733;                                  | [75%, 80%)   |
 | &#9785;                                  | [0%, 75%)    |

Profiles are tested in two conditions:

1. **Closed**
    * All example sentences from the profile's [sentences.ini](https://voice2json.org/sentences.html) are run through [Google WaveNet](https://cloud.google.com/text-to-speech/docs/wavenet) to produce synthetic speech
    * The profile is trained and tested on *exactly* the sentences it should recognize (ideal case)
    * This resembles the intended use case of `voice2json`, though real world speech will be less perfect
2. **Open**
    * Speech examples are provided by contributors, [VoxForge](http://voxforge.org), or [Mozilla Common Voice](https://voice.mozilla.org/)
    * The profile is tested using the sample WAV files with the `--open` flag
    * This (usually) demonstrates why its best to define voice commands first!
    
Transcription **speed-up** is given as (*Nx*) where *N* is the average ratio of real-time to transcription time.
A value of 2x means that `voice2json` was able to transcribe the test WAV files twice as fast as their real-time durations on average.
The reported values come from an Intel Core i7-based laptop with 16GB of RAM, so expect slower transcriptions on Raspberry Pi's.

## Acknowledgements

The acoustic models and pronunciation dictionaries come from one of:

* [CMU Sphinx Acoustic Models](https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/)
* [Zamia ASR Models](https://github.com/gooofy/zamia-speech)
* [Montreal Forced Aligner Pretrained Models](https://montreal-forced-aligner.readthedocs.io/en/latest/pretrained_models.html)
* [Julius Models](https://sourceforge.net/projects/juliusmodels/)

When language models or grapheme-to-phoneme models were unavailable, they were generated using:

* Data from [Universal Dependencies](https://github.com/UniversalDependencies)
* The [Phonetisaurus](https://github.com/AdolfVonKleist/Phonetisaurus) G2P tool
