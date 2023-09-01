from machine import Pin, PWM
import time
_init()
 
LedPin = 16
led = Pin(LedPin, Pin.OUT)
 
while True:
    led.on()
    time.sleep_ms(2)
    led.off()
    time.sleep_ms(18)