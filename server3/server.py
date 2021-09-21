'''server 3 should recieve json data from server 2, and give CSV to server 1'''

from bottle import run, get, post, request
import time
import requests














run(host="127.0.0.1" , port=3333 , debug=True , reloader=True )