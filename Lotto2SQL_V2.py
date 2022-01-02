import pymysql
import bs4 as bs
import requests
import time

requests.packages.urllib3.disable_warnings()
sauce = requests.get('https://www.lotto-hessen.de/lotto6aus49/gewinnzahlen-quoten/gewinnzahlen', verify=False)
soup = bs.BeautifulSoup(sauce.text, 'lxml')
print(soup)
Lottozahlen = {'Datum': '', 'Z1': '', 'Z2': '', 'Z3': '', 'Z4': '', 'Z5': '', 'Z6': '', 'Superzahl': '',
               'Spiel77': '', 'Super6': ''}
a = 0
daten = soup.find_all('span')
zahlen = []
for i in daten:
    if a >= 1 and a < 7:
        Lottozahlen['Z' + str(a)] = i.text
    if a == 7:
        Lottozahlen['Superzahl'] = i.text
    a = a + 1
    if i.text == 'Tag':
        a = 1
for i in daten:
    if a > 0 and a < 8:
        Lottozahlen['Spiel77'] = Lottozahlen['Spiel77']+i.text
    if a > 7 and a < 14:
        Lottozahlen['Super6'] = Lottozahlen['Super6']+i.text
    a = a +1
    if i.text == 'Superzahl':
        a = 1
daten = soup.find_all('h2', class_="h4")
for i in daten:
    Lottozahlen['Datum']=i.text
a=1
while a < 7:
    Lottozahlen['Z' + str(a)] = int(Lottozahlen['Z'+str(a)])
    a = a + 1
Lottozahlen['Superzahl'] = int(Lottozahlen['Superzahl'])
Lottozahlen['Spiel77'] = int(Lottozahlen['Spiel77'])
Lottozahlen['Super6'] = int(Lottozahlen['Super6'])
datum = Lottozahlen['Datum']
start = datum.find(', ')
Lottozahlen['Datum'] = datum[start+2:]
print(Lottozahlen)
requests.packages.urllib3.disable_warnings()
sauce = requests.get('https://www.lotto-hessen.de/eurojackpot/gewinnzahlen-quoten/gewinnzahlen?gbn=5', verify=False)
soup = bs.BeautifulSoup(sauce.text, 'lxml')
ZahlenEuro = {'Datum': '', 'Z1': '', 'Z2': '', 'Z3': '', 'Z4': '', 'Z5': '', 'Eurozahl1': '', 'Eurozahl2': ''}
daten = soup.find_all('span')
for i in daten:
    if i.text =='Tag':
        a = -1
    a = a + 1
    if a >= 1 and a < 6:
        ZahlenEuro['Z'+str(a)] = int(i.text)
    if a == 6:
        ZahlenEuro['Eurozahl1'] = int(i.text)
    if a == 7:
        ZahlenEuro['Eurozahl2'] = int(i.text)
daten = soup.find_all('h2', class_="h4")
for i in daten:
    ZahlenEuro['Datum'] = i.text
datums = ZahlenEuro['Datum']
start = datums.find(', ')
ZahlenEuro['Datum'] = datums[start+2:]
print(ZahlenEuro)

connection = pymysql.connect(db="hubobel",
                       user="hubobel",
                       passwd="polier2003",
                       host='10.0.1.123',charset='utf8')
cursor = connection.cursor()

data = ZahlenEuro
sql = "INSERT INTO `euro`(`datum`, `z1`, `z2`, `z3`, `z4`, `z5`, `sz1`, `sz2`) VALUES" \
      " ('" + str(data['Datum']) + "','" + str(data['Z1']) + "','" + str(data['Z2']) + "','" + str(data['Z3']) + \
      "','" + str(data['Z4']) + "','" + str(data['Z5']) + "','" + str(data['Eurozahl1']) + "','" + str(
    data['Eurozahl2']) + "')"
sql_q = "SELECT * FROM euro WHERE datum like '%" + data['Datum'] + "%'"
resp = cursor.execute(sql_q)
if resp == 0:
    cursor.execute(sql)

data = Lottozahlen
if 'Samstag,' in datum:
    sql = "INSERT INTO `samstag`(`datum`, `z1`, `z2`, `z3`, `z4`, `z5`, `z6`, `sz`, `super6`, `spiel77`) VALUES" \
          " ('" + str(data['Datum']) + "','" + str(data['Z1']) + "','" + str(data['Z2']) + "','" + str(data['Z3']) + \
          "','" + str(data['Z4']) + "','" + str(data['Z5']) + "','" + str(data['Z6']) + "','" + str(data['Superzahl']) + \
          "','" + str(data['Super6']) + "','" + str(data['Spiel77']) + "')"
    sql_q = "SELECT * FROM samstag WHERE datum like '%" + data['Datum'] + "%'"
    resp = cursor.execute(sql_q)
    if resp == 0:
        cursor.execute(sql)

if 'Mittwoch,' in datum:
    sql = "INSERT INTO `mittwoch`(`datum`, `z1`, `z2`, `z3`, `z4`, `z5`, `z6`, `sz`, `super6`, `spiel77`) VALUES" \
          " ('" + str(data['Datum']) + "','" + str(data['Z1']) + "','" + str(data['Z2']) + "','" + str(data['Z3']) + \
          "','" + str(data['Z4']) + "','" + str(data['Z5']) + "','" + str(data['Z6']) + "','" + str(data['Superzahl']) + \
          "','" + str(data['Super6']) + "','" + str(data['Spiel77']) + "')"
    sql_q = "SELECT * FROM mittwoch WHERE datum like '%" + data['Datum'] + "%'"
    resp = cursor.execute(sql_q)
    if resp == 0:
        cursor.execute(sql)

sql = "INSERT INTO `6aus49`(`datum`, `z1`, `z2`, `z3`, `z4`, `z5`, `z6`, `sz`, `super6`, `spiel77`) VALUES" \
      " ('" + str(data['Datum']) + "','" + str(data['Z1']) + "','" + str(data['Z2']) + "','" + str(data['Z3']) + \
      "','" + str(data['Z4']) + "','" + str(data['Z5']) + "','" + str(data['Z6']) + "','" + str(data['Superzahl']) + \
      "','" + str(data['Super6']) + "','" + str(data['Spiel77']) + "')"
sql_q = "SELECT * FROM 6aus49 WHERE datum like '%" + data['Datum'] + "%'"
resp = cursor.execute(sql_q)
if resp == 0:
    cursor.execute(sql)

connection.commit()
cursor.close()
connection.close()