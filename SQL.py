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

sql = "SELECT * FROM speed ORDER BY Nr DESC"

Anzahl = cursor.execute(sql)

Anzahl = int(Anzahl+1)
print(Anzahl)
results_dict = {'client': {'rating': '0', 'loggedin': '0', 'isprating': '3.7', 'ispdlavg': '0', 'ip': '84.63.254.177', 'isp': 'Vodafone Germany DSL', 'lon': '8.1189', 'ispulavg': '0', 'country': 'DE', 'lat': '49.7403'}, 'bytes_sent': 22970368, 'download': 28727296.703763857, 'timestamp': '2022-01-02T15:26:51.753501Z', 'share': u'http://www.speedtest.net/result/12547122848.png', 'bytes_received': 36013552, 'ping': 15.811, 'upload': 17662540.706131537, 'server': {'latency': 15.811, 'name': 'Frankfurt', 'url': 'http://speedtest.ropa.de:8080/speedtest/upload.php', 'country': 'Germany', 'lon': '8.6821', 'cc': 'DE', 'host': 'speedtest.ropa.de:8080', 'sponsor': 'ropa GmbH & Co. KG', 'lat': '50.1109', 'id': '37748', 'd': 57.65047622507195}}

up = float(results_dict['upload'])/1000000
ping = float(results_dict['ping'])
down = float(results_dict['download'])/1000000
time = str(results_dict['timestamp'])
ip = str(results_dict['client']['ip'])
server = str(results_dict['server']['url'])
down = round(down, 2)
up = round(up, 2)
ping = round(ping, 1)


val = f'"{Anzahl}", "{time}", "{server}", "{ip}", "{ping}", "{down}", "{up}"'
sql = f'INSERT INTO speed VALUE ({val})'

print(sql)
resp = cursor.execute(sql)
connection.commit()


cursor.close()
connection.close()