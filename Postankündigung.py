from imap_tools import MailBox
import telebot
import os
import json

if os.path.isfile('Postankündigung.conf') is False:
    print('"Postankündigung.conf" scheint es nicht zu geben.')
    print('Ich lege eine neue Datei "Postankündigung.conf" an.')
    passw={"mail_pass": "","mail_user": "",
           "mail_host": "",
           "mail_folder": "",
           "Chat_ID": "","TOKEN": ""
           }
    print(str(passw)+ ' bitte entsprechend befüllen.')
    with open('Postankündigung.conf', 'w') as fp:
        json.dump(passw, fp, sort_keys=True, indent=4)
    quit()
else:
    with open('Postankündigung.conf') as file:
        passw = json.load(file)

TOKEN = passw['TOKEN']
chat_id = passw['Chat_ID']
host = passw['mail_host']
username = passw['mail_user']
password = passw['mail_pass']
folder = passw['mail_folder']

tb = telebot.TeleBot(TOKEN)


with MailBox(host).login(username, password, folder) as mailbox:
    anzahl = len(mailbox.numbers(criteria='UNSEEN'))
    ankuendigung = 'Heute befinden sich ' + str(anzahl) + ' Sendungen auf dem Weg in die Hintergasse.'
    tb.send_message(chat_id, ankuendigung)
    for msg in mailbox.fetch(mark_seen=True,criteria='UNSEEN' ):     #criteria='UNSEEN'
        for att in msg.attachments:
            fn = att.filename
            ext = (att.content_type[-3:])
            fn = str(msg.uid) + fn +'.'+ ext
            with open(fn, 'wb') as f:
                f.write(att.payload)
            document = open(fn, 'rb')
            tb.send_document(chat_id, document, caption=msg.date)
            os.remove(fn)