import bs4 as bs
import urllib.request



sauce=urllib.request.urlopen('http://www.lottotip-check.de').read()
soup=bs.BeautifulSoup(sauce,'html.parser')

#print(soup.prettify())
table=soup.find_all('table')
row=[]
ZahlenAll=[]
ZahlenMittwoch={'Datum':'','Z1':'','Z2':'','Z3':'','Z4':'','Z5':'','Z6':'','Superzahl':'','Spiel77':'','Super6':''}
ZahlenSamstag={'Datum':'','Z1':'','Z2':'','Z3':'','Z4':'','Z5':'','Z6':'','Superzahl':'','Spiel77':'','Super6':''}
ZahlenEuro={'Datum':'','Z1':'','Z2':'','Z3':'','Z4':'','Z5':'','Superzahl1':'','Superzahl2':''}
for i in table:
    table_rows = i.find_all('tr')
    for tr in table_rows:
        #print(tr)
        td = tr.find_all('td')
        if td != []:
            row = [i.text for i in td]
            #print(row)
            th = tr.find_all('th')
            sz = [i.text for i in th]
            #print(len(sz))
            if len(sz)==5:
                row.append(str(sz[2]))
                row.append(str(sz[3]))
            date = 'Ziehung vom: ' + str(sz[0])
            sz = str(sz[1])
            row.append(sz)
            row.insert(0, date)
    ZahlenAll.extend(row)
a=0
while a<=5:
    a=a+1
    ZahlenMittwoch['Z'+str(a)]=int(ZahlenAll[a])
ZahlenMittwoch['Datum']=ZahlenAll[0]
ZahlenMittwoch['Superzahl']=int(ZahlenAll[9])
ZahlenMittwoch['Super6']=int(ZahlenAll[8])
ZahlenMittwoch['Spiel77']=int(ZahlenAll[7])
print(ZahlenMittwoch)
a=0
while a<=5:
    a=a+1
    ZahlenSamstag['Z'+str(a)]=int(ZahlenAll[a + 18])
ZahlenSamstag['Datum']=ZahlenAll[18]
ZahlenSamstag['Superzahl']=int(ZahlenAll[27])
ZahlenSamstag['Super6']=int(ZahlenAll[26])
ZahlenSamstag['Spiel77']=int(ZahlenAll[25])
print(ZahlenSamstag)

a=0
while a<=4:
    a=a+1
    ZahlenEuro['Z'+str(a)]=int(ZahlenAll[a + 10])
ZahlenEuro['Datum']=ZahlenAll[10]
ZahlenEuro['Superzahl2']=int(ZahlenAll[17])
ZahlenEuro['Superzahl1']=int(ZahlenAll[16])
print(ZahlenEuro)
