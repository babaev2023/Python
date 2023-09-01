import time
from machine import I2C, Pin
from esp8266_i2c_lcd import I2cLcd
import mfrc522
_init()
 
buzzer = Pin(15, Pin.OUT)
 
DEFAULT_I2C_ADDR = 0x3F
 
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=400000)
lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)
lcd.backlight_on()
 
rdr = mfrc522.MFRC522(0, 2, 12, 13, 14) #sck, mosi, miso, rst, sda
 
allow_cards = [
    '4449be2'
]
 
def print_lcd(data):
    lcd.clear()
    lcd.putstr(str(data))
 
def signal_ok():
    buzzer.on()
    time.sleep_ms(200)
    buzzer.off()
 
def signal_fail():
    for i in range(3):
        buzzer.on()
        time.sleep_ms(100)
        buzzer.off()
        time.sleep_ms(100)
 
while True:
    (stat, tag_type) = rdr.request(rdr.REQIDL)
 
    if stat == rdr.OK:
        (stat, raw_uid) = rdr.anticoll()
 
        if stat == rdr.OK:
            card_number = '{:x}{:x}{:x}{:x}'.format(raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3])
            print_lcd(card_number)
            print("Card detected: " + card_number)
 
            if (card_number in allow_cards):
                print('OK')
                signal_ok()
            else:
                print('NO')
                signal_fail()