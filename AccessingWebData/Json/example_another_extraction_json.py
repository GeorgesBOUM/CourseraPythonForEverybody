#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 12:04:39 2020

@author: gregoire
"""

import json
import requests

# Getting the page, via the url, manually
page_manually = requests.get("https://api.datamuse.com/words?rel_rhy=funny")
# Extracting the gross data with the text attribute
data_from_text_attibute = json.loads(page_manually.text)
# Extracting the gross data with the json() method
data_from_json_method = page_manually.json()
print(type(data_from_json_method))
# formatting nicely data
data_formatted = json.dumps(data_from_json_method, indent=4)
# Page with params
"""
p = {'rel_rhy': 'funny'}
page_with_params = requests.get("https://api.datamuse.com/words", params=p)
print(json.dumps(page_with_params.json(), indent=2))
"""
