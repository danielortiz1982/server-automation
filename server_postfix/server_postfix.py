import json
import subprocess

server_config = {}

with open('env.json', 'r') as config:
    content = config.read()
    server_config = json.loads(content)

files = [
  'master',
  'main',
  'mysql_virtual_domains',
  'mysql_virtual_forwardings',
  'mysql_virtual_mailboxes',
  'mysql_virtual_email2email'
]

template = ""

for index, file in enumerate(files):
    with open(f'server_postfix/{file}.template.cf', 'r') as f:
        f = f.read()
        f = f.replace(f'$SERVER_ADMIN_USER', server_config["SERVER_ADMIN_USER"])
        f = f.replace(f'$SERVER_DB_NAME', server_config["SERVER_DB_NAME"])
        f = f.replace('$SERVER_ADMIN_PASSWORD', server_config["SERVER_ADMIN_PASSWORD"])
        f = f.replace('$SERVER_DOMAIN_NAME', server_config["SERVER_DOMAIN_NAME"])
        f = f.replace('$SERVER_IP_ADDRESS', server_config["SERVER_IP_ADDRESS"])
        template = f

    with open(f'/etc/postfix/{file}.cf', 'w') as f:
        f.write(template)

subprocess.run(f'sudo chmod o-rwx /etc/postfix/mysql_virtual_*', shell=True)
subprocess.run(f'sudo chown root:postfix /etc/postfix/mysql_virtual_*', shell=True)
subprocess.run(f'sudo groupadd -g 5000 vmail', shell=True)
subprocess.run(f'sudo useradd -g vmail -u 5000 -d /var/vmail -m vmail', shell=True)

print('Server Postfix automation successfully!')
