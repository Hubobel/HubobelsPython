import requests
import json
import time
import datetime
import os

pfad = os.path.dirname(__file__)
url_ferien ='http://api.smartnoob.de/ferien/v1/ferien/?bundesland=rp'
url_feiertage = 'http://api.smartnoob.de/ferien/v1/feiertage/?bundesland=rp'

jetzt = int(time.strftime('%j'))
tag = time.strftime('%d')

ferien = False
feiertag = False

if int(tag) == 1:       #Update einmal pro Monat
    print("Update Time!!!")
    resp_ferien = requests.get(url_ferien)
    resp_feiertage = requests.get(url_feiertage)
    data_ferien = resp_ferien.json()
    data_feiertage = resp_feiertage.json()

    with open(pfad + '/json_ferien.data', 'w') as outfile:
        json.dump(data_ferien, outfile)

    with open(pfad + '/json_feiertage.data', 'w') as outfile:
        json.dump(data_feiertage, outfile)

if os.path.isfile(pfad+'/json_ferien.data')!= True:     #Download der json, falls diese lokal nicht existieren
    print('nicht da!!!')

    resp_ferien = requests.get(url_ferien)
    resp_feiertage = requests.get(url_feiertage)
    data_ferien = resp_ferien.json()
    data_feiertage = resp_feiertage.json()

    with open(pfad+'/json_ferien.data','w') as outfile:
        json.dump(data_ferien, outfile)

    with open(pfad+'/json_feiertage.data','w') as outfile:
        json.dump(data_feiertage, outfile)

with open(pfad+'/json_ferien.data') as file:
    data_ferien=json.load(file)
with open(pfad+'/json_feiertage.data') as file:
    data_feiertage=json.load(file)

a= len(data_ferien['daten'])
x = 0

while x <a:
    beginn = data_ferien['daten'][x]['beginn']
    beginn = datetime.datetime.fromtimestamp(beginn)
    beginn = int(beginn.strftime('%j'))

    ende = data_ferien['daten'][x]['ende']
    ende = datetime.datetime.fromtimestamp(ende)
    ende = int(ende.strftime('%j'))-1

    if jetzt <= ende and jetzt >= beginn:
        ferien = True

    x = x+1

a= len(data_feiertage['daten'])
x = 0

while x <a:
    beginn = data_feiertage['daten'][x]['beginn']
    beginn = datetime.datetime.fromtimestamp(beginn)
    beginn = int(beginn.strftime('%j'))

    ende = data_feiertage['daten'][x]['ende']
    ende = datetime.datetime.fromtimestamp(ende)
    ende = int(ende.strftime('%j'))-1

    if jetzt <= ende and jetzt >= beginn:
        feiertag = True

    x = x+1

print('Es sind Ferien: '+ str(ferien))
print('Es ist ein Feiertag: '+str(feiertag))