from micropyserver import MicroPyServer 
import time
from machine import Pin
import network
import gc
_init()
gc.collect()
 
Led = Pin(13, Pin.OUT)
 
wlan_id = ""
wlan_pass = ""
 
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(wlan_id, wlan_pass)
time.sleep(1)
 
while wlan.isconnected() == False:
    pass
 
print('Device IP:', wlan.ifconfig()[0])
 
 
def show_message(request, params):
    ''' request handler '''
    print(request)
    server.send("HELLO WORLD!")
 
def do_on(request, params):
    ''' on request handler '''
    Led.on()
    server.send("ON")
 
def do_off(request, params):
    ''' off request handler '''
    Led.off()
    server.send("OFF")
 
 
server = MicroPyServer()
''' add request handler '''
server.add_route("/", show_message)
server.add_route("/on", do_on)
server.add_route("/off", do_off)
''' start server '''
server.start()