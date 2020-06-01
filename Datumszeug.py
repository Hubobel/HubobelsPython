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

pfadflur="/media/cameras/flur/"+year+"/"+month+"/"+day
pfadgarten="/media/cameras/garten/"+year+"/"+month+"/"+day
pfadwz="/media/cameras/wz/"+year+"/"+month+"/"+day

try:
    shutil.rmtree(pfadflur)
    print('Lösche '+ pfadflur)
except Exception as e:
    print('Beim Löschen kam es zu folgendem Fehler: ' + str(e))

try:
    shutil.rmtree(pfadgarten)
    print('Lösche '+ pfadgarten)
except Exception as e:
    print('Beim Löschen kam es zu folgendem Fehler: ' + str(e))

try:
    shutil.rmtree(pfadwz)
    print('Lösche '+ pfadwz)
except Exception as e:
    print('Beim Löschen kam es zu folgendem Fehler: ' + str(e))
