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

if os.path.isdir(pfad+'/mpg')!= True:   #prüfen, ob das UNTERverzeichniss /mpg bereits existiert
    os.makedirs(pfad+'/mpg')
    print ('Downloadverzeichniss bei '+pfad +' /mpg/ created!!!')

if int(tag) == 1:       #Update einmal pro Monat
    print("It´s Update Time!!!")
    resp_ferien = requests.get(url_ferien)
    resp_feiertage = requests.get(url_feiertage)
    data_ferien = resp_ferien.json()
    data_feiertage = resp_feiertage.json()

    with open(pfad + '/json_ferien.data', 'w') as outfile:
        json.dump(data_ferien, outfile)

    with open(pfad + '/json_feiertage.data', 'w') as outfile:
        json.dump(data_feiertage, outfile)

if os.path.isfile(pfad+'/json_ferien.data')!= True:     #Download der json, falls diese lokal nicht existieren
    print('The json_xxx.datas not found, will try to download them from the API')

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

def download(url):
    #return None
    filename = pfad+'/mpg/'+url+'.pdf'
    url = 'http://www.mpglu.de/vps/'+url+'.pdf'
    req = requests.get(url, auth=('schueler', 'Ing8gresk'))
    file = open(filename, 'wb')
    for chunk in req.iter_content(100000):
        file.write(chunk)
    file.close()
    return None

def modification_date(filename):
    t = os.path.getmtime(filename)
    return datetime.datetime.fromtimestamp(t)


try:
    os.rename(pfad + '/mpg/heute.pdf', pfad +'/mpg/heute1.pdf')
    url = 'heute'
    download(url)
    x = os.stat(pfad+'/mpg/heute.pdf')
    x = x.st_size
    x1 = str(x)
    y = os.stat(pfad+'/mpg/heute1.pdf')
    y = y.st_size
    y1 = str(y)
    if x != y:
        print("die Dateien 'heute' sind ungleich")
        os.system('s-nail -a mpg/heute.pdf -s "Alpha-MPG-Vertretungsliste" schneeschieben@web.de')
    else:
        print("Es gibt keine neuen Mals mit 'heute'")
        d = modification_date(pfad+'/mpg/heute.pdf')
        d = d.strftime('%H:%M:%S')
        print("heute: " + d + ' '+ x1 + ' Bytes')
        d = modification_date(pfad+'/mpg/heute1.pdf')
        d = d.strftime('%H:%M:%S')
        print("heute1: " + d + ' '+ y1 + ' Bytes')
except FileNotFoundError:
    print("File Heute.PDF not found")
    print("Will try to download it from the MPG-Server")
    url = 'heute'
    download(url)

try:
    os.rename(pfad+'/mpg/morgen.pdf', pfad+'/mpg/morgen1.pdf')
    url = 'morgen'
    download(url)
    x = os.stat(pfad+'/mpg/morgen.pdf')
    x = x.st_size
    x1 = str(x)
    y = os.stat(pfad+'/mpg/morgen1.pdf')
    y = y.st_size
    y1 = str(y)
    if x != y:
        print("die Dateien 'morgen' sind ungleich")
        os.system('s-nail -a mpg/morgen.pdf -s "Alpha-MPG-Vertretungsliste" schneeschieben@web.de')
    else:
        print("Es gibt keine neuen Mails mit 'morgen'")

        d= modification_date(pfad+'/mpg/morgen.pdf')
        d = d.strftime('%H:%M:%S')
        print("morgen: " + d + ' ' + x1 + ' Bytes')
        d = modification_date(pfad+'/mpg/morgen1.pdf')
        d = d.strftime('%H:%M:%S')
        print("morgen1: " + d + ' ' + x1 + ' Bytes')
except FileNotFoundError:
    print("File Morgen.PDF not found")
    print("Will try to download it from the MPG-Server")
    url = 'morgen'
    download(url)

print ("Tats. Dateiposition:", __file__)
pfad = os.path.dirname(__file__)
print (pfad)
