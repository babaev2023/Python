from machine import Pin
import time
_init()
 
adc = machine.ADC(0)
 
while True:
    value = adc.read()
    print(value)
    time.sleep(1)