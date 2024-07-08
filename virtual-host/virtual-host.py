import os

with open('your-domain-name.conf', 'r') as file:
  filedata = file.read()

filedata = filedata.replace('$EBLAST_DOMAIN_NAME', os.environ['EBLAST_DOMAIN_NAME'])
filedata = filedata.replace('$EBLAST_SITE_NAME', os.environ['EBLAST_SITE_NAME'])

with open(os.environ['EBLAST_DOMAIN_NAME'] + '.conf', 'w') as file:
  file.write(filedata)
