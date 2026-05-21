import json
import subprocess

server_config = {}

files = [
    'KeyTable',
    'SigningTable',
    'TrustedHosts'
]
template = ""

with open('env.json', 'r') as config:
    content = config.read()
    server_config = json.loads(content)
    subprocess.run(f'sudo mkdir -p /etc/opendkim/keys/{server_config["SERVER_DOMAIN_NAME"]}', shell=True)
    subprocess.run(f'sudo opendkim-genkey -s mail -d {server_config["SERVER_DOMAIN_NAME"]} -D /etc/opendkim/keys/{server_config["SERVER_DOMAIN_NAME"]}', shell=True)
    subprocess.run(f'sudo chown -R opendkim:opendkim /etc/opendkim/keys', shell=True)
    subprocess.run(f'rm -rf /etc/opendkim.conf', shell=True)
    subprocess.run(f'cp server_dkim/opendkim.conf /etc/opendkim.conf', shell=True)

for index, file in enumerate(files):
    with open(f'server_dkim/template.{file}', 'r') as f:
        f = f.read()
        f = f.replace("$SERVER_DOMAIN_NAME", server_config["SERVER_DOMAIN_NAME"])
        f = f.replace("$SERVER_IP_ADDRESS", server_config["SERVER_IP_ADDRESS"])
        template = f

    with open(f'/etc/opendkim/{file}', 'w') as f:
        f.write(template)

print('Server DKIM automation successfully!')

####### Old Script ########

# with open('server_dkim/template.KeyTable', 'r') as f:
#     f = f.read()
#     f = f.replace("$SERVER_DOMAIN_NAME", server_config["SERVER_DOMAIN_NAME"])
#     keytable = f

# with open('/etc/opendkim/KeyTable', 'w') as f:
#     f.write(keytable)

# with open('server_dkim/template.SigningTable', 'r') as f:
#     f = f.read()
#     f = f.replace("$SERVER_DOMAIN_NAME", server_config["SERVER_DOMAIN_NAME"])
#     signingtable = f

# with open('/etc/opendkim/SigningTable', 'w') as f:
#     f.write(signingtable)

# with open('server_dkim/template.TrustedHosts', 'r') as f:
#     f = f.read()
#     f = f.replace("$SERVER_DOMAIN_NAME", server_config["SERVER_DOMAIN_NAME"])
#     f = f.replace("$SERVER_IP_ADDRESS", server_config["SERVER_IP_ADDRESS"])
#     trustedhosts = f

# with open('/etc/opendkim/TrustedHosts', 'w') as f:
#     f.write(trustedhosts)
    

