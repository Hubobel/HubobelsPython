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
telegramm='Mainz - Alzey\n'
for i in data_zitat['departures']:
    #print(i)
    if i['train'] == "RE 13":
        if i['delayDeparture'] != None:
            #print(i)
            antwort=(i['train']+' '+i['platform'] +' '+ str(i['scheduledDeparture']))
            if i['delayDeparture'] != 0:
                antwort = antwort + (' Verspätung: ' + str(i['delayDeparture']))
            else:
                antwort = antwort +' PÜNKTLICH'
            telegramm = telegramm + antwort + '\n'
    if i['train'] == "RB 31":
        if i['delayDeparture'] != None:
            #print(i)
            antwort=(i['train']+' '+i['platform'] +' '+ str(i['scheduledDeparture']))
            if i['delayDeparture'] != 0:
                antwort = antwort + (' Verspätung: ' + str(i['delayDeparture']))
            else:
                antwort = antwort +' PÜNKTLICH'
            telegramm = telegramm+antwort+'\n'
#print(telegramm)

tb.send_message(ChatID,telegramm)