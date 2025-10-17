#!/bin/bash

##### Dovecot Vmail #####

sudo rm -rf /etc/postfix/master.cf
sudo cp server-dovecot/master.cf /etc/postfix/master.cf
sudo cp server-dovecot/dovecot.conf /etc/dovecot/dovecot.conf
sudo cp server-dovecot/dovecot-sql.conf /etc/dovecot/dovecot-sql.conf

sudo systemctl restart dovecot
