import random
from flask import Flask, jsonify, make_response
from flask import request, send_file
import pymysql
import bs4 as bs
import requests as req
import datetime
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
import time
import json

app = Flask(__name__)


def Update():
    connection = pymysql.connect(db="hubobel",
                                 user="hubobel",
                                 passwd="polier2003",
                                 host='10.0.1.59', charset='utf8')
    cursor = connection.cursor()
    sql = "SELECT * FROM facts"
    resp = cursor.execute(sql)
    x = cursor.fetchall()
    fact = dict(x)
    cursor.close()
    connection.close()
    a = len(fact)
    return fact, a


def Lotto():
    connection = pymysql.connect(db="hubobel",
                                 user="hubobel",
                                 passwd="polier2003",
                                 host='10.0.1.59', charset='utf8')
    cursor = connection.cursor()
    sql = "SELECT * FROM mittwoch ORDER BY id DESC"
    resp = cursor.execute(sql)
    x = int(resp)
    sql_q = "SELECT * FROM mittwoch WHERE id like '" + str(x) + "'"
    cursor.execute(sql_q)
    resp = cursor.fetchall()
    resp = (resp[0][1:])
    ZahlenMittwoch = {'Datum': '', 'Z1': '', 'Z2': '', 'Z3': '', 'Z4': '', 'Z5': '', 'Z6': '', 'Superzahl': '',
                      'Spiel77': '', 'Super6': ''}
    a = 1
    while a != 7:
        ZahlenMittwoch['Z' + str(a)] = resp[a]
        a = a + 1
    ZahlenMittwoch['Datum'] = resp[0]
    ZahlenMittwoch['Superzahl'] = resp[7]
    ZahlenMittwoch['Spiel77'] = resp[9]
    ZahlenMittwoch['Super6'] = resp[8]

    cursor = connection.cursor()
    sql = "SELECT * FROM samstag ORDER BY id DESC"
    resp = cursor.execute(sql)
    x = int(resp)
    sql_q = "SELECT * FROM samstag WHERE id like '" + str(x) + "'"
    cursor.execute(sql_q)
    resp = cursor.fetchall()
    resp = resp[0][1:]
    ZahlenSamstag = {'Datum': '', 'Z1': '', 'Z2': '', 'Z3': '', 'Z4': '', 'Z5': '', 'Z6': '', 'Superzahl': '',
                     'Spiel77': '', 'Super6': ''}
    a = 1
    while a != 7:
        ZahlenSamstag['Z' + str(a)] = resp[a]
        a = a + 1
    ZahlenSamstag['Datum'] = resp[0]
    ZahlenSamstag['Superzahl'] = resp[7]
    ZahlenSamstag['Spiel77'] = resp[9]
    ZahlenSamstag['Super6'] = resp[8]

    cursor = connection.cursor()
    sql = "SELECT * FROM euro ORDER BY id DESC"
    resp = cursor.execute(sql)
    x = int(resp)
    sql_q = "SELECT * FROM euro WHERE id like '" + str(x) + "'"
    cursor.execute(sql_q)
    resp = cursor.fetchall()
    resp = resp[0][1:]
    ZahlenEuro = {'Datum': '', 'Z1': '', 'Z2': '', 'Z3': '', 'Z4': '', 'Z5': '', 'Eurozahl1': '', 'Eurozahl2': ''}
    a = 1
    while a != 6:
        ZahlenEuro['Z' + str(a)] = resp[a]
        a = a + 1
    ZahlenEuro['Datum'] = resp[0]
    ZahlenEuro['Eurozahl1'] = resp[6]
    ZahlenEuro['Eurozahl2'] = resp[7]
    connection.commit()
    cursor.close()
    connection.close()
    return ZahlenMittwoch, ZahlenEuro, ZahlenSamstag


