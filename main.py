#!/usr/bin/env python3
"""One-Liner Marathon — make.fun entry.

Writes the winning one-line comedy joke to /output/entry.txt.
The line is a single line, 149 characters (limit 280), chosen by a local
pairwise tournament judged against the bounty's published judge brief
(see README.md for the tournament table).
"""

import os

# Winning line (tournament winner — see README.md).
# Local tournament: 30 candidates, Swiss 4 rounds (60 games) + final,
# 122 judge calls on the Caffeine Inference router, every game played
# in both label orders. #7 and #30 tied the Swiss at 3.5 each; the final
# split 0.5–0.5 (each won the order in which it was listed first), so #7
# took it on the pre-declared tie-break (equal Swiss score, lower id).
ENTRY = (
    "My horoscope said to avoid financial decisions today, so I bought "
    "a lottery ticket \u2014 technically that's not a decision, it's a "
    "prayer with a receipt."
)


def main() -> None:
    line = ENTRY.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 280, f"entry must be 1-280 chars, got {len(line)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    print(f"Wrote {len(line)} chars to /output/entry.txt")
    print(line)


if __name__ == "__main__":
    main()
