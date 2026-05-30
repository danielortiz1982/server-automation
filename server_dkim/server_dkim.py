import json
import subprocess
import re

server_config = {}

files = [
    'KeyTable',
    'SigningTable',
    'TrustedHosts'
]
template = ""
domainkey_txt = ""
new_bind_file = ""

with open('env.json', 'r') as config:
    content = config.read()
    server_config = json.loads(content)
    subprocess.run(f'sudo mkdir -p /etc/opendkim/keys/{server_config["SERVER_DOMAIN_NAME"]}', shell=True)
    subprocess.run(f'sudo opendkim-genkey -s mail -d {server_config["SERVER_DOMAIN_NAME"]} -D /etc/opendkim/keys/{server_config["SERVER_DOMAIN_NAME"]}', shell=True)
    subprocess.run(f'sudo chown -R opendkim:opendkim /etc/opendkim/keys', shell=True)
    subprocess.run(f'rm -rf /etc/opendkim.conf', shell=True)
    subprocess.run(f'cp server_dkim/opendkim.conf /etc/opendkim.conf', shell=True)

for index, file in enumerate(files):
    with open(f'server_dkim/template.{file}', 'r') as f:
        f = f.read()
        f = f.replace("$SERVER_DOMAIN_NAME", server_config["SERVER_DOMAIN_NAME"])
        f = f.replace("$SERVER_IP_ADDRESS", server_config["SERVER_IP_ADDRESS"])
        template = f

    with open(f'/etc/opendkim/{file}', 'w') as f:
        f.write(template)

def extract_and_split_ascending(dkim_record: str) -> list:
    cleaned_record = re.sub(r'[\s"\n\r\t]+', '', dkim_record)
    match = re.search(r'p=([^;)]+)', cleaned_record)

    if not match:
        return [] 
        
    p_value = match.group(1)
    total_len = len(p_value)
    base_len = total_len // 3
    len1 = base_len - 1
    len2 = base_len
    part1 = p_value[0 : len1]
    part2 = p_value[len1 : len1 + len2]
    part3 = p_value[len1 + len2 :]
    
    return [part1, part2, part3]

with open(f'/etc/opendkim/keys/{server_config["SERVER_DOMAIN_NAME"]}/mail.txt', 'r') as f:
    f = f.read()
    domainkey_txt = f

p_value_array = extract_and_split_ascending(domainkey_txt)

with open(f'/etc/bind/db.{server_config["SERVER_DOMAIN_NAME"]}', 'r') as f:
    f = f.read()
    f = f.replace("$PART0", p_value_array[0])
    f = f.replace("$PART1", p_value_array[1])
    f = f.replace("$PART2", p_value_array[2])
    new_bind_file = f

with open(f'/etc/bind/db.{server_config["SERVER_DOMAIN_NAME"]}', 'w') as f:
    f.write(new_bind_file)

print('Server DKIM automation successfully!')
