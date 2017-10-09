import requests
import os
import datetime

def download(url):
    #return None
    filename = 'mpg/'+url+'.pdf'
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

if os.path.isdir('mpg')!= True:
    os.makedirs('mpg')

try:
    os.rename('mpg/heute.pdf', 'mpg/heute1.pdf')
    url = 'heute'
    download(url)
    x = os.stat('mpg/heute.pdf')
    x = x.st_size
    y = os.stat('mpg/heute1.pdf')
    y = y.st_size
    if x != y:
        print("die Dateien 'heute' sind ungleich")
        os.system('s-nail -a mpg/heute.pdf -s "Alpha-MPG-Vertretungsliste" schneeschieben@web.de')
    else:
        print("Es gibt keine neuen Mals mit 'heute'")
        d = modification_date('mpg/heute.pdf')
        d = d.strftime('%H:%M:%S')
        print("heute: " + d )
        d = modification_date('mpg/heute1.pdf')
        d = d.strftime('%H:%M:%S')
        print("heute1: " + d)
except FileNotFoundError:
    print("File Heute.PDF not found")
    print("Will try to download it from the MPG-Server")
    url = 'heute'
    download(url)

try:
    os.rename('mpg/morgen.pdf', 'mpg/morgen1.pdf')
    url = 'morgen'
    download(url)
    x = os.stat('mpg/morgen.pdf')
    x = x.st_size
    y = os.stat('mpg/morgen1.pdf')
    y = y.st_size
    if x != y:
        print("die Dateien 'morgen' sind ungleich")
        os.system('s-nail -a mpg/morgen.pdf -s "Alpha-MPG-Vertretungsliste" schneeschieben@web.de')
    else:
        print("Es gibt keine neuen Mails mit 'morgen'")

        d= modification_date('mpg/morgen.pdf')
        d = d.strftime('%H:%M:%S')
        print ("morgen: " + d)
        d = modification_date('mpg/morgen1.pdf')
        d = d.strftime('%H:%M:%S')
        print("morgen1: " + d)
except FileNotFoundError:
    print("File Morgen.PDF not found")
    print("Will try to download it from the MPG-Server")
    url = 'morgen'
    download(url)


