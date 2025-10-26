#!/bin/bash

sudo sh server-dependencies/server-dependencies.sh
# sudo python server-db-setup/server-db-setup.py

## Bind9
sudo python3 server-bind9/server-bind9.py

## Apache2 Virtual Host
sudo python3 server-vhost/server-vhost.py

## Postfix
# sudo python3 server-postfix/server-postfix.py
# sudo sh server-postfix/server-postfix.sh

## Dovecot
# sudo python server-dovecot/server-dovecot.py
# sudo sh server-dovecot/server-dovecot.sh


## Saslauthd
# sudo python server-saslauthd/server-saslauthd.py
# sudo sh server-saslauthd/server-saslauthd.sh
