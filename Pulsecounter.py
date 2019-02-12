import requests

url = 'http://10.0.1.103/?json:'
response = requests.get(url)
data_response = response.json()
a=[1,2,3,4,5,6]
for i in a:
       print(data_response['vars'][i]['value'], data_response['vars'][i]['unit'])

