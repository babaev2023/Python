import mfrc522
_init()
 
rdr = mfrc522.MFRC522(0, 2, 12, 13, 14) #sck, mosi, miso, rst, sda
 
while True:
    (stat, tag_type) = rdr.request(rdr.REQIDL)
 
    if stat == rdr.OK:
        (stat, raw_uid) = rdr.anticoll()
 
        if stat == rdr.OK:
            card_number = '{:x}{:x}{:x}{:x}'.format(raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3])
            print("Card detected: " + card_number)