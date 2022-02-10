from gpiozero import DistanceSensor
from gpiozero.pins.pigpio import PiGPIOFactory

class CarSensor(DistanceSensor):
    def __init__(self, echo_pin: int, trig_pin: int):
        DistanceSensor.__init__(
            self,
            echo_pin,
	        trig_pin,
	        max_distance=1,
	        pin_factory=PiGPIOFactory(),
	        threshold_distance=0.3
        )
        self.intersection: Intersection = None

