import json
import subprocess

server_config = {}

with open('env.json', 'r') as config:
    content = config.read()
    server_config = json.loads(content)

subprocess.run(f'sudo mkdir -p /etc/opendkim/keys/{server_config["SERVER_DOMAIN_NAME"]}', shell=True)
subprocess.run(f'sudo opendkim-genkey -s mail -d {server_config["SERVER_DOMAIN_NAME"]} -D /etc/opendkim/keys/{server_config["SERVER_DOMAIN_NAME"]}', shell=True)
subprocess.run(f'sudo chown -R opendkim:opendkim /etc/opendkim/keys')
