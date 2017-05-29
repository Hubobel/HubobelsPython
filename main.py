import urllib.request


def kodi(suchstring,a):

    # KODI aus:
    # a = "{\"id\":\"VideoGetItem\",\"jsonrpc\":\"2.0\",\"result\":{\"item\":{\"album\":\"\",\"artist\":[],\"episode\":-1,\"fanart\":\"\",\"file\":\"\",\"label\":\"\",\"season\":-1,\"showtitle\":\"\",\"streamdetails\":{\"audio\":[],\"subtitle\":[],\"video\":[]},\"thumbnail\":\"\",\"title\":\"\",\"tvshowid\":-1,\"type\":\"unknown\"}}}"
    # KODI TV-Show:
    #a = "{\"id\":\"VideoGetItem\",\"jsonrpc\":\"2.0\",\"result\":{\"item\":{\"album\":\"\",\"artist\":[],\"episode\":1,\"fanart\":\"image://http%3a%2f%2fthetvdb.com%2fbanners%2ffanart%2foriginal%2f81189-13.jpg/\",\"file\":\"nfs://10.0.1.30/mnt/2T/Serien/Breaking Bad/S01/Brak.Bad.s01e01.Der.Einstieg.Ger.AC51.DL.72p.BRay.x264-Kristallprinz.mp4\",\"id\":3466,\"label\":\"Der Einstieg\",\"season\":1,\"showtitle\":\"Breaking Bad\",\"streamdetails\":{\"audio\":[],\"subtitle\":[],\"video\":[]},\"thumbnail\":\"image://http%3a%2f%2fthetvdb.com%2fbanners%2fepisodes%2f81189%2f349232.jpg/\",\"title\":\"Der Einstieg\",\"tvshowid\":165,\"type\":\"episode\"}}}"
    # KODI Movie:
    #a = "{\"id\":\"VideoGetItem\",\"jsonrpc\":\"2.0\",\"result\":{\"item\":{\"album\":\"\",\"artist\":[],\"episode\":-1,\"fanart\":\"image://http%3a%2f%2fimage.tmdb.org%2ft%2fp%2foriginal%2fyIZ1xendyqKvY3FGeeUYUd5X9Mm.jpg/\",\"file\":\"nfs://10.0.1.30/mnt/2T/NFS_Filme/Arrival.2016.German.720p.BluRay.x264-DOUCEMENT/arrival.2016.german.720p.bluray.x264-doucement.mkv\",\"id\":389,\"label\":\"Arrival\",\"season\":-1,\"showtitle\":\"\",\"streamdetails\":{\"audio\":[{\"channels\":6,\"codec\":\"dca\",\"language\":\"ger\"}],\"subtitle\":[{\"language\":\"ger\"}],\"video\":[{\"aspect\":2.3880600929260253906,\"codec\":\"h264\",\"duration\":6991,\"height\":536,\"language\":\"eng\",\"stereomode\":\"\",\"width\":1280}]},\"thumbnail\":\"image://http%3a%2f%2fimage.tmdb.org%2ft%2fp%2foriginal%2fx9DnIgHVWbW3uIJIQ2KeqeW0n2u.jpg/\",\"title\":\"Arrival\",\"tvshowid\":-1,\"type\":\"movie\"}}}"


    start = len(suchstring) + 3  # berechnet die Anfangsposition des Wertes
    ende = len(a)  # gibt die Gesamtlänge der URL Antwort an
    position = a.find("\"" + suchstring, 46, ende)  # sucht in der gesamten URL Antwort nach dem Suchbegriff und ermittelt dessen Position im String (Anfang)
    if position > 0:
        position2 = a.find(",\"", position, ende)  # sucht anhand der Anfangspos. des Suchstrings nach dem Ende des dazugehörigen Wertes (endet mit ,")
        wert = (a[position + start:position2])  # gibt den Wert des Suchbegriffes aus
        x=0
        while wert.isalnum() is False and x<2:
            wert = wert.strip("\"}][{")
            x=x+1
        return wert

    return None
    
