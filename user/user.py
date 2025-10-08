import sys
import subprocess

def add_user(username, password):
        add_user_command = ['useradd', '-p', password, username]
        subprocess.run(add_user_command)
        sys.exit(0)

def remove_user(username):
        remove_user_command = ['deluser', '--remove-all-files', username]
        subprocess.run(remove_user_command)
        print(f'${username} was removed')
        exit(0)

# add_user('sample555', 'whoami')
# remove_user('danielortiz')