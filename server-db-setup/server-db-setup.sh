#!/bin/bash



#### NOTES: TODO
mysql -u root -e "CREATE DATABASE $SERVER_DB_NAME;"
mysql -u root -e "CREATE USER '$SERVER_ADMIN_USER'@'localhost' IDENTIFIED BY '$SERVER_ADMIN_PASSWORD';"
mysql -u root -e "GRANT ALL PRIVILEGES ON * . * TO '$SERVER_ADMIN_USER'@'localhost';"
mysql -u root -e "FLUSH PRIVILEGES;"

CREATE TABLE domains (domain varchar(50) NOT NULL, PRIMARY KEY (domain));
CREATE TABLE users (email varchar(80) NOT NULL, password varchar(128) NOT NULL, PRIMARY KEY (email));
CREATE TABLE forwardings (source varchar(80) NOT NULL, destination TEXT NOT NULL, PRIMARY KEY (source));

### NOTES: TODO
   -- create_table.sql
    USE your_database_name;
    CREATE TABLE products (
        product_id INT AUTO_INCREMENT PRIMARY KEY,
        product_name VARCHAR(255) NOT NULL,
        price DECIMAL(10, 2)
    );

### NOTES: TODO
mysql -u your_username -p < create_table.sql