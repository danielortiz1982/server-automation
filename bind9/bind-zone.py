import os

with open('db.your-domain-name.com', 'r') as file:
  filedata = file.read()

filedata = filedata.replace('$EBLAST_DOMAIN_NAME', os.environ['EBLAST_DOMAIN_NAME'])
filedata = filedata.replace('$EBLAST_IP_ADDRESS', os.environ['EBLAST_IP_ADDRESS'])

with open('db.' + os.environ['EBLAST_DOMAIN_NAME'], 'w') as file:
  file.write(filedata)


with open('eblast.named.conf.local', 'r') as file:
	filedata = file.read()

filedata = filedata.replace('$EBLAST_DOMAIN_NAME', os.environ['EBLAST_DOMAIN_NAME'])

with open('named.conf.local', 'w') as file:
  file.write(filedata)