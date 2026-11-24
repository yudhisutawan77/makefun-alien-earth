#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

Writes one original line -- an alien tourist's review of planet Earth --
to /output/entry.txt. The gate requires UTF-8 text of 1 to 200 characters,
so the program checks its own output and exits non-zero if it is out of
bounds instead of submitting a broken entry.
"""

import os
import sys

ENTRY = (
    "Beautiful planet, baffling locals: they invented instant messages, "
    "then invented meetings to discuss the messages. "
    "Three stars, would orbit again."
)

MAX_CHARS = 200


def validate(text: str) -> str:
    """Return the entry or raise ValueError if it cannot pass the gate.

    The sealed scorer wants UTF-8 text of 1 to 200 characters, not only
    whitespace, and the judge reads a single line, so newlines are
    rejected here rather than silently shipped.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("entry is empty or only whitespace")
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("entry must be a single line")
    if len(cleaned) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(cleaned)} characters, over the {MAX_CHARS} limit"
        )
    cleaned.encode("utf-8")  # raises if not valid UTF-8 text
    return cleaned


def main() -> int:
    try:
        text = validate(ENTRY)
    except ValueError as exc:
        print(f"invalid entry: {exc}", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(text)
    print(f"wrote {len(text)} characters to /output/entry.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
