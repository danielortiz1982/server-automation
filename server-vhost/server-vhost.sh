#!/bin/bash

cp server-vhost/$SERVER_DOMAIN_NAME.conf /etc/apache2/sites-available/$SERVER_DOMAIN_NAME.conf

a2dissite 000-default.conf
a2ensite $SERVER_DOMAIN_NAME
systemctl reload apache2
systemctl restart apache2
