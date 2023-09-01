from machine import Pin, PWM
import time
import math
_init()
 
LedPin = 15
 
led = Pin(LedPin, Pin.OUT)
pwmLed = PWM(led)
 
def pulse(l, t):
    for i in range(20):
        l.duty(int(math.sin(i / 10 * math.pi) * 500 + 500))
        time.sleep_ms(t)
 
while 1:
    pulse(pwmLed, 50)