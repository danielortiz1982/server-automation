#!/bin/bash

### Server Dependencies ###
sudo sh server_dependencies/server_dependencies.sh
### Mysql Database ###
sudo python3 server_db/server_db.py
## Bind9 Zones ###
sudo python3 server_bind9/server_bind9.py
### Virtual Host ###
sudo python3 server_vhost/server_vhost.py
### Postfix ###
sudo python3 server_postfix/server_postfix.py
### Dovecot ###
sudo python3 server_dovecot/server_dovecot.py
### Saslauthd ###
sudo python3 server_saslauthd/server_saslauthd.py
### DKIM & DMARC ###
# sudo python3 server_dkim/server_dkim.py
### Exit Message ###
echo "Server Automation Complete!"
