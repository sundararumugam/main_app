# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 16:38:45 2022

@author: Arumugam
"""

class user():
    def __init__ (self,_id,username,password):
        self.id = _id
        self.username = username
        self.password = password
        
    def sample_fun(self):
        print(self.id)
        
        