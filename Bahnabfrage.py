#dsfsf

import requests
import telebot
import datetime
import json
from datetime import datetime as DateTime

hour = datetime.datetime.now().hour
TOKEN='680737840:AAEaa7Vxl_kZz_LWS1_S-lH6Eda7HXqu6Y4'
ChatID='322673713'
tb = telebot.TeleBot(TOKEN)
ort = '/home/carsten/Scripts/'
ort = ''
Zeitstempel = DateTime.now().strftime('%Y_%m_%d_%H_%M_%S')
antwort=''

def mzwi():
    url_zitat = 'https://dbf.finalrewind.org/mainzhbf.json?version=3'
    resp_zitat = requests.get(url_zitat)
    data_zitat = resp_zitat.json()
    telegramm = 'Mainz - Wiesbaden\n'
    with open(ort + str(Zeitstempel) + '_data.txt', 'w') as outfile:
        json.dump(data_zitat, outfile)
    for i in data_zitat['departures']:
        if i['train'] == "S 8":
            if i['destination'] == 'Wiesbaden Hbf':
                antwort = (i['train'] + ' ' + i['platform'] + ' ' + str(i['scheduledDeparture']))
                if i['isCancelled'] != 1:
                    if i['delayDeparture'] != 0:
                        antwort = antwort + (' Verspätung: ' + str(i['delayDeparture']) + ' Minuten')
                    else:
                        antwort = antwort + ' PÜNKTLICH'
                else:
                    antwort = antwort + 'CANCELLED!!!'
                telegramm = telegramm + antwort + '\n'
        if i['train'] == "RB 75":
            if i['isCancelled'] != 1:
                if i['delayDeparture'] != 0:
                    antwort = antwort + (' Verspätung: ' + str(i['delayDeparture']) + ' Minuten')
                else:
                    antwort = antwort + ' PÜNKTLICH'
            else:
                antwort = antwort + 'CANCELLED!!!'
            telegramm = telegramm + antwort + '\n'
    return telegramm

def wimz():
    url_zitat = 'https://dbf.finalrewind.org/Wiesbadenhbf.json?version=3'
    resp_zitat = requests.get(url_zitat)
    data_zitat = resp_zitat.json()
    telegramm = 'Wiesbaden - Mainz\n'
    with open(ort + str(Zeitstempel) + '_data.txt', 'w') as outfile:
        json.dump(data_zitat, outfile)
    for i in data_zitat['departures']:
        if i['train'] == "S 8":
            if i['destination'] == 'Offenbach(Main)Ost':
                antwort = (i['train'] + ' ' + i['platform'] + ' ' + str(i['scheduledDeparture']))
                if i['isCancelled'] != 1:
                    if i['delayDeparture'] != 0:
                        antwort = antwort + (' Verspätung: ' + str(i['delayDeparture']) + ' Minuten')
                    else:
                        antwort = antwort + ' PÜNKTLICH'
                else:
                    antwort = antwort + 'CANCELLED!!!'
                telegramm = telegramm + antwort + '\n'

        if i['train'] == "RB 75":
            if i['destination'] == 'Aschaffenburg Hbf':
                antwort = (i['train'] + ' ' + i['platform'] + ' ' + str(i['scheduledDeparture']))
                if i['isCancelled'] != 1:
                    if i['delayDeparture'] != 0:
                        antwort = antwort + (' Verspätung: ' + str(i['delayDeparture']) + ' Minuten')
                    else:
                        antwort = antwort + ' PÜNKTLICH'
                else:
                    antwort = antwort + 'CANCELLED!!!'
                telegramm = telegramm + antwort + '\n'
    return telegramm

def mzaz():
    url_zitat = 'https://dbf.finalrewind.org/mainzhbf.json?version=3'
    resp_zitat = requests.get(url_zitat)
    data_zitat = resp_zitat.json()
    telegramm = 'Mainz - Alzey\n'
    with open(ort + str(Zeitstempel) + '_data.txt', 'w') as outfile:
        json.dump(data_zitat, outfile)
    for i in data_zitat['departures']:
        if i['train'] == "RE 13":
            if i['delayDeparture'] != None:
                antwort = (i['train'] + ' ' + i['platform'] + ' ' + str(i['scheduledDeparture']))
                if i['isCancelled'] != 1:
                    if i['delayDeparture'] != 0:
                        antwort = antwort + (' Verspätung: ' + str(i['delayDeparture']) + ' Minuten')
                    else:
                        antwort = antwort + ' PÜNKTLICH'
                else:
                    antwort = antwort + 'CANCELLED!!!'
                telegramm = telegramm + antwort + '\n'
        if i['train'] == "RB 31":
            if i['delayDeparture'] != None:
                antwort = (i['train'] + ' ' + i['platform'] + ' ' + str(i['scheduledDeparture']))
                if i['isCancelled'] != 1:
                    if i['delayDeparture'] != 0:
                        antwort = antwort + (' Verspätung: ' + str(i['delayDeparture']) + ' Minuten')
                    else:
                        antwort = antwort + ' PÜNKTLICH'
                else:
                    antwort = antwort + 'CANCELLED!!!'
                telegramm = telegramm + antwort + '\n'
    return telegramm

def azmz():
    url_zitat = 'https://dbf.finalrewind.org/alzeyhbf.json?version=3'
    resp_zitat = requests.get(url_zitat)
    data_zitat = resp_zitat.json()
    telegramm = 'Alzey - Mainz\n'
    with open(ort + str(Zeitstempel) + '_data.txt', 'w') as outfile:
        json.dump(data_zitat, outfile)
    for i in data_zitat['departures']:
        # print(i)
        if i['train'] == "RE 13":
            # print(i)
            if i['destination'] == 'Mainz Hbf':
                antwort = (i['train'] + ' ' + i['platform'] + ' ' + str(i['scheduledDeparture']))
                if i['isCancelled'] != 1:
                    if i['delayDeparture'] != 0:
                        antwort = antwort + (' Verspätung: ' + str(i['delayDeparture']) + ' Minuten')
                    else:
                        antwort = antwort + ' PÜNKTLICH'
                else:
                    antwort = antwort + 'CANCELLED!!!'
                telegramm = telegramm + antwort + '\n'
        if i['train'] == "RB 31":
            if i['destination'] == 'Mainz Hbf':
                antwort = (i['train'] + ' ' + i['platform'] + ' ' + str(i['scheduledDeparture']))
                if i['isCancelled'] != 1:
                    if i['delayDeparture'] != 0:
                        antwort = antwort + (' Verspätung: ' + str(i['delayDeparture']) + ' Minuten')
                    else:
                        antwort = antwort + ' PÜNKTLICH'
                else:
                    antwort = antwort + 'CANCELLED!!!'
                telegramm = telegramm + antwort + '\n'
    return telegramm

if hour <=12:
    sendto=(azmz())+'\n'+mzwi()
    tb.send_message(ChatID, sendto)
if hour >=13:
    sendto = (wimz()) + '\n' + mzaz()
    tb.send_message(ChatID, sendto)

