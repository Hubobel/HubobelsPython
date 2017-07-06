import urllib.request
import time

class kodi():
    def __init__(self,url):
        self.kodiurl="http://"+url+"/jsonrpc?request=%7B%22jsonrpc%22:%20%222.0%22,%20%22method%22:%20%22Player.GetItem%22,%20%22params%22:%20%7B%20%22properties%22:%20%5B%22title%22,%20%22album%22,%20%22artist%22,%20%22season%22,%20%22episode%22,%20%22duration%22,%20%22showtitle%22,%20%22tvshowid%22,%20%22thumbnail%22,%20%22file%22,%20%22fanart%22,%20%22streamdetails%22%5D,%20%22playerid%22:%201%20%7D,%20%22id%22:%20%22VideoGetItem%22%7D"
        print("Kodi-Objekt erzeugt")
        self.a = self.JSON_holen()


    def JSON_holen(self):
        try:
            antwort = urllib.request.urlopen(self.kodiurl)
            b = (antwort.read())
            a = b.decode("utf-8")
            return a
        except:
            return None

    def Suchen_nach(self, suchstring, json=""):
        start = len(suchstring) + 3  # berechnet die Anfangsposition des Wertes
        ende = len(self.a)  # gibt die Gesamtlänge der URL Antwort an
        position = self.a.find("\"" + suchstring, 46,
                          ende)  # sucht in der gesamten URL Antwort nach dem Suchbegriff und ermittelt dessen Position im String (Anfang)
        if position > 0:
            position2 = self.a.find(",\"", position,
                               ende)  # sucht anhand der Anfangspos. des Suchstrings nach dem Ende des dazugehörigen Wertes (endet mit ,")
            wert = (self.a[position + start:position2])  # gibt den Wert des Suchbegriffes aus
            x = 0
            while wert.isalnum() is False and x < 2:
                wert = wert.strip("\"}][{")
                x = x + 1
            return wert
        return None

    def kodiitem(self,koditems = {"episode": "", "fanart": "", "file": "", "label": "", "season": "", "showtitle": "", "type": "",
                    "title": "", "id": "", "width": ""}):
        a = self.JSON_holen()
        if a != None:
            for i in koditems:
                string = self.Suchen_nach(i, a)
                if type(string)==str:
                    string = string.replace("ä", "ae").replace("Ä", "Ae").replace("ö", "oe").replace("Ö", "oe").replace(
                        "ü", "ue").replace("Ü", "Ue").replace(" ", "_")
                elif string == None:
                    string =""
                koditems[i] = string
            if "type" in koditems:
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
            return koditems
koditems = {"episode": "", "width": "","label": ""}
a = kodi("10.0.1.102")

print(a.kodiitem(koditems))
