import bs4 as bs
import requests
import pymysql

connection = pymysql.connect(db="hubobel",
                       user="admin",
                       passwd="polier2003",
                       host='192.168.4.1',charset='utf8')
cursor = connection.cursor()
try:
    cursor.execute("""CREATE TABLE Filosofie ( 
        Nr INTEGER, Filosofie TEXT)""")
except:
    print('Error')
    None