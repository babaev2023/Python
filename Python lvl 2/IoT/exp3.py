from machine import Pin
import time
_init()
 
LedPin = 16
 
led = Pin(LedPin, Pin.OUT)
 
while True:
    led.off()
    time.sleep(1)
    led.on()
    time.sleep(1)