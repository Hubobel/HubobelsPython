from unifi.controller import Controller
c = Controller('10.0.1.59', 'hubobel', 'polier2003','8443', 'v3')
for ap in c.get_aps():
	print (ap.get('name'), ap['mac'])

