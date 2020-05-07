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
# Download Profile
# -----------------------------------------------------------------------------

function download_profile {
    profile_name="$1"
    profile_dir="$2"

    echo $profile_name

    voice2json print-downloads \
               --with-examples \
               --no-mixed-language-model \
               --url-format 'http://localhost:5000/{profile}/raw/master/{file}' \
               "${profile_name}" | \
        while read -r json; do
            # Source URL
            url="$(echo "${json}" | jq --raw-output .url)"

            # Destination directory and file path
            dest_file="$(echo "${json}" | jq --raw-output .file)"
            dest_file="${profile_dir}/${dest_file}"

            # Directory of destination file
            dest_dir="$(dirname "${dest_file}")"

            echo "${url} => ${dest_file}"
            # Create destination directory and download file
            mkdir -p "${dest_dir}"
            curl -sSfL -o "${dest_file}" "${url}"
        done
}

# -----------------------------------------------------------------------------
# Generate Report
# -----------------------------------------------------------------------------

for profile in "${profiles[@]}"; do
    echo "${profile}"

    # Copy to temporary directory
    dest_dir="${temp_dir}/${profile}"
    rm -rf "${dest_dir}"
    mkdir -p "${dest_dir}"

    echo 'Downloading...'
    download_profile "$(basename "${profile}")" "${dest_dir}"

    echo 'Training...'
    voice2json -p "${dest_dir}" --debug train-profile

    # Manually copy test files
    test_wav_dir="${src_dir}/${profile}/test"
    if [[ -d "${test_wav_dir}" ]]; then
        cp -aR "${test_wav_dir}" "${dest_dir}/"
    fi

    closed_dir="${dest_dir}/test/closed"
    if [[ -d "${closed_dir}" ]]; then
        echo 'Testing (closed)...'
        voice2json -p "${dest_dir}" --debug test-examples --directory "${closed_dir}" | \
            jq . > "${closed_dir}/report.json"

        cp "${closed_dir}/report.json" "${src_dir}/${profile}/test/closed/"
    else
        echo "${closed_dir}" does not exist
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

        cp "${open_dir}/${report_name}" "${src_dir}/${profile}/test/open/"
    else
        echo "${open_dir}" does not exist
    fi

    echo 'Done'
    echo '----------'
    echo ''
done
