import json
import subprocess

server_config = {}
conf_file = ""
template = ""

with open('env.json', 'r') as config:
    content = config.read()
    server_config = json.loads(content)

with open('server-vhost/your-domain-name.conf', 'r') as f:
    f = f.read()
    f = f.replace('$SERVER_DOMAIN_NAME', server_config['SERVER_DOMAIN_NAME'])
    f = f.replace('$SERVER_NAME', server_config['SERVER_NAME'])
    conf_file = f

with open(f'/etc/apache2/sites-available/{server_config["SERVER_DOMAIN_NAME"]}.conf', 'w') as f:
    f.write(conf_file)


subprocess.run(f'sudo mkdir -p /var/www/{server_config["SERVER_DOMAIN_NAME"]}/', shell=True)

with open('server-vhost/template.html', 'r') as f:
    f = f.read()
    f = f.replace('$SERVER_NAME', server_config['SERVER_NAME'])
    template = f

with open(f'/var/www/{server_config["SERVER_DOMAIN_NAME"]}/index.html', 'w') as f:
    f.write(template)

subprocess.run(f'sudo chown www-data: /var/www/{server_config["SERVER_DOMAIN_NAME"]}', shell=True)
subprocess.run('sudo a2dissite 000-default', shell=True)
subprocess.run(f'sudo a2ensite {server_config["SERVER_DOMAIN_NAME"]}', shell=True)
subprocess.run(f'sudo systemctl reload apache2', shell=True)
subprocess.run(f'sudo systemctl restart apache2', shell=True)

### todo check if client has a wp hosting plan ###
### WordPress Automation ###
# subprocess.run(f'curl https://wordpress.org/latest.tar.gz | sudo -u www-data tar zx -C /var/www/{server_config["SERVER_DOMAIN_NAME"]}', shell=True)
# subprocess.run(f'sudo -u www-data cp /var/www/{server_config["SERVER_DOMAIN_NAME"]}/wordpress/wp-config-sample.php /var/www/{server_config["SERVER_DOMAIN_NAME"]}/wordpress/wp-config.php', shell=True)
# subprocess.run(f'sudo -u www-data sed -i "s/database_name_here/{server_config["SERVER_DB_NAME"]}/" /var/www/{server_config["SERVER_DOMAIN_NAME"]}/wordpress/wp-config.php', shell=True)
# subprocess.run(f'sudo -u www-data sed -i "s/username_here/{server_config["SERVER_ADMIN_USER"]}/" /var/www/{server_config["SERVER_DOMAIN_NAME"]}/wordpress/wp-config.php', shell=True)
# subprocess.run(f'sudo -u www-data sed -i "s/password_here/{server_config["SERVER_ADMIN_PASSWORD"]}/" /var/www/{server_config["SERVER_DOMAIN_NAME"]}/wordpress/wp-config.php', shell=True)

print('Vhost automation successfully complete!')
