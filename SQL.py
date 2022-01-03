import pymysql

connection = pymysql.connect(db="hubobel",
                       user="hubobel",
                       passwd="polier2003",
                       host='10.0.1.123',charset='utf8')
cursor = connection.cursor()
try:
    cursor.execute("""CREATE TABLE speed ( 
        nr INT, timestamp TEXT,server TEXT,ip TEXT, ping FLOAT, download FLOAT, upload FLOAT)""")
except:
    print ('weiter')

sql = "SELECT * FROM speed"

Anzahl = cursor.execute(sql)
resp = cursor.fetchall()
a = (len(resp)) - 7
resp = resp[a:]
for i in resp:
    print(i[5])


cursor.close()
connection.close()