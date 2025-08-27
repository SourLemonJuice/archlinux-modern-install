#!/usr/bin/env bash
# In some case, this repo's etc folder has some really bad permissions.
# It may be caused by the USB's exFAT filesystem or GitHub's ZIP download.

if [[ -z "$1" || "$1" == "--help" ]]; then
    echo "Usage: [--help] <source> <destination>"
    exit 0
fi

cat "$1" > "$2"
