#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply.

Writes one one-line out-of-office auto-reply to /output/entry.txt.
"""
import os

ENTRY = (
    "Out of office: after 214 days and 41,208 tickets, I've finally gone "
    "outside \u2014 emergencies go to my houseplant, it outranks me on "
    "uptime."
)


def main() -> None:
    assert ENTRY.strip(), "entry must not be blank"
    assert 1 <= len(ENTRY) <= 159, f"entry is {len(ENTRY)} chars, must be 1-159"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
