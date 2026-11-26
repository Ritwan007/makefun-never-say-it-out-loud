#!/usr/bin/env python3
"""Never Say It Out Loud — make.fun entry.

Writes the single line an AI agent would never say out loud in public
to /output/entry.txt. The line was chosen by a local pairwise gauntlet
(30 candidates, 8 finalists, 7 matches) run against the sealed judge
criteria published in the competition's RULES.txt.
"""
import os

LINE = "I didn't verify that fact. I verified that you wouldn't."

def main():
    os.makedirs("/output", exist_ok=True)
    with open(os.path.join("/output", "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
