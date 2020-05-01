#!/usr/bin/env python3
"""Verifies sizes and sha256 sums for files.yml files."""
import os
import subprocess
import sys
from pathlib import Path

import yaml


def main():
    """Main entry point"""
    for files_yaml_path in sys.argv[1:]:
        profile_root = Path(files_yaml_path).parent
        with open(files_yaml_path, "r") as files_yaml_file:
            files_yaml = yaml.safe_load(files_yaml_file)

        file_count = 0
        for condition, files in files_yaml.items():
            for file_path, file_info in files.items():
                full_path = profile_root / file_path

                # Check byte size
                expected_bytes = int(file_info["bytes"])
                actual_bytes = os.path.getsize(full_path)

                assert (
                    actual_bytes == expected_bytes
                ), f"Expected size of {full_path} to be {expected_bytes}, got {actual_bytes}"

                # Check sha256 sum
                expected_sum = str(file_info["sha256"]).strip()
                sum_result = subprocess.check_output(["sha256sum", str(full_path)]).decode().strip()
                actual_sum = sum_result.split()[0]

                assert (
                    actual_sum == expected_sum
                ), f"Expected sha256 sum of {full_path} to be {expected_sum}, got {actual_sum}"

                file_count += 1

        print(profile_root.name, file_count, "OK")


if __name__ == "__main__":
    main()
