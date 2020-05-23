import os
import time
path = "testa"
monat = (time.strftime("%m"))
jahr = (time.strftime("%Y"))

path = path + '/' + jahr + '/' + monat
if os.path.exists(path) == False:
    print('gibts nicht')
    os.makedirs(path)

