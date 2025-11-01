#!/bin/bash

sudo sh server-dependencies/server-dependencies.sh
# sudo python3 server-db-setup/server-db-setup.py

## Bind9
sudo python3 server-bind9/server-bind9.py

## Apache2 Virtual Host
sudo python3 server-vhost/server-vhost.py

## Postfix
sudo python3 server-postfix/server-postfix.py

## Dovecot
sudo python3 server-dovecot/server-dovecot.py

## Saslauthd
sudo python3 server-saslauthd/server-saslauthd.py

# Reboot System
sudo reboot now
