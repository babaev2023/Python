from machine import Pin
import network
import gc
import time
import socket
 
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
 
 
 
def http_get(url, port=80):
    _, _, host, path = url.split('/', 3)
    addr = socket.getaddrinfo(host, port)[0][-1]
 
    s = socket.socket()
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
 
    text = ''
 
    while True:
        data = s.recv(100)
        if data:
            text += str(data, 'utf8')
            pass
        else:
            a = text.split('\r\n\r\n', 2)[1]
            return a
            break
 
 
deviceName = 'PinLabIoTSensor010923'
temp = 22.9
 
data = http_get('http://dweet.io/dweet/for/' + deviceName + '?temp=' + str(temp))