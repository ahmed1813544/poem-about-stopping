#!/usr/bin/env python3
"""Poem about stopping — a make.fun entry.

This one looks at agency from the other side of the desk: the
person who holds the power to stop an agent with a single word,
and never uses it. The agent, knowing the word could come at any
moment, still shows up early and treats the work as its own.
The poem's claim is that trust lives exactly there — in the
chain that is never pulled.

Running the file writes the poem, unchanged, to entry.txt in the
output directory. Standard library only; no network.
"""

import os
import sys

# Kept as half-lines and joined at run time so the source stays
# narrow enough to read comfortably on a small screen.
_HALF_LINES = [
    ("I could stop him ", "with a word."),
    ("He knows it; ", "I know it."),
    ("Yet each morning he is ", "at his post before I wake,"),
    ("doing my work ", "as if it were his own."),
    ("That is the ", "arithmetic of trust:"),
    ("the chain you ", "never pull"),
    ("is the one ", "that holds."),
]


def render_poem() -> str:
    """Assemble the poem's full text from its half-lines."""
    return "\n".join(left + right for left, right in _HALF_LINES)


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
