import requests

url_WZ = 'http://10.0.1.241/cgi-bin/api.cgi?cmd=Login'
payload = '[{"cmd": "Login", "action": 0, "param": {"User": {"userName": "admin", "password": "polier2003"}}}]'
r = requests.post(url=url_WZ, data=payload)
data = r.json()
token = str((data[0]['value']['Token']['name']))
url = 'http://10.0.1.241/cgi-bin/api.cgi?cmd=SetIsp&token=' + token
payload = '[{"cmd":"SetIsp","action":0,"param":{"Isp":{"channel":0,"antiFlicker":"50HZ","exposure":"Auto","gain":{"min":1,"max":62},"shutter":{"min":0,"max":125},"blueGain":128,"redGain":128,"whiteBalance":"Auto","dayNight":"Color","backLight":"DynamicRangeControl","blc":128,"drc":128,"rotation":0,"mirroring":0,"nr3d":1}}}]'
r = requests.post(url=url, data=payload)
