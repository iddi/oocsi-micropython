# Copyright (c) 2021 Mathias Funk
# This software is released under the MIT License.
# http://opensource.org/licenses/mit-license.php

import network
from oocsi import OOCSI
import time

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

# start responder OOCSI client
responder = OOCSI('variable1', 'SERVER_ADDRESS')
# create variable 'color' for first client
v1 = responder.variable('colorChannel', 'color')
v1p = responder.variable('colorChannel', 'position')

# start caller OOCSI client
caller = OOCSI('variable2', 'SERVER_ADDRESS')
# create variable 'color' for second client
v2 = caller.variable('colorChannel', 'color')
v2p = caller.variable('colorChannel', 'position')

# assign a string
v1.set(40)
v1p.set(210)
print('value of first color: ', v1.get())
print('value of first position: ', v1p.get())

time.sleep(1)

print('value of second color: ', v2.get())
print('value of second position: ', v2p.get())

responder.stop()
caller.stop()

time.sleep(1)
