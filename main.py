#!/usr/bin/env python3
"""One Letter for Your Day.

Writes exactly one letter, A to Z, to /output/entry.txt (or to the
directory named by MAKEFUN_OUTPUT_DIR when it is set).

The letter is the initial of the single word that describes the day.
It is read from entry.txt, kept beside this script, so the program
copies the entry rather than hard-coding it.
"""

import os
import sys
from pathlib import Path
from typing import NoReturn

HERE = Path(__file__).resolve().parent


def fail(message: str) -> "NoReturn":
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    source = HERE / "entry.txt"
    letter = source.read_text(encoding="utf-8").strip()

    # Fail loudly rather than ever writing an invalid entry: the sealed
    # scorer only accepts exactly one letter, A to Z.
    if len(letter) != 1 or not ("A" <= letter <= "Z"):
        fail(f"entry.txt must hold exactly one letter A-Z, got {letter!r}")

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(letter + "\n", encoding="utf-8")

    # Read back what was written and verify it before reporting success.
    written = out_path.read_text(encoding="utf-8")
    if written != letter + "\n":
        fail(f"wrote unexpected content to {out_path}: {written!r}")


if __name__ == "__main__":
    main()
