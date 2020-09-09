# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 15:35:19 2020

"""


import xml.etree.ElementTree as ET

data = '''
<stuff>
  <users>
    <user x="2">
      <id>001</id>
      <name>Chuck</name>
    </user>
    <user x="7">
      <id>009</id>
      <name>Brent</name>
    </user>
  </users>
</stuff>'''

stu = ET.fromstring(data)
one = stu.findall('users/user')
print('user count:', len(one))
for tag in one:
    print('name:', tag.find('name').text)
    print('id:', tag.find('id').text)
    print('atrr:', tag.get('x'))




#%%
data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
    +1 734 303 4456
  </phone>
  <email hide="yes" />
</person>'''

tree  = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Phn:', tree.find('phone').text.strip())
print('Attr:', tree.find('email').get('hide'))





