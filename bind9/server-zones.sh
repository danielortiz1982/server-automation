#!/bin/bash

##### Server Host Zone #####

rm -rf /etc/bind/named.conf.local
rm -rf /etc/bind/named.conf.options

cp ~/server-components/bind9/db.$EBLAST_DOMAIN_NAME /etc/bind/db.$EBLAST_DOMAIN_NAME
cp ~/server-components/bind9/named.conf.local /etc/bind/named.conf.local
cp ~/server-components/bind9/named.conf.options /etc/bind/named.conf.options

systemctl restart bind9
