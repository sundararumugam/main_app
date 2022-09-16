# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 14:11:18 2022

@author: Arumugam
"""

from flask import Flask, render_template,request,jsonify
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/update/',methods=['post'])
def update():
    data = request.form()
    print(type(data))
    print(data)
    






if __name__ == '__main__':
   app.run()
   
   
   