import base64
pool = {'cm90': 'MjAuMDAwMQ==', 'c2Nod2Fyeg==': 'MzAuMTIzNA==', 'Z29sZA==': 'NDAuMTIzNA=='}
while True:
    antwort = input('Farbe:').lower()
    code = (base64.b64encode(str.encode(antwort))).decode('utf-8')
    if code in pool:
        print(base64.b64decode((pool[code])).decode('utf-8'))
    elif antwort[0] == '#':
        print(base64.b64encode(str.encode(antwort[1:])).decode('utf-8'))
    elif antwort == 'exit':
        break
    else:
        print('Diese Farbe gibt es nicht')