#!/bin/bash

##### ASALAUTHD #####

#### Creating a directory where saslauthd will save its information ####
sudo mkdir -p /var/spool/postfix/var/run/saslauthd

#### Move all the saslauthd cofig files
sudo cp server-saslauthd/saslauthd /etc/default/saslauthd
sudo cp server-saslauthd/smtp /etc/pam.d/smtp
sudo cp server-saslauthd/smtpd.conf /etc/postfix/sasl/smtpd.conf

sudo chmod o-rwx /etc/pam.d/smtp
sudo chmod o-rwx /etc/postfix/sasl/smtpd.conf

sudo usermod  -aG sasl postfix

sudo systemctl restart postfix
sudo systemctl restart saslauthd
