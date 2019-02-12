#!/usr/bin/python

import datetime
import logging
import urllib2
#import scapy

# Constants
timespan_threshhold = 3

# Globals
lastpress = datetime.datetime(1970, 1, 1)

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *


def button_pressed_dash1():
    global lastpress
    thistime = datetime.datetime.now()
    timespan = thistime - lastpress
    if timespan.total_seconds() > timespan_threshhold:
        current_time = datetime.datetime.strftime(thistime, '%Y-%m-%d %H:%M:%S')
        print
        'Dash button pressed at ' + current_time
        urllib2.urlopen('http://10.0.1.100:8181/loksoft.exe?ret=dom.GetObject("Dash1").State(1)')


def button_pressed_dash2():
    global lastpress
    thistime = datetime.datetime.now()
    timespan = thistime - lastpress
    if timespan.total_seconds() > timespan_threshhold:
        current_time = datetime.datetime.strftime(thistime, '%Y-%m-%d %H:%M:%S')
        print
        'Dash button pressed at ' + current_time
        urllib2.urlopen('http://10.0.1.100:8181/loksoft.exe?ret=dom.GetObject("Dash2").State(1)')


def button_pressed_dash3():
    global lastpress
    thistime = datetime.datetime.now()
    timespan = thistime - lastpress
    if timespan.total_seconds() > timespan_threshhold:
        current_time = datetime.datetime.strftime(thistime, '%Y-%m-%d %H:%M:%S')
        print
        'Dash button pressed at ' + current_time
        urllib2.urlopen('http://10.0.1.100:8181/loksoft.exe?ret=dom.GetObject("Dash3").State(1)')


def button_pressed_dash4():
    global lastpress
    thistime = datetime.datetime.now()
    timespan = thistime - lastpress
    if timespan.total_seconds() > timespan_threshhold:
        current_time = datetime.datetime.strftime(thistime, '%Y-%m-%d %H:%M:%S')
        print
        'Dash button pressed at ' + current_time
        urllib2.urlopen('http://10.0.1.100:8181/loksoft.exe?ret=dom.GetObject("Dash3").State(1)')

    lastpress = thistime


def udp_filter(pkt):
    options = pkt[DHCP].options
    for option in options:
        if isinstance(option, tuple):
            if 'requested_addr' in option:
                # we've found the IP address, which means its the second and final UDP request, so we can trigger our action
                mac_to_action[pkt.src]()
                break


mac_to_action = {'ac:63:be:f8:54:72': button_pressed_dash2, '50:f5:da:1a:6b:39': button_pressed_dash1,
                 '50:f5:da:5c:c1:59': button_pressed_dash3, 'ac:63:be:4f:41:a1': button_pressed_dash4}
mac_id_list = list(mac_to_action.keys())

print
"Waiting for a button press..."
sniff(prn=udp_filter, store=0, filter="udp", lfilter=lambda d: d.src in mac_id_list)

if __name__ == "__main__":
    main()