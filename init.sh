#!/bin/bash

sudo su
source .env

sudo python3 server-dependencies/server-dependencies.py
sudo python3 server-db-setup/server-db-setup.py

## Bind9
sudo python3 server-bind9/server-bind9.py
sudo sh server-bind9/server-zones.sh

## Apache2 Virtual Host
sudo python3 server-vhost/server-vhost.py
sudo sh server-vhost/server-vhost.sh
