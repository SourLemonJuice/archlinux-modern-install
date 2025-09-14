#!/usr/bin/env bash

set -e

if [[ -z "$1" || -z "$2" ]]; then
    echo "Usage: install-config.sh <src_etc> <dest_etc>"
    exit 1
fi

src="$1"
dest="$2"

mkdir --verbose --parents "${dest}/sysconfig"
install --verbose --mode 644 ${src}/sysconfig/* ${dest}/sysconfig

mkdir --verbose --parents "${dest}/kernel"
install --verbose --mode 600 ${src}/kernel/* ${dest}/kernel

mkdir --verbose --parents "${dest}/dracut.conf.d"
install --verbose --mode 600 ${src}/dracut.conf.d/* ${dest}/dracut.conf.d

mkdir --verbose --parents "${dest}/NetworkManager/conf.d"
install --verbose --mode 644 ${src}/NetworkManager/conf.d/* ${dest}/NetworkManager/conf.d

mkdir --verbose --parents "${dest}/systemd/resolved.conf.d"
install --verbose --mode 644 ${src}/systemd/resolved.conf.d/* ${dest}/systemd/resolved.conf.d

install --verbose --mode 644 "${src}/chrony.conf" "${dest}/chrony.conf"
