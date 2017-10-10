import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

fromaddr = 'carsten.richter77@gmail.com'
toaddr = 'carsten.richter77@gmail.com'

pfad = os.path.dirname(__file__)

fobj = open(pfad+"/mpg/adressen.txt")
bcc =[]
for line in fobj:
    a = line.rstrip()
    bcc.append(a)
fobj.close()

pwd = bcc[0]

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = 'Hello World of Python-LISTENtest'

body = 'Hello World again and again and again'

msg.attach(MIMEText(body, 'plain'))

filename = 'heute.pdf'
attachment = open(pfad+'/mpg/heute.pdf','rb')

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition','attachment; filename= %s'% filename)

msg.attach(part)

filename = 'morgen.pdf'
attachment = open(pfad+'/mpg/morgen.pdf','rb')

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition','attachment; filename= %s'% filename)

msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr,pwd)
text = msg.as_string()
server.sendmail(fromaddr, bcc[1:], text)
server.quit()

