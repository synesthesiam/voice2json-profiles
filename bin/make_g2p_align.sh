#!/usr/bin/env bash
set -e

# Creates a grapheme-to-phoneme alignment corpus from a pronunciation dictionary
# using phonetiaurus.

if [[ -z "$2" ]]; then
    echo "Usage: make-g2p_align.sh DICTIONARY_IN CORPUS_OUT"
    exit 1
fi

this_dir="$( cd "$( dirname "$0" )" && pwd )"

corpus_path="$(realpath "$2")"

# -----------------------------------------------------------------------------

temp_dir="$(mktemp -d)"
function finish {
    rm -rf "${temp_dir}"
}

trap finish EXIT

# -----------------------------------------------------------------------------

if [[ "$1" == '-' ]]; then
    # Read from stdin into temporary file
    dict_path="${temp_dir}/unformatted.dict"
    cat > "${dict_path}"
else
    dict_path="$(realpath "$1")"
fi

# Format dictionary for phonetisaurus
cd "${temp_dir}"
perl -pe 's/\([0-9]+\)//;
            s/[ ]+/ /g; s/^[ ]+//;
            s/[ ]+$//; @_ = split (/[ ]+/);
            $w = shift (@_);
            $_ = $w."\t".join (" ", @_)."\n";' < "${dict_path}" | sed -e '/[_|\xA0]/d' > formatted.dict

# Generate g2p corpus
"${this_dir}/phonetisaurus-alignment" --lexicon formatted.dict --seq2_del --verbose

# Copy out of temporary directory
cp train/model.corpus "${corpus_path}"
