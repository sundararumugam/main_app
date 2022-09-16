# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 14:53:58 2022

@author: Arumugam
"""

import requests
api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(api_url)
data = response.json()

print(data)
print('headers')
print(response.headers)
print('status_code')
print(response.status_code)
print('content')
print(response.content)

print('cookies')
print(response.cookies)
print('history')
print(response.history)
print('text')
print(response.text)

print(response.url)