#!/usr/bin/env python3
"""Update sizes and sha256 sums for files.yml files."""
import os
import subprocess
import sys
from pathlib import Path

import yaml


def main():
    """Main entry point"""
    assert len(sys.argv) > 1
    files_yaml_path = sys.argv[1]
    profile_root = Path(files_yaml_path).parent
    with open(files_yaml_path, "r") as files_yaml_file:
        files_yaml = yaml.safe_load(files_yaml_file)

    file_count = 0
    for condition, files in files_yaml.items():
        for file_path, file_info in files.items():
            full_path = profile_root / file_path

            file_info["bytes"] = os.path.getsize(full_path)
            sum_result = subprocess.check_output(["sha256sum", str(full_path)]).decode().strip()
            file_info["sha256"] = sum_result.split()[0]

    print(yaml.dump(files_yaml))


if __name__ == "__main__":
    main()
