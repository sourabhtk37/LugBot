import time
import requests

while 1:
    time.sleep(50)
    r = requests.get('https://glacial-plateau-17952.herokuapp.com/')
