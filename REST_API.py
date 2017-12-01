import os
import random
from flask import Flask, jsonify
import bs4 as bs
import urllib.request

app = Flask(__name__)
fact=[]
pfad = os.path.dirname(__file__)
chuck_file= open(pfad + '/mpg/chuck.rtf','r')
for line in chuck_file:
    fact.append(line)
chuck_file.close()
ran=random.randint(1,len(fact)-1)
fakt={}
a=0
for i in fact:
    fakt[a]=i
    a  =a +1

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/facts', methods=['GET'])
def get_tasks():
    return jsonify({'facts': fakt})

@app.route('/lotto', methods=['GET'])
def get_lotto():
    sauce = urllib.request.urlopen('http://www.lottotip-check.de').read()
    soup = bs.BeautifulSoup(sauce, 'html.parser')
    table = soup.find_all('table')
    row = []
    test = []
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
                # print(sz)
                date = 'Ziehung vom: ' + str(sz[0])
                sz = 'Superzahl: ' + str(sz[1])
                row.append(sz)
                row.insert(0, date)
        test.extend(row)

    test[14] = 'Superzahl: ' + test[14]
    test = test[0:24]
    Mit = {test[0]: test[1:8]}
    EUR = {test[8]: test[9:16]}
    Sam = {test[16]: test[17:24]}
    return jsonify(test)

@app.route('/facts/<int:task_id>', methods=['GET'])
def get_task(task_id):
    if len(fact)-1<task_id:
        return jsonify({'error':"Auch Chuck Norris Witze sind begrenzt"})
    return jsonify({'fact': fact[task_id]})
if __name__ == '__main__':
    app.run(host='0.0.0.0')