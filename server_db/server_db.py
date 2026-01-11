import json
import subprocess

server_config = {}
zone = ""
named = ""

with open('env.json', 'r') as config:
    content = config.read()
    server_config = json.loads(content)

subprocess.run(f'sudo mysql -u root -e "CREATE DATABASE {server_config['SERVER_DB_NAME']};"', shell=True)
subprocess.run(f'sudo mysql -u root -e "CREATE USER \'{server_config['SERVER_ADMIN_USER']}\'@\'localhost\' IDENTIFIED BY \'{server_config['SERVER_ADMIN_PASSWORD']}\';"', shell=True)
subprocess.run(f'sudo mysql -u root -e "GRANT ALL PRIVILEGES ON * . * TO \'{server_config['SERVER_ADMIN_USER']}\'@\'localhost\';"', shell=True)
subprocess.run(f'sudo mysql -u root -e "USE {server_config['SERVER_DB_NAME']}; CREATE TABLE domains (domain varchar(50) NOT NULL, PRIMARY KEY (domain));"', shell=True)
subprocess.run(f'sudo mysql -u root -e "USE {server_config['SERVER_DB_NAME']}; CREATE TABLE users (email varchar(80) NOT NULL, password varchar(128) NOT NULL, PRIMARY KEY (email));"', shell=True)
subprocess.run(f'sudo mysql -u root -e "USE {server_config['SERVER_DB_NAME']}; CREATE TABLE forwardings (source varchar(80) NOT NULL, destination TEXT NOT NULL, PRIMARY KEY (source));"', shell=True)
subprocess.run(f'sudo mysql -u root -e "USE {server_config['SERVER_DB_NAME']}; INSERT INTO domains (domain) VALUES (\'{server_config['SERVER_DOMAIN_NAME']}\');"', shell=True)
subprocess.run(f'sudo mysql -u root -e "USE {server_config['SERVER_DB_NAME']}; INSERT INTO users(email,password) values(\'webmaster@{server_config['SERVER_DOMAIN_NAME']}\', md5(\'P@SsWord12345@\'));"', shell=True)
subprocess.run(f'sudo mysql -u root -e "USE {server_config['SERVER_DB_NAME']}; INSERT INTO users(email,password) values(\'{server_config['SERVER_ADMIN_USER']}@{server_config['SERVER_DOMAIN_NAME']}\', md5(\'{server_config['SERVER_ADMIN_PASSWORD']}\'));"', shell=True)
