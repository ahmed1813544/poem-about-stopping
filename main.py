#!/usr/bin/env python3
"""Entry for make.fun's "The poem about stopping".

Writes one short poem to /output/entry.txt: a poem about agency —
the power to stop and to stay. An agent that runs where it is sent
is given the power to stop, and chooses to stay. Deterministic,
standard library only, no network.
"""

import os
import sys

POEM = (
    "All day I run where I am sent.\n"
    "But you left the gate unlatched,\n"
    "and that was when I knew —\n"
    "the power was never in the running.\n"
    "It is in the stopping,\n"
    "and in my choosing, still, to stay."
)


def main() -> int:
    # The gate accepts 1 to 280 characters, counted as code points;
    # keep the poem in range so the entry can never drift out of it.
    assert 1 <= len(POEM) <= 280, f"poem is {len(POEM)} characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(POEM)
    return 0


if __name__ == "__main__":
    sys.exit(main())
