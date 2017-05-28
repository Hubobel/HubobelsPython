import urllib.request
import re


def kodi(suchstring):

    url = "http://10.0.1.102/jsonrpc?request=%7B%22jsonrpc%22:%20%222.0%22,%20%22method%22:%20%22Player.GetItem%22,%20%22params%22:%20%7B%20%22properties%22:%20%5B%22title%22,%20%22album%22,%20%22artist%22,%20%22season%22,%20%22episode%22,%20%22duration%22,%20%22showtitle%22,%20%22tvshowid%22,%20%22thumbnail%22,%20%22file%22,%20%22fanart%22,%20%22streamdetails%22%5D,%20%22playerid%22:%201%20%7D,%20%22id%22:%20%22VideoGetItem%22%7D"
    antwort = urllib.request.urlopen(url)
    b=(antwort.read())
    a = b.decode("utf-8")

    #KODI aus:
    #a = "{\"id\":\"VideoGetItem\",\"jsonrpc\":\"2.0\",\"result\":{\"item\":{\"album\":\"\",\"artist\":[],\"episode\":-1,\"fanart\":\"\",\"file\":\"\",\"label\":\"\",\"season\":-1,\"showtitle\":\"\",\"streamdetails\":{\"audio\":[],\"subtitle\":[],\"video\":[]},\"thumbnail\":\"\",\"title\":\"\",\"tvshowid\":-1,\"type\":\"unknown\"}}}"
    #KODI TV-Show:
    #a = "{\"id\":\"VideoGetItem\",\"jsonrpc\":\"2.0\",\"result\":{\"item\":{\"album\":\"\",\"artist\":[],\"episode\":1,\"fanart\":\"image://http%3a%2f%2fthetvdb.com%2fbanners%2ffanart%2foriginal%2f81189-13.jpg/\",\"file\":\"nfs://10.0.1.30/mnt/2T/Serien/Breaking Bad/S01/Brak.Bad.s01e01.Der.Einstieg.Ger.AC51.DL.72p.BRay.x264-Kristallprinz.mp4\",\"id\":3466,\"label\":\"Der Einstieg\",\"season\":1,\"showtitle\":\"Breaking Bad\",\"streamdetails\":{\"audio\":[],\"subtitle\":[],\"video\":[]},\"thumbnail\":\"image://http%3a%2f%2fthetvdb.com%2fbanners%2fepisodes%2f81189%2f349232.jpg/\",\"title\":\"Der Einstieg\",\"tvshowid\":165,\"type\":\"episode\"}}}"
    #KODI Movie:
    a = "{\"id\":\"VideoGetItem\",\"jsonrpc\":\"2.0\",\"result\":{\"item\":{\"album\":\"\",\"artist\":[],\"episode\":-1,\"fanart\":\"image://http%3a%2f%2fimage.tmdb.org%2ft%2fp%2foriginal%2fyIZ1xendyqKvY3FGeeUYUd5X9Mm.jpg/\",\"file\":\"nfs://10.0.1.30/mnt/2T/NFS_Filme/Arrival.2016.German.720p.BluRay.x264-DOUCEMENT/arrival.2016.german.720p.bluray.x264-doucement.mkv\",\"id\":389,\"label\":\"Arrival\",\"season\":-1,\"showtitle\":\"\",\"streamdetails\":{\"audio\":[{\"channels\":6,\"codec\":\"dca\",\"language\":\"ger\"}],\"subtitle\":[{\"language\":\"ger\"}],\"video\":[{\"aspect\":2.3880600929260253906,\"codec\":\"h264\",\"duration\":6991,\"height\":536,\"language\":\"eng\",\"stereomode\":\"\",\"width\":1280}]},\"thumbnail\":\"image://http%3a%2f%2fimage.tmdb.org%2ft%2fp%2foriginal%2fx9DnIgHVWbW3uIJIQ2KeqeW0n2u.jpg/\",\"title\":\"Arrival\",\"tvshowid\":-1,\"type\":\"movie\"}}}"


    start = len(suchstring)+4   # berechnet die Anfangsposition des Wertes
    ende = len(a)               # gibt die Gesamtlänge der URL Antwort an

    position = a.find("\""+suchstring,0,ende)   #sucht in der gesamten URL Antwort nach dem Suchbegriff und ermittelt dessen Position im String (Anfang)
    if position>0:
        position2 = a.find(",\"",position,ende)     #sucht anhand der Anfangspos. des Suchstrings nach dem Ende des dazugehörigen Wertes (endet mit ,")
        if position2<0:                             #filter das Ende des JSON-Objektes heraus (kein ," mehr vorhanden)
            position2 =ende-3
        wert = (a[position+start:position2-1])        #gibt den Wert des Suchbegriffes aus

        return (wert)
    return 0

eingabe = input("was: ")

label = kodi(eingabe)
print(label)
