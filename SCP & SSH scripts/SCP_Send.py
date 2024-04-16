# Michael Gouveia
# January 26, 2024
# Version 1.0
#
# This function sends a file using scp protocols by being called from the terminal with an argument

'''
Please note that this script has been modified to remove any information specific to our project.
In this version there are far more inputs. I would recommend that anyone using this function replace
certain inputs with information specific to your use case, such as server, port, user, password.

Please reference the proper order for inputs from within the code

'''

import paramiko
from scp import SCPClient
import sys

def createSSHClient(server, port, user, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client

def send_File(file, server, port, username, password):

    ssh = createSSHClient(server, port, username, password)
    scp = SCPClient(ssh.get_transport())
    scp.put(file)
    return



# I have not tested this with all the inputs
file = sys.argv[1]
server = sys.argv[2]
port = sys.argv[3]
username = sys.argv[4]
password = sys.argv[5]

send_File(file, server, username, password)
