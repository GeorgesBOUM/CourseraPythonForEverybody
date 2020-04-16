import requests
import xml.etree.ElementTree as ET

comments_page = requests.get(
    "http://py4e-data.dr-chuck.net/comments_412207.xml").text
tree = ET.fromstring(comments_page)
comments_counts_list = tree.findall("comments/comment/count")
total = 0
for elt in comments_counts_list:
    total += int(elt.text)
print(total)
