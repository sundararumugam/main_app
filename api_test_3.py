# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 19:00:30 2022

@author: Arumugam
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 13:13:40 2022

@author: Arumugam
"""

from flask import Flask,render_template,request,jsonify



app = Flask(__name__)

#  data
items=[
        { "name": "a1",
          "purpose":"cleaning",
          "rate":23,
          "expiry data":"12-3-2022"
               }
       ]


# home page 
@app.route('/')
def home():
    return render_template('home.html')


# get method
    
@app.route('/items',methods=['get']) 
def store():
    return {'items':items}


# post method
    
@app.route('/items',methods=['post'])
def add_item():
    data = request.get_json()
    for item in items:
        if item['name'] == data['name']:
            return jsonify({"message":"Name already exist ! "})

    new_dic = {"name":data["name"],
               "purpose": data["purpose"],
               "rate":data["rate"],
               "expiry data":data["expiry data"]
               }
    items.append(data)
    return jsonify(new_dic)

# put method
    
@app.route('/items',methods=['put'])
def modify_rate():
   data = request.get_json()
   for item in items:
       if item['name'] == data['name']:
           item['rate'] = data['rate']
           return jsonify(item)

   return jsonify({"Message":"your mentioned name not there ! "})
           
# delete the idem from data
@app.route('/items/<string:name>',methods=['delete'])
def remove_item(name):
    for i,item in enumerate(items):
        if item['name'] == name:
            items.pop(i)
            return jsonify({"message":" {} the name is deleted...".format(name)})
    return jsonify({"message":"this name not presented in this items list"})
# main application calling  
if __name__ == "__main__":
    app.run()
    