def Lottoaktuell():
    # req.packages.urllib3.disable_warnings()
    # sauce = req.get('https://www.eurojackpot.org/gewinnzahlen/', verify=False)
    # soup = bs.BeautifulSoup(sauce.text, 'lxml')
    #
    # zahlen = []
    # ergebniss = []
    # ZahlenEuro = {'Datum': '', 'Z1': '', 'Z2': '', 'Z3': '', 'Z4': '', 'Z5': '', 'Eurozahl1': '', 'Eurozahl2': ''}
    # a = 1
    #
    # datum = soup.find_all('time')
    # tag = []
    # for i in datum:
    #     tag.append(i.text)
    # for li in soup.find_all('li'):
    #     zahlen.append(li.text)
    # for i in zahlen[0:7]:
    #     ergebniss.append(int(i))
    # ergebniss.append(tag[1])
    # while a != 6:
    #     ZahlenEuro['Z' + str(a)] = ergebniss[a - 1]
    #     a = a + 1
    #
    #
    #
    # ende = (ergebniss[7].find('- Freitag'))
    # Datum=ergebniss[7]
    # ZahlenEuro['Datum'] = Datum[:ende-1]
    # ZahlenEuro['Eurozahl1'] = ergebniss[5]
    # ZahlenEuro['Eurozahl2'] = ergebniss[6]
    req.packages.urllib3.disable_warnings()
    sauce = req.get(
        'https://www.sachsenlotto.de/portal/zahlen-quoten/gewinnzahlen/eurojackpot-gewinnzahlen/eurojackpot-gewinnzahlen.jsp',
        verify=False)
    soup = bs.BeautifulSoup(sauce.text, 'lxml')

    zahlen = []
    ergebniss = []
    ZahlenEuro = {'Datum': '', 'Z1': '', 'Z2': '', 'Z3': '', 'Z4': '', 'Z5': '', 'Eurozahl1': '', 'Eurozahl2': ''}
    a = 1
    source = soup.find_all('span',
                           class_='sl-statistic-number-circle-container-filled col-lg-1 col-md-1 col-sm-1 col-xs-1')
    for i in source:
        zahlen.append(i.text)
    while a <= 5:
        ZahlenEuro['Z' + str(a)] = int(zahlen[a - 1])
        a += 1
    ZahlenEuro['Eurozahl1'] = zahlen[5]
    ZahlenEuro['Eurozahl2'] = zahlen[6]
    print(ZahlenEuro)

    source = soup.find_all('h3', style='color: white')
    for i in source:
        datum = i.text
    start = (datum.find('Freitag,')) + 9
    ZahlenEuro['Datum'] = datum[start:]

    req.packages.urllib3.disable_warnings()
    sauce = req.get('https://www.lotto24.de/webshop/product/lottonormal/result', verify=False)
    soup = bs.BeautifulSoup(sauce.text, 'lxml')

    # print(soup.prettify())
    Lottozahlen = {'Datum': '', 'Z1': '', 'Z2': '', 'Z3': '', 'Z4': '', 'Z5': '', 'Z6': '', 'Superzahl': '',
                   'Spiel77': '', 'Super6': ''}
    daten = soup.find_all('div', class_="winning-numbers__number")
    zahlen = []
    for i in daten:
        zahlen.append(int(i.text))
    a = 1
    while a != 7:
        Lottozahlen['Z' + str(a)] = zahlen[a - 1]
        a = a + 1
    Spiel77 = ''
    Super6 = ''
    zahlen77 = []
    daten = soup.find_all('div', class_="winning-numbers__number--additional")
    for i in daten:
        zahlen77.append(int(i.text))
    spiel77 = zahlen77[0:7]
    super6 = zahlen77[-6:]
    for i in spiel77:
        Spiel77 = Spiel77 + str(i)
    for i in super6:
        Super6 = Super6 + str(i)

    daten = soup.find_all('h2', class_="strong hidden-xs")
    for i in daten:
        date = i.text
        date = date.replace('  ', '')
        date = date.replace('\n', '')

    start = (date.find('dem')) + 4
    ende = (date.find('(Alle'))

    Lottozahlen['Superzahl'] = zahlen[6]
    Lottozahlen['Spiel77'] = Spiel77
    Lottozahlen['Super6'] = Super6
    Lottozahlen['Datum'] = date[start:ende]

    return Lottozahlen, ZahlenEuro


