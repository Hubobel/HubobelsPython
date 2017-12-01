import requests
import json
import telebot
import os
import pymysql

def laenge():
    datas = '{"sid":"' + id + '","op":"getHeadlines","feed_id":-1}'
    resp = requests.post(url, datas)
    data = resp.json()
    a=(len(data['content']))
    return a

TOKEN ='312534798:AAFbMjS-tfd2BiZ_j3NEZuQYKwzACMcioVo'
chat_id ='322673713'
tb = telebot.TeleBot(TOKEN)

url = 'http://hubobel.de/tt-rss/api/'
pfad = os.path.dirname(__file__)

datas = '{"op":"login","user":"admin","password":"password"}'
resp = requests.post(url,datas)
data = resp.json()
id= str(data['content']['session_id'])
datas = '{"sid":"'+id+'","op":"getFeeds","cat_id":-4}'
resp = requests.post(url,datas)
data = resp.json()
ids=[]
gefunden=[]
laenge_start=laenge()

suchstring=[]
fobj = open(pfad+"/toFind.txt")
for line in fobj:
    suchstring.append(line.rstrip())
fobj.close()



for i in data['content']:
    if int(i['unread'])>0 and int(i['id'])>0:
        datas = '{"sid":"'+id+'","op":"getHeadlines","feed_id":'+str(i['id'])+'}'
        resp = requests.post(url,datas)
        feeds = resp.json()
        for headlines in feeds['content']:
            if headlines['unread']:
                a=0
                b=len(suchstring)
                if headlines['feed_id'] == '4':
                    article_id=str(headlines['id'])
                    datas = '{"sid":"' + id + '","op":"getArticle","article_id":'+article_id+'}'
                    resp = requests.post(url, datas)
                    data = resp.json()
                    antwort=str(data['content'][0]['content'])

                    connection = pymysql.connect(db="hubobel",
                                                 user="hubobel",
                                                 passwd="polier2003",
                                                 host='10.0.1.59', charset='utf8')
                    cursor = connection.cursor()
                    sql = "SELECT * FROM facts ORDER BY nr DESC"
                    resp = cursor.execute(sql)
                    x = int(resp) + 1

                    line = antwort.replace('<p>', '')
                    line = line.replace('</p>', '')
                    sql = "INSERT INTO `facts`(`nr`, `fact`) VALUES ('" + str(x) + "','" + line + "')"
                    sql_q = "SELECT * FROM facts WHERE fact like '%" + line + "%'"
                    resp = cursor.execute(sql_q)
                    if resp == 0:
                        resp = cursor.execute(sql)
                    connection.commit()
                    cursor.close()
                    connection.close()


                while a<b:
                    if suchstring[a] in str(headlines['title']):
                        ids.append(headlines['id'])
                        if suchstring[a] not in gefunden:
                            gefunden.append(suchstring[a])
                    a=a+1
if ids != []:
    idstring=str(ids)
    idstring=idstring.replace('[',"")
    idstring=idstring.replace(']',"")
    idstring=idstring.replace(' ','')
    datas = '{"sid":"'+id+'","op":"updateArticle","article_ids":"'+idstring+'","mode":1,"field":0}'
    resp = requests.post(url,datas)
    data = resp.json()

laenge_ende=laenge()
ergebniss=laenge_ende-laenge_start

datas = '{"sid":"'+id+'","op":"getCounters","output_mode":"c"}'
resp = requests.post(url,datas)
data = resp.json()
unreadcount=int(data['content'][3]['counter'])

if ergebniss>0:
    bericht='Es gibt '+str(ergebniss)+' neue Nachrichte(n) mit den Begriffen '+str(gefunden)+\
            ' in deinen News!\nEs sind nun '+str(unreadcount)+' ungelesene Nachrichten in deinen News.'
    tb.send_message(chat_id, bericht)




