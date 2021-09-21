'''server 1 should send xml data to server 2, and recieve a CSV from server 3'''

from bottle import run, get, post, requests
import time
import requests
import xml.etree.cElementTree as ET

data='''<?xml version="1.0" encoding="UTF-8"?>
<data>
    10
</data>
'''
myroot = ET.fromstring(data)

#########################################
@post("/request")
def do():
    request = requests.post('http//:127.0.0.1:2222', data=data, headers={"application":"xml"})
    print("XML sent")
    
    
   
#########################################






run(host="127.0.0.1" , port=1111 , debug=True , reloader=True )