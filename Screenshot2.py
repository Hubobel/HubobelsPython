#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import telebot
import sys
from time import sleep

Pfad=''
#Pfad='/home/'

#todo
# Einbau User Agent
# kompletter screenshot!!!!

url=sys.argv[1]
url = url.replace ('http://','')
url = 'http://' + url

ios6ua = '--user-agent="Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Version/10.0 Mobile/14D27 Safari/602.1"'

if (len(sys.argv)) == 3:
    zoom = sys.argv[2]
else:
    zoom = '1'
options = Options()
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')
options.add_argument(ios6ua)
print(options.arguments)
driver=webdriver.Chrome(chrome_options=options)
#driver.set_window_size(1024, 768)
driver.get(url)
driver.execute_script("document.body.style.zoom='"+zoom+"'")


for isec in (4, 3, 2, 1):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight / %s);" % isec)
    sleep(1)
driver.save_screenshot(Pfad+"dashboard.png")
driver.close()



# TOKEN='680737840:AAEaa7Vxl_kZz_LWS1_S-lH6Eda7HXqu6Y4'
# ChatID='322673713'
# tb = telebot.TeleBot(TOKEN)
# document=open(Pfad+'dashboard.png','rb')
# tb.send_photo(ChatID,document)