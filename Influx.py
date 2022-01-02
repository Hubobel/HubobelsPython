from influxdb import InfluxDBClient

client = InfluxDBClient(host='10.0.1.59', port=8086, username='admin', password='polier2003')

    #databases = client.get_list_database()

client.switch_database('iobroker')

    # measurements = client.get_list_measurements()
    # antwort = client.query('SELECT * FROM "javascript.0.Variablen.Tagesverbrauch" WHERE time > now() -24h')
    # antwort = client.query('SELECT * FROM "javascript.0.Variablen.Tagesverbrauch" WHERE time > '+"'2020-07-16T19:16:30.665000Z' and time < '2020-07-16T19:20:30.572000Z'")
    # antwort = client.query('SELECT * FROM "javascript.0.Variablen.Tagesverbrauch" WHERE time = '+"'2020-07-16T19:16:30.665000Z'")

antwort = client.query('SELECT * FROM "javascript.0.Variablen.Tagesverbrauch" WHERE time > now() -1440m and time < now() -1439m')
cpu_points = list(antwort.get_points())
print(antwort)
print(cpu_points)
print(cpu_points[0]['time'])
print(cpu_points[0]['value'])
client.close()

