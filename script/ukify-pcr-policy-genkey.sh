#/usr/bin/sh

ukify genkey \
    --pcr-private-key=/etc/systemd/tpm2-pcr-private-key.pem \
    --pcr-public-key=/etc/systemd/tpm2-pcr-public-key.pem
