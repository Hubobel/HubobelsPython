mv#!/usr/bin/env python

import poplib
import email
import os
import sys
import string
import time

#
# attsave.py
# Check emails at PROVIDER for attachments and save them to SAVEDIR.
#
#

PROVIDER = "pop3.web.de"
USER = "debhubobel@web.de"
PASSWORD = "PL19zPL19z"

SAVEDIR = "/home/carsten"


def saveAttachment(mstring):

    filenames = []
    attachedcontents = []

    msg = email.message_from_string(mstring)

    for part in msg.walk():

        fn = part.get_filename()

        if fn <> None:
            filenames.append(fn)
            attachedcontents.append(part.get_payload(decode = True))

    for i in range(len(filenames)):
        fp = file(SAVEDIR + "/" + filenames[i], "wb")
        fp.write(attachedcontents[i])
        print 'Found and saved attachment "' + filenames[i] + '".'
        fp.close()

try:
    client = poplib.POP3_SSL(PROVIDER)
except:
    print "Error: Provider not found."
    sys.exit(1)

client.user(USER)
client.pass_(PASSWORD)

anzahl_mails = len(client.list()[1])

for i in range(anzahl_mails):
    lines = client.retr(i + 1)[1]
    mailstring = string.join(lines, "\n")
    saveAttachment(mailstring)



poplist = client.list()
if poplist[0].startswith('+OK') :
    msglist = poplist[1]
    for msgspec in msglist :
        # msgspec is something like "3 3941",
        # msg number and size in octets
        msgnum = int(msgspec.split(' ')[0])
        client.dele(msgnum)
    else :
        None


wtag = time.strftime('%H%M')
if wtag == '1945':
    for filename in os.listdir(SAVEDIR+'/added'):
        print filename+' wurde erfolgreich geloescht.'
        os.remove(SAVEDIR+'/added/'+filename)

client.quit()
