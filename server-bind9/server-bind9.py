import json

server_config = {}
zone = ""
named = ""

with open('env.json', 'r') as config:
    content = config.read()
    server_config = json.loads(content)

with open('server-bind9/db.your-domain-name.com') as f:
    f = f.read()
    f = f.replace('$SERVER_DOMAIN_NAME', server_config['SERVER_DOMAIN_NAME'])
    f = f.replace('$SERVER_IP_ADDRESS', server_config['SERVER_IP_ADDRESS'])
    zone = f

with open(f'/etc/bind/db.{server_config["SERVER_DOMAIN_NAME"]}', "w") as f:
    f.write(zone)
    
with open('server-bind9/server.named.conf.local') as f:
    f = f.read()
    f = f.replace('$SERVER_DOMAIN_NAME', server_config['SERVER_DOMAIN_NAME'])
    named = f

with open('server-bind9/named.conf.local', 'w') as f:
    f.write(named)

print('Server Bind9 automation successfully!')
