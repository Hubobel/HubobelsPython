import pymysql

connection = pymysql.connect(db="hubobel",
                       user="hubobel",
                       passwd="polier2003",
                       host='10.0.1.59',charset='utf8')
cursor = connection.cursor()
try:
    cursor.execute("""CREATE TABLE facts ( 
        nr INTEGER, fact TEXT)""")
except:
    print ('weiter')

sql="SELECT * FROM facts ORDER BY nr DESC"
resp=cursor.execute(sql)
x=int(resp)+1
updatecount=0
with open('api/chuck.txt', 'r') as fp:
    for line in fp:
        line=line.replace('\n','')
        sql = "INSERT INTO `facts`(`nr`, `fact`) VALUES ('"+str(x)+"','"+line+"')"
        sql_q = "SELECT * FROM facts WHERE fact like '%" + line + "%'"
        resp = cursor.execute(sql_q)
        if resp == 0:
            cursor.execute(sql)
            x=x+1
            updatecount=updatecount+1
connection.commit()
cursor.close()
connection.close()
print('Es wurden '+str(updatecount)+' neue Einträge der Datenbank hinzugefügt.')