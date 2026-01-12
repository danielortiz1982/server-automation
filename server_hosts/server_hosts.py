import json

server_config = {}
hosts = ""

with open('env.json', 'r') as config:
    content = config.read()
    server_config = json.loads(content)

with open('server_hosts/hosts.template', 'r') as f:
    f = f.read()
    f = f.replace('$SERVER_DOMAIN_NAME', server_config['SERVER_DOMAIN_NAME'])
    f = f.replace('$SERVER_IP_ADDRESS', server_config['SERVER_IP_ADDRESS'])
    hosts = f

with open(f'/etc/hosts', "w") as f:
    f.write(hosts)