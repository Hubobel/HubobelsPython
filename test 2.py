import requests
import random

def Lotto():
    a = (sorted(random.sample(range(1, 49), 6)))
    b = random.randrange(0, 9)
    while b in a:
        b = random.randrange(1, 9)
    lotto =  str(a) + ',Superzahl: ' + str(b)
    return lotto,a,b

url_zitat = 'http://api.hubobel.de/lotto/Mittwoch'
resp_zitat = requests.get(url_zitat)
data_zitat = resp_zitat.json()


inhalt=data_zitat[1]
a=[]

count=1

while count<7:
    index=str('Z'+str(count))
    a.append(inhalt[index])
    count=count+1


b,c,d=Lotto()


treffer=0
ergebniss=[]
superzahl=''
for i in c:
    if i in a:
        treffer=treffer+1
        ergebniss.append(i)
    if d == inhalt['Superzahl']:
        superzahl=' und die Superzahl!'
print('Die aktuellen Lottozahlen der '+inhalt['Datum']+' lauten: '+str(a)+',Superzahl: '+str(inhalt['Superzahl']))
print('Sie haben getippt: '+ b)
print('Sie haben '+str(treffer)+' Richtige '+str(ergebniss)+superzahl)