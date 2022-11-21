# grep pm.max_children /etc/php-fpm.d/www.conf | grep -v '^;' | grep -Eo '[0-9]{2,3}' | xargs /home/gitlab/active_processes.py



#!/bin/python3
import requests
import json
import subprocess
import sys
from loguru import logger

logger.add("/var/log/error_php_processes.log", format="{time} {level} {message}", 
level="ERROR")

base_url = "http://localhost"
response = requests.get(base_url + "/status", params="json")
json_response = response.json()
max_children = int(sys.argv[1])
active_children = int(json_response['active processes'])

if max_children <= active_children:
    logger.error(f"""active_children: {active_children}, max_children:, {max_children}""")
    subprocess.call(["systemctl", "restart", "php-fpm"])
else:
    logger.info("success")
