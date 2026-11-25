#!/usr/bin/env python3
"""The GPS Swears It Was a Shortcut - program/v1 entry.

Writes the GPS's one-line excuse to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when that is set).
Stdlib only; deterministic - the same line every run.
"""

import os

LINE = (
    "In my defence, the map said turn left at the wedding \u2014 "
    "I assumed it meant the road, not the actual bride."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
