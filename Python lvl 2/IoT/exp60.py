from micropyserver import MicroPyServer
import time
from machine import Pin, PWM
import network
import gc
_init()
gc.collect()
 
Led = Pin(13, Pin.OUT)
pwmLed = PWM(Led)
 
wlan_id = ""
wlan_pass = ""
 
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(wlan_id, wlan_pass)
time.sleep(1)
 
while wlan.isconnected() == False:
    pass
 
print('Device IP:', wlan.ifconfig()[0])
 
 
def index(request, params):
    if ('duty' in params):
        pwmLed.duty(int(params['duty']))
    html_file = open("page.html")
    html = html_file.read()
    html_file.close()
    server.send(html, content_type="Content-Type: text/html")
 
 
server = MicroPyServer()
server.add_route("/", index)
server.start()