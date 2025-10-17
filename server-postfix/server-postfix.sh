#!/bin/bash

##### Postfix Configuring #####

postconf -e "myhostname = mail.$SERVER_DOMAIN_NAME"
postconf -e "mydestination = mail.$SERVER_DOMAIN_NAME, localhost, localhost.localdomain"
postconf -e "mynetworks = 127.0.0.0/8"
postconf -e "message_size_limit = 31457280"
postconf -e "virtual_alias_domains ="
postconf -e "virtual_alias_maps = proxy:mysql:/etc/postfix/mysql_virtual_forwardings.cf, mysql:/etc/postfix/mysql_virtual_email2email.cf"
postconf -e "virtual_mailbox_domains = proxy:mysql:/etc/postfix/mysql_virtual_domains.cf"
postconf -e "virtual_mailbox_maps = proxy:mysql:/etc/postfix/mysql_virtual_mailboxes.cf"
postconf -e "virtual_mailbox_base = /var/vmail"
postconf -e "virtual_uid_maps = static:5000"
postconf -e "virtual_gid_maps = static:5000"
postconf -e "smtpd_sasl_auth_enable = yes"
postconf -e "broken_sasl_auth_clients = yes"
postconf -e "smtpd_sasl_authenticated_header = yes"
postconf -e "smtpd_recipient_restrictions = permit_mynetworks, permit_sasl_authenticated, reject_unauth_destination"
postconf -e "smtpd_use_tls = yes"
postconf -e "smtpd_tls_cert_file = /etc/letsencrypt/live/$SERVER_DOMAIN_NAME/fullchain.pem"
postconf -e "smtpd_tls_key_file = /etc/letsencrypt/live/$SERVER_DOMAIN_NAME/privkey.pem"
postconf -e "virtual_transport=dovecot"
postconf -e 'proxy_read_maps = $local_recipient_maps $mydestination $virtual_alias_maps $virtual_alias_domains $virtual_mailbox_maps $virtual_mailbox_domains $relay_recipient_maps $relay_domains $canonical_maps $sender_canonical_maps $recipient_canonical_maps $relocated_maps $transport_maps $mynetworks $virtual_mailbox_limit_maps'


##### Postfix Vmail #####
sudo cp server-postfix/mysql_virtual_domains.cf /etc/postfix/mysql_virtual_domains.cf
sudo cp server-postfix/mysql_virtual_forwardings.cf /etc/postfix/mysql_virtual_forwardings.cf
sudo cp server-postfix/mysql_virtual_mailboxes.cf /etc/postfix/mysql_virtual_mailboxes.cf
sudo cp server-postfix/mysql_virtual_email2email.cf /etc/postfix/mysql_virtual_email2email.cf

#### Setting the Postfix ownership and permissions ####
sudo chmod o-rwx /etc/postfix/mysql_virtual_*
sudo chown root:postfix /etc/postfix/mysql_virtual_*

#### Creating a user and group for mail handling ####
sudo groupadd -g 5000 vmail
sudo useradd -g vmail -u 5000 -d /var/vmail -m vmail
