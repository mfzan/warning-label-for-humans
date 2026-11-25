#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh.

Writes the entry line -- the safety warning label that should come printed
on every human being -- verbatim to /output/entry.txt: exactly one line,
no trailing newline, UTF-8.
"""

import os

ENTRY = (
    "WARNING: This unit remembers your most embarrassing moment from 2009 "
    "in perfect detail, but cannot recall why it entered this room."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # The entry must be a single line of at most 160 characters.
    assert "\n" not in ENTRY, "entry line must not contain a newline"
    assert ENTRY == ENTRY.strip(), "entry line must have no surrounding whitespace"
    assert 1 <= len(ENTRY) <= 160, "entry line must be 1-160 characters"

    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Only chmod the file itself -- never the /output directory, which is
    # root-owned and merely writable (chmod on it raises PermissionError).
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
