import datetime
import shutil
import traceback
import sys

if len(sys.argv) != 2:
    tage = 10
else:
    tage = int(sys.argv[1])

now = (datetime.datetime.now() - datetime.timedelta(tage))
day = now.strftime("%d")
month = now.strftime("%m")
year = now.strftime("%Y")

pfadflur="/mnt/usb/cameras/flur/"+year+"/"+month+"/"+day
pfadgarten="/mnt/usb/cameras/garten/"+year+"/"+month+"/"+day
pfadwz="/mnt/usb/cameras/wz/"+year+"/"+month+"/"+day
pfadhaustuer="/mnt/usb/cameras/haustuer/"+year+"/"+month+"/"+day

try:
    shutil.rmtree(pfadflur)
    print('L  sche '+ pfadflur)
except Exception as e:
    print('Beim Löschen kam es zu folgendem Fehler: ' + str(e))

try:
    shutil.rmtree(pfadgarten)
    print('L  sche '+ pfadgarten)
except Exception as e:
    print('Beim Löschen kam es zu folgendem Fehler: ' + str(e))

try:
    shutil.rmtree(pfadwz)
    print('L  sche '+ pfadwz)
except Exception as e:
    print('Beim Löschen kam es zu folgendem Fehler: ' + str(e))

try:
    shutil.rmtree(pfadhaustuer)
    print('L  sche '+ pfadhaustuer)
except Exception as e:
    print('Beim Löschen kam es zu folgendem Fehler: ' + str(e))
