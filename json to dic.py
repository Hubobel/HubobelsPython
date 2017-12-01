import json
import time
import requests

def update():
    with open('pass.json') as file:
        jsonpass=json.load(file)
    zeit = time.strftime("%s")
    if 'Tag_Nummer' in jsonpass:
        print (jsonpass['Tag_Nummer'])
        if jsonpass['Tag_Nummer']!= zeit:
            print ('update json mit '+zeit)
            jsonpass['Tag_Nummer']=zeit
            with open('pass.json', 'w') as fp:
                json.dump(jsonpass, fp, sort_keys=True, indent=4)
            return True
        else:
            print('kein Update')
            return False
    else:
        jsonpass['Tag_Nummer']=''
        with open('pass.json', 'w') as fp:
            json.dump(jsonpass, fp, sort_keys=True, indent=4)
if update():
    print ('Neuer Tag, neues Gluck!')
    url_zitat = 'https://taeglicheszit.at/zitat-api.php?format=json'
    resp_zitat = requests.get(url_zitat)
    data_zitat = resp_zitat.json()
    #with open(pfad + '/mpg/json_ferien.data', 'w') as outfile:
        #json.dump(data_ferien, outfile)
else:
    print ('im Westen nix neues')

url_zitat = 'https://taeglicheszit.at/zitat-api.php?format=json'
resp_zitat = requests.get(url_zitat)
data_zitat = resp_zitat.json()
print (data_zitat)


