#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the
contents of the web_static folder of your AirBnB Clone repo."""
import os
from fabric.api import *
from datetime import datetime

env.hosts = ['54.237.118.67', '52.91.146.16']
env.username = 'ubuntu'
env.key_filename = '/root/.ssh/id_rsa'
# '~/.ssh/id_rsa'


def do_pack():
    """Function to generate a .tgz archive"""
    # Creating the folder versions
    local('sudo mkdir -p versions')

    # Getting the current time
    time_now = datetime.now()
    str_time = time_now.strftime("%Y%m%d%H%M%S")

    local(f'sudo tar -cvzf versions/web_static_{str_time}.tgz web_static')

    file_path = f"versions/web_static_{str_time}.tgz"
    file_size = os.path.getsize(file_path)

    if os.path.exists(file_path):
        print(f"web_static packed: {file_path} -> {file_size}Bytes")
    else:
        return None


# Path: 2-do_deploy_web_static.py
def do_deploy(archive_path):
    """
    Fabric script (based on the file 1-pack_web_static.py
    that distributes an archive to your web servers, using
    the function do_deploy.
    """
    if not os.path.exists(archive_path):
        return False
    try:
        archive_name = archive_path.split("/")[-1]
        file_name = archive_name.split(".")[0]

        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")

        # Create the directory to uncompress the file
        run(f"sudo mkdir -p /data/web_static/releases/{file_name}")
        path = f"/data/web_static/releases/{file_name}"
        # Uncompress the file into the created directory
        run(f"sudo tar -xzf /tmp/{archive_name} -C {path}")

        # Delete the archive from the web server
        run(f"sudo rm /tmp/{archive_name}")

        # Delete the symbolic link
        run("sudo rm -rf /data/web_static/current")
        path_s = f"/data/web_static/curren"
        # Create a new symbolic link
        run(f"sudo ln -s /data/web_static/releases/{file_name}/ {path_s}")

        # Finish the deployment
        print("New version deployed!")
    except Exception as e:
        print(e)
        print("Deployment failed!")
        return False
    # Return True if the deployment was successful
    return True
