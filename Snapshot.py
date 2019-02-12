import urllib.request
import telebot

urllib.request.urlretrieve('http://10.0.1.59:8765/picture/1/current/', 'snap.jpg')

TOKEN='680737840:AAEaa7Vxl_kZz_LWS1_S-lH6Eda7HXqu6Y4'
ChatID='322673713'
tb = telebot.TeleBot(TOKEN)
document=open('snap.jpg','rb')
tb.send_photo(ChatID,document)
