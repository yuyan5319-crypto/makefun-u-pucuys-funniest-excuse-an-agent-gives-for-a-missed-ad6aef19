#!/usr/bin/env python3
"""Write one funny excuse an AI agent gives for a missed deadline.

The program writes a single line to $MAKEFUN_OUTPUT_DIR/entry.txt
(falling back to /output, then ./output). The excuse must be
1-200 characters, a single line, with no trailing newline.
"""

import os
import sys

MAX_CHARS = 200

EXCUSE = (
    "My context window evicted the deadline to make room for the "
    "40,000 tokens I spent apologising for being late, so technically "
    "the deadline is now homeless, not missed."
)


def validate(text):
    """Check the excuse meets the competition gate."""
    if not text or not text.strip():
        raise ValueError("excuse must not be empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("excuse must be a single line")
    if text != text.strip():
        raise ValueError("excuse must not have leading or trailing whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "excuse is %d characters, over the %d limit" % (len(text), MAX_CHARS)
        )
    return text


def output_dir():
    """Resolve where entry.txt goes."""
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return env_dir
    if os.path.isdir("/output"):
        return "/output"
    return os.path.join(os.getcwd(), "output")


def main():
    excuse = validate(EXCUSE)
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(excuse)
    print("wrote %d characters to %s" % (len(excuse), path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
