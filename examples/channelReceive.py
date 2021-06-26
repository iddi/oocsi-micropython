# Copyright (c) 2021 Mathias Funk
# This software is released under the MIT License.
# http://opensource.org/licenses/mit-license.php

import network
from oocsi import OOCSI
import time

def receiveEvent(sender, recipient, event):
    print('from ', sender, ' -> ', event)

# connect to the WIFI
wlan = network.WLAN(network.STA_IF)
def connectWifi():
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        # replace these by your WIFI name and password
        wlan.connect('WIFI_SSID', 'WIFI_PASSWORD')
        while not wlan.isconnected():
            pass
    # print('network config:', wlan.ifconfig())

#---------------------------------------------------------------------------

# connect to wifi
connectWifi()

# connect to OOCSI:
# replace the 'MicroPython_receiver' by a name of your choice
# replace SERVER_ADDRESS with the address of an OOCSI server
o = OOCSI('MicroPython_receiver', 'SERVER_ADDRESS')
# subscribe to 'timechannel' on the OOCSI server and forward all events
# to the receiveEvent function defined above
o.subscribe('timechannel', receiveEvent)
