#!/bin/bash

### Server Dependencies ###
sudo sh server_dependencies/server_dependencies.sh
### Server Network Hosts
sudo python3 server_hosts/server_hosts.py
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
sudo python3 server_dkim/server_dkim.py
### Certbot & SSL ###
sudo python3 server_ssl/server_ssl.py
### UFW Rules ###
sudo sh server_ufw/server-ufw.sh
### Restart Services ###
sudo systemctl restart bind9
sudo systemctl restart apache2
sudo systemctl restart mysql
sudo systemctl restart postfix
sudo systemctl restart dovecot
sudo systemctl restart saslauthd
sudo systemctl restart opendkim
### Print Service Status ###
sudo systemctl status bind9
sudo systemctl status apache2
sudo systemctl status mysql
sudo systemctl status postfix
sudo systemctl status dovecot
sudo systemctl status saslauthd
sudo systemctl status opendkim
### Exit Message ###
echo "Server Automation Complete!"
