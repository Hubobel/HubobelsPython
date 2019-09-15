# -*- coding: utf-8 -*-
import bs4 as bs
import requests
import pymysql

connection = pymysql.connect(db="hubobel",
                       user="hubobel",
                       passwd="polier2003",
                       host='10.0.1.59',charset='utf8')
cursor = connection.cursor()
try:
    cursor.execute("""CREATE TABLE Filosofie ( 
        Nr INTEGER, Filosofie TEXT)""")
except:
    print('Error')
    None
sql = "SELECT * FROM Filosofie ORDER BY Nr DESC"
resp = cursor.execute(sql)
AnzahlStart=resp
db=[]
ergebniss=''
requests.packages.urllib3.disable_warnings()
sauce = requests.get('https://www.swr3.de/wraps/fun/filosofie/neu.php?id=1151', verify=False)
soup = bs.BeautifulSoup(sauce.text, 'lxml')
for i in soup.find_all('div'):
    ergebniss=ergebniss+str(i)
start=(ergebniss.find('href="/wraps/fun/filosofie/neu.php?id=1152&amp;cf=42"> weiter &gt; </a>   <a class="linkred" href='))
anzahl=int(ergebniss[start+131:start+135])
start=int(resp)+1+110

while start <= anzahl:
    url='https://www.swr3.de/wraps/fun/filosofie/neu.php?id='+str(start)
    sauce = requests.get(url, verify=False)
    soup = bs.BeautifulSoup(sauce.content,'lxml')
    for i in soup.find_all('strong'):
        filosophie=(i.text)
    #print(filosophie)
    #print(start,' von ',anzahl)
    sql = "INSERT INTO `Filosofie`(`Nr`, `Filosofie`) VALUES ('" + str(start) + "','" + filosophie + "')"
    sql_q = "SELECT * FROM Filosofie WHERE Filosofie like '%" + str(filosophie) + "%'"
    try:
        resp = cursor.execute(sql_q)
        if resp == 0:
            try:
                resp = cursor.execute(sql)
                db.append(filosophie)
            except:
                print('Es gab ein Problem beim Schreiben des facts in die DB')
    except:
        None
    connection.commit()
    start +=1
sql = "SELECT * FROM Filosofie ORDER BY Nr DESC"
AnzahlEnde = cursor.execute(sql)
print('Es wurden ', int(AnzahlEnde) - int(AnzahlStart), ' neue Filosofien der DB hinzugefügt.')
if len(db)>0:
    for i in db:
        print(i)
cursor.close()
connection.close()