def TV(mode):
    if mode == 0:
        mode = 'jetzt'
        range = 7
    if mode == 1:
        mode = 'abends'
        range = 7
    if mode == 2:
        mode = 'fernsehprogramm-nachts'
        range = 7
    if mode == 3:
        mode = 'jetzt'
        range = 1

    Sendungen = {}
    x = 1
    while x <= range:
        sauce = req.get('http://www.tvspielfilm.de/tv-programm/sendungen/' + mode + '.html?page=' + str(x),
                        verify=False)
        soup = bs.BeautifulSoup(sauce.text, 'lxml')

        sender_source = soup.find_all('td', class_='programm-col1')
        sendungen_source = soup.find_all('strong')

        Sender = []
        Sendung = []

        for i in sendungen_source:
            Sendung.append(i.text)
        for i in sender_source:
            text = i.text
            text = text.replace('\n', '')
            text = text.replace(' ', '')
            Sender.append(text)
        Sendung.pop(0)  # erstes Element des Listenelements 'Sendung' wird entfernt
        programm = {}
        a = 0
        b = 0

        while a < len(Sender):
            programm['Uhrzeit'] = Sendung[b]
            programm['Titel'] = Sendung[b + 1]
            Sendungen[Sender[a]] = {}
            Sendungen[Sender[a]].update(programm)
            a += 1
            b += 2
        x += 1
        liste = []
        for i in Sendungen:
            liste.append(i)
        Sendungen['Senderliste'] = liste
    return Sendungen


@app.route('/lotto', methods=['GET'])
def get_lotto():
    Mit, EUR, Sam = Lotto()
    return jsonify('Hinweis: Alle Angaben ohne Gewaehr auf Richtigkeit:', Mit, EUR, Sam)


@app.route('/lotto/Samstag', methods=['GET'])
def get_lottoSam():
    Mit, EUR, Sam = Lotto()
    return jsonify('Hinweis: Alle Angaben ohne Gewaehr auf Richtigkeit:', Sam)


@app.route('/lotto/Mittwoch', methods=['GET'])
def get_lottoMit():
    Mit, EUR, Sam = Lotto()
    return jsonify('Hinweis: Alle Angaben ohne Gewaehr auf Richtigkeit:', Mit)


@app.route('/lotto/Euro', methods=['GET'])
def get_lottoEur():
    Mit, EUR, Sam = Lotto()
    return jsonify('Hinweis: Alle Angaben ohne Gewaehr auf Richtigkeit:', EUR)


@app.route('/lotto/aktuell', methods=['GET'])
def get_lottoAktuell():
    Lottozahlen, ZahlenEuro = Lottoaktuell()

    return jsonify(Lottozahlen, ZahlenEuro)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Nicht unterstuetzt'}), 404)


