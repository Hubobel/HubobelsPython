import json
import os
import sys
conf = os.path.basename(sys.argv[0])
conf = conf.replace(".py", ".conf")
if os.path.isfile(conf) is False:
    print(conf + ' scheint es nicht zu geben.')
    print('Ich lege eine neue Datei '+ conf + ' an.')
    passw={"mail_pass": "","mail_user": "",
           "mail_host": "",
           "mail_folder": "",
           "Chat_ID": "","TOKEN": ""
           }
    print(str(conf)+ ' bitte entsprechend befüllen.')
    with open(conf, 'w') as fp:
        json.dump(passw, fp, sort_keys=True, indent=4)
    quit()
else:
    with open(conf) as file:
        passw = json.load(file)