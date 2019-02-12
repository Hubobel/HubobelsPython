import bs4 as bs
import requests as req
mode=3
if mode == 0:
    mode = 'jetzt'
if mode == 1:
    mode = 'abends'
if mode == 3:
    mode = 'fernsehprogramm-nachts'
Sendungen = {}
x = 1





Sendungen={}
x=1
while x<=7:
    sauce = req.get('http://www.tvspielfilm.de/tv-programm/sendungen/' + mode + '.html?page=' + str(x), verify=False)
    soup = bs.BeautifulSoup(sauce.text, 'lxml')

    sender_source = soup.find_all('td', class_='programm-col1')
    sendungen_source= soup.find_all('strong')

    Sender=[]
    Sendung=[]

    for i in sendungen_source:
        Sendung.append(i.text)
    for i in sender_source:
        text=i.text
        text=text.replace('\n','')
        text = text.replace(' ', '')
        Sender.append(text)
    Sendung.pop(0)              #erstes Element des Listenelements 'Sendung' wird entfernt
    programm={}
    a=0
    b=0

    while a<len(Sender):
        programm['Uhrzeit']=Sendung[b]
        programm['Titel']=Sendung[b+1]
        Sendungen[Sender[a]]={}
        Sendungen[Sender[a]].update(programm)
        a+=1
        b+=2
    x+=1

liste=[]
for i in Sendungen:
    liste.append(i)
Sendungen['0:Sender']=liste
print(Sendungen)
