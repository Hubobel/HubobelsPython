import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = 'carsten.richter77@gmail.com'
bcc = ['schneeschieben@web.de', 'carsten@hubobel.de', 'johanna.richter.vogt@googlemail.com', 'crichter@soka-bau.de']
toaddr = 'carsten.richter77@gmail.com'
pwd = 'xxxxxxxx'

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = 'Hello World of Python-test2'


body = 'Hello World again and again and again'

msg.attach(MIMEText(body, 'plain'))

filename = 'heute.pdf'
attachment = open('mpg/heute.pdf','rb')

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition','attachment; filename= %s'% filename)

msg.attach(part)

filename = 'morgen.pdf'
attachment = open('mpg/morgen.pdf','rb')

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition','attachment; filename= %s'% filename)

msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr,pwd)
text = msg.as_string()
server.sendmail(fromaddr, bcc, text)
server.quit()

