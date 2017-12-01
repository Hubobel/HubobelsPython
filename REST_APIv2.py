import random
from flask import Flask, jsonify,make_response
import pymysql
import bs4 as bs
import urllib.request

app = Flask(__name__)

def Lotto():
    sauce = urllib.request.urlopen('http://www.lottotip-check.de').read()
    soup = bs.BeautifulSoup(sauce, 'html.parser')

    # print(soup.prettify())
    table = soup.find_all('table')
    row = []
    ZahlenAll = []
    ZahlenMittwoch = {'Datum': '', 'Z1': '', 'Z2': '', 'Z3': '', 'Z4': '', 'Z5': '', 'Z6': '', 'Superzahl': '',
                      'Spiel77': '', 'Super6': ''}
    ZahlenSamstag = {'Datum': '', 'Z1': '', 'Z2': '', 'Z3': '', 'Z4': '', 'Z5': '', 'Z6': '', 'Superzahl': '',
                     'Spiel77': '', 'Super6': ''}
    ZahlenEuro = {'Datum': '', 'Z1': '', 'Z2': '', 'Z3': '', 'Z4': '', 'Z5': '', 'Superzahl1': '', 'Superzahl2': ''}
    for i in table:
        table_rows = i.find_all('tr')
        for tr in table_rows:
            # print(tr)
            td = tr.find_all('td')
            if td != []:
                row = [i.text for i in td]
                # print(row)
                th = tr.find_all('th')
                sz = [i.text for i in th]
                # print(len(sz))
                if len(sz) == 5:
                    row.append(str(sz[2]))
                    row.append(str(sz[3]))
                date = 'Ziehung vom: ' + str(sz[0])
                sz = str(sz[1])
                row.append(sz)
                row.insert(0, date)
        ZahlenAll.extend(row)
    a = 0
    while a <= 5:
        a = a + 1
        ZahlenMittwoch['Z' + str(a)] = int(ZahlenAll[a])
    ZahlenMittwoch['Datum'] = ZahlenAll[0]
    ZahlenMittwoch['Superzahl'] = int(ZahlenAll[9])
    ZahlenMittwoch['Super6'] = int(ZahlenAll[8])
    ZahlenMittwoch['Spiel77'] = int(ZahlenAll[7])
    print(ZahlenMittwoch)
    a = 0
    while a <= 5:
        a = a + 1
        ZahlenSamstag['Z' + str(a)] = int(ZahlenAll[a + 18])
    ZahlenSamstag['Datum'] = ZahlenAll[18]
    ZahlenSamstag['Superzahl'] = int(ZahlenAll[27])
    ZahlenSamstag['Super6'] = int(ZahlenAll[26])
    ZahlenSamstag['Spiel77'] = int(ZahlenAll[25])
    print(ZahlenSamstag)

    a = 0
    while a <= 4:
        a = a + 1
        ZahlenEuro['Z' + str(a)] = int(ZahlenAll[a + 10])
    ZahlenEuro['Datum'] = ZahlenAll[10]
    ZahlenEuro['Superzahl2'] = int(ZahlenAll[17])
    ZahlenEuro['Superzahl1'] = int(ZahlenAll[16])
    print(ZahlenEuro)
    return ZahlenMittwoch,ZahlenEuro,ZahlenSamstag

@app.route('/lotto', methods=['GET'])
def get_lotto():
    Mit,EUR,Sam=Lotto()
    return jsonify('alle Angaben ohne Gewaehr:',Mit,EUR,Sam)

@app.route('/lotto/Samstag', methods=['GET'])
def get_lottoSam():
    Mit,EUR,Sam=Lotto()
    return jsonify('alle Angaben ohne Gewaehr:',Sam)

@app.route('/lotto/Mittwoch', methods=['GET'])
def get_lottoMit():
    Mit,EUR,Sam=Lotto()
    return jsonify('alle Angaben ohne Gewaehr:',Mit)

@app.route('/lotto/Euro', methods=['GET'])
def get_lottoEur():
    Mit,EUR,Sam=Lotto()
    return jsonify('alle Angaben ohne Gewaehr:',EUR)

def Update():
    connection = pymysql.connect(db="hubobel",
                           user="hubobel",
                           passwd="polier2003",
                           host='10.0.1.59',charset='utf8')
    cursor = connection.cursor()
    sql="SELECT * FROM facts"
    resp=cursor.execute(sql)
    x=cursor.fetchall()
    fact=dict(x)
    cursor.close()
    connection.close()
    a=len(fact)
    return fact,a
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Nicht unterstuetzt'}), 404)
@app.route('/')
def index():
    fact,a = Update()
    fact={
          'GET:api.hubobel.de/facts.....':'Uebersicht ueber alle verfuegbaren Facts mit ihrer ID',
          'GET: api.hubobel.de/facts/<ID>.....':'JSON des abgefragten Facts',
          'GET: api.hubobel.de/facts/zufall.....':'ein zufaellig ausgewaehlter Fact wird im JSON zurueck gegeben',
          'facts':a,
          'GET: api.hubobel.de/lotto....':'Liefert die letzten Zahlen von Mittwochs-, Euro- und Samstagslotto',
          'GET: api.hubobel.de/lotto/Mittwoch.....':'Liefert die letzten Mottwochszahlen',
          'GET: api.hubobel.de/lotto/Euro.....':'Liefert die letzten Eurojackpotzahlen',
          'GET: api.hubobel.de/lotto/Samstag.....':'Liefert die letzten Samstagszahlen'}
    return jsonify({'eine REST-API von hubobel.de Methoden/Funktionen':fact})
@app.route('/facts', methods=['GET'])
def get_tasks():
    fact, a = Update()
    return jsonify({'facts': fact})
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
    if x<task_id:
        return jsonify({'error':"Auch Chuck Norris FACTS sind begrenzt"})
    sql_q = "SELECT * FROM facts WHERE nr like '" + str(task_id) + "'"
    cursor.execute(sql_q)
    resp = cursor.fetchall()
    resp = (resp[0][1])
    cursor.close()
    connection.close()
    return jsonify({'fact': resp})
@app.route('/zufall', methods=['GET'])
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
if __name__ == '__main__':
    app.run(host='0.0.0.0')