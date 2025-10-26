import json

server_config = {}

with open('env.json', 'r') as config:
    content = config.read()
    server_config = json.loads(content)

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
  filedata = filedata.replace(f'$SERVER_ADMIN_USER', server_config["SERVER_ADMIN_USER"])
  filedata = filedata.replace(f'$SERVER_DB_NAME', server_config["SERVER_DB_NAME"])
  filedata = filedata.replace('$SERVER_ADMIN_PASSWORD', server_config["SERVER_ADMIN_PASSWORD"])
  with open(item + '.cf', 'w') as file:
    file.write(filedata)

print('Server Postfix')
