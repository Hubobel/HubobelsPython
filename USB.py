import os
from shutil import copyfile
import time

while True:
    mount = os.getcwd() + "/media"
    b = os.getcwd() + "/Ziel"
    inhaltmount = (os.listdir(mount))
    for all in inhaltmount:
        try:
            a = os.getcwd() + "/media/" + all
            inhalta = (os.listdir(a))
            inhaltb = (os.listdir(b))
            print(inhalta)
            if "sicherheitgehtvor.txt" in inhalta:
                #print('Stick steckt und wurde autentifiziert')
                inhalta.remove('sicherheitgehtvor.txt')
                for i in inhalta:
                    if i not in inhaltb:
                        print('copy')
                        copyfile(a+'/'+ i, b + '/' + i)
        except:
            None
    time.sleep(2)