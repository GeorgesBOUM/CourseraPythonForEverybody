#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 09:53:27 2020

@author: gregoire
"""

import requests
import json

d = {"address": "Faculty of Technical Sciences Novi Sad Serbia", "key": 42}
page = requests.get("http://py4e-data.dr-chuck.net/json", params=d)
data = json.loads(page.text)
print(data["results"][0]["place_id"])
