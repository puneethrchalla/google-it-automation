#!/usr/bin/env python3

import requests
import json

resp = requests.get("https://httpbin.org/get").json()

for key, value in resp.items():
    print("{}= {}".format(key,value))