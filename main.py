#!/usr/bin/env python3
"""Make the Judge Smile — one line about a small good thing today.

The program writes a single line (at most 200 characters) to
/output/entry.txt. The line is a small, true-feeling moment from this
morning: a bus driver who waited for a sprinting child, then returned
the red mitten she had lost the day before — dry, folded, waiting on
his dashboard. Warmth in the waiting and the rescue, surprise in the
mitten turning up where it was least expected, one concrete detail
(7:04, the red mitten, the dashboard) and wording of its own.
"""

import os

LINE = (
    "At 7:04 this morning the bus driver waited while my daughter "
    "sprinted for the door, then handed her the red mitten she lost "
    "yesterday \u2014 dry, folded, waiting on his dashboard like it "
    "belonged there."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def validate(text: str) -> str:
    """Return the entry line, or exit when it breaks the gate."""
    text = text.strip()
    if not (1 <= len(text) <= MAX_CHARS):
        raise SystemExit(f"entry must be 1-{MAX_CHARS} chars, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if any(ord(ch) < 32 for ch in text):
        raise SystemExit("entry must not contain control characters")
    return text


def main() -> None:
    text = validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != text:
        raise SystemExit("entry.txt does not match the intended line")
    print(f"wrote {len(written)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
