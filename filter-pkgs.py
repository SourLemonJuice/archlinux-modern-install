#!/usr/bin/python3
import argparse
import sys

NAME = "install-pkgs.py"


def main():
    arg_parser = argparse.ArgumentParser(
        prog=NAME,
        description="Arch Linux Modern Install packages filter",
        usage="%(prog)s [-h | --help] <pkgs_path> [<pkgs...>]",
    )
    _, pkgs = arg_parser.parse_known_args()

    for pkg in pkgs:
        filter_one_file(pkg)


def filter_one_file(path: str):
    try:
        pkgs_file = open(path, "r", encoding="utf-8", newline="\n")
    except FileNotFoundError as err:
        print(f"{NAME}: File can't open: {err}", file=sys.stderr)
        sys.exit(1)

    for line in pkgs_file:
        line = line.removesuffix("\n")

        # remove blank
        if not line:
            continue
        # remove comment
        if line.startswith("#"):
            continue

        print(line)


main()
