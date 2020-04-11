#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 10:44:49 2020

@author: gregoire
"""


import requests
from bs4 import BeautifulSoup

webpage = requests.get(
    'http://py4e-data.dr-chuck.net/known_by_Natan.html').text
soup = BeautifulSoup(webpage, 'lxml')

for i in range(6):
    links = soup.find_all('a')
    webpage = requests.get(links[17]['href']).text
    soup = BeautifulSoup(webpage, 'lxml')

links = soup.find_all('a')
print(links[17].text)
