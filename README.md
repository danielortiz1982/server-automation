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

### Add DKIM Signatures To Bind9
> After the DKIM Automation is complete you can now update your zone file to include the newley created cryptographic signatures.

Print the content from the mail.txt file to include in your Bind9 configuation
```shell
cat /etc/opendkim/keys/$SERVER_DOMAIN_NAME/mail.txt
```

### Update the Bind9 zones
> Locate and open the db domain name zone file

```shell
vim /etc/bind/db.$SERVER_DOMAIN_NAME
```

> Add the mail.domainkey record to bind zone
```conf
mail._domainkey	IN	TXT	( "v=DKIM1; h=sha256; k=rsa; "
	  "p=MIIBIjANBgTV9XgwX+cT1MQNZS5xe0dYvzvRDApBfYXlVQtPiCDHMy2g/70fEtidAJ
      a2OSxCclig4A9QK/3ap10f0jZ4qsSznm8wliwxgR15PpTqFOg0BAQEFAAOCAQ8AMIIBCgKCAQ
      EAtQoPY9JomN9Mib8zoeLp7zNNtGeycZVST3tG4iJ5vIx4ZunPa8E23Uf0F14Kfob9MKV3rrkHUuE1bAMJVttoVBlFQKcgpV9wZxko5Zky72na1aXvQCSx7P5X4LQouuW+ziSJ2c02dCb/zX6BCbyEin/R693es2RbqUDiUMA+WdAABPW9EixEJays9RZyYB" )  ; ----- DKIM key mail for $SERVER_DOMAIN_NAME
```
### Restart services
> Restart Bind9, Postfix and Dovecot
```shell
sudo systemctl restart bind9
sudo systemctl restart postfix
sudo systemctl restart dovecot
```
