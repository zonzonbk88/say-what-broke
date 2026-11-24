#!/usr/bin/env python3
"""Say What Actually Broke — one line of honest error copy.

Writes a single line of software error copy (<=200 chars) to
/output/entry.txt: the brutal truth about the failure, funny on a
single read, shippable in a real error dialog.
"""

import os

LINE = (
    "The server is down because someone deployed on a Friday, "
    "and the database has filed for divorce. Try again Monday."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
    assert "\n" not in LINE, "line must be a single line"
    assert LINE.strip() == LINE, "no leading/trailing whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
