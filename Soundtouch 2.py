import urllib.request

class soundtouch():
    def __init__(self):
        self.url="http://10.0.1.27:8090/"
    def Webaufruf(self,befehl):
        try:
            self.urli=self.url+befehl
            antwort = urllib.request.urlopen(self.urli)
            b = (antwort.read())
            self.xmlString = b.decode("utf-8")
            return self.xmlString
        except:
            return None
    def now_playing(self):
        return self.Webaufruf("now_playing")
        return antwort
    def info(self):
        return self.Webaufruf("info")
    def sources(self):
        return self.Webaufruf("sources")
    def presets(self):
        return self.Webaufruf("presets")
    def volume(self):
        return self.Webaufruf("volume")
    def suche (self,suchstring):
        string = self.info()
        anfang = string.find("<"+suchstring+">") + len("<"+suchstring+">")
        ende = string.find("</"+suchstring+">")
        if ende != -1:
            return string[anfang:ende]
        else:
            return None

bose=soundtouch()
print((bose.info()))
print((bose.presets()))
print((bose.volume()))
print((bose.now_playing()))
print((bose.suche("softwareVersion")))