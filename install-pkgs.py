#!/usr/bin/python3
import argparse
import sys
import subprocess

NAME = "install-pkgs.py"

arg_parser = argparse.ArgumentParser(
    prog=NAME,
    description="Arch Linux Modern Install packages installer",
    usage="%(prog)s [-h | --help] <pkgs_path>",
)
arg_parser.add_argument("pkgs_path")
args = arg_parser.parse_args()

try:
    pkgs_file = open(args.pkgs_path, "r", encoding="utf-8", newline="\n")
except FileNotFoundError as err:
    print(f"{NAME}: File can't open: {err}", file=sys.stderr)
    sys.exit(1)

pkgs = []
for line in pkgs_file:
    line = line.removesuffix("\n")

    # remove blank
    if not line:
        continue
    # remove comment
    if line.startswith("#"):
        continue

    pkgs.append(line)

# install packages
try:
    subprocess.run(["pacman", "-Sy"] + pkgs, check=True)
except subprocess.CalledProcessError as err:
    sys.exit(err.returncode)
