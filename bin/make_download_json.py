#!/usr/bin/env python3
import argparse
import json
import os
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
    for file_name in args.files:
        file_path = Path(file_name).absolute()
        file_key = str(file_path.relative_to(profile_dir))
        files[file_key] = file_path

    json.dump(
        {
            "conditions": {
                file_key: f"{profile_dir.name}/{file_key}" for file_key in files
            },
            "files": {
                f"{profile_dir.name}/{file_key}": {
                    "url": f"{profile_dir.name}/raw/master/{file_key}",
                    "bytes_expected": os.path.getsize(file_path),
                    "unzip": file_path.suffix == ".gz",
                }
                for file_key, file_path in files.items()
            },
        },
        sys.stdout,
        indent=4,
    )


# -----------------------------------------------------------------------------

if __name__ == "__main__":
    main()
