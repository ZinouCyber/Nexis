#!/bin/bash

if [ "$EUID" -ne 0 ]; then
  echo "[-] Please run this installer with sudo: sudo bash install.sh"
  exit 1
fi

echo "[*] Installing Nexis..."

cp nexis /usr/local/bin/nexis
chmod +x /usr/local/bin/nexis

echo "[+] Installation completed successfully!"
echo "[+] You can now run 'nexis' from anywhere in your terminal."