import requests
import json
import time
import datetime
import os

url = 'http://hubobel.de/tt-rss/api/'
pfad = os.path.dirname(__file__)

datas = '{"op":"login","user":"admin","password":"polier2003"}'
resp = requests.post(url,datas)
data = resp.json()
print(data)
id = str(data['content']['session_id'])
datas = '{"sid":"'+id+'","op":"getFeeds","cat_id":-4}'
resp = requests.post(url,datas)
data = resp.json()

for i in data['content']:
    #print(i)
    if int(i['unread'])>0:
        print(i)

datas = '{"sid":"'+id+'","op":"getLabels","cat_id":-4}'
resp = requests.post(url,datas)
data = resp.json()
print(data['content'])




