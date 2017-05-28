#!/usr/bin/python

import imaplib
import re
from urllib.request import urlopen

password= 'XXXXXXX'
user= 'XXXXXXXXXX'
mark = 1   #1  = markiert alle Mails als gelesen
ip = '10.0.1.100' # IP der CCU / RaspberryMatic / YAHM
SV = 'Mail' # Name der Systemvariable vom Typ Zahl


imap_server = imaplib.IMAP4_SSL("imap.gmail.com",993)
imap_server.login(user, password)
imap_server.select('INBOX')

status, response = imap_server.status('INBOX', "(UNSEEN)")
unreadcount = response[0].split()[2]
xyz = str(unreadcount)
zahlen=re.findall('([0-9]+)', xyz)
string="".join([str(i) for i in zahlen])

url = 'http://'+ip+':8181/loksoft.exe?ret=dom.GetObject("'+SV+'").State('+string+')'
urlopen(url)


if mark == 1:
    result, data = imap_server.uid('SEARCH', None, '(UNSEEN)')
    uids = data[0].split()
    for uid in uids:
        result, data = imap_server.uid('fetch', uid, '(RFC822)')
        # ------   data is manufactured
        result = imap_server.uid("STORE", uid, '+FLAGS', '\\Seen')