@app.route('/')
def index():
    fact, a = Update()

    return """
<!DOCTYPE html>
<head>
   <title>Hubobel.de RESTful-API</title>
   <link rel="stylesheet" href="http://stash.compjour.org/assets/css/foundation.css">
</head>
<body style="width: 880px; margin: auto;">  
    <h1>Willkommen bei der RESTful-API von hubobel.de</h1>
    <p>folgende Aufrufe sind derzeit realisisert:</p>
    <p>GET: api.hubobel.de/facts.....: Uebersicht ueber alle verfuegbaren Facts mit ihrer ID</p>
    <p>GET: api.hubobel.de/facts/'ID'.....: JSON des abgefragten Facts</p>
    <p>GET: api.hubobel.de/facts/zufall.....: ein zufaellig ausgewaehlter Fact wird im JSON zurueck gegeben</p>
    <p>GET: api.hubobel.de/lotto....: Liefert die letzten Zahlen von Mittwochs-, Euro- und Samstagslotto 
    (aus der Datenbank)</p>
    <p>GET: api.hubobel.de/lotto/Mittwoch.....: Liefert die letzten Mottwochszahlen (aus der Datenbank)</p>
    <p>GET: api.hubobel.de/lotto/Euro.....: Liefert die letzten Eurojackpotzahlen (aus der Datenbank)</p>
    <p>GET: api.hubobel.de/lotto/Samstag.....: Liefert die letzten Samstagszahlen (aus der Datenbank)</p>
    <p>GET: api.hubobel.de/lotto/aktuell.....: Liefert die letzten Lottozahlen des Euro- und Mittwoch 
    bzw.Samstagslotto (online jeweils neu ermittelt)</p>
    <p>GET: api.hubobel.de/bitcoin.....: Liefert die aktuellen Bitcoinkurse in EURO</p>
    <p>GET: api.hubobel.de/wetter.....: Liefert das aktuelle Wetter in Oggersheim</p>
    <p>GET: api.hubobel.de/sprit/'km'.....: Liefert die aktuellen Kraftstoffpreise im Umreis von 'km' Radius um 67071</p>
    <p>GET: api.hubobel.de/sprit/'Ort'.....: Liefert die aktuellen Kraftstoffpreise im 10km Radius 
    um den übergebenen Ort</p>
    <p>GET: api.hubobel.de/tv.....: Liefert das aktuelle TV Programm der Hauptsender</p>
    <p>GET: api.hubobel.de/tv/jetzt.....: Liefert das aktuelle TV Programm aller Sender</p>
    <p>GET: api.hubobel.de/tv/2015.....: Liefert das aktuelle TV Programm aller Sender um 20.15Uhr</p>
    <p>GET: api.hubobel.de/tv/2200.....: Liefert das aktuelle TV Programm aller Sender um 22.00Uhr</p>
    <p>GET: api.hubobel.de/filosophie.....: Liefert Filosophie des SWR3 zurück</p>
    <p>GET: api.hubobel.de/shoot/'www.example.de'.....: Liefert Screenshot von example.de zurück</p>
    <p>POST: api.hubobel.de/tv/check.....: Uebergabe von beliebigen Sendern als Liste - liefert Programm zurueck</p>
    <p>POST: api.hubobel.de/lotto/6aus49/check.....: Uebergabe der 6+1 Zahlen als Liste - liefert Anzahl
     der Treffer zurueck</p>
    <p>POST: api.hubobel.de/lotto/6aus49/check.....: Uebergabe der 5+2 Zahlen als Liste - liefert Anzahl 
    der Treffer zurueck</p>
    <p>...to be continued</p>

</body>
"""


@app.route('/facts', methods=['GET'])
def get_tasks():
    fact, a = Update()
    return json.dumps(fact, ensure_ascii=False, sort_keys=True, indent=4)


@app.route('/facts/<int:task_id>', methods=['GET'])
def get_task(task_id):
    connection = pymysql.connect(db="hubobel",
                                 user="hubobel",
                                 passwd="polier2003",
                                 host='10.0.1.59', charset='utf8')
    cursor = connection.cursor()
    sql = "SELECT * FROM facts ORDER BY nr DESC"
    resp = cursor.execute(sql)
    x = int(resp)
    if x < task_id:
        return jsonify({'error': "Auch Chuck Norris FACTS sind begrenzt"})
    sql_q = "SELECT * FROM facts WHERE nr like '" + str(task_id) + "'"
    cursor.execute(sql_q)
    resp = cursor.fetchall()
    resp = (resp[0][1])
    cursor.close()
    connection.close()
    return json.dumps(resp, ensure_ascii=False, sort_keys=True, indent=4)


