# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 16:44:07 2020

"""


import json

data = '''
{
  "name" : "Chuck",
  "phone" : {
    "type" : "intl",
    "number" : "+1 734 303 4456"
   },
   "email" : {
     "hide" : "yes"
   }
}'''

dat = json.loads(data)

print('name:', dat['name'])
print('number:', dat['phone']['number'])

#%%

data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]'''

new = json.loads(data)
for item in new:
    print('name:', item['name'])
    print('ID:', item['id'])
    print('attr:', item['x'])




















