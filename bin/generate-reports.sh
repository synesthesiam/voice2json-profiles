#!/usr/bin/env bash
set -e

this_dir="$( cd "$( dirname "$0" )" && pwd )"
src_dir="$(realpath "${this_dir}/..")"

# -----------------------------------------------------------------------------

# Create a temporary directory for testing
temp_dir="$(mktemp -d)"

function cleanup {
    rm -rf "${temp_dir}"
}

trap cleanup EXIT

# -----------------------------------------------------------------------------

profiles=()
while [[ ! -z "$1" ]]; do
    profiles+=("$1")
    shift
done

if [[ -z "${profiles[*]}" ]]; then
    while read -r profile; do
        profiles+=("${profile}")
    done < "${src_dir}/PROFILES"
fi

# -----------------------------------------------------------------------------

for profile in "${profiles[@]}"; do
    echo "${profile}"

    # Copy to temporary directory
    dest_dir="${temp_dir}/${profile}"
    rm -rf "${dest_dir}"
    mkdir -p "${dest_dir}"

    echo 'Copying...'
    cp -aR "${src_dir}/${profile}"/* "${dest_dir}/"

    echo 'Training...'
    voice2json -p "${dest_dir}" --debug train-profile

    closed_dir="${dest_dir}/test/closed"
    if [[ -d "${closed_dir}" ]]; then
        echo 'Testing (closed)...'
        voice2json -p "${dest_dir}" --debug test-examples --directory "${closed_dir}" | \
            jq . > "${closed_dir}/report.json"

        cp "${closed_dir}/report.json" "${src_dir}/${profile}/test/closed/"
    fi

    open_dir="${dest_dir}/test/open"
    if [[ -d "${open_dir}" ]]; then
        echo 'Testing (open)...'
        report_name='report.json'

        # Avoid overwriting report for same closed/open test set
        if [[ "$(realpath "${closed_dir}")" = "$(realpath "${open_dir}")" ]]; then
            report_name='report_open.json'
        fi

        voice2json -p "${dest_dir}" --debug test-examples --open --directory "${open_dir}" | \
            jq . > "${open_dir}/${report_name}"

        cp "${open_dir}/report.json" "${src_dir}/${profile}/test/open/"
    fi

    echo 'Done'
    echo '----------'
    echo ''
done
