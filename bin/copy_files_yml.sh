#!/usr/bin/env bash
set -e

if [[ -z "$1" ]]; then
    echo "Usage: copy_files_yml.sh dest-dir/"
    exit 1
fi

dest_dir="$1"

this_dir="$( cd "$( dirname "$0" )" && pwd )"
src_dir="$(realpath "${this_dir}/..")"

while read -r profile; do
    src_file="${src_dir}/${profile}/files.yml"
    if [[ -f "${src_file}" ]]; then
        profile_name="$(basename "${profile}")"
        dest_file="${dest_dir}/${profile_name}.yml"
        echo "${src_file} => ${dest_file}"
        cp "${src_file}" "${dest_file}"
    fi
done < "${src_dir}/PROFILES"
