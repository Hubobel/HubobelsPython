import pymysql
import bs4 as bs
import requests
import time

connection = pymysql.connect(db="hubobel",
                       user="hubobel",
                       passwd="polier2003",
                       host='10.0.1.123',charset='utf8')
cursor = connection.cursor()


requests.packages.urllib3.disable_warnings()
sauce = requests.get('https://lotto.web.de/webshop/product/eurojackpot/result', verify=False)
soup = bs.BeautifulSoup(sauce.text, 'lxml')
#print(soup)
ZahlenEuro = {'Datum': '', 'Z1': '', 'Z2': '', 'Z3': '', 'Z4': '', 'Z5': '', 'Eurozahl1': '', 'Eurozahl2': ''}
a = 1
daten = soup.find_all('div', class_="winning-numbers__number")
for i in daten:
    #print(i.text)
    if a <= 5:
        ZahlenEuro['Z' + str(a)] = int(i.text)
    elif a == 6:
        ZahlenEuro['Eurozahl1'] = int(i.text)
    elif a == 7:
        ZahlenEuro['Eurozahl2'] = int(i.text)
    a  = a + 1
#print(ZahlenEuro)
daten = soup.find_all('h2', class_="strong hidden-xs")
#print(daten)
for i in daten:
    date = i.text
    date = date.replace('  ', '')
    date = date.replace('\n', '')

start = (date.find('dem')) + 4
ende = (date.find('(Alle'))
ZahlenEuro['Datum'] = date[start:ende]
#print(ZahlenEuro)

requests.packages.urllib3.disable_warnings()
sauce = requests.get('https://lotto.web.de/webshop/product/lottonormal/result', verify=False)
soup = bs.BeautifulSoup(sauce.text, 'lxml')

Lottozahlen = {'Datum': '', 'Z1': '', 'Z2': '', 'Z3': '', 'Z4': '', 'Z5': '', 'Z6': '', 'Superzahl': '',
               'Spiel77': '', 'Super6': ''}
daten = soup.find_all('div', class_="winning-numbers__number")
zahlen = []
for i in daten:
    zahlen.append(int(i.text))
a = 1
while a != 7:
    Lottozahlen['Z' + str(a)] = zahlen[a - 1]
    a = a + 1
Spiel77 = ''
Super6 = ''
zahlen77 = []
daten = soup.find_all('div', class_="winning-numbers__number--additional")
for i in daten:
    zahlen77.append(int(i.text))
spiel77 = zahlen77[0:7]
super6 = zahlen77[-6:]
for i in spiel77:
    Spiel77 = Spiel77 + str(i)
for i in super6:
    Super6 = Super6 + str(i)

daten = soup.find_all('h2', class_="strong hidden-xs")
for i in daten:
    date = i.text
    date = date.replace('  ', '')
    date = date.replace('\n', '')

start = (date.find('dem')) + 4
ende = (date.find('(Alle'))

Lottozahlen['Superzahl'] = zahlen[6]
Lottozahlen['Spiel77'] = Spiel77
Lottozahlen['Super6'] = Super6
Lottozahlen['Datum'] = date[start:ende]




try:
    cursor.execute("""CREATE TABLE euro ( 
        datum Text, z1 INTEGER, z2 INTEGER, z3 INTEGER, z4 INTEGER, z5 INTEGER, sz1 INTEGER, sz2 INTEGER )""")
except:
    None

data = ZahlenEuro
sql = "INSERT INTO `euro`(`datum`, `z1`, `z2`, `z3`, `z4`, `z5`, `sz1`, `sz2`) VALUES" \
      " ('" + str(data['Datum']) + "','" + str(data['Z1']) + "','" + str(data['Z2']) + "','" + str(data['Z3']) + \
      "','" + str(data['Z4']) + "','" + str(data['Z5']) + "','" + str(data['Eurozahl1']) + "','" + str(
    data['Eurozahl2']) + "')"
sql_q = "SELECT * FROM euro WHERE datum like '%" + data['Datum'] + "%'"
resp = cursor.execute(sql_q)
if resp == 0:
    cursor.execute(sql)
data=Lottozahlen

if "Samstag," in date:
    try:
        cursor.execute("""CREATE TABLE samstag ( 
            datum Text, z1 INTEGER, z2 INTEGER, z3 INTEGER, z4 INTEGER, z5 INTEGER, z6 INTEGER, sz INTEGER, super6 INTEGER, spiel77 INTEGER)""")
    except:
        None
    sql = "INSERT INTO `samstag`(`datum`, `z1`, `z2`, `z3`, `z4`, `z5`, `z6`, `sz`, `super6`, `spiel77`) VALUES" \
          " ('" + str(data['Datum']) + "','" + str(data['Z1']) + "','" + str(data['Z2']) + "','" + str(data['Z3']) + \
          "','" + str(data['Z4']) + "','" + str(data['Z5']) + "','" + str(data['Z6']) + "','" + str(data['Superzahl']) + \
          "','" + str(data['Super6']) + "','" + str(data['Spiel77']) + "')"
    sql_q = "SELECT * FROM samstag WHERE datum like '%" + data['Datum'] + "%'"
    resp = cursor.execute(sql_q)
    if resp == 0:
        cursor.execute(sql)
    connection.commit()

if "Mittwoch," in date:
    try:
        cursor.execute("""CREATE TABLE mittwoch ( 
            datum Text, z1 INTEGER, z2 INTEGER, z3 INTEGER, z4 INTEGER, z5 INTEGER, z6 INTEGER, sz INTEGER, super6 INTEGER, spiel77 INTEGER)""")
    except:
        None

    sql = "INSERT INTO `mittwoch`(`datum`, `z1`, `z2`, `z3`, `z4`, `z5`, `z6`, `sz`, `super6`, `spiel77`) VALUES" \
          " ('" + str(data['Datum']) + "','" + str(data['Z1']) + "','" + str(data['Z2']) + "','" + str(data['Z3']) + \
          "','" + str(data['Z4']) + "','" + str(data['Z5']) + "','" + str(data['Z6']) + "','" + str(data['Superzahl']) + \
          "','" + str(data['Super6']) + "','" + str(data['Spiel77']) + "')"
    sql_q = "SELECT * FROM mittwoch WHERE datum like '%" + data['Datum'] + "%'"
    resp = cursor.execute(sql_q)
    if resp == 0:
        cursor.execute(sql)
    connection.commit()

    try:
        cursor.execute("""CREATE TABLE 6aus49 ( 
            datum Text, z1 INTEGER, z2 INTEGER, z3 INTEGER, z4 INTEGER, z5 INTEGER, z6 INTEGER, sz INTEGER, super6 INTEGER, spiel77 INTEGER)""")
    except:
        None

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

tag=int((time.strftime("%w")))
if tag != 5:
    print(Lottozahlen)
elif tag == 7:
    print(ZahlenEuro)
print(ZahlenEuro)