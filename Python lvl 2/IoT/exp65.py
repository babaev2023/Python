import time
from machine import I2C, Pin
import onewire
import ds18x20
from micropyserver import MicroPyServer 
import network
import gc
_init()
gc.collect()
 
# the device is on GPIO12
ow = onewire.OneWire(Pin(12))
 
# create the onewire object
ds = ds18x20.DS18X20(ow)
 
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
    roms = ds.scan()
    ds.convert_temp()
    time.sleep_ms(750)
 
    for rom in roms:
        temp = str(ds.read_temp(rom))
        server.send(temp)
 
server = MicroPyServer()
''' add request handler '''
server.add_route("/", show_message)
''' start server '''
server.start()