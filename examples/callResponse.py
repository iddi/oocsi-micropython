# Copyright (c) 2021 Mathias Funk
# This software is released under the MIT License.
# http://opensource.org/licenses/mit-license.php

import network
from oocsi import OOCSI
import time

def respondToEvent(response):
    # set data field in the response
    response['newColor'] = int(response['oldColor']) + 1
    
    # play with this delay to let the caller time out
    # time.sleep(4)

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
responder = OOCSI(host='SERVER_ADDRESS')
print('responder: ' + responder.handle)

# register responder
responder.register('colorChannel', 'colorGenerator', respondToEvent)


### test colorGenerator with two calls

# start caller OOCSI client
caller = OOCSI(host='SERVER_ADDRESS')
print('caller: ' + caller.handle)

# asynchronous call
call1 = caller.call('colorChannel', 'colorGenerator', {'oldColor': 9}, 1)
# wait for 2 seconds
time.sleep(2)

# check response in call object
if 'response' in call1:
    print(call1['response'])
else:
    print('response not found')

# blocking call
call2 = caller.callAndWait('colorChannel', 'colorGenerator', {'oldColor': 19}, 1)
# check response in call object directly
if 'response' in call2:
    print(call2['response'])
else:
    print('response not found')

caller.stop()
responder.stop()

time.sleep(1)
