# Server Setup

> Install Dependecies


```shell
sudo sh server-setup.sh
```

#### Dependecies Commands
> server-setup.sh source code
```shell

sudo apt-get update
sudo apt-get dist-upgrade -y
sudo apt-get install curl -y
sudo apt-get install git -y
sudo apt-get install openssh-server -y
sudo apt-get install lamp-server^ -y
sudo apt-get install phpmyadmin -y
sudo apt install python3-pip -y
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
```