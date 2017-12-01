import requests
import json
import time
import datetime
import os

session = requests.session()
url = 'http://www.newsblur.com/api/login'
datas = {'username':'hubobel','password':'polier2003'}
resp = session.post(url,datas)
data = resp.json()
print (data)


url = 'http://www.newsblur.com/reader/refresh_feeds'
resp = session.get(url)
data = resp.json()
print (json.dumps(data, indent=4))
print (data['id'])
url = 'http://www.newsblur.com/reader/feed/6212608'
resp = session.get(url)
data = resp.json()
print (json.dumps(data, indent=4))
print(data)