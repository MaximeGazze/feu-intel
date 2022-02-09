from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory
import time

def lumiere(r, y, g):
	ledR = LED(pin=r, pin_factory=PiGPIOFactory())
	ledY =  LED(pin=y, pin_factory=PiGPIOFactory())
	ledG =  LED(pin=g, pin_factory=PiGPIOFactory())
	try:
		ledG.on()
		time.sleep(2)
		ledG.on()
	except KeyboardInterrupt:
		GPIO.cleanup()
