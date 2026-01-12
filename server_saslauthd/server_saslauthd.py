
import json
import subprocess

server_config = {}
smtp = ""
saslauthd = ''

with open('env.json', 'r') as config:
    content = config.read()
    server_config = json.loads(content)

with open('server_saslauthd/smtp', 'r') as f:
    f = f.read()
    f = f.replace('$SERVER_ADMIN_USER', server_config['SERVER_ADMIN_USER'])
    f = f.replace('$SERVER_ADMIN_PASSWORD', server_config['SERVER_ADMIN_PASSWORD'])
    f = f.replace('$SERVER_DB_NAME', server_config['SERVER_DB_NAME'])
    smtp = f

with open('/etc/pam.d/smtp', 'w') as f:
    f.write(smtp)

with open('/usr/lib/systemd/system/saslauthd.service', 'r') as f:
    f = f.read()
    f = f.replace('# PIDFile=/var/run/saslauthd/saslauthd.pid', '# PIDFile=/var/spool/postfix/var/run/saslauthd/saslauthd.pid')
    saslauthd = f

with open('/usr/lib/systemd/system/saslauthd.service', 'w') as f:
    f.write(saslauthd)

subprocess.run("sudo mkdir -p /var/spool/postfix/var/run/saslauthd", shell=True)
subprocess.run("sudo cp server_saslauthd/saslauthd /etc/default/saslauthd", shell=True)
subprocess.run("sudo cp server_saslauthd/smtpd.conf /etc/postfix/sasl/smtpd.conf", shell=True)
subprocess.run("sudo chmod o-rwx /etc/pam.d/smtp", shell=True)
subprocess.run("sudo chmod o-rwx /etc/postfix/sasl/smtpd.conf", shell=True)
subprocess.run("sudo usermod  -aG sasl postfix", shell=True)
subprocess.run("sudo systemctl daemon-reload", shell=True)
subprocess.run("sudo systemctl restart postfix", shell=True)
subprocess.run("sudo systemctl restart saslauthd", shell=True)

print("'Server saslauthd automation successfully!'")
