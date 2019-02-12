#Filmdatenbank abfragen
import pymysql
connection = pymysql.connect(db="MyVideos107",
                                 user="hubobel",
                                 passwd="polier2003",
                                 host='10.0.1.59', charset='utf8')
cursor = connection.cursor()
sql = "SELECT * FROM tvshow_view ORDER BY c00 DESC"
resp = cursor.execute(sql)
x = cursor.fetchall()
a=1
antwort={}
for i in x:
    print(i[1]+str(i[33]))
    antwort[a] = i[1]
    a = a + 1
print (antwort)