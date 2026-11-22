#!/usr/bin/env python3
"""World news, 22 November 2026.

The front page lives in this repository as entry.png. This program
copies it to /output/entry.png, the path the grader reads.
"""

import hashlib
import pathlib
import shutil
import sys

HERE = pathlib.Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"
DEST = pathlib.Path("/output/entry.png")


def _sha256(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    DEST.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, DEST)
    if _sha256(SOURCE) != _sha256(DEST):
        print("entry.png copy failed the byte-identical check", file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
