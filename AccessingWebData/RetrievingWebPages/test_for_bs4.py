#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 15:06:53 2020

@author: gregoire
"""

from bs4 import BeautifulSoup


with open('test_for_bs4.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')
articles = soup.find_all('div', class_='article')

for article in articles:
    print(article.a.text)
    print(article.p.text)
    print()
