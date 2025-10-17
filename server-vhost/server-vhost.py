from dotenv import load_dotenv
import os

load_dotenv()

with open('server-vhost/your-domain-name.conf', 'r') as file:
  filedata = file.read()

filedata = filedata.replace('$SERVER_DOMAIN_NAME', os.environ['SERVER_DOMAIN_NAME'])
filedata = filedata.replace('$SERVER_NAME', os.environ['SERVER_NAME'])

with open('server-vhost/' + os.environ['SERVER_DOMAIN_NAME'] + '.conf', 'w') as file:
  file.write(filedata)

print('Vhost!')
