import requests
import telebot

TOKEN='680737840:AAEaa7Vxl_kZz_LWS1_S-lH6Eda7HXqu6Y4'
ChatID='322673713'
tb = telebot.TeleBot(TOKEN)

url_zitat = 'https://dbf.finalrewind.org/mainzhbf.json?version=3'
resp_zitat = requests.get(url_zitat)
data_zitat = resp_zitat.json()
#print (data_zitat)

antwort=''
telegramm='Mainz - Wiesbaden\n'
for i in data_zitat['departures']:
    print(i)
