#!/bin/bash

echo "y" | sudo ufw enable
echo "y" | sudo ufw allow 22
echo "y" | sudo ufw allow 587
echo "y" | sudo ufw allow 443
echo "y" | sudo ufw allow 993
echo "y" | sudo ufw allow bind9
echo "y" | sudo ufw allow https
echo "y" | sudo ufw allow postfix
echo "Server Automation UFW Enable and Rules Applied."
