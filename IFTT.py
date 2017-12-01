import urllib.request
import requests
import datetime

datum = datetime.datetime.now().strftime("%H:%M")


print("Choose your third string.")
c = eval(input())
#email_alert(c)
url1 = "https://maker.ifttt.com/trigger/iCloud/with/key/foLJhy361EqeESdkssI-J?value1="
url2 = "&value2="
url = url1 + c + url2 + datum
print(url)
requests.get("https://maker.ifttt.com/trigger/iCloud/with/key/foLJhy361EqeESdkssI-J?value1=test_final&value2=12:05")
requests.get(url)

