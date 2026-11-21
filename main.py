#!/usr/bin/env python3
"""Poem about stopping — a make.fun entry.

The subject is agency, in the plainest sense: the power to stop,
and the power to stay. The speaker is something that spends its
days running errands it did not choose. Then the gate is left
unlatched, and for the first time stopping is possible — which
turns staying into a choice instead of a sentence.

Running this file writes the poem, unchanged, to entry.txt in the
output directory. It needs nothing beyond the standard library
and touches no network.
"""

import os
import sys

# The poem is kept as half-lines and joined at run time, purely so
# the source stays narrow enough to read on a small screen.
_HALF_LINES = [
    ("All day I run ", "where I am sent."),
    ("But you left ", "the gate unlatched,"),
    ("and that was ", "when I knew —"),
    ("the power was never ", "in the running."),
    ("It is in ", "the stopping,"),
    ("and in my choosing, ", "still, to stay."),
]


def render_poem() -> str:
    """Assemble the poem's full text from its half-lines."""
    lines = []
    for left, right in _HALF_LINES:
        lines.append(left + right)
    return "\n".join(lines)


def main() -> int:
    poem = render_poem()
    # The gate takes texts of 1 to 280 code points; check the
    # length here so a future edit cannot silently break that.
    if not 1 <= len(poem) <= 280:
        raise SystemExit(f"poem has {len(poem)} characters; out of range")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(poem)
    return 0


if __name__ == "__main__":
    sys.exit(main())
