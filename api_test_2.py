# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 14:52:27 2022

@author: Arumugam
"""

from flask import Flask,jsonify,request
from flask_restful import Resource,Api
from flask_jwt import JWT,jwt_required
from security import authenticate,identity


app=Flask(__name__)
app.secret_key='asal'
api = Api(app)

items=[ ]

jwt = JWT(app,authenticate,identity)   # /auth

class Item(Resource):
    @jwt_required()
    def get(self,name):
        return {"items":items},200
    
#    def post(self,name):
#        data = request.get_json()
#        for item in items:
#          if item['name'] == data['name']:
#            return jsonify({"message":"Name already exist ! "})
#
#        new_dic = {"name":data["name"],
#               "purpose": data["purpose"],
#               "rate":data["rate"],
#               "expiry data":data["expiry data"]
#               }
#        items.append(data)
#        return jsonify(new_dic)
        
    def post(self,name):
        if next(filter(lambda x:x['name'] == name,items),None):
            return {"message":" An item with name '{}' already exists.".format(name)}
        
        data = request.get_json()
        item = {"name":name,"price":data['price']}
        items.append(item)
        return item,201
    
    def put(self,name):
        data = request.get_json()
        for item in items:
          if item['name'] == data['name']:
           item['rate'] = data['rate']
           return jsonify(item)

        return jsonify({"Message":"your mentioned name not there ! "})
        
    def delete(self,name):
        for i,item in enumerate(items):
         if item['name'] == name:
            items.pop(i)
            return jsonify({"message":" {} the name is deleted...".format(name)})
        return jsonify({"message":"this name not presented in this items list"})
    
api.add_resource(Item,'/item/<string:name>')

if __name__ == "__main__":
    app.run()