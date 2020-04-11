import urllib.request, urllib.parse, urllib.error
import requests
from bs4 import BeautifulSoup


#web_file = urllib.request.urlopen('https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M')
web_file =  requests.get('https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M')
soup = BeautifulSoup(web_file, 'web_file.parser')
tags = soup('a')
print(tags[0:5])
for line in web_file:
    #print(line.decode().strip())
    #print(line)
    pass

"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_412205.html'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
"""
