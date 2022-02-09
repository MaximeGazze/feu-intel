# Important de faire sudo pigpio en commencant
#import RPi.GPIO as GPIO
from gpiozero import DistanceSensor
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep
from carPresent import *
from lumiere import *

# Feu de circulation
r1, y1, g1 = 14, 12, 16 # pin a determiner
#r2, y2, g2 = 14, 12, 16 # pin a determiner
#r3, y3, g3 = 14, 12, 16 # pin a determiner
#r4, y4, g4 = 14, 12, 16 # pin a determiner


# Capteurs distances
trig1, echo1 = 24, 23
trig2, echo2 = 21, 20 # pin a determiner
#trig3, echo3 = 24, 23 # pin a determiner
#trig4, echo4 = 24, 23 # pin a determiner

#Senseurs
nord = carPresent(trig1, echo1)
sud = carPresent(trig2, echo2)
#est = carPresent(trig3, echo33)
#ouest = carPresent(trig4, echo4)
#GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BCM)


try:
	while True:
		print("la boucle commence")
		
		
		print("vehicule present au nord ", nord.distance * 100)
		print("vehicule present au sud", sud.distance * 100)
		#print("vehicule present au est", est)
		#print("vehicule present au ouest", ouest)
		
		if nord:
		    print("commencement lumiere")
		    lumiere(r1, y1, g1)
		#if sud:
		#    lumiere(r2, y2, g2)
		#if est:
		#    lumiere(r3, y3, g3)
		#if ouest:
		#    lumiere(r4, y4, g4)

except KeyboardInterrupt:
    GPIO.cleanup()
