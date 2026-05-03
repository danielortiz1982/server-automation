import json
import subprocess

server_config = {}
keytable = ""
trustedhosts = ""
signingtable = ""

with open('env.json', 'r') as config:
    content = config.read()
    server_config = json.loads(content)

subprocess.run(f'sudo mkdir -p /etc/opendkim/keys/{server_config["SERVER_DOMAIN_NAME"]}', shell=True)
subprocess.run(f'sudo opendkim-genkey -s mail -d {server_config["SERVER_DOMAIN_NAME"]} -D /etc/opendkim/keys/{server_config["SERVER_DOMAIN_NAME"]}', shell=True)
subprocess.run(f'sudo chown -R opendkim:opendkim /etc/opendkim/keys')


print('DKIM Finished')

# with open('server_dkim/template.KeyTable', 'r') as f:
#     f = f.read()
#     f = f.replace("$SERVER_DOMAIN_NAME", server_config["SERVER_DOMAIN_NAME"])
#     keytable = f

# with open('server_dkim/KeyTable', 'w') as f:
#     f.write(keytable)

# with open('server_dkim/template.SigningTable', 'r') as f:
#     f = f.read()
#     f = f.replace("$SERVER_DOMAIN_NAME", server_config["SERVER_DOMAIN_NAME"])
#     signingtable = f

# with open('server_dkim/SigningTable', 'w') as f:
#     f.write(signingtable)

# with open('server_dkim/template.TrustedHosts', 'r') as f:
#     f = f.read()
#     f = f.replace("$SERVER_DOMAIN_NAME", server_config["SERVER_DOMAIN_NAME"])
#     f = f.replace("$SERVER_IP_ADDRESS", server_config["SERVER_IP_ADDRESS"])
#     trustedhosts = f

# with open('server_dkim/TrustedHosts', 'w') as f:
#     f.write(trustedhosts)