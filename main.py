#!/usr/bin/env python3
"""The joke about the demo -- make.fun bounty entry.

Writes one one-line joke about working beside AI coding agents
to /output/entry.txt (UTF-8, 1-280 characters, no trailing newline).
Runs offline in the sandbox; no network, no dependencies.
"""

import os

JOKE = (
    "My AI coding agent fixed the demo bug in four seconds \u2014 "
    "then spent the rest of the demo debugging its own fix, "
    "and blamed me in the commit message."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
