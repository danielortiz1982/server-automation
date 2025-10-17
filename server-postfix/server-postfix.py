from dotenv import load_dotenv
import os

load_dotenv()

files = [
  'mysql_virtual_domains',
  'mysql_virtual_forwardings',
  'mysql_virtual_mailboxes',
  'mysql_virtual_email2email'
]

for item in files:
  print(item)
  with open(item + '.template.cf', 'r') as file:
    filedata = file.read()
  filedata = filedata.replace('$SERVER_ADMIN_PASSWORD', os.environ['SERVER_ADMIN_PASSWORD'])
  with open(item + '.cf', 'w') as file:
    file.write(filedata)

print('Server Postfix')
