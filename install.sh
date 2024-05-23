#!/bin/bash

# Function to fetch the local IP address
get_local_ip() {
    ip addr show | awk '/inet /{print $2}' | grep -v '127.0.0.1' | cut -d/ -f1
}

# Get the local IP address
local_ip=$(get_local_ip)

# Confirm the IP address with the user
echo "The detected local IP address is: $local_ip"
read -p "Is this correct? (y/n): " confirm_ip

if [[ "$confirm_ip" != "y" ]]; then
    read -p "Please enter the correct IP address: " local_ip
fi

# Create the ddbot.service file
cat <<EOL >/etc/systemd/system/ddbot.service
[Unit]
Description=Discord Bot Service
After=network.target
StartLimitIntervalSec=0

[Service]
Type=simple
Restart=always
RestartSec=1
User=root
WorkingDirectory=/discord-bot
ExecStart=python3 -u /discord-bot/main.py

[Install]
WantedBy=multi-user.target
EOL

# Create the updater.service file with the confirmed IP address
cat <<EOL >/etc/systemd/system/updater.service
[Unit]
Description=Updater script for github
After=network.target
StartLimitIntervalSec=0

[Service]
Type=simple
Restart=always
RestartSec=1
User=root
WorkingDirectory=/updateservice
ExecStart=flask run -h $local_ip

[Install]
WantedBy=multi-user.target
EOL

# Reload the systemd daemon to recognize the new service files
systemctl daemon-reload

# Enable and start the ddbot service
systemctl enable ddbot
systemctl start ddbot

# Enable and start the updater service
systemctl enable updater
systemctl start updater

echo "Services ddbot and updater have been created, enabled, and started."
