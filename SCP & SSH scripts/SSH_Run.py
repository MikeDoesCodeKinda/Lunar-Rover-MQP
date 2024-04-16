# Michael Gouveia
# April 16, 2024
# Version 1.0
#
# This function runs a command over ssh. The command is given as the argument. Intended to be
# called from the terminal.

'''
Please note that this script has been modified to remove any information specific to our project.
In this version there are far more inputs. I would recommend that anyone using this function replace
certain inputs with information specific to your use case, such as server, port, user, password.

Please reference the proper order for inputs from within the code

'''

import paramiko
from scp import SCPClient
import sys
import shutil
import os
import time


def createSSHClient(server, port, user, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client


# I have not tested this with all the inputs
server = sys.argv[2]
port = sys.argv[3]
username = sys.argv[4]
password = sys.argv[5]



ssh = createSSHClient(server, port, username, password)
ssh.connect(server, username=username, password=password)

#cmd_to_execute1 = "source env/bin/activate"
cmd_to_execute = sys.argv[1]
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(cmd_to_execute1)

time.sleep(1)

#ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(cmd_to_execute)

#ssh.exec_command(cmd_to_execute)
ssh.close()

print(ssh_stdout.read().decode())



