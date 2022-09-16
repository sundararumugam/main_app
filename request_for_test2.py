# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 14:22:15 2022

@author: Arumugam
"""

import requests 

# get method

api_url = "http://127.0.0.1:5000/item/a2"
response = requests.get(api_url)
data = response.json()
print(data)


# Post method

#df = { "name": "a2",
#          "purpose":"washing",
#          "rate":73,
#          "expiry data":"23-4-2022"
#               }

#df = { "name": "a3",
#          "purpose":"painting",
#          "rate":63,
#          "expiry data":"7-6-2022"
#               }
#
#
#api_url = "http://127.0.0.1:5000/item/a2"
#response = requests.post(api_url,json=df)
#data = response.json()
#print(data)

# put method
#df = { "name": "a3",
#          "purpose":"painting",
#          "rate":103,
#          "expiry data":"7-6-2022"
#               }
#
#api_url = "http://127.0.0.1:5000/items"
#response = requests.put(api_url,json=df)
#data = response.json()
#print(data)


# delete method
#
#api_url = "http://127.0.0.1:5000/items/a3"
#response = requests.delete(api_url)
#data = response.json()
#print(data)

