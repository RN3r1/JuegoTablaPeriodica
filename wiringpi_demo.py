import wiringpi
import time

wiringpi.wiringPiSetup()

wiringpi.pinMode(0, 1)
wiringpi.pinMode(1, 1)
wiringpi.pinMode(2, 1)
wiringpi.pinMode(3, 1)
wiringpi.pinMode(4, 1)
wiringpi.pinMode(5, 1)
wiringpi.pinMode(6, 1)

wiringpi.digitalWrite(6, 1) # enable!

# 7 

secuencia = [0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 7, 15, 23, 31]

def binDigitalWrite(num):
    num = bin(num)[2:].zfill(6)
    wiringpi.digitalWrite(0, int(num[5]))
    wiringpi.digitalWrite(1, int(num[4]))
    wiringpi.digitalWrite(2, int(num[3]))
    wiringpi.digitalWrite(3, int(num[2]))
    wiringpi.digitalWrite(4, int(num[1]))
    wiringpi.digitalWrite(5, int(num[0]))

# binDigitalWrite(23)
# time.sleep(10)

for i in secuencia:
    binDigitalWrite(i)
    time.sleep(0.5)

