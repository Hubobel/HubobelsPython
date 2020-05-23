import pymysql
import bs4 as bs
import requests
import time

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
print(soup)
# zahlen = []
# ergebniss = []
ZahlenEuro = {'Datum': '', 'Z1': '', 'Z2': '', 'Z3': '', 'Z4': '', 'Z5': '', 'Eurozahl1': '', 'Eurozahl2': ''}
a = 1
datum = soup.find_all('li')

for i in datum:
   j = str(i)
   print(j)
   if j[:4] == '<li>':
       if j[:5] != '<li><':
           print(i)



for i in datum:
    j = str(i)
    #print(j)
    if j[:17] == '<li class="extra"':
        print(j[18:19])

print(ZahlenEuro)

sauce=(soup.find_all('div', class_ ='calendar'))
print(sauce)
#date=(soup.select_one('input[id=calendar]')['value'])
#ZahlenEuro['Datum']=date

tag=int((time.strftime("%w")))
if tag == 6:
    datum = (time.strftime("%d.%m.%Y"))
    print(datum)