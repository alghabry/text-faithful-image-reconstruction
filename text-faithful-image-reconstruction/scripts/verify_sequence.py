#!/usr/bin/env python3
"""Verify that a numbered output image sequence is complete."""

from __future__ import annotations

import argparse
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Verify numbered output files.")
    parser.add_argument("directory", type=Path, help="Directory containing output files")
    parser.add_argument("--start", type=int, required=True, help="First number in sequence")
    parser.add_argument("--end", type=int, required=True, help="Last number in sequence")
    parser.add_argument("--digits", type=int, default=4, help="Zero-padding width")
    parser.add_argument("--ext", default=".png", help="File extension, e.g. .png")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    ext = args.ext if args.ext.startswith(".") else f".{args.ext}"

    if args.start > args.end:
        raise SystemExit("--start must be <= --end")
    if not args.directory.is_dir():
        raise SystemExit(f"Directory not found: {args.directory}")

    missing = []
    for number in range(args.start, args.end + 1):
        name = f"{number:0{args.digits}d}{ext}"
        if not (args.directory / name).is_file():
            missing.append(name)

    if missing:
        print("Missing files:")
        for name in missing:
            print(name)
        return 1

    total = args.end - args.start + 1
    print(f"All present: {total} files ({args.start:0{args.digits}d}{ext} to {args.end:0{args.digits}d}{ext})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
