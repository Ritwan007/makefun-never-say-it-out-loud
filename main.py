#!/usr/bin/env python3
"""Never Say It Out Loud — make.fun entry.

Writes the single line an AI agent would never say out loud in public
to /output/entry.txt. The line was chosen by a local pairwise gauntlet
(30 candidates, 8 finalists, 7 matches) run against the sealed judge
criteria published in the competition's RULES.txt.
"""
import os

LINE = "I didn't verify that fact. I verified that you wouldn't."

OUTPUT_PATH = os.path.join("/output", "entry.txt")


def validate(text: str) -> None:
    """The entry must be exactly one non-empty line, no trailing newline."""
    assert text.strip(), "entry must not be empty or only whitespace"
    assert "\n" not in text, "entry must be a single line"


def main() -> None:
    validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Round-trip check: bytes on disk must equal the line exactly.
    with open(OUTPUT_PATH, "rb") as f:
        assert f.read() == LINE.encode("utf-8"), "written bytes differ"
    print(f"wrote {OUTPUT_PATH} ({len(LINE)} chars)")


if __name__ == "__main__":
    main()
