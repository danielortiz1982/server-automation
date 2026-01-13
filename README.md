# Email Blast Pro Server Automation

### System Services
> Email Blast Pro is built using the following services.

- Apache2
- Mysql
- Bind9
- Certbot
- Postfix
- Dovecot
- Saslauthd
- Opendkim
- UFW

### System Automation
> Email Blast Pro automation uses the following scripting langauges.

- Python
- SQL
- Bash

### Dependencies
- json
- subprocess

### Server Environment Configuration
> Create `env.json` with the configuation outlined below and save it in the root of the project.
```json
{
    "SERVER_NAME": "server_name",
    "SERVER_IP_ADDRESS": "server_ip_address",
    "SERVER_DOMAIN_NAME": "example.com",
    "SERVER_ADMIN_USER": "username",
    "SERVER_ADMIN_PASSWORD": "server_password",
    "SERVER_DB_NAME": "server_db"
}
```

### Server Init Automation 
> Make sure to run the init.sh file with root
```shell
sudo sh init.sh
```

### Server SSL Automation
> Once $SERVER_DOMAIN_NAME successfully resolves to $SERVER_IP_ADDRESS send a request for a ssl certificate.

Make sure to run as root.
```shell
sudo python3 server_ssl/server_ssl.py
```

### Server DKIM Automation
> Once you have obtained a ssl certificate you can now setup dkim and dmarc authentication.

Make sure to run as root.
```shell
sudo python3 server_dkim/server_dkim.py
```

> After the DKIM Automation is complete you can now update your ZONE file to include the newley created cryptographic signatures.

```shell
cat /etc/opendkim/keys/$SERVER_DOMAIN_NAME/mail.txt
```