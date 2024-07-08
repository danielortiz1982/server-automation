#!/bin/bash

mysql -u root -e "CREATE DATABASE $EBLAST_DB_NAME;"
mysql -u root -e "CREATE USER '$EBLAST_DB_USER'@'localhost' IDENTIFIED BY '$EBLAST_DB_PASSWORD';"
mysql -u root -e "GRANT ALL PRIVILEGES ON * . * TO '$EBLAST_DB_USER'@'localhost';"
mysql -u root -e "FLUSH PRIVILEGES;"

systemctl restart mysql.service


