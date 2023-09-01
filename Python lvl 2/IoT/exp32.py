from machine import Pin
import time
import math
_init()
 
Bcoef = 3950
R1 = 10000
Rtnom = 10000
T0 = 273.15
 
adc = machine.ADC(0)
 
while True:
    value = adc.read()
 
    R2 = (-R1 * value)/(value-1023)
 
    temp = 1 / (math.log(R2 / Rtnom) / Bcoef + 1/(25+T0)) -T0
 
    print(temp)
    time.sleep(1)