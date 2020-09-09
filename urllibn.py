# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 12:26:15 2020

"""

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup as bs
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter-')
html = urllib.request.urlopen(url, context=ctx).read()
soup = bs(html, 'html.parser')

tags = soup('a')
for tag in tags:
    print(tag.get('href', None))













'''
for line in fhand:
    print(line.decode().strip())
'''


'''

counts = dict()
for line in fhand:
    words = line.decode().strip().split()
    for word in words:
        counts[word] = counts.get(word, 0)+1
print(counts)
'''
















