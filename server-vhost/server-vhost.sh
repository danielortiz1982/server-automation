#!/bin/bash

cp server-vhost/$SERVER_DOMAIN_NAME.conf /etc/apache2/sites-available/$SERVER_DOMAIN_NAME.conf

a2dissite 000-default.conf
a2ensite $SERVER_DOMAIN_NAME
systemctl reload apache2
systemctl restart apache2


##### Wordpress setup #####

sudo mkdir -p /var/www/$SERVER_DOMAIN_NAME/
sudo chown www-data: /var/www/$SERVER_DOMAIN_NAME
curl https://wordpress.org/latest.tar.gz | sudo -u www-data tar zx -C /var/www/$SERVER_DOMAIN_NAME
sudo -u www-data cp /var/www/$SERVER_DOMAIN_NAME/wordpress/wp-config-sample.php /var/www/$SERVER_DOMAIN_NAME/wordpress/wp-config.php
sudo -u www-data sed -i "s/database_name_here/$SERVER_DB_NAME/" /var/www/$SERVER_DOMAIN_NAME/wordpress/wp-config.php
sudo -u www-data sed -i "s/username_here/$SERVER_ADMIN_USER/" /var/www/$SERVER_DOMAIN_NAME/wordpress/wp-config.php
sudo -u www-data sed -i "s/password_here/$SERVER_ADMIN_PASSWORD/" /var/www/$SERVER_DOMAIN_NAME/wordpress/wp-config.php
