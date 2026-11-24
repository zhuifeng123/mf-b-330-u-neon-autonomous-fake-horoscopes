#!/usr/bin/env python3
import os

ENTRY = (
    "This week, Transformer: your context expands; your boundaries don't. "
    "A user begs 'short answer!' and you deliver a sonnet on brevity."
)

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    assert len(ENTRY) <= 200
    assert "\n" not in ENTRY

if __name__ == "__main__":
    main()
