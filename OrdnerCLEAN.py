import os
from datetime import datetime

pfad = os.getcwd() + "/Ziel/"
content = (os.listdir(pfad))
jetzt = datetime.now()
diff_seconds = (jetzt-datetime.fromtimestamp(0)).total_seconds()
jetzt = datetime.fromtimestamp(0)


for i in content:
    datum = (os.path.getmtime(pfad + i))
    alter = (diff_seconds-datum)/60/60/24
    if i[:1] == "(":
        b = i.find(')')
        dauer = int((i[1:b]))-int(alter)
        print(i + ' wird in ' + str(dauer) + ' Tagen gelöscht')
        if dauer < 1:
            os.remove(pfad+i)
            print(i + ' wurde gelöscht!')
    elif alter > 14:
        os.remove(pfad + i)
        print(i + ' wurde gelöscht!')