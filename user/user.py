import sys
import subprocess

def add_user(username, password):
        add_user_command = ['useradd', '-p', password, '-m', '-g', 'users, mail', username]
        results = subprocess.run(add_user_command, capture_output=True)
        if results.returncode > 0:
                print(f'Had an issue could not create {username}, please check and try agin.')
                sys.exit(1)   
        else:
                print(f'{username} was created successfully!')
                sys.exit(0)

def remove_user(username):
        remove_user_command = ['deluser', '--remove-all-files', username]
        results = subprocess.run(remove_user_command, capture_output=True)
        if results.returncode > 0:
                print(f'{username} was not found, please try another username.')
                sys.exit(1)
        else:
                print(f'{username} was removed!')
                sys.exit(0)

def add_user_group(username, group):
        group_user_command = ['usermod', '-aG', group, username ]
        results = subprocess.run(group_user_command)
        if results.returncode > 0:
                print(f'{username} or {group} could not be found, please check and try again.')
        else:
                print(f'{username} was added to {group} successfully!')
