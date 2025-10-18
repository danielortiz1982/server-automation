#!/bin/bash

sudo sh server-dependencies/server-dependencies.sh
# sudo python3 server-db-setup/server-db-setup.py

## Bind9
sudo python3 server-bind9/server-bind9.py
sudo sh server-bind9/server-zones.sh

## Apache2 Virtual Host
sudo python3 server-vhost/server-vhost.py
sudo sh server-vhost/server-vhost.sh


## Postfix
# sudo python3 server-postfix/server-postfix.py
# sudo sh server-postfix/server-postfix.sh

## Dovecot
# sudo python3 server-dovecot/server-dovecot.py
# sudo sh server-dovecot/server-dovecot.sh


## Saslauthd
# sudo python3 server-saslauthd/server-saslauthd.py
# sudo sh server-saslauthd/server-saslauthd.sh
