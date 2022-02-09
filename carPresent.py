from gpiozero import DistanceSensor
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep


def carPresent(TRIG, ECHO):
	sensor = DistanceSensor(ECHO,
	TRIG,
	max_distance=1,
	pin_factory=PiGPIOFactory(),
	threshold_distance=0.3)
	return sensor

