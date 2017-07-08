import wiringpi2 as wpi
import time
wpi.wiringPiSetup()

#x=1

print("Hello")
wpi.pinMode(7,1)
wpi.digitalWrite(7,1)
print("Goodbye")

#while (x>0):
#	wpi.digitalWrite(7,1)
#	time.sleep(0.05)
#	wpi.digitalWrite(7,1)
#	time.sleep(0.05)