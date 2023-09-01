from machine import Pin
import time 
_init()
 
LedPin = 2
 
led = Pin(LedPin, Pin.OUT)
 
while True:
    led.off()
    time.sleep(1)
    led.on()
    time.sleep(1)