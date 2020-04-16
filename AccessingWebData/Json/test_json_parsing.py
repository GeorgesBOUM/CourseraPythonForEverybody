#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 15:11:07 2020

@author: gregoire
"""


import json

data = '''
{
    "name": {
        "first name": "Georges",
        "last name": "BOUM"
    },
    "phone": {
        "type": "intl",
        "number": 123456789
    },
    "email": {
        "hide": "yes"
    }
}
'''

info = json.loads(data)
print(info['name'])
