# Server Automation

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
> Email Blast Pro automation uses the following script langauges.

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

### Init Server Automation 
> Make sure to run the init.sh file with root

`sudo sh init.sh`