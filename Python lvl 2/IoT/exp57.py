from micropyserver import MicroPyServer 
import time
import network
import gc
_init()
gc.collect()
 
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
    server.send("HELLO WORLD!")
 
server = MicroPyServer()
''' add request handler '''
server.add_route("/", show_message)
''' start server '''
server.start()