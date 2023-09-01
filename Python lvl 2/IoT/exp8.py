from machine import Pin, PWM
import time
_init()
 
LedPin = 15
 
led = Pin(LedPin, Pin.OUT)
pwmLed = PWM(led)
pwmLed.freq(200)
 
while True:
    pwmLed.duty(200)
    time.sleep(1)
    pwmLed.duty(1023)
    time.sleep(1)