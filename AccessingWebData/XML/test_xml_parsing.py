import xml.etree.ElementTree as ET

data = '''
<person>
    <name>Boum</name>
    <forename>Georges</forename>
    <phone>123456789</phone>
    <email hide='yes'/>
</person>
'''
tree = ET.fromstring(data)
name = tree.find('name').text
forename = tree.find('forename').text
email = tree.find('email').get('hide')

print(type(data))
'''
print('Name:', name)
print('Forename:', forename)
print('Email:', email)
'''