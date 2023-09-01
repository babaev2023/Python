from machine import Pin, I2C
from esp8266_i2c_lcd import I2cLcd
import time
import math
 
_init()
 
Bcoef = 3950
R1 = 10000
Rtnom = 10000
T0 = 273.15
 
adc = machine.ADC(0)
 
 
DEFAULT_I2C_ADDR = 0x3F
 
 
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=400000)
lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)
lcd.backlight_on()
 
 
while True:
    value = adc.read()
 
    R = (-R1 * value)/(value-1023)
 
    temp = 1 / (math.log(R / Rtnom) / Bcoef + 1/(25+T0)) -T0
 
    round_temp = round(temp, 1)
 
    print(round_temp)
 
    lcd.clear()
    lcd.putstr("T=" + str(round_temp))
    time.sleep(3)