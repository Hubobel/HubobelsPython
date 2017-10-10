import requests
import os
import datetime

pfad = os.path.dirname(__file__)

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

if os.path.isdir(pfad+'/mpg')!= True:
    os.makedirs(pfad+'/mpg')
    print ('Downloadverzeichniss bei '+pfad +' /mpg/ created!!!')

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
