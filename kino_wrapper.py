import bs4 as bs
import requests
import time

requests.packages.urllib3.disable_warnings()
sauce=requests.get('https://www.eurojackpot.org/gewinnzahlen/',verify=False)
soup = bs.BeautifulSoup(sauce.text,'lxml')