def kodiserie():
    if koditems ["type"] == "episode":
        if len(koditems["season"]) == 1:
            koditems["season"] = "S0" + koditems["season"]
        else:koditems["season"] = "S" + koditems["season"]
        
        if len(koditems["episode"]) == 1:
            koditems["episode"] = "E0" + koditems["episode"]
        else:koditems["episode"] = "E" + koditems["episode"]
    elif koditems["type"] == "movie":
        koditems["season"] = ""
        koditems["episode"]  = ""
    elif koditems["type"] == "unknown":
        koditems["season"] = ""
        koditems["episode"]  = ""
        
    return


koditems = {"episode": "", "fanart": "", "file": "", "label": "", "season": "", "showtitle": "", "type": "",
            "title": "","id":"","width":""}

# KODI aus:
a = "{\"id\":\"VideoGetItem\",\"jsonrpc\":\"2.0\",\"result\":{\"item\":{\"album\":\"\",\"artist\":[],\"episode\":-1,\"fanart\":\"\",\"file\":\"\",\"label\":\"\",\"season\":-1,\"showtitle\":\"\",\"streamdetails\":{\"audio\":[],\"subtitle\":[],\"video\":[]},\"thumbnail\":\"\",\"title\":\"\",\"tvshowid\":-1,\"type\":\"unknown\"}}}"
# KODI TV-Show:
#a = "{\"id\":\"VideoGetItem\",\"jsonrpc\":\"2.0\",\"result\":{\"item\":{\"album\":\"\",\"artist\":[],\"episode\":1,\"fanart\":\"image://http%3a%2f%2fthetvdb.com%2fbanners%2ffanart%2foriginal%2f81189-13.jpg/\",\"file\":\"nfs://10.0.1.30/mnt/2T/Serien/Breaking Bad/S01/Brak.Bad.s01e01.Der.Einstieg.Ger.AC51.DL.72p.BRay.x264-Kristallprinz.mp4\",\"id\":3466,\"label\":\"Der Einstieg\",\"season\":1,\"showtitle\":\"Breaking Bad\",\"streamdetails\":{\"audio\":[],\"subtitle\":[],\"video\":[]},\"thumbnail\":\"image://http%3a%2f%2fthetvdb.com%2fbanners%2fepisodes%2f81189%2f349232.jpg/\",\"title\":\"Der Einstieg\",\"tvshowid\":165,\"type\":\"episode\"}}}"
# KODI Movie:
#a = "{\"id\":\"VideoGetItem\",\"jsonrpc\":\"2.0\",\"result\":{\"item\":{\"album\":\"\",\"artist\":[],\"episode\":-1,\"fanart\":\"image://http%3a%2f%2fimage.tmdb.org%2ft%2fp%2foriginal%2fyIZ1xendyqKvY3FGeeUYUd5X9Mm.jpg/\",\"file\":\"nfs://10.0.1.30/mnt/2T/NFS_Filme/Arrival.2016.German.720p.BluRay.x264-DOUCEMENT/arrival.2016.german.720p.bluray.x264-doucement.mkv\",\"id\":389,\"label\":\"Arrival\",\"season\":-1,\"showtitle\":\"\",\"streamdetails\":{\"audio\":[{\"channels\":6,\"codec\":\"dca\",\"language\":\"ger\"}],\"subtitle\":[{\"language\":\"ger\"}],\"video\":[{\"aspect\":2.3880600929260253906,\"codec\":\"h264\",\"duration\":6991,\"height\":536,\"language\":\"eng\",\"stereomode\":\"\",\"width\":1280}]},\"thumbnail\":\"image://http%3a%2f%2fimage.tmdb.org%2ft%2fp%2foriginal%2fx9DnIgHVWbW3uIJIQ2KeqeW0n2u.jpg/\",\"title\":\"Arrival\",\"tvshowid\":-1,\"type\":\"movie\"}}}"

for i in koditems:
    wert = kodi(i,a)
    koditems[i] = wert
    if wert!=None:
        print(i + " : " + wert)

kodiserie()
print (koditems)
print (koditems["showtitle"]+" - "+koditems["label"]+" "+koditems["season"] + koditems["episode"])



