from dotenv import load_dotenv
import os

load_dotenv()

with open('server-dovecot/dovecot.template.conf', 'r') as file:
	filedata = file.read()

filedata = filedata.replace('$SERVER_DOMAIN_NAME', os.environ['SERVER_DOMAIN_NAME'])

with open('server-dovecot/dovecot.conf', 'w') as file:
  file.write(filedata)

with open('server-dovecot/dovecot-sql.template.conf', 'r') as file:
	filedata = file.read()

filedata = filedata.replace('$SERVER_ADMIN_PASSWORD', os.environ['SERVER_ADMIN_PASSWORD'])

with open('server-dovecot/dovecot-sql.conf', 'w') as file:
  file.write(filedata)