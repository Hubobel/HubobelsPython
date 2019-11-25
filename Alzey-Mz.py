import requests
import telebot

TOKEN='680737840:AAEaa7Vxl_kZz_LWS1_S-lH6Eda7HXqu6Y4'
ChatID='322673713'
tb = telebot.TeleBot(TOKEN)

url_zitat = 'https://dbf.finalrewind.org/alzeyhbf.json?version=3'
resp_zitat = requests.get(url_zitat)
data_zitat = resp_zitat.json()


antwort=''
telegramm='Mainz - Alzey\n'
for i in data_zitat['departures']:
    if i['train'] == 'RB 31':

        print(i)


print(telegramm)

#tb.send_message(ChatID,telegramm)