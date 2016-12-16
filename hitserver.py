import os
import time
import requests

port=str(os.environ.get('PORT',5000))
while 1:
    #time.sleep(3)
    r=requests.get('http://0.0.0.0:'+port+'/')
    print(r.text)

