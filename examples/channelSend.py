# Copyright (c) 2021 Mathias Funk
# This software is released under the MIT License.
# http://opensource.org/licenses/mit-license.php

from oocsi import OOCSI
import time
from random import random

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
o = OOCSI('MicroPython_sender', 'SERVER_ADDRESS')

while 1:   
    message = {}
    message['color'] = int(random() * 255)
    message['position'] = int(random() * 255)

    o.send('testchannel', message)

    # wait and continue
    time.sleep(1)
