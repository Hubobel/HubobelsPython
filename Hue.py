from qhue import Bridge
import requests
import paho.mqtt.client as mqtt
import time


client = mqtt.Client()
client.username_pw_set(username="hubobel",password="polier2003")


while True:
    b = Bridge("10.0.1.19", "GxPN8lQmEvY5LXwtGRfKM5vwXegY9Yv10N0j2kxr")
    url=b.url
    response = requests.get(url)
    data_response = response.json()
    #print('Elemente in Bridge angemeldet: ',len(data_response))

    for i in data_response['sensors']:
        try:
            if data_response['sensors'][i]['productname'] == 'Hue dimmer switch':
                print(data_response['sensors'][i])

                states={'1002':'On', '2002':'Dim up', '3002':'Dim down', '4002':'Off', '1000':True, '4000':False}

                for a in states:
                    if str(a) == str(data_response['sensors'][i]['state']['buttonevent']):
                        #print(data_response['sensors'][i]['name'], ' buttonstate: ',states[a])
                        pfad="Test/"+data_response['sensors'][i]['name']
                        pfad=pfad.replace(' ','_')
                        #print(pfad)
                        try:
                            client.connect("10.0.1.59", 1884, 60)
                            client.publish(pfad, states[a])
                            print('puplished',states[a])
                            client.disconnect()
                        except:
                            print('error')
                        time.sleep(1)
        except:
            None
    time.sleep(5)
#client.disconnect()
