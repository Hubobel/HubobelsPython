import pymysql
import bs4 as bs
import requests

connection = pymysql.connect(db="hubobel",
                       user="hubobel",
                       passwd="polier2003",
                       host='10.0.1.59',charset='utf8')
cursor = connection.cursor()

#todo eurojackpot wieder fixen

requests.packages.urllib3.disable_warnings()
sauce = requests.get('https://www.eurojackpot.org/gewinnzahlen/', verify=False)
soup = bs.BeautifulSoup(sauce.text, 'lxml')
#print(soup)
#print(soup)
# zahlen = []
# ergebniss = []
ZahlenEuro = {'Datum': '', 'Z1': '', 'Z2': '', 'Z3': '', 'Z4': '', 'Z5': '', 'Eurozahl1': '', 'Eurozahl2': ''}
a = 1
datum = soup.find_all('li')
for i in datum:
    i=str(i)
    i = i.replace('<li>' , '').replace('</li>' , '').replace('<li class="extra">' , '')
    if a <= 7:
        if a<6:
            ZahlenEuro['Z'+str(a)]=i
        if a ==6:
            ZahlenEuro['Eurozahl1']=i
        if a ==7:
            ZahlenEuro['Eurozahl2']=i
        a +=1

#print(soup)
sauce=(soup.find_all('div', class_ ='calendar'))
date=(soup.select_one('input[id=calendar]')['value'])
ZahlenEuro['Datum']=date
print(ZahlenEuro)