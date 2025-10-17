# Create the $SERVER_USER_NAME ssh directory
sudo mkdir /home/$SERVER_USER_NAME/.ssh

# Copy authorized_keys from the root user into $SERVER_USER_NAME ssh directory
sudo cp ~/.ssh/authorized_keys /home/$SERVER_USER_NAME/.ssh

# Adjust $SERVER_USER_NAME ssh directory permissions 
sudo chown -R $SERVER_USER_NAME:$SERVER_USER_NAME /home/$SERVER_USER_NAME/.ssh
sudo chmod 0700 /home/$SERVER_USER_NAME/.ssh
sudo chmod 0600 /home/$SERVER_USER_NAME/.ssh/authorized_keys

echo "$SERVER_USER_NAME Permissions Adjusted"

# Create the $SERVER_USER_NAME ssh directory
sudo mkdir /home/mediapigeons/.ssh

# Copy authorized_keys from the root user into mediapigeons ssh directory
sudo cp ~/.ssh/authorized_keys /home/psingh/.ssh

# Adjust mediapigeons ssh directory permissions 
sudo chown -R dortiz:dortiz /home/dortiz/.ssh
sudo chmod 0700 /home/dortiz/.ssh
sudo chmod 0600 /home/dortiz/.ssh/authorized_keys

echo "mediapigeons Permissions Adjusted"



postconf -e "smtpd_tls_cert_file = /etc/letsencrypt/live/mediapigeons.com/fullchain.pem"
postconf -e "smtpd_tls_key_file = /etc/letsencrypt/live/mediapigeons.com/privkey.pem"















Key is saved at:         