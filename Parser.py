import urllib.request
import time


ip = "10.0.1.100"
SV = "xyz"

def kodi(suchstring, a):
    start = len(suchstring) + 3  # berechnet die Anfangsposition des Wertes
    ende = len(a)  # gibt die Gesamtlänge der URL Antwort an
    position = a.find("\"" + suchstring, 46,
                      ende)  # sucht in der gesamten URL Antwort nach dem Suchbegriff und ermittelt dessen Position im String (Anfang)
    if position > 0:
        position2 = a.find(",\"", position,
                           ende)  # sucht anhand der Anfangspos. des Suchstrings nach dem Ende des dazugehörigen Wertes (endet mit ,")
        wert = (a[position + start:position2])  # gibt den Wert des Suchbegriffes aus
        x = 0
        while wert.isalnum() is False and x < 2:
            wert = wert.strip("\"}][{")
            x = x + 1
        return wert
    return None
def kodiserie():
    if koditems["type"] == "episode":
        if len(koditems["season"]) == 1:
            koditems["season"] = "S0" + koditems["season"]
        else:
            koditems["season"] = "S" + koditems["season"]

        if len(koditems["episode"]) == 1:
            koditems["episode"] = "E0" + koditems["episode"]
        else:
            koditems["episode"] = "E" + koditems["episode"]
    elif koditems["type"] == "movie":
        koditems["season"] = ""
        koditems["episode"] = ""
    elif koditems["type"] == "unknown":
        koditems["season"] = ""
        koditems["episode"] = ""
    return
lauf = 1
urlREF = ""
while lauf < 2:
    koditems = {"episode": "", "fanart": "", "file": "", "label": "", "season": "", "showtitle": "", "type": "",
                "title": "", "id": "", "width": ""}
    url = "http://10.0.1.102/jsonrpc?request=%7B%22jsonrpc%22:%20%222.0%22,%20%22method%22:%20%22Player.GetItem%22,%20%22params%22:%20%7B%20%22properties%22:%20%5B%22title%22,%20%22album%22,%20%22artist%22,%20%22season%22,%20%22episode%22,%20%22duration%22,%20%22showtitle%22,%20%22tvshowid%22,%20%22thumbnail%22,%20%22file%22,%20%22fanart%22,%20%22streamdetails%22%5D,%20%22playerid%22:%201%20%7D,%20%22id%22:%20%22VideoGetItem%22%7D"
    antwort = urllib.request.urlopen(url)
    b = (antwort.read())
    a = b.decode("utf-8")
    for i in koditems:
        wert = kodi(i, a)
        koditems[i] = wert
    kodiserie()
    string = koditems["showtitle"] + " " + koditems["label"] + " " + koditems["season"] + koditems["episode"]
    string = string.replace("ä", "ae").replace("Ä", "Ae").replace("ö", "oe").replace("Ö", "oe").replace("ü", "ue").replace("Ü", "Ue").replace(" ", "_")
    if string == "__":
        string = ""
    url = 'http://' + ip + ':8181/loksoft.exe?ret=dom.GetObject("' + SV + '").State("' + string + '")'
    if url != urlREF:
        urllib.request.urlopen(url)
        urlREF = url
    time.sleep(10)
