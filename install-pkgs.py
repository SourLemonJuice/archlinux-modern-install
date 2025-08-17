#!/usr/bin/python3
import sys
import subprocess

MSG_PREFIX = "install-pkgs.py: "

match len(sys.argv):
    case 1:
        print(MSG_PREFIX + "The packages list file wasn't given.", file=sys.stderr)
        sys.exit(1)
    case 2:
        pass
    case _:
        print(MSG_PREFIX + "Too many arguments.", file=sys.stderr)
        sys.exit(1)

pkgs_path = sys.argv[1]

try:
    pkgs_file = open(pkgs_path, "r", encoding="utf-8", newline="\n")
except FileNotFoundError as err:
    print(MSG_PREFIX + f"File can't open: {err}", file=sys.stderr)
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
