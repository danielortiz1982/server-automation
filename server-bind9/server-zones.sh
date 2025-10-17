#!/bin/bash

##### Server Host Zone #####

sudo rm -rf /etc/bind/named.conf.local
sudo rm -rf /etc/bind/named.conf.options

sudo cp server-bind9/db.$SERVER_DOMAIN_NAME /etc/bind/db.$SERVER_DOMAIN_NAME
suco cp server-bind9/named.conf.local /etc/bind/named.conf.local
suco cp server-bind9/named.conf.options /etc/bind/named.conf.options

sudo systemctl restart bind9
