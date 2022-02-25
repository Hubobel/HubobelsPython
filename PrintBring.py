from imbox import Imbox
import traceback
import os
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import sys
from datetime import datetime
import logging
import json

appname = os.path.basename(sys.argv[0])
appname = appname.replace(".py", ".conf")
absFilePath = os.path.abspath(__file__)
absFilePath = absFilePath.replace(".py", ".conf")


if os.path.isfile(absFilePath) is False:
    print(appname + ' scheint es nicht zu geben.')
    print('Ich lege eine neue Datei ' + appname + ' an.')
    passw={'mail':
            {
                "mail_pass": "",
                "mail_user": "",
                "mail_host": "",
                "mail_smtp": ""
            }

        }


    print(str(appname) + ' bitte entsprechend befüllen.')
    with open(absFilePath, 'w') as fp:
        json.dump(passw, fp, sort_keys=True, indent=4)
    quit()
else:
    with open(absFilePath) as file:
        passw = json.load(file)
print(passw)
if not os.path.exists('Post'):
    os.makedirs('Post')
empfänger = sys.argv
if (len(empfänger)) != 2:
    print('Geben Sie bitte GENAU EINEN Empfänger als Argument an!')
    exit()
absFilePath = os.path.abspath(__file__)
path, filename = os.path.split(absFilePath)

host = passw['mail']['mail_host']
username = passw['mail']['mail_user']
password = passw['mail']['mail_pass']
smtpServer = passw['mail']['mail_smtp']
smtpPort = 587
sender = username
reciever = empfänger[1]
subject = "Hallo Welt!"
msg = MIMEMultipart()
msg['Subject'] = subject
msg['From'] = sender
msg['To'] = reciever

Log_Format = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename = path + "/printbring.log",
                    filemode = "a",
                    format = Log_Format,
                    level = logging.ERROR)
logger = logging.getLogger()

mail = Imbox(host, username=username, password=password, ssl=True, ssl_context=None, starttls=False)
messages = mail.messages(unread=True)

logger.setLevel(logging.INFO)

for (uid, message) in messages:
    mail.mark_seen(uid) # optional, mark message as read

    bodie = message.sent_from
    body = 'von: ' + str(bodie[0]['name']) + ' über: '+ str(bodie[0]['email'])
    body = body + ' mit dem Betreff: ' + message.subject
    body = body + '\n'
    body = body + 'Datum der ursprünglichen Nachricht: ' + message.date
    body = body + '\n'
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    body = body + 'Datum der Jobverarbeitung: ' + dt_string
    #print(body)
    for idx, attachment in enumerate(message.attachments):
        try:
            name = time.time()
            fn = attachment.get('filename')
            root, extension = os.path.splitext(fn)
            att_fn = str(name)+str(extension)
            print(att_fn)
            with open('Post/' + att_fn, "wb") as fp:
                fp.write(attachment.get('content').read())
            msg = MIMEMultipart()
            msg.attach(MIMEText(body, 'plain'))
            filename = att_fn
            attachment = open('Post/'+filename, 'rb')
            part = MIMEBase('application', 'octet-stream')
            part.set_payload((attachment).read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename= %s' % att_fn)
            msg.attach(part)
            server = smtplib.SMTP(smtpServer, 587)
            server.starttls()
            server.login(username, password)
            msg['Subject'] = str(fn) + ' to ' + str(name)
            text = msg.as_string()
            server.sendmail(username, reciever, text)
            server.quit()
            logger.info(msg['Subject'])

        except:
            print(traceback.print_exc())
            logger.error(traceback.print_exc())
    mail.delete(uid)
for filename in os.listdir('Post'):
    os.remove('Post/'+filename)

logger.setLevel(logging.ERROR)
mail.logout()