@app.route('/facts/zufall', methods=['GET'])
def zufall():
    connection = pymysql.connect(db="hubobel",
                                 user="hubobel",
                                 passwd="polier2003",
                                 host='10.0.1.59', charset='utf8')
    cursor = connection.cursor()
    sql = "SELECT * FROM facts ORDER BY nr DESC"
    resp = cursor.execute(sql)
    x = int(resp)
    ran = random.randint(1, x)
    print(x, ran)
    sql_q = "SELECT * FROM facts WHERE nr like '" + str(ran) + "'"
    resp = cursor.execute(sql_q)
    resp = cursor.fetchall()
    resp = (resp[0][1])
    cursor.close()
    connection.close()
    return jsonify({ran: resp})


@app.route('/lotto/6aus49/check', methods=['POST'])
def checkMittwoch():
    if len(request.json) != 7:
        return make_response(jsonify({'error': 'Sie müssen 6+1 Zahl als Liste übergeben'}), 404)
    Treffer = 0
    Ziffern = []
    eingabe = request.json
    Lottozahlen_aktuell, ZahlenEuro_aktuell = Lottoaktuell()

    Lottozahlen = []
    Lottofee = []
    a = 1
    while a != 7:
        Lottozahlen.append(Lottozahlen_aktuell['Z' + str(a)])
        Lottofee.append(Lottozahlen_aktuell['Z' + str(a)])
        a += 1

    for i in eingabe[:6]:
        if i in Lottozahlen:
            Treffer += 1
            Ziffern.append(i)
            Lottozahlen.remove(i)
    if eingabe[6] == Lottozahlen_aktuell['Superzahl']:
        Superzahl = True
    else:
        Superzahl = False

    return jsonify({'Treffer': Treffer, 'Superzahl': Superzahl, 'richtige Ziffern': Ziffern,
                    'aktuelle Ziehung': Lottofee[:6], 'aktuelle Superzahl': Lottozahlen_aktuell['Superzahl'],
                    'Ziehung vom': Lottozahlen_aktuell['Datum']})


@app.route('/lotto/Euro/check', methods=['POST'])
def checkEuro():
    if len(request.json) != 7:
        return make_response(jsonify({'error': 'Sie müssen 5+2 Zahlen als Liste übergeben'}), 404)
    Treffer = 0
    Ziffern = []
    eingabe = request.json
    Lottozahlen_aktuell, ZahlenEuro_aktuell = Lottoaktuell()

    Lottozahlen = []
    Lottofee = []
    a = 1
    while a != 6:
        Lottozahlen.append(ZahlenEuro_aktuell['Z' + str(a)])
        Lottofee.append(ZahlenEuro_aktuell['Z' + str(a)])
        a += 1
    for i in eingabe[:6]:
        if i in Lottozahlen:
            Treffer += 1
            Ziffern.append(i)
            Lottozahlen.remove(i)
    if eingabe[5] == ZahlenEuro_aktuell['Eurozahl1']:
        Eurozahl1 = True
    else:
        Eurozahl1 = False
    if eingabe[6] == ZahlenEuro_aktuell['Eurozahl2']:
        Eurozahl2 = True
    else:
        Eurozahl2 = False

    return jsonify({'Treffer': Treffer, 'Eurozahl1': Eurozahl1, 'Eurozahl2': Eurozahl2, 'richtige Ziffern': Ziffern,
                    'aktuelle Ziehung': Lottofee[:5], 'aktuelle Eurozahl1': ZahlenEuro_aktuell['Eurozahl1'],
                    'aktuelle Eurozahl2': ZahlenEuro_aktuell['Eurozahl2'], 'Ziehung vom': ZahlenEuro_aktuell['Datum']})


