import subprocess

dependencies_list = [
    'sudo apt-get update',
    'sudo apt-get dist-upgrade -y',
    'sudo apt-get install curl -y',
    'sudo apt-get install git -y',
    'sudo apt-get install openssh-server -y',
    'sudo apt-get install lamp-server^ -y',
    'sudo apt-get install phpmyadmin -y',
    'sudo apt-get install ghostscript -y',
    'sudo apt-get install libapache2-mod-php -y',
    'sudo apt-get install php-bcmath -y',
    'sudo apt-get install php-curl -y',
    'sudo apt-get install php-imagick -y',
    'sudo apt-get install php-intl -y',
    'sudo apt-get install php-json -y',
    'sudo apt-get install php-mbstring -y',
    'sudo apt-get install php-mysql -y',
    'sudo apt-get install php-xml -y',
    'sudo apt-get install php-zip -y',
    'sudo apt install python3-pip -y',
    'python3 -m venv pyenv',
    'source pyenv/bin/activate',
    'pip install mysql-connector --break-system-packages',
    'pip install python-dotenv',
    'curl -fsSL https://deb.nodesource.com/setup_21.x | sudo -E bash -',
    'sudo apt install nodejs -y',
    'sudo npm install -g n',
    'sudo n lts',
    'sudo npm install -g --save-dev @babel/core @babel/cli',
    'sudo npm install -g --save-dev webpack',
    'sudo npm install -g --save-dev webpack-cli',
    'sudo npm install -g @angular/cli -y',
    'sudo apt install bind9 -y',
    'sudo apt install bind9utils -y ',
    'sudo apt install bind9-doc -y',
    'sudo apt install certbot -y',
    'sudo apt install python3-certbot-apache -y',
    'apt install postfix -y',
    'apt install postfix-mysql -y',
    'apt install postfix-doc -y',
    'apt install dovecot-common -y',
    'apt install dovecot-imapd -y',
    'apt install dovecot-pop3d -y',
    'apt install libsasl2-2 -y',
    'apt install libsasl2-modules -y',
    'apt install libsasl2-modules-sql -y',
    'apt install sasl2-bin -y',
    'apt install libpam-mysql -y',
    'apt install mailutils -y',
    'apt install dovecot-mysql -y',
    'apt install dovecot-sieve -y',
    'apt install dovecot-managesieved -y',
    'source .env'
]

def server_dependencies(list):

    for d in list:
        subprocess.run(d, shell=True)

server_dependencies(dependencies_list)
