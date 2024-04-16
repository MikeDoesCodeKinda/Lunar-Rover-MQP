# Michael Gouveia
# January 26, 2024
# Version 1.0
#
# This function pulls a file using scp protocols by being called from the terminal with an argument

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


def createSSHClient(server, port, user, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client

def pull_File(file, server, port, username, password):
    ssh = createSSHClient(server, port, username, password)
    scp = SCPClient(ssh.get_transport())
    scp.get(file)
    return


file = sys.argv[1]
server = sys.argv[2]
port = sys.argv[3]
username = sys.argv[4]
password = sys.argv[5]
pull_File(file)

# Since this is meant to be called from matlab via the command line, the file defaults to the matlab directory.
# I don't like having the files stored in the matlab directory, so I move it to a preferrable location
matlab_path = sys.argv[6]
filename = file

original_path= os.path.join(matlab_path, filename)

# This is the path to the folder that you would like to move the files to
receive_path = sys.argv[7]

new_path = os.path.join(receive_path, filename)

shutil.move(original_path, new_path)

