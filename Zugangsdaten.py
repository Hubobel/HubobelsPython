import json
import os
import sys
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
                "mail_folder": ""
            },
        'Telegram':
            {
                "Chat_ID": "",
                "TOKEN": ""
            }
        }


    print(str(appname) + ' bitte entsprechend befüllen.')
    with open(absFilePath, 'w') as fp:
        json.dump(passw, fp, sort_keys=True, indent=4)
    quit()
else:
    with open(absFilePath) as file:
        passw = json.load(file)
