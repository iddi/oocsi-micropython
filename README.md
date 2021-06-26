# oocsi-micropython
OOCSI for MicroPython (ESP32, ESP8266, micro:bit, pyboard etc.)

## About
What is __MicroPython__? It's a version of the popular Python language and runtime environment that allows to program in Python for microprocessor boards such as ESP32, ESP8266 or many others. The official [site](https://docs.micropython.org/en/latest/index.html) is probably worth a look. 👀

Now we have made the OOCSI library available for MicroPython. This allows to program in high-level Python and connect your boards to the OOCSI network. Super useful for _remote data collection_ and _rapid design prototyping_. If you are already familiar with MicroPython, jumpt to the bottom of the page for a direct intro to OOCSI on MicroPython. 🏃‍♀️


## Getting started

To get started with MicroPython on your board, you need to go through three easy steps:
 - flash MicroPython firmware _(only once!)_
 - connect to the board with a serial connection
 - copy the oocsi.py file to the board and run the first program

### Flash MicroPython firmware

The entire process below is also explained in more detail on the official [MicroPython site](https://docs.micropython.org/en/latest/esp32/tutorial/intro.html). The process is very similar for other baord than the ESP32 that we will use in this example. Ok, let's go! 💪

Install the `esptools` Python package on your system:

````bash
# Python 2.7
pip install esptools

# Python3
pip3 install esptools
````
Now you can flash the firmware on the board. First download a firmware file for your board. For example, assuming an ESP32 board, you select [esp32-20210623-v1.16.bin](https://micropython.org/resources/firmware/esp32-20210623-v1.16.bin) on the [MicroPython download page](https://micropython.org/download/esp32/). With `esptools` and your ESP32 connected to a USB port, you can now flash the firmware directly on the board - in two steps:

1. Erase the flash

````bash
# use esptools directly
esptool --port /dev/tty.usbserial-0001 erase_flash
# or call with python3 interpreter
python3 -m esptool --port /dev/tty.usbserial-0001 erase_flash

````

2. Flash the new firmware

````bash
# use esptools directly
esptool --port /dev/tty.usbserial-0001 --chip esp32 write_flash -z 0x1000 esp32-20210623-v1.16.bin
# or call with python3 interpreter
python3 -m esptool --port /dev/tty.usbserial-0001 --chip esp32 write_flash -z 0x1000 esp32-20210623-v1.16.bin
````

The `--port` command line argument selects the USB port that your ESP32 is connected to. The example above is for macOS and should work imilarly on Linux. For Windows, you might need to figure out which COM port your ESP32 is connected to and adapt the command: `--port COM4`.

The `--chip` command line argument selects the board type. So, if you are not using an ESP32, but an ESP8266 or else, you would need to adapt this part in the command.

The final command line arguments specify the firmware image that will be flashed. Make sure that you specify the filename right and that the firmware file is in the same directory.

Now you have erased and flashed the new firmware. If you see problems, please check the [troubleshooting section](https://docs.micropython.org/en/latest/esp32/tutorial/intro.html#troubleshooting-installation-problems) on the official MicroPython site.


### Connect to the board

The next step is to connect to the board and execute your first commands on the connected board. For this step, you can follow the [ESP8266 tutorial](https://docs.micropython.org/en/latest/esp8266/tutorial/repl.html).

What is a REPL? This is a programming interface that allows to execute code on the ESP32 line by line, which is great to get started. REPL means 'Read Evaluate Print Loop', so you type a short piece of code, it's run on the board, and then you the output back. Easy.

On __macOS__ you can directly attach to the REPL on the Terminal: 

````bash
screen /dev/tty.usbserial-0001 115200 
````
This opens a prompt where you can start typing Python code. Adapt the `/dev/tty.usbserial...` part to your USB serial connection.

On __Linux__ you can use on the Terminal:
````bash
picocom /dev/ttyUSB0 -b115200
````

For __Windows__ and other platforms, check the [reference](https://docs.micropython.org/en/latest/wipy/tutorial/repl.html).

Ok, assuming that you are getting a REPL prompt, let's run the first piece of code on the board:

````python
>>> print('hello esp32!')
hello esp32!
````

The first line is the part that you type, then hit ENTER. After that, the second line will be printed. After that, you can enter the next line of code.

If your board has an LED attached to GPIO2 (the ESP32 modules do) then you can turn it on and off 🚨 using the following code:

````python
>>> import machine
>>> pin = machine.Pin(2, machine.Pin.OUT)
>>> pin.on()
>>> pin.off()
````

There is more information on the [MicroPython site](https://docs.micropython.org/en/latest/esp8266/tutorial/repl.html) that explains a lot of other possibilities of the REPL prompt. Now that you can run code, it might be interesting to check out the [platform](https://docs.micropython.org/en/latest/esp32/quickref.html) in more detail. 🚀


### Access files on the board

Running code line by line is fun, but what about longer programs? Or running a longer program automatically when you power-on the board? Files on the board to the rescue! 🥳

Again, you have multiple options to access files on the board: the [pyboard](https://docs.micropython.org/en/latest/reference/pyboard.py.html) tool or [ampy](https://pypi.org/project/adafruit-ampy/). Let's go with the second one here. Either follow the steps below or a [short tutorial](https://pythonforundergradengineers.com/upload-py-files-to-esp8266-running-micropython.html).

First, install the tool:

````bash
pip3 install adafruit-ampy
````

#### List files

Then run it with the correct serial _port_ (see above) to retrieve the currently stored files on the board:

````bash
ampy --port /dev/tty.usbserial-0001 ls
````

The final `ls` command line argument is the actual command that will be executed by ampy: in this case, `ls` lists the files on the board. You will probably see only a single file `boot.py` which is the first file that will be run when you power-on the board.

#### Run MicroPython code in a file

To run a file directly on the board, just use: 

````bash
# run the code in mycode.py and print the output on the console
ampy --port /dev/tty.usbserial-0001 run mycode.py
````

The output from running this code on the board will be printed on the console.

#### Retrieve files

To retrieve a file from the board, just use: 

````bash
# print the file contents on the console
ampy --port /dev/tty.usbserial-0001 get boot.py
# store the file locally as boot.py
ampy --port /dev/tty.usbserial-0001 get boot.py boot.py
````

#### Store files

To store a local file on the board, use:

````bash
# upload the local boot.py file to the board
ampy --port /dev/tty.usbserial-0001 put boot.py
````

You can now read and write files on the board, and start making bigger steps.

#### Which files matter?

There are two central files `boot.py` and `main.py` for any MicroPython runtime. The first one, `boot.py`, is the first code that will be run when the board boots up. You can leave this file as is, and focus on the second file `main.py`, which is the main program for embedded application.

The `main.py` file is a simple Python file that usually starts with importing packages, then defining a few functions, then the main code body. Let's jump directly to connecting to the OOCSI network with MicroPython.

### OOCSI for MicroPython

Ok, finally, how to get started with OOCSO for MicroPython on a microprocessor board. This way, please!

#### Upload the OOCSI library

The first step is to download the OOCSI library for MicroPython from this repository and then to upload it to your board:

````bash
# store the oocsi.py file on the board
ampy --port /dev/tty.usbserial-0001 put oocsi.py
````

#### Use the OOCSI library

Now you can use OOCSI in your MicroPython code as usual: create an OOCSI connection and use it to send and receive data from the network. Let's try a simple example:

````python
import network
import time
from oocsi import OOCSI

# print event information
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

# keep the program running, can be quit with CTRL-C
while True:
    time.sleep(2)
    print(".")
````

What happens in this piece of code? First of all, we import three libraries to be able to use WIFI (network), sleep (time) and the OOCSI connectivity (OOCSI). Next, we define two functions: the first prints out received events and the second is responsible for connecting to an available WIFI. You need to replace the `WIFI_SSID` and `WIFI_PASSWORD` with the credentials of the WIFI network you would the board to connect to.

The main part of the code, after the dashed line, basically connects to the WIFI, then establishes an connection to the OOCSI network, and finally sleeps indefinitely, so the network communication can take off. You can quit the program by pressing CTRL-C on your keyboard.

The output of this program should be first a few lines about connecting to the WIFI and the OOCSI network, then the events that the board receives from the OOCSI server. In this case we subscribe to the `timechannel` which sends the current time every second.

This is the end of the mini tutorial. ✨ Thanks for staying until here, and don't forget to check out the examples in this repository. ☕️

