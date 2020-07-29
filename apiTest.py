#!/usr/bin/python3

import requests

response = requests.get("http://localhost:3000/")

if response.status_code == 200 :
    sys.exit()
else:
    sys.exit(1)