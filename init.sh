#!/bin/bash

### Dependencies ###
sudo sh server-dependencies/server-dependencies.sh

### Mysql Database ###
sudo python3 server-db/server-db.py

## Bind9 ###
sudo python3 server-bind9/server-bind9.py

### Virtual Host ###
sudo python3 server-vhost/server-vhost.py

### Postfix ###
sudo python3 server-postfix/server-postfix.py

### Dovecot ###
sudo python3 server-dovecot/server-dovecot.py

### Saslauthd ###
sudo python3 server-saslauthd/server-saslauthd.py

echo "Server Automation Complete!"
