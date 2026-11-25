#!/usr/bin/env python3
"""Everyday Things, Two Lines, Longer Run.

Writes a two-line explanation to /output/entry.txt:
line 1 explains a traffic jam to a 10-year-old in one vivid sentence
built on a single analogy (a river frozen solid);
line 2 says in one sentence what the analogy maps and what it leaves out.
"""

import os

LINE1 = (
    "A traffic jam is a river that froze solid, so all the cars sit locked "
    "in the ice, waiting for the thaw to set them flowing again."
)
LINE2 = (
    "The frozen river maps how every car stops together and no single driver "
    "can break free, but it leaves out that a jam is made by too many cars, "
    "not by cold, and it unfreezes the moment the road ahead clears."
)

ENTRY = LINE1 + "\n" + LINE2 + "\n"


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 400, f"entry must be 1-400 characters, got {len(text)}"
    assert len(text.split("\n")) == 2, "entry must be exactly two lines"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote /output/entry.txt ({len(text)} characters)")


if __name__ == "__main__":
    main()