@app.route('/kodi', methods=['GET'])
def kodi():
    connection = pymysql.connect(db="MyVideos107",
                                 user="hubobel",
                                 passwd="polier2003",
                                 host='10.0.1.59', charset='utf8')
    cursor = connection.cursor()
    sql = "SELECT * FROM movie_view ORDER BY playCount DESC"
    resp = cursor.execute(sql)
    x = cursor.fetchall()
    a = 1
    antwort = {}
    for i in x:
        antwort[a] = i[2]
        a = a + 1
    return jsonify(antwort)


@app.route('/bitcoin', methods=['GET'])
def bitcoin():
    url_zitat = 'https://blockchain.info/de/ticker'
    resp_zitat = req.get(url_zitat)
    data_zitat = resp_zitat.json()
    return jsonify(data_zitat['EUR'])


@app.route('/wetter', methods=['GET'])
def wetter():
    url = 'http://api.wunderground.com/api/35a8e37c649985d5/conditions/lang:DL/q/Germany/pws:ILUDWIGS227.json'
    response = req.get(url)
    data_response = response.json()
    temperatur = (data_response['current_observation']['temp_c'])
    wetter = (data_response['current_observation']['weather'])
    feuchte = (data_response['current_observation']['relative_humidity'])
    return jsonify({'Temperatur': temperatur, 'Wetter': wetter, 'Feuchte': feuchte})


@app.route('/sprit/<int:task_id>', methods=['GET'])
def sprit(task_id):
    url = 'https://creativecommons.tankerkoenig.de/json/list.php?lat=49.492995&lng=8.358411&' \
          'rad=' + str(task_id) + '&sort=dist&type=all&apikey=e5574b6b-9470-b1dd-7745-187750cf439a'
    resp = req.get(url)
    data = resp.json()
    station = {}
    daten = {}
    for i in data['stations']:
        daten['Ort'] = i['place']
        daten['Adresse'] = i['street']
        daten['preis_diesel'] = i['diesel']
        daten['preis_e5'] = i['e5']
        daten['preis_e10'] = i['e10']
        station[i['name']] = {}
        station[i['name']].update(daten)
    return jsonify(station)


@app.route('/sprit/<string:task_id>', methods=['GET'])
def test(task_id):
    url = 'https://maps.googleapis.com/maps/api/geocode/json'
    params = {'sensor': 'false', 'address': task_id, 'key': 'AIzaSyDdT2hs83_FklFfJDulHf62V7HKWDu0VtU'}
    r = req.get(url, params=params)
    results = r.json()['results']
    location = results[0]['geometry']['location']
    lat = location['lat']
    lng = location['lng']
    url = 'https://creativecommons.tankerkoenig.de/json/list.php?lat=' + str(lat) + '&lng=' + str(lng) + \
          '&rad=10&sort=dist&type=all&apikey=e5574b6b-9470-b1dd-7745-187750cf439a'
    print(url)
    resp = req.get(url)
    data = resp.json()
    station = {}
    daten = {}
    for i in data['stations']:
        daten['Ort'] = i['place']
        daten['Adresse'] = i['street']
        daten['preis_diesel'] = i['diesel']
        daten['preis_e5'] = i['e5']
        daten['preis_e10'] = i['e10']
        station[i['name']] = {}
        station[i['name']].update(daten)
    return jsonify(station)


@app.route('/tv/jetzt', methods=['GET'])
def tv_now():
    Sendungen = TV(0)
    return jsonify(Sendungen)


@app.route('/tv/2015', methods=['GET'])
def tv_abends():
    Sendungen = TV(1)
    return jsonify(Sendungen)


@app.route('/tv/2200', methods=['GET'])
def tv_nachts():
    Sendungen = TV(2)
    return jsonify(Sendungen)


@app.route('/tv', methods=['GET'])
def tv():
    Sendungen = TV(3)
    return jsonify(Sendungen)


