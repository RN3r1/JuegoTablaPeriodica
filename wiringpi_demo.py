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

def binDigitalWrite(num):
    num = bin(num)[2:].zfill(6)
    wiringpi.digitalWrite(0, int(num[5]))
    wiringpi.digitalWrite(1, int(num[4]))
    wiringpi.digitalWrite(2, int(num[3]))
    wiringpi.digitalWrite(3, int(num[2]))
    wiringpi.digitalWrite(4, int(num[1]))
    wiringpi.digitalWrite(5, int(num[0]))

binDigitalWrite(0)

# for i in range(0,39):
#     binDigitalWrite(i)
#     time.sleep(5)

