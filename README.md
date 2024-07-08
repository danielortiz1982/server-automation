# Ubuntu Linux server automation

#### Clone repo

```shell
git clone https://github.com/danielortiz1982/server-automation.git
```

#### Set and export server environment variables

> Edit server-env.sh and configure your new server env values.

```shell
export EBLAST_SITE_NAME="example-site"
export EBLAST_DOMAIN_NAME="example-site.com"
export EBLAST_IP_ADDRESS="145.26.185.200"
export EBLAST_DB_NAME="example_site"
export EBLAST_DB_USER="example"
export EBLAST_DB_PASSWORD="example-pass-2024"
```

> Export system var

```shell
source server-env.sh
```

> Init eBlast server setup

```shell
sh init.sh
```
