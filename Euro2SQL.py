import bs4 as bs
import requests

requests.packages.urllib3.disable_warnings()
sauce = requests.get('https://www.lotto24.de/webshop/product/eurojackpot/result', verify=False)
soup = bs.BeautifulSoup(sauce.text, 'lxml')

ZahlenEuro = {'Datum': '', 'Z1': '', 'Z2': '', 'Z3': '', 'Z4': '', 'Z5': '', 'Eurozahl1': '', 'Eurozahl2': ''}
a = 1
daten = soup.find_all('div', class_="winning-numbers__number")
for i in daten:
    print(i.text)
    if a <= 5:
        ZahlenEuro['Z' + str(a)] = int(i.text)
    elif a == 6:
        ZahlenEuro['Eurozahl1'] = int(i.text)
    elif a == 7:
        ZahlenEuro['Eurozahl2'] = int(i.text)
    a  = a + 1

daten = soup.find_all('h2', class_="strong hidden-xs")
for i in daten:
    date = i.text
    date = date.replace('  ', '')
    date = date.replace('\n', '')

start = (date.find('dem')) + 4
ende = (date.find('(Alle'))
ZahlenEuro['Datum'] = date[start:ende]
print(ZahlenEuro)


