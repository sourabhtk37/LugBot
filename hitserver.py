import os
import time
import requests

while 1:
    time.sleep(50)
    r=requests.get('http://0.0.0.0:5000/')
