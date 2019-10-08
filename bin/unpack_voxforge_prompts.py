#!/usr/bin/env python3
import re
import sys
from pathlib import Path

def main():
    lines = Path(sys.argv[1]).read_text().splitlines()
    for line in lines:
        p, text = re.split(r"\s+", line, maxsplit=1)
        p = Path(p)
        p = Path(p.name + ".txt")
        p.write_text(text.lower())

if __name__ == "__main__":
    main()