@app.route('/tv/check', methods=['POST'])
def tv_check():
    auswahl = request.json
    Sendungen = TV(0)
    rück = {}
    for i in auswahl:
        if i in Sendungen.keys():
            rück[i] = {}
            rück[i].update(Sendungen[i])
    return jsonify(rück)


@app.route('/beta', methods=['GET'])
def beta():
    req.packages.urllib3.disable_warnings()
    sauce = req.get(
        'https://www.sachsenlotto.de/portal/zahlen-quoten/gewinnzahlen/eurojackpot-gewinnzahlen/eurojackpot-gewinnzahlen.jsp',
        verify=False)
    soup = bs.BeautifulSoup(sauce.text, 'lxml')

    zahlen = []
    ergebniss = []
    ZahlenEuro = {'Datum': '', 'Z1': '', 'Z2': '', 'Z3': '', 'Z4': '', 'Z5': '', 'Eurozahl1': '', 'Eurozahl2': ''}
    a = 1
    source = soup.find_all('span',
                           class_='sl-statistic-number-circle-container-filled col-lg-1 col-md-1 col-sm-1 col-xs-1')
    for i in source:
        zahlen.append(i.text)
    while a <= 5:
        ZahlenEuro['Z' + str(a)] = int(zahlen[a - 1])
        a += 1
    ZahlenEuro['Eurozahl1'] = zahlen[5]
    ZahlenEuro['Eurozahl2'] = zahlen[6]
    print(ZahlenEuro)

    source = soup.find_all('h3', style='color: white')
    for i in source:
        datum = i.text
    return jsonify(ZahlenEuro, datum)


@app.route('/ferien/<string:task_id>', methods=['GET'])
def ferien(task_id):
    url = 'http://api.smartnoob.de/ferien/v1/ferien/?bundesland=' + task_id
    resp = req.get(url)
    data = resp.json()

    ferien = False

    jetzt = 356

    for i in data['daten']:
        beginn = int(datetime.datetime.fromtimestamp(i['beginn']).strftime('%j'))
        ende = int(datetime.datetime.fromtimestamp(i['ende']).strftime('%j')) - 1
        if jetzt <= ende and jetzt >= beginn:
            ferien = True
        if jetzt >= beginn and ende > beginn:
            ferien = True
        if jetzt <= ende:
            ferien = True
        if jetzt > ende and jetzt < beginn:
            ferien = False
    return jsonify(ferien)


@app.route('/filosophie', methods=['GET'])
def filosphie():
    connection = pymysql.connect(db="hubobel",
                                 user="hubobel",
                                 passwd="polier2003",
                                 host='10.0.1.59', charset='utf8')
    cursor = connection.cursor()
    sql = "SELECT * FROM Filosofie"
    resp = cursor.execute(sql)
    x = cursor.fetchall()
    fact = dict(x)
    cursor.close()
    connection.close()

    return json.dumps(fact, ensure_ascii=False, sort_keys=True, indent=4)


@app.route('/energy', methods=['GET'])
def energy():
    Pfad = ''
    Pfad = '/home/'

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(chrome_options=options)
    driver.set_window_size(1024, 768)
    driver.get("http://10.0.1.59:1880/ui/#/1")

    for isec in (4, 3, 2, 1):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight / %s);" % isec)
        sleep(1)
    driver.save_screenshot(Pfad + "dashboard.png")

    return send_file(Pfad + 'dashboard.png')


@app.route('/shoot/<string:task_id>', methods=['GET'])
def shoot(task_id):
    url = 'http://' + task_id
    Pfad = '/home/'
    # Pfad=''
    # run first time to get scrollHeight
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--hide-scrollbars")
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(2560, 1600)
    driver.get(url)
    # pause 3 second to let page load
    time.sleep(3)

    driver.save_screenshot(Pfad + task_id + '.png')
    driver.close()
    return send_file(Pfad + task_id + '.png')


if __name__ == '__main__':
    app.run(host='0.0.0.0')


