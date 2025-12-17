import json
import subprocess

server_config = {}
template = ""

files = [
    'dovecot-sql',
    'dovecot'
]

with open('env.json', 'r') as config:
    content = config.read()
    server_config = json.loads(content)

for index, file in enumerate(files):
    with open(f'server-dovecot/{file}.template.conf', 'r') as f:
        f = f.read()
        f = f.replace('$SERVER_DOMAIN_NAME', server_config["SERVER_DOMAIN_NAME"])
        f = f.replace('$SERVER_DB_NAME', server_config["SERVER_DB_NAME"])
        f = f.replace('$SERVER_ADMIN_USER', server_config["SERVER_ADMIN_USER"])
        f = f.replace('$SERVER_ADMIN_PASSWORD', server_config["SERVER_ADMIN_PASSWORD"])
        template = f

    with open(f'/etc/dovecot/{file}.conf', 'w') as f:
        f.write(template)

# subprocess.run(f'sudo systemctl restart dovecot', shell=True)

print('Dovecot automation successfully complete!')