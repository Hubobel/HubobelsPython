import requests
import json
import time
import datetime

url_ferien ='http://api.smartnoob.de/ferien/v1/ferien/?bundesland=rp'
url_feiertage = 'http://api.smartnoob.de/ferien/v1/feiertage/?bundesland=rp'

resp_ferien = requests.get(url_ferien)
resp_feiertage = requests.get(url_feiertage)

data_ferien = resp_ferien.json()
data_feiertage = resp_feiertage.json()

a= len(data_ferien['daten'])
x = 0

while x <a:
    jetzt = time.strftime('%j')

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
