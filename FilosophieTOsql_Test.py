import requests as req
import bs4 as bs

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
#print(soup)
source = soup.find_all('li')
print(source)
for i in source:
    datum = i.text
    print(i)

