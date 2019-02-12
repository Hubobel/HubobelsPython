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

sql = "SELECT * FROM facts ORDER BY nr DESC"
resp = cursor.execute(sql)

print(resp)