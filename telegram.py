import telebot

TOKEN = '467241832:AAH3e0y6Fm7ig5DtConJP29GsD-zX1psNZo'
chat_id = '@mpglu'
text='Es gibt einen neuen Vertretungsplan.'
tb=telebot.TeleBot(TOKEN)
tb.send_message(chat_id,text)

document = open('heute.pdf','rb')
tb.send_document(chat_id, document,caption='NEUUUUU')