from dotenv import load_dotenv
import os

load_dotenv()

with open('server-bind9/db.your-domain-name.com', 'r') as file:
  filedata = file.read()

filedata = filedata.replace('$SERVER_DOMAIN_NAME', os.environ['SERVER_DOMAIN_NAME'])
filedata = filedata.replace('$SERVER_IP_ADDRESS', os.environ['SERVER_IP_ADDRESS'])

with open('server-bind9/db.' + os.environ['SERVER_DOMAIN_NAME'], 'w') as file:
  file.write(filedata)


with open('server-bind9/server.named.conf.local', 'r') as file:
	filedata = file.read()

filedata = filedata.replace('$SERVER_DOMAIN_NAME', os.environ['SERVER_DOMAIN_NAME'])

with open('server-bind9/named.conf.local', 'w') as file:
  file.write(filedata)

print('Server Bind9 automation successfully!')