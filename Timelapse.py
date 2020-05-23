import urllib.request
import requests
from datetime import datetime as DateTime
import time
import os
path = os.getcwd() + "/cameras/wz"
print(path)
monat = (time.strftime("%m"))
jahr = (time.strftime("%Y"))
tag = (time.strftime("%d"))

path = path + '/' + jahr + '/' + monat + '/' + tag

if not os.path.exists(path):
    print('gibts nicht')
    os.makedirs(path)

while True:
    url_WZ = 'http://10.0.1.241/api.cgi?cmd=GetMdState&user=admin&password=polier2003'
    resp_WZ = requests.get(url_WZ)
    data_WZ = resp_WZ.json()
    motion_wz = data_WZ[0]['value']['state']
    if motion_wz == 1:
        Zeit = DateTime.now().strftime('%H_%M_%S')
        url = 'http://10.0.1.241/cgi-bin/api.cgi?cmd=Snap&channel=0&rs=wuuPhkmUCeI9WG7C&user=admin&password=polier2003'
        urllib.request.urlretrieve(url, path + '/Bild'+Zeit+'.jpg')
    time.sleep(2)
