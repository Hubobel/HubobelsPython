# -*- coding: utf-8 -*-
import bs4 as bs
import requests
import time
import pymysql

connection = pymysql.connect(db="hubobel",
                       user="hubobel",
                       passwd="polier2003",
                       host='10.0.1.59',charset='utf8')
cursor = connection.cursor()
try:
    cursor.execute("""CREATE TABLE test ( 
        nr INTEGER, Filosophiefact TEXT)""")
except:
    print ('weiter')
sql = "SELECT * FROM test ORDER BY nr DESC"
resp = cursor.execute(sql)

ergebniss=''

requests.packages.urllib3.disable_warnings()
sauce = requests.get('https://www.swr3.de/wraps/fun/filosofie/neu.php?id=11', verify=False)
soup = bs.BeautifulSoup(sauce.text, 'lxml')

for i in soup.find_all('div'):
    ergebniss=ergebniss+str(i)

start=(ergebniss.find('href="/wraps/fun/filosofie/neu.php?id=12"> weiter &gt; </a>   <a class="linkred" href='))
anzahl=int(ergebniss[start+119:start+123])
start=int(resp)+1

while start <= anzahl:
    url='https://www.swr3.de/wraps/fun/filosofie/neu.php?id='+str(start)
    sauce = requests.get(url, verify=False)
    soup = bs.BeautifulSoup(sauce.content,'lxml')
    for i in soup.find_all('strong'):
        filosophie=(i.text)
    print(filosophie)
    print(start,' von ',anzahl)
    sql = "INSERT INTO `test`(`nr`, `Filosophiefact`) VALUES ('" + str(start) + "','" + filosophie + "')"
    sql_q = "SELECT * FROM test WHERE Filosophiefact like '%" + str(filosophie) + "%'"
    resp = cursor.execute(sql_q)
    if resp == 0:
        try:
            resp = cursor.execute(sql)
        except:
            print('Es gab ein Problem beim Schreiben des facts in die DB')
    connection.commit()
    start +=1
    time.sleep(1)
cursor.close()
connection.close()

