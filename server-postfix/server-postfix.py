import json
import subprocess

server_config = {}

with open('env.json', 'r') as config:
    content = config.read()
    server_config = json.loads(content)

files = [
  'master',
  'mysql_virtual_domains',
  'mysql_virtual_forwardings',
  'mysql_virtual_mailboxes',
  'mysql_virtual_email2email'
]

template = ""

for index, file in enumerate(files):
    with open(f'server-postfix/{file}.template.cf', 'r') as f:
        f = f.read()
        f = f.replace(f'$SERVER_ADMIN_USER', server_config["SERVER_ADMIN_USER"])
        f = f.replace(f'$SERVER_DB_NAME', server_config["SERVER_DB_NAME"])
        f = f.replace('$SERVER_ADMIN_PASSWORD', server_config["SERVER_ADMIN_PASSWORD"])
        template = f

    with open(f'/etc/postfix/{file}.cf', 'w') as f:
        f.write(template)

subprocess.run(f'sudo postconf -e "myhostname = mail.{server_config["SERVER_DOMAIN_NAME"]}"', shell=True)
subprocess.run(f'sudo postconf -e "mydestination = mail.{server_config["SERVER_DOMAIN_NAME"]}, localhost, localhost.localdomain, {server_config["SERVER_IP_ADDRESS"]}"', shell=True)
subprocess.run(f'sudo postconf -e "mynetworks = 127.0.0.0/8"', shell=True)
subprocess.run(f'sudo postconf -e "message_size_limit = 31457280"', shell=True)
subprocess.run(f'sudo postconf -e "virtual_alias_domains ="', shell=True)
subprocess.run(f'sudo postconf -e "virtual_alias_maps = proxy:mysql:/etc/postfix/mysql_virtual_forwardings.cf, mysql:/etc/postfix/mysql_virtual_email2email.cf"', shell=True)
subprocess.run(f'sudo postconf -e "virtual_mailbox_domains = proxy:mysql:/etc/postfix/mysql_virtual_domains.cf"', shell=True)
subprocess.run(f'sudo postconf -e "virtual_mailbox_maps = proxy:mysql:/etc/postfix/mysql_virtual_mailboxes.cf"', shell=True)
subprocess.run(f'sudo postconf -e "virtual_mailbox_base = /var/vmail"', shell=True)
subprocess.run(f'sudo postconf -e "virtual_uid_maps = static:5000"', shell=True)
subprocess.run(f'sudo postconf -e "virtual_gid_maps = static:5000"', shell=True)
subprocess.run(f'sudo postconf -e "smtpd_sasl_auth_enable = yes"', shell=True)
subprocess.run(f'sudo postconf -e "broken_sasl_auth_clients = yes"', shell=True)
subprocess.run(f'sudo postconf -e "smtpd_sasl_authenticated_header = yes"', shell=True)
subprocess.run(f'sudo postconf -e "smtpd_recipient_restrictions = permit_mynetworks, permit_sasl_authenticated, reject_unauth_destination"', shell=True)
subprocess.run(f'sudo postconf -e "smtpd_use_tls = yes"', shell=True)
subprocess.run(f'sudo postconf -e "smtpd_tls_cert_file = /etc/letsencrypt/live/{server_config["SERVER_DOMAIN_NAME"]}/fullchain.pem"', shell=True)
subprocess.run(f'sudo postconf -e "smtpd_tls_key_file = /etc/letsencrypt/live/{server_config["SERVER_DOMAIN_NAME"]}/privkey.pem"', shell=True)
subprocess.run(f'sudo postconf -e "virtual_transport=dovecot"', shell=True)
subprocess.run(f'sudo postconf -e "proxy_read_maps = $local_recipient_maps $mydestination $virtual_alias_maps $virtual_alias_domains $virtual_mailbox_maps $virtual_mailbox_domains $relay_recipient_maps $relay_domains $canonical_maps $sender_canonical_maps $recipient_canonical_maps $relocated_maps $transport_maps $mynetworks $virtual_mailbox_limit_maps"', shell=True)
subprocess.run(f'sudo chmod o-rwx /etc/postfix/mysql_virtual_*', shell=True)
subprocess.run(f'sudo chown root:postfix /etc/postfix/mysql_virtual_*', shell=True)
subprocess.run(f'sudo groupadd -g 5000 vmail', shell=True)
subprocess.run(f'sudo useradd -g vmail -u 5000 -d /var/vmail -m vmail', shell=True)

print('Server Postfix automation successfully!')
