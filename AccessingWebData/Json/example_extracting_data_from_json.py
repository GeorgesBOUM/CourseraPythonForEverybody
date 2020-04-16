#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 10:16:18 2020

@author: gregoire
"""

import json
import requests
data_from_web = requests.get(
    "http://py4e-data.dr-chuck.net/comments_412208.json").text
data_parsed = json.loads(data_from_web)
print(type(data_parsed))
'''
total = 0
for i in range(len(data_parsed['comments'])):
    total += data_parsed['comments'][i]['count']
print(total)
'''
