from machine import Pin, PWM
_init()
 
LedPin = 15
 
led = Pin(LedPin, Pin.OUT)
pwmLed = PWM(led)
 
pwmLed.freq(1)
pwmLed.duty(512)