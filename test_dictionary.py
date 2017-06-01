import urllib.request
import requests
def email_alert(first):
    report = {}
    report["value1"] = first

    urllib.request.urlopen("https://maker.ifttt.com/trigger/kalender/with/key/foLJhy361EqeESdkssI-J", data=report)


print("Choose your third string.")
c = input()
#email_alert(c)
url1 = "https://maker.ifttt.com/trigger/iCloud/with/key/foLJhy361EqeESdkssI-J?value1="
url2 = "&value2=12:05"
url = url1 + c + url2
print(url)
#requests.get("https://maker.ifttt.com/trigger/iCloud/with/key/foLJhy361EqeESdkssI-J?value1=test_final&value2=12:05")
requests.get(url)








