import requests

url = 'http://10.0.1.122:8087/getPlainValue/javascript.0.Variablen.Benutzer'

resp = requests.get(url)
print(resp.text)

