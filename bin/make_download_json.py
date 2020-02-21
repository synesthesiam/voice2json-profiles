#!/usr/bin/env python3
import argparse
import json
import os
import subprocess
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(prog="make_download_json.py")
    # parser.add_argument("url_base")
    parser.add_argument("profile_dir")
    parser.add_argument("files", nargs="+")
    args = parser.parse_args()

    # url_base = args.url_base
    profile_dir = Path(args.profile_dir).absolute()
    files = {}
    file_paths = {}
    for file_name in args.files:
        file_path = Path(file_name).absolute()
        if not file_path.is_file():
            # Skip directories
            continue

        file_suffix = file_path.suffix
        unzip = False
        has_parts = False

        if file_suffix.startswith(".part-"):
            file_path = file_path.with_suffix("")
            file_suffix = file_path.suffix
            has_parts = True

        if file_suffix == ".gz":
            file_path = file_path.with_suffix("")
            unzip = True

        file_key = str(file_path.relative_to(profile_dir))
        file_details = files.get(file_key)
        if not file_details:
            file_details = {
                "unzip": unzip,
                "url": f"{profile_dir.name}/raw/master/{file_key}",
            }

        if has_parts:
            file_parent_key = str(file_path.relative_to(profile_dir).parent)
            if not file_parent_key.endswith("/"):
                file_parent_key += "/"

            file_details["url"] = f"{profile_dir.name}/raw/master/{file_parent_key}"
            parts = file_details.get("parts", [])
            parts.append(
                {
                    "fragment": Path(file_name).name,
                    "bytes_expected": os.path.getsize(file_name),
                }
            )
            file_details["parts"] = parts
        elif unzip:
            file_details["url"] += ".gz"

            # Record zipped and unzipped sizes
            file_details["zip_bytes_expected"] = os.path.getsize(file_name)
            file_details["bytes_expected"] = int(
                subprocess.check_output(f"zcat '{file_path}' | wc -c", shell=True)
                .strip()
                .decode()
            )
        else:
            # Record size
            file_details["bytes_expected"] = os.path.getsize(file_name)

        files[file_key] = file_details
        file_paths[file_key] = file_path

    # Add sizes for files with parts
    for file_key, file_details in files.items():
        parts = file_details.get("parts")
        if parts:
            file_path = file_paths[file_key]
            sum_size = sum(part["bytes_expected"] for part in parts)
            if file_details["unzip"]:
                file_details["zip_bytes_expected"] = sum_size
                file_details["bytes_expected"] = int(
                    subprocess.check_output(
                        f"cat '{file_path}.gz'.part-* | zcat | wc -c", shell=True
                    )
                    .strip()
                    .decode()
                )
            else:
                file_details["bytes_expected"] = sum_size

    json.dump(
        {
            "conditions": {
                file_key: f"{profile_dir.name}/{file_key}" for file_key in files
            },
            "files": {
                f"{profile_dir.name}/{file_key}": file_details
                for file_key, file_details in files.items()
            },
        },
        sys.stdout,
        indent=4,
    )


# -----------------------------------------------------------------------------


def make_file(file_dict, file_details):
    file_path = file_details["path"]
    file_dict["unzip"] = file_details["unzip"]

    if file_dict["unzip"]:
        file_dict["zip_bytes_expected"] = os.path.getsize(file_path)
        file_dict["bytes_expected"] = int(
            subprocess.check_output(f"zcat '{file_path}' | wc -c", shell=True)
            .strip()
            .decode()
        )
    else:
        file_dict["bytes_expected"] = os.path.getsize(file_path)

    return file_dict


# -----------------------------------------------------------------------------

if __name__ == "__main__":
    main()
