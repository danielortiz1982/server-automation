# Virtual Host

Create a new site enable configuration file. Save the file in format below
> /etc/apache2/sites-available/your-domain-name.conf

Change the $EBLAST_DOMAIN_NAME placeholder to your domain name.
> $EBLAST_DOMAIN_NAME to something like example.com

Change the $EBLAST_SITE_NAME placeholder to your domain name.
> $EBLAST_SITE_NAME to something like example-site

> Example site enable conf source
```shell
<VirtualHost *:80>
	ServerName $EBLAST_DOMAIN_NAME
	ServerAlias www.$EBLAST_DOMAIN_NAME
	DocumentRoot /var/www/$EBLAST_DOMAIN_NAME/wordpress

	<Directory /var/www/$EBLAST_DOMAIN_NAME/wordpress>
    	Options FollowSymLinks
    	AllowOverride Limit Options FileInfo
    	DirectoryIndex index.php
    	Require all granted
    </Directory>
    <Directory /var/www/$EBLAST_DOMAIN_NAME/wordpress/wp-content>
        Options FollowSymLinks
        Require all granted
    </Directory>

	ServerAdmin webmaster@$EBLAST_DOMAIN_NAME
	ErrorLog /var/log/apache2/$EBLAST_SITE_NAME_error.log
	CustomLog /var/log/apache2/$EBLAST_SITE_NAME_access.log combined
</VirtualHost>
```

After you have created a your-domain-name.conf file, enable your new site.
```shell
a2ensite
```

Restart apache2
```shell
systemctl restart apache2
```

Reload apache2
```shell
systemctl reload apache2
```

Set up SSL
```shell
certbot -d $EBLAST_DOMAIN_NAME
```