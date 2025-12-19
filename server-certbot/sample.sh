#!/bin/bash

# --- Variables (Modify these) ---
EMAIL="your_email@example.com" # Your contact email for urgent renewal notices
DOMAIN="example.com"           # Your main domain name
WWW_DOMAIN="www.example.com"   # The www subdomain
WEBSERVER="apache"             # Or "nginx" if you use Nginx
# ---------------------------------

# Check if running as root
if [ "$EUID" -ne 0 ]; then
    echo "Please run as root or with sudo"
    exit 1
fi

echo "Starting Certbot installation and configuration for $DOMAIN..."

# 1. Remove any existing Certbot OS packages to prevent conflicts
echo "Removing old Certbot packages..."
apt-get remove certbot -y
apt-get purge certbot -y
dnf remove certbot -y
yum remove certbot -y

# 2. Install snapd (if not already installed)
echo "Installing snapd..."
apt-get update
apt-get install snapd -y

# 3. Install Certbot via snap
echo "Installing Certbot snap..."
snap install --classic certbot

# 4. Create a symlink to ensure the 'certbot' command is found
echo "Creating certbot symlink..."
ln -s /snap/bin/certbot /usr/bin/certbot

# 5. Obtain and install certificates
echo "Obtaining certificates for $DOMAIN and $WWW_DOMAIN using the $WEBSERVER plugin..."
# The --noninteractive flag prevents prompts; --agree-tos agrees to terms of service
# The appropriate plugin (--apache or --nginx) will automatically edit the server config
certbot run --$WEBSERVER -d "$DOMAIN" -d "$WWW_DOMAIN" --noninteractive --agree-tos -m "$EMAIL"

# 6. Test the automatic renewal process
echo "Testing automatic renewal process with a dry run..."
certbot renew --dry-run

if [ $? -eq 0 ]; then
    echo "Certbot installation, configuration, and renewal test successful!"
    echo "Your certificates are located in /etc/letsencrypt/live/$DOMAIN/"
else
    echo "Certbot configuration or dry run failed. Please check the logs for errors."
fi
