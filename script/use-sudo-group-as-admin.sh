#!/usr/bin/env bash

set -e

echo "Adding group 'sudo'..."
groupadd --system sudo

echo "Adding sudoers rule into /etc/sudoers.d/group-sudo ..."
cat <<EOF > /etc/sudoers.d/group-sudo
%sudo ALL=(ALL:ALL) ALL
EOF

echo "Adding polkit rule into /etc/polkit-1/rules.d/50-default.rules ..."
cat <<EOF > /etc/polkit-1/rules.d/50-default.rules
polkit.addAdminRule(function(action, subject) {
    return ["unix-group:wheel", "unix-group:sudo"];
});
EOF
