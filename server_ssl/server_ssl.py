import json
import subprocess

server_config = {}
conf_file = ""
template = ""

with open('env.json', 'r') as config:
    content = config.read()
    server_config = json.loads(content)

### Certbot variables (Modify these) ###
EMAIL=f'webmaster@{server_config["SERVER_DOMAIN_NAME"]}'                        # Your contact email for urgent renewal notices
DOMAIN=server_config["SERVER_DOMAIN_NAME"]                                      # Your main domain name
WWW_DOMAIN=f'www.{server_config["SERVER_DOMAIN_NAME"]}'                         # The www subdomain
WEBSERVER="apache"                                                              # Or "nginx" if you use Nginx

### Certbot Automation ###
SHELL_COMMAND=f'sudo certbot run --{WEBSERVER} -d {DOMAIN} -d {WWW_DOMAIN} --noninteractive --agree-tos -m {EMAIL}'
subprocess.run(SHELL_COMMAND, shell=True)
print("Certbot & ssl certificate automation successfully!")
