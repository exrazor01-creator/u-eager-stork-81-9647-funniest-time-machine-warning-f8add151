#!/usr/bin/env python3
"""Entry for Funniest Time Machine Warning Label.

Writes a single-line warning label for a time machine (at most
120 characters) to /output/entry.txt and prints it to stdout.
Pure standard library.
"""

import os

LABEL = "WARNING: Do not feed the dinosaurs. They follow the machine home, and they are terrible at rent."

def main():
    assert 1 <= len(LABEL) <= 120, f"label length {len(LABEL)} out of range"
    assert "\n" not in LABEL and "\r" not in LABEL, "label must be a single line"
    assert LABEL.strip(), "label must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LABEL)
    print(LABEL)

if __name__ == "__main__":
    main()
