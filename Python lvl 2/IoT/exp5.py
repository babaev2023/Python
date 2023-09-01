from machine import Pin
_init()
 
ButtonPin = 16
LedPin = 0
old_button_value = 0
LedState = 0
 
Button = Pin(ButtonPin, Pin.IN)
Led = Pin(LedPin, Pin.OUT)
 
while True:
    button_value = Button.value()
    if old_button_value != button_value and button_value == 1:
        if LedState:
            Led.off()
            LedState = 0
        else:
            Led.on()
            LedState = 1
 
    old_button_value = button_value