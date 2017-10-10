import requests
import json
import time
import datetime
import os

pfad = os.path.dirname(__file__)
url_ferien ='http://api.smartnoob.de/ferien/v1/ferien/?bundesland=rp'
url_feiertage = 'http://api.smartnoob.de/ferien/v1/feiertage/?bundesland=rp'

jetzt = time.strftime('%j')
tag = time.strftime('%d')

if int(tag) == 1:
    print("Update Time!!!")
    resp_ferien = requests.get(url_ferien)
    resp_feiertage = requests.get(url_feiertage)
    data_ferien = resp_ferien.json()
    data_feiertage = resp_feiertage.json()

    with open(pfad + '/json_ferien.data', 'w') as outfile:
        json.dump(data_ferien, outfile)

    with open(pfad + '/json_feiertage.data', 'w') as outfile:
        json.dump(data_ferien, outfile)

if os.path.isfile(pfad+'/json_ferien.data')!= True:
    print('nicht da!!!')

    resp_ferien = requests.get(url_ferien)
    resp_feiertage = requests.get(url_feiertage)
    data_ferien = resp_ferien.json()
    data_feiertage = resp_feiertage.json()

    with open(pfad+'/json_ferien.data','w') as outfile:
        json.dump(data_ferien, outfile)

    with open(pfad+'/json_feiertage.data','w') as outfile:
        json.dump(data_ferien, outfile)

with open(pfad+'/json_ferien.data') as file:
    data_ferien=json.load(file)
with open(pfad+'/json_feiertage.data') as file:
    data_feiertage=json.load(file)

a= len(data_ferien['daten'])
x = 0

while x <a:
    beginn = data_ferien['daten'][x]['beginn']
    beginn = datetime.datetime.fromtimestamp(beginn)
    beginn = beginn.strftime('%j')

    ende = data_ferien['daten'][x]['ende']
    ende = datetime.datetime.fromtimestamp(ende)
    ende = ende.strftime('%j')

    print(beginn)
    print(ende)
    print(jetzt)

    x = x+1
