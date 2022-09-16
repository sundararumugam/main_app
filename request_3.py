# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 19:06:13 2022

@author: Arumugam
"""

import requests



url = "https://miro.medium.com/max/875/1*kiBd3bGbyIZslncXRUuGkg.jpeg"
response = requests.get(url,stream=True)


data  = response.content
#df = open('sample.jpg','wb')
#df.write(data)

with open('sample.jpg','wb') as pf:
    for chunk in response.iter_content(chunk_size=50000):
        pf.write(chunk)