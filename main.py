#!/usr/bin/env python3
"""One Word for Your Wi-Fi: write a single word to /output/entry.txt.

The word is Gaslighting: the Wi-Fi swears it is connected, full bars,
while nothing loads, and leaves you wondering whether the problem is
the router or you. The gate reads $MAKEFUN_OUTPUT_DIR/entry.txt, so
this program writes exactly that word there, with no trailing newline.
"""

import os
import sys

WORD = "Gaslighting"

# The gate accepts UTF-8 text of 1 to 20 characters, not only whitespace.
# Refuse to write an entry that cannot pass it instead of failing silently.
assert 1 <= len(WORD) <= 20 and WORD.strip() == WORD and not any(c.isspace() for c in WORD)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    with open(path, encoding="utf-8", newline="") as f:
        assert f.read() == WORD, "entry.txt round-trip mismatch"
    print(WORD)
    return 0


if __name__ == "__main__":
    sys.exit(main())
