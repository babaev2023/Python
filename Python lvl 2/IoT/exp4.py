from machine import Pin
_init()
 
ButtonPin = 16
LedPin = 0
 
Button = Pin(ButtonPin, Pin.IN)
Led = Pin(LedPin, Pin.OUT)
 
while True:
    button_value = Button.value()
    if button_value == 1:
        Led.on()
    else:
        Led.off()