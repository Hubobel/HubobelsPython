import requests
import pymysql
import time


connection = pymysql.connect(db="hubobel",
                       user="hubobel",
                       passwd="polier2003",
                       host='10.0.1.59',charset='utf8')
cursor = connection.cursor()

wtag = time.strftime('%w')

if wtag == 3:
    try:
        cursor.execute("""CREATE TABLE mittwoch ( 
            datum Text, z1 INTEGER, z2 INTEGER, z3 INTEGER, z4 INTEGER, z5 INTEGER, z6 INTEGER, sz INTEGER, super6 INTEGER, spiel77 INTEGER)""")
    except:
        None
    url_zitat = 'http://api.hubobel.de/lotto/Mittwoch'
    resp_zitat = requests.get(url_zitat)
    data_zitat = resp_zitat.json()
    data=data_zitat[1]
    sql = "INSERT INTO `mittwoch`(`datum`, `z1`, `z2`, `z3`, `z4`, `z5`, `z6`, `sz`, `super6`, `spiel77` ) VALUES " \
          "('"+str(data['Datum'])+"','"+str(data['Z1'])+"','"+str(data['Z2'])+"','"+str(data['Z3'])+"','"+\
          str(data['Z4'])+"','"+str(data['Z5'])+"','"+str(data['Z6'])+"','"+str(data['Superzahl'])+\
          "','"+str(data['Super6'])+"','"+str(data['Spiel77'])+"')"
    sql_q = "SELECT * FROM mittwoch WHERE datum like '%" + data['Datum'] + "%'"
    resp = cursor.execute(sql_q)
    if resp == 0:
        cursor.execute(sql)
    connection.commit()

if wtag == 6:
    try:
        cursor.execute("""CREATE TABLE samstag ( 
            datum Text, z1 INTEGER, z2 INTEGER, z3 INTEGER, z4 INTEGER, z5 INTEGER, z6 INTEGER, sz INTEGER, super6 INTEGER, spiel77 INTEGER)""")
    except:
        None
    url_zitat = 'http://api.hubobel.de/lotto/Samstag'
    resp_zitat = requests.get(url_zitat)
    data_zitat = resp_zitat.json()
    data=data_zitat[1]
    sql = "INSERT INTO `samstag`(`datum`, `z1`, `z2`, `z3`, `z4`, `z5`, `z6`, `sz`, `super6`, `spiel77`) VALUES" \
          " ('"+str(data['Datum'])+"','"+str(data['Z1'])+"','"+str(data['Z2'])+"','"+str(data['Z3'])+\
          "','"+str(data['Z4'])+"','"+str(data['Z5'])+"','"+str(data['Z6'])+"','"+str(data['Superzahl'])+\
          "','"+str(data['Super6'])+"','"+str(data['Spiel77'])+"')"
    sql_q = "SELECT * FROM samstag WHERE datum like '%" + data['Datum'] + "%'"
    resp = cursor.execute(sql_q)
    if resp == 0:
        cursor.execute(sql)
    connection.commit()

if wtag == 5:
    try:
        cursor.execute("""CREATE TABLE euro ( 
            datum Text, z1 INTEGER, z2 INTEGER, z3 INTEGER, z4 INTEGER, z5 INTEGER, sz1 INTEGER, sz2 INTEGER )""")
    except:
        None
    url_zitat = 'http://api.hubobel.de/lotto/Euro'
    resp_zitat = requests.get(url_zitat)
    data_zitat = resp_zitat.json()
    data=data_zitat[1]
    sql = "INSERT INTO `euro`(`datum`, `z1`, `z2`, `z3`, `z4`, `z5`, `sz1`, `sz2`) VALUES" \
          " ('"+str(data['Datum'])+"','"+str(data['Z1'])+"','"+str(data['Z2'])+"','"+str(data['Z3'])+\
          "','"+str(data['Z4'])+"','"+str(data['Z5'])+"','"+str(data['Superzahl1'])+"','"+str(data['Superzahl2'])+"')"
    sql_q = "SELECT * FROM euro WHERE datum like '%" + data['Datum'] + "%'"
    resp = cursor.execute(sql_q)
    if resp == 0:
        cursor.execute(sql)

    connection.commit()

cursor.close()
connection.close()
