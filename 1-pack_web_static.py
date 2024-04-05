#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the contents of the web_static folder of your AirBnB Clone repo"""
import os
from fabric.api import *
from datetime import datetime

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
    
    

    
