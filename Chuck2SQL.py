# -*- coding: UTF8 -*-
import requests
import pymysql



class BotHandler:
    def __init__(self, token):
            self.token = token
            self.api_url = "https://api.telegram.org/bot{}/".format(token)

    #url = "https://api.telegram.org/bot<token>/"

    def get_updates(self, offset=0, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text, 'parse_mode': 'HTML'}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_first_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[0]
        else:
            last_update = None

        return last_update


token = '1030619458:AAGTrWO2-m38ViL0y2R8XaV0P1gg8kHxj3o' #Token of your bot
magnito_bot = BotHandler(token) #Your bot's name



def main():
    new_offset = 0
    print('hi, now launching...')

    while True:

        all_updates=magnito_bot.get_updates(new_offset)

        if len(all_updates) > 0:
            for current_update in all_updates:
                print(current_update)
                first_update_id = current_update['update_id']

                if 'text' not in current_update['message']:
                    first_chat_text='New member'
                else:
                    first_chat_text = current_update['message']['text']
                first_chat_id = current_update['message']['chat']['id']
                if 'first_name' in current_update['message']:
                    first_chat_name = current_update['message']['chat']['first_name']
                elif 'new_chat_member' in current_update['message']:
                    first_chat_name = current_update['message']['new_chat_member']['username']
                elif 'from' in current_update['message']:
                    first_chat_name = current_update['message']['from']['first_name']
                else:
                    first_chat_name = "unknown"
                signal = first_chat_text[0:5]

                if signal == '/0815':
                    magnito_bot.send_message(first_chat_id, 'Ich lausche deinem Befehl ' + first_chat_name)
                    new_offset = first_update_id + 1
                    connection = pymysql.connect(db="hubobel",
                                                 user="hubobel",
                                                 passwd="polier2003",
                                                 host='10.0.1.59', charset='utf8')
                    cursor = connection.cursor()
                    sql = "SELECT * FROM facts ORDER BY nr DESC"
                    resp = cursor.execute(sql)
                    x = int(resp)
                    magnito_bot.send_message(first_chat_id, 'Es gibt derzeit ' + str(x) + ' Facts')

                    fact = first_chat_text[6:]

                    sql = "INSERT INTO `facts`(`nr`, `fact`) VALUES ('" + str(x+1) + "','" + fact + "')"
                    sql_q = "SELECT * FROM facts WHERE fact like '%" + fact + "%'"
                    resp = cursor.execute(sql_q)
                    if resp == 0:
                        try:
                            resp = cursor.execute(sql)
                            magnito_bot.send_message(first_chat_id, 'Ich habe diesen Fact an SQL übertragen: ' + fact)
                        except:
                            magnito_bot.send_message(first_chat_id, 'Ich hatte ein Problem, den Fact an SQL zu übermitteln!')
                    else:
                        magnito_bot.send_message(first_chat_id, 'Den Fact "' + fact+ ' "gibt es schon in meiner Database!')
                    connection.commit()
                    cursor.close()
                    connection.close()
                else:
                    if first_chat_text == 'Hi':
                        magnito_bot.send_message(first_chat_id, 'Morning ' + first_chat_name)
                        new_offset = first_update_id + 1
                    elif first_chat_text == 'Wer bin ich':
                        magnito_bot.send_message(first_chat_id, 'Du bist der Größte '+ signal)
                        new_offset = first_update_id + 1
                    else:
                        magnito_bot.send_message(first_chat_id, 'How are you doing '+first_chat_name)
                        new_offset = first_update_id + 1


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()