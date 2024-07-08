#!/bin/bash

##### Wordpress setup #####

sudo mkdir -p /var/www/$EBLAST_DOMAIN_NAME/
sudo chown www-data: /var/www/$EBLAST_DOMAIN_NAME
curl https://wordpress.org/latest.tar.gz | sudo -u www-data tar zx -C /var/www/$EBLAST_DOMAIN_NAME
sudo -u www-data cp /var/www/$EBLAST_DOMAIN_NAME/wordpress/wp-config-sample.php /var/www/$EBLAST_DOMAIN_NAME/wordpress/wp-config.php
sudo -u www-data sed -i "s/database_name_here/$EBLAST_DB_NAME/" /var/www/$EBLAST_DOMAIN_NAME/wordpress/wp-config.php
sudo -u www-data sed -i "s/username_here/$EBLAST_DB_USER/" /var/www/$EBLAST_DOMAIN_NAME/wordpress/wp-config.php
sudo -u www-data sed -i "s/password_here/$EBLAST_DB_PASSWORD/" /var/www/$EBLAST_DOMAIN_NAME/wordpress/wp-config.php
