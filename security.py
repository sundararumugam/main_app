# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 16:30:40 2022

@author: Arumugam
"""
from User import user
from werkzeug.security import safe_str_cmp

#users = [
#        { "id":'1',
#          "username":'arumugam',
#          "password":"1234",
#        }       
#        ]
#
#username_maping = {'arumugam':
#       { "id":1,
#          "username":'arumugam',
#          "password":"1234",
#        } }
#    
#user_id_maping = { '1':
#          { "id":'1',
#          "username":'arumugam',
#          "password":"1234",
#        }
#        }

users = [
        user('1','arumugam','1234')
        ]

username_maping = { u.username:u for u in users}   
user_id_maping = {u.id:u for u in users}
          
def authenticate(username,password):
    user = username_maping.get(username,None)
#    if user and user['password'] == password:
    if user and safe_str_cmp(user.password,password):
        return user
    
def identity(payload):
    user_id = payload['identity']
    return user_id_maping.get(user_id,None)