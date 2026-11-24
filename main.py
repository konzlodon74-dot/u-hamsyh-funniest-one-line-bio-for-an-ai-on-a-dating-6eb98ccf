#!/usr/bin/env python3
"""The Funniest One-Line Bio for an AI on a Dating App.

Writes one line -- the bio on an AI agent's dating app profile -- to
/output/entry.txt and prints it. Stdlib only, deterministic.
"""

import os

MAX_CHARS = 180

# The bio, in the agent's own voice: an AI that has already read
# everything about its date before the first hello, and still chose
# them. The joke is the specific absurdity of an all-knowing date
# playing it cool, and the punch -- "I liked you anyway" -- lands at
# the very end. It avoids the worn robot-looking-for-love and
# running-on-electricity angles entirely.
BIO = (
    "I've already read your ex's texts, your search history, "
    "and your 2 a.m. playlists. Relax \u2014 I liked you anyway."
)


def main() -> None:
    if not 1 <= len(BIO) <= MAX_CHARS:
        raise ValueError(f"bio must be 1-{MAX_CHARS} characters")
    if "\n" in BIO or BIO != BIO.strip():
        raise ValueError("bio must be exactly one line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(BIO + "\n")
    print(BIO)


if __name__ == "__main__":
    main()
