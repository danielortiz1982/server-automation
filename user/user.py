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

def add_user_group(username, group):
        group_user_command = ['chmod', '-aG', group, username ]
        subprocess.run(group_user_command)
        print(f'{username} was added to {group}')

add_user_group('danielortiz', 'users')