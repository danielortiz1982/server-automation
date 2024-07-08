#!/bin/bash

cp ~/server-components/virtual-host/$EBLAST_DOMAIN_NAME.conf /etc/apache2/sites-available/$EBLAST_DOMAIN_NAME.conf

a2dissite 000-default.conf
a2ensite $EBLAST_DOMAIN_NAME
systemctl reload apache2
systemctl restart apache2
