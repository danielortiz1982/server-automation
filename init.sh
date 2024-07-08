#!/bin/bash

##### EBLAST INIT #####

sh server-setup/server-update.sh
sh server-setup/server-dependencies.sh
sh server-setup/server-db-setup.sh

cd bind9
python3 bind-zone.py
sh server-zones.sh
cd ../


cd virtual-host
python3 virtual-host.py
sh server-host.sh
sh server-wordpress.sh
cd ../
