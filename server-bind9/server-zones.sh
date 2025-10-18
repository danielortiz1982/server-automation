#!/bin/bash

##### Server Host Zone #####

sudo rm -rf /etc/bind/named.conf.local
sudo rm -rf /etc/bind/named.conf.options

sudo cp server-bind9/db.$SERVER_DOMAIN_NAME /etc/bind/db.$SERVER_DOMAIN_NAME
sudo cp server-bind9/named.conf.local /etc/bind/named.conf.local
sudo cp server-bind9/named.conf.options /etc/bind/named.conf.options

sudo systemctl restart bind9
