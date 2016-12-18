import time
import requests

while 1:
    time.sleep(50)
    r = requests.get('http://glacial-plateau-17952.herokuapp.com/')
    print(r.text)
