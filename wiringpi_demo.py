import wiringpi

wiringpi.wiringPiSetup()

wiringpi.pinMode(0, 1)
wiringpi.pinMode(1, 1)
wiringpi.pinMode(2, 1)

wiringpi.digitalWrite(0, 0)
wiringpi.digitalWrite(1, 0)
wiringpi.digitalWrite(2, 0)
