#!/bin/bash

##### Server Dependencies #####

sudo apt-get install curl -y
sudo apt-get install git -y
sudo apt-get install openssh-server -y
sudo apt-get install lamp-server^ -y
sudo apt-get install phpmyadmin -y
sudo apt-get install ghostscript -y
sudo apt-get install libapache2-mod-php -y
sudo apt-get install php-bcmath -y
sudo apt-get install php-curl -y
sudo apt-get install php-imagick -y
sudo apt-get install php-intl -y
sudo apt-get install php-json -y
sudo apt-get install php-mbstring -y
sudo apt-get install php-mysql -y
sudo apt-get install php-xml -y
sudo apt-get install php-zip -y
sudo apt install python3-pip -y
pip3 install mysql-connector --break-system-packages
curl -fsSL https://deb.nodesource.com/setup_21.x | sudo -E bash -
sudo apt install nodejs -y
sudo npm install -g n
sudo n lts
sudo npm install -g --save-dev @babel/core @babel/cli
sudo npm install -g --save-dev webpack
sudo npm install -g --save-dev webpack-cli
sudo npm install -g @angular/cli -y
sudo apt install bind9 -y
sudo apt install bind9utils -y 
sudo apt install bind9-doc -y
sudo apt install certbot -y
sudo apt install python3-certbot-apache -y

echo "Server Dependencies Complete."
