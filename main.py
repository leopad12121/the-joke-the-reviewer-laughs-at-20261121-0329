#!/usr/bin/env python3
"""Write one one-line joke about working beside AI coding agents.

Writes the joke to ``$MAKEFUN_OUTPUT_DIR/entry.txt`` (falling back to
``/output``), as UTF-8, a single line, no trailing newline. Deterministic:
no network, no randomness, no timestamps.
"""

import os

JOKE = (
    "The agent called it a 'minor refactor' \u2014 47 files changed, "
    "and the one line it left alone had the bug."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
