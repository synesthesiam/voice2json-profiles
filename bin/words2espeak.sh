#!/usr/bin/env bash
# Reads words from standard in and prints their eSpeak phonemes to standard out.

espeak_args=()
while [[ -n "$1" ]];
do
    if [[ "$1" == '--print-word' ]];
    then
        print_word='1'
    else
        espeak_args+=("$1")
    fi

    shift
done

# -----------------------------------------------------------------------------

echo 'Reading words from stdin...' >&2

while read line || [[ -n "${line}" ]];
do
    if [[ -n "${print_word}" ]]; then
        echo -n "${line} "
    fi

    phones="$(espeak-ng "${espeak_args[@]}" -q -x --sep=' ' "${line}" | sed -e 's/^[[:space:]]*//')"
    echo "${phones}"
done
