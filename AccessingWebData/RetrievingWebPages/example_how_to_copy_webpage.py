#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 17:10:54 2020

@author: gregoire
"""


from bs4 import BeautifulSoup
import requests


webpage = requests.get('http://www.marmelune.net').text
soup = BeautifulSoup(webpage, 'lxml')
with open('marmelune_copy.html', 'w') as marmelune:
    marmelune.write(soup.prettify